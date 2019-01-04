all: test docs/source clean/dist build publish

.PHONY: docs/source
docs/source:
	@sphinx-apidoc -f -o docs/source stat_arb_tools

.PHONY: docs
docs:
	@make -C docs html

.PHONY: run/docs
run/docs:
	@(cd docs/build/html && python -m SimpleHTTPServer)

.PHONY: requirements
requirements:
	@pip-compile --generate-hashes --output-file requirements.txt setup.py

.PHONY: install/deps
install/deps:
	@pip install -r requirements.txt

.PHONY: test
test:
	@python3 setup.py test

.PHONY: test/specific
test/specific:
	@python3 setup.py nosetests --tests stat_arb_tools/tests/adf_test.py:TestADF.test_female_births -v

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
