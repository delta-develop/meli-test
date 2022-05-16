THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: help build up start down destroy stop restart ps

help:
		make -pRrq  -f $(THIS_FILE) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

build:
		docker-compose -f docker-compose.yml build

up:
		docker-compose -f docker-compose.yml up -d

start:
		docker-compose -f docker-compose.yml start

down:
		docker-compose -f docker-compose.yml down

destroy:
		docker-compose -f docker-compose.yml down -v

stop:
		docker-compose -f docker-compose.yml stop

restart:
		docker-compose -f docker-compose.yml stop
		docker-compose -f docker-compose.yml up -d

ps:
		docker-compose -f docker-compose.yml ps
