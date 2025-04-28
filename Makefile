# ANSI color codes
COLOR_RESET=\033[0m
COLOR_BOLD=\033[1m
COLOR_GREEN=\033[32m
COLOR_YELLOW=\033[33m

help:
	@echo ""
	@echo "  $(COLOR_YELLOW)Available targets:$(COLOR_RESET)"
	@echo ""
	@echo "  $(COLOR_GREEN)upgrade-pip$(COLOR_RESET)		- Upgrade Pip Version"
	@echo "  $(COLOR_GREEN)install$(COLOR_RESET)		- Install Libraries / Dependencies"
	@echo "  $(COLOR_GREEN)freeze$(COLOR_RESET)		- Freeze Libraries / Dependencies"
	@echo "  $(COLOR_GREEN)run$(COLOR_RESET)			- Run FastAPI/Mongo DB"
	@echo ""
	@echo "  $(COLOR_YELLOW)Note:$(COLOR_RESET) Use 'make <target>' to execute a specific target."
	@echo ""


upgrade-pip:
	pip install --upgrade pip

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt
	
run:
	docker-compose up --build

build:
	docker compose up -d --build
