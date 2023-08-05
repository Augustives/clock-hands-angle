up:
	docker-compose up -d --build django

down:
	docker-compose -p clock-hands-angle stop django

rm: down
	docker-compose -p clock-hands-angle rm -f -v django

test:
	pytest ./src