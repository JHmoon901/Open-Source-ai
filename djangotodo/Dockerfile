From python:3.10
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD ["python","mytodo/manage.py","runserver","0.0.0.0:8000"]