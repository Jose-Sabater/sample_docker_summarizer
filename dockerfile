FROM python:3.9-slim

WORKDIR /app

COPY ./src /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV NAME World

CMD ["python", "main.py"]
