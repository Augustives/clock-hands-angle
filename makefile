up:
	docker-compose up -d --build django

down:
	docker-compose -p clock-hours-angle stop django

rm: down
	docker-compose -p clock-hours-angle rm -f -v django

test:
	pytest ./src