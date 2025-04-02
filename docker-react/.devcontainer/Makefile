include .env
export $(shell sed 's/=.*//' .env)

DOCKER_COMPOSE_FILE_PATH=-f docker-compose.yml
ENV_PATH=--env-file .env
PROJECT_FLAG=--project-name ${PROJECT_NAME}_devcontainer
USER_FLAG=--user ${USER_NAME}

up:
	docker compose ${DOCKER_COMPOSE_FILE_PATH} ${ENV_PATH} up -d --build
down:
	docker compose ${DOCKER_COMPOSE_FILE_PATH} ${ENV_PATH} down
exec:
	docker compose ${DOCKER_COMPOSE_FILE_PATH} exec ${USER_FLAG} workspace bash
destroy:
	docker-compose ${DOCKER_COMPOSE_FILE_PATH} down --rmi all --volumes --remove-orphans
logs:
	docker compose ${DOCKER_COMPOSE_FILE_PATH} logs -f


