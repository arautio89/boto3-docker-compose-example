FROM python:3.8.0-slim-buster

ENV DEBIAN_FRONTEND=noninteractive

RUN pip install \
	boto3

WORKDIR /bin/uploader

CMD python upload.py