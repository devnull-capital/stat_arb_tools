all: test clean/dist build publish

.PHONY: requirements
requirements:
	@pip-compile --generate-hashes --output-file requirements.txt setup.py

.PHONY: install/deps
install/deps:
	@pip install -r requirements.txt

.PHONY: test
test:
	@python3 setup.py test

.PHONY: clean/dist
clean/dist:
	@rm ./dist/*

.PHONY: build
build:
	@echo "don't forget to bump versions in setup.py and docs/build/conf.py"
	@python3 setup.py sdist bdist_wheel

.PHONY: publish
publish:
	@twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
