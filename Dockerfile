FROM python:3.7.3-alpine

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

#CMD ["python3","--version"]
COPY src/exporter-ecoadapt/exporter-ecoadapt.py /exporter-ecoadapt.py

CMD ["python3", "exporter-ecoadapt.py"]
