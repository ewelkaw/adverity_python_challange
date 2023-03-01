build:
	docker build --tag swapi_app .
run:
	docker run -p 8000:8000 -v "$(PWD):/app" -it swapi_app
makemigrations:
	docker run -it -v "$(PWD):/app" --rm swapi_app python3 manage.py makemigrations swapi_app
migrate:
	docker run -it -v "$(PWD):/app" --rm swapi_app python3 manage.py migrate
createsuperuser:
	docker run -it -v  "$(PWD):/app" --rm swapi_app python3 manage.py createsuperuser
test:
	docker run -it -v  "$(PWD):/app" --rm swapi_app python3 manage.py test
