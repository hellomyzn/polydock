include .env
export $(shell sed 's/=.*//' .env)

DOCKER_COMPOSE_FILE_PATH=-f docker-compose.yml

ENV_PATH=--env-file .env
PROJECT_FLAG=--project-name ${PROJECT_NAME}_devcontainer
USER_FLAG=--user ${USER_NAME}

up:
	@echo vscode, .devcontainer経由で起動してください
down:
	docker compose ${DOCKER_COMPOSE_FILE_PATH} ${PROJECT_FLAG} ${ENV_PATH} down
destroy:
	docker-compose ${DOCKER_COMPOSE_FILE_PATH} ${PROJECT_FLAG} down --rmi all --volumes --remove-orphans
exec:
	docker compose ${DOCKER_COMPOSE_FILE_PATH} ${PROJECT_FLAG} exec ${USER_FLAG} workspace bash
logs:
	docker compose ${DOCKER_COMPOSE_FILE_PATH} ${PROJECT_FLAG} logs -f
dev:
	docker compose ${DOCKER_COMPOSE_FILE_PATH} ${PROJECT_FLAG} exec ${USER_FLAG} workspace bash -c 'cd ${WORKDIR}/src && npm run dev'
build:
	docker compose ${DOCKER_COMPOSE_FILE_PATH} ${PROJECT_FLAG} exec ${USER_FLAG} workspace bash -c 'cd ${WORKDIR}/src && npm run build'
