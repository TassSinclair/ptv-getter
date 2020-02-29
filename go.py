from flask import Flask, request, Response
from hashlib import sha1
import hmac
import requests
import binascii
import secrets

app = Flask(__name__)

BASE_URL='https://timetableapi.ptv.vic.gov.au'

@app.route('/<path:path>')
def forward(path):
    pathWithDevid = '/{path}?devid={devId}{paramSpacer}{params}'.format(
        path = path,
        paramSpacer = ('&' if request.query_string else ''),
        params = request.query_string.decode('utf-8'),
        devId = secrets.DEV_ID
    )

    signature = hmac.new(
        secrets.API_KEY.encode(),
        pathWithDevid.encode(),
        sha1
    ).hexdigest()

    url = '{base}{path}&signature={signature}'.format(
        base = BASE_URL,
        path = pathWithDevid,
        signature = signature
    )

    downstream = requests.request(
        method=request.method, 
        url = url)

    return Response(downstream.content, downstream.status_code)
