up:
	docker-compose up -d --build

down:
	docker-compose -p clock-hands-angle stop

rm: down
	docker-compose -p clock-hands-angle rm -f -v

test:
	pytest ./src