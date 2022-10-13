FROM python:3.7.3-alpine

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . .

CMD ["python3", "main.py"]
