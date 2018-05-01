PROJECT_NAME = wren
DEV_COMPOSE_FILE := docker/docker-compose.yml

.PHONY: build

default: buildrelease

build:
	docker-compose -p $(PROJECT_NAME) -f $(DEV_COMPOSE_FILE) build
	docker-compose -p $(PROJECT_NAME) -f $(DEV_COMPOSE_FILE) up -d


clean:
	docker-compose -p $(PROJECT_NAME) -f $(DEV_COMPOSE_FILE) down -v
