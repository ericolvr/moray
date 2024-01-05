# ANSI color codes
COLOR_RESET=\033[0m
COLOR_BOLD=\033[1m
COLOR_GREEN=\033[32m
COLOR_YELLOW=\033[33m

start:
	docker compose up -d

stop:
	docker compose down

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 7777

exec:
	docker exec -it web bash

logs:
	docker logs web -f


help:
	@echo ""
	@echo "  $(COLOR_YELLOW)Available targets:$(COLOR_RESET)"
	@echo "  $(COLOR_GREEN)start$(COLOR_RESET)			- Start Docker Services"
	@echo "  $(COLOR_GREEN)stop$(COLOR_RESET)			- Stop Docker Services"
	@echo "  $(COLOR_GREEN)exec$(COLOR_RESET)			- Enter on Container"
	@echo "  $(COLOR_GREEN)logs$(COLOR_RESET)			- Logs From Container"
	@echo ""
	@echo "$(COLOR_YELLOW)Note:$(COLOR_RESET) Use 'make <target>' to execute a specific target."
	@echo ""

.PHONY: start, stop, run, exec, logs, help