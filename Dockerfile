FROM python:3.8

RUN apt-get update && \
    apt-get -y install gcc && \
    apt-get clean

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "app:app", "--log-file", "-"]
