FROM python:latest

WORKDIR /app

ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ADD . .

EXPOSE 80
CMD uvicorn fastq.main:app