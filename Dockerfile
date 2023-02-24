FROM python:3.8.3-slim
RUN apt-get update && apt-get install -y build-essential
COPY . /app
WORKDIR /app/swapi_project
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD [ "python3", "manage.py", "runserver"]
