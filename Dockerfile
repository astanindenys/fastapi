FROM python:3.9

WORKDIR /app

COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

COPY ./ /app

