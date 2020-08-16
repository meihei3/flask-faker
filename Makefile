lint:
	docker-compose exec flask pycodestyle . --ignore="E501" --exclude database
.PHONY: lint

fix:
	docker-compose exec flask bash -c " pycodestyle . --ignore="E501" --exclude database | cut -d: -f1 | sort | uniq | xargs autopep8 --in-place --aggressive --aggressive"
.PHONY: fix
