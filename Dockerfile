FROM python:alpine3.11

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP go.py

EXPOSE 5000

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0"]