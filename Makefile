.PHONY: setup test clean structure

setup:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

clean:
	rm -rf data/interim/* data/processed/*
	find . -type d -name __pycache__ -exec rm -rf {} +

structure:
	@echo "Project structure:"
	@find . -type f -not -path './.git/*' -not -path './.venv/*' | sort