FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y poppler-utils
RUN apt install -y tesseract-ocr
RUN apt install -y libtesseract-dev
COPY . /code/