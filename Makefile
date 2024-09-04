build:
	docker build . -t image

run:
	docker run -p8000:8000 --name container image

remove:
	docker rm -f container

exec:
	make remove || true
	make build
	make run

venv:
	clear
	@echo "Creating VirtualENV...."
	@python -m venv .venv
	.venv/bin/pip install -r requirements_unit_test.txt || true
	.venv/bin/pip install -r requirements.txt || true
	.venv/bin/pip install pytest
	.venv/bin/pip install pytest-cov
	@echo
	@echo "VirtualENV Setup Complete. Now run: source .venv/bin/activate"
	@echo


test:
	clear && python -m pytest -s --cov-report=term-missing --cov=name_space_do_projeto tests/unit/

pip_test:
	pip install pytest
	pip install pytest-cov
