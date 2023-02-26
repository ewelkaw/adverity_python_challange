build:
	docker build --tag swapi_app .
run:
	docker run -p 8000:8000 -v "$(PWD):/app" -it swapi_app
