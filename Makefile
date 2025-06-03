run:
	docker compose run --rm app bash

cleaning:
	docker system prune -af