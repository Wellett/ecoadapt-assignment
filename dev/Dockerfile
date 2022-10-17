FROM ubuntu:20.04

RUN apt update \
    && apt install --no-install-recommends -y \
    python3 \
    python3-pip

COPY . .

RUN pip install -r ./requirements-dev.txt

CMD ["python3", "server.py"]

