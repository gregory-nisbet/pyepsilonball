all: test

.PHONY: check-virtualenv
check-virtualenv:
	@(test -n $$VIRTUAL_ENV || ( printf '%s\n' "must be inside virtualenv"; exit 10; ))

install-deps: check-virtualenv

test: check-virtualenv
	@for path in ./src/pyepsilonball/*.py; do \
	  python ./src/pyepsilonball/pyepsilonball.py; \
	done

format:
	black ./src/pyepsilonball/*.py
