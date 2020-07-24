lint:
	docker-compose exec flask pycodestyle .
.PHONY: lint

fix:
	docker-compose exec flask bash -c " pycodestyle . | cut -d: -f1 | sort | uniq | xargs autopep8 --in-place --aggressive --aggressive"
.PHONY: fix
