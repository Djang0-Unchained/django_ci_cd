posts:
	docker exec -it backend python manage.py generate

tests:
	docker exec -it backend python manage.py test

