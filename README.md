# PTV Getter

A tool for proxying requests to the [PTV Timetable API](https://www.ptv.vic.gov.au/footer/data-and-reporting/datasets/ptv-timetable-api/). Requires a `Dev Id` and `API Key` to use.

# Requirements

* Follow the steps in the [API Key and Signature Information](https://static.ptv.vic.gov.au/PTV/PTV%20docs/API/1475462320/PTV-Timetable-API-key-and-signature-document.RTF) guide to request a PTV `Dev Id` and `API Key`
* Running locally requires Python3 with Flask installed
* Running in a Docker container requires Docker

# Getting Started

If you cannot use `make`, just copy the commands from the `Makefile` directly.

* Clone this repository
* Copy `secrets.template.py` to `secrets.py` and add your `Dev Id` and `API Key` to the secrets file.
* To run it locally
  * Run `make run-locally`
* To run the Docker container
  * Run `make build` to build the Docker container
  * Run `make run` to run the Docker container
* To install as a system service (on Linux machines that support `systemd`, like Raspbian)
  * Run `make build` to build the Docker container
  * Copy `ptv-getter.service` to `/etc/systemd/system`

# How it works

PTV Getter is a Flask app that proxies incoming calls to the PTV Timetable API.

1. Make call to PTV Getter:
   * eg. `http://localhost:8763/v3/route_types`
2. PTV Getter appends `Dev Id` and uses `API Key` to calculate signature
   * eg. `?devid=0000000&signature=0000000000000000000000000000000000000000`
3. PTV Getter forwards request to PTV Timetable API
   * eg. `http://timetableapi.ptv.vic.gov.au/v3/route_types?devid=0000000&signature=0000000000000000000000000000000000000000`
4. The PTV Timetable API response is returned directly