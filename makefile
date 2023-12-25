DC = docker compose
APP = docker-compose.yml

.PHONY: app
app-start:
	${DC} -f ${APP} --env-file ./backend/.env up 

.PHONY: app
app-reload:
	${DC} -f ${APP} --env-file ./backend/.env up --force-recreate

.PHONY: logs
app-logs:
	${DC} -f ${APP} logs -f
