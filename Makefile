all: test

.PHONY: check-virtualenv
check-virtualenv:
	@env | grep '^VIRTUAL_ENV=' > /dev/null

install-deps: check-virtualenv

test: check-virtualenv
	@for path in ./src/pyepsilonball/*.py; do \
	  python ./src/pyepsilonball/pyepsilonball.py; \
	done

format: check-virtualenv
	@black ./src/pyepsilonball/*.py

repl: check-virtualenv
	@bash repl.sh
