build:
	docker build -t frontend:develop .

push:
	docker push vianagallery/frontend:stable

stable:
	docker buildx build --platform linux/arm64 --push -t vianagallery/frontend:stable .

run:
	python main.debug.py

docker-run: 
	docker run -p 80:8000 frontend:develop