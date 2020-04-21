.PHONY: login build push pull rundockercompose

all: login build push

build:
	docker build . -t magida/in-out

push:
	docker push magida/in-out

pull:
	docker pull magida/in-out

rundockercompose:
	docker-compose up -d && docker-compose logs --follow

rundocker:
	docker container run -p 80:3000 magida/in-out

login:
	docker login

clean:
	echo "hello world"