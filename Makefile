.PHONY: ndocker
ndocker:
	docker-compose down && docker-compose build --no-cache && docker-compose up

.PHONY: ndocker-dev
ndocker-dev:
	docker-compose down \
	&& docker-compose build --no-cache --build-arg MODE=DEV \
	&& docker-compose -f docker-compose.yaml -f docker-compose-dev.yaml up

.PHONY: precommit
precommit:
	pre-commit run --all-files

ndocker-test-no-cache:
	docker-compose down -v --rmi local \
	&& docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml build --no-cache \
	&& docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up
