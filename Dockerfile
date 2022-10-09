FROM python:3.7.3-alpine

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY dev /dev
COPY src /src

CMD ["python3", "src/main.py"]
