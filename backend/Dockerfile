FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY . /app

# Flaskのホットリロードをサポートするため、flask runを使う
CMD ["watchmedo", "auto-restart", "--patterns=*.py", "--recursive", "--", "python", "app.py"]
