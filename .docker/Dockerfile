FROM python:3.10 AS BUILD

WORKDIR /app
COPY . /app
COPY requirements.txt /app

RUN python -m pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]