PYTHON ?= python3
FLOW := $(PYTHON) script/socflow.py

.PHONY: doctor validate mock mock-negative selftest contracts flow-test
doctor:
	$(FLOW) doctor --profile mock

validate:
	$(FLOW) validate --suite regress/mock_smoke.json

mock:
	$(FLOW) regress --suite regress/mock_smoke.json --jobs 2

mock-negative:
	$(FLOW) regress --suite regress/mock_negative.json

selftest:
	$(FLOW) regress --suite regress/uvm_selftest.json --profile uvm_selftest --simulator $(SIMULATOR) --site config/site.json

contracts:
	$(FLOW) contracts

flow-test:
	$(PYTHON) -m unittest discover -s tests_flow -v

SIMULATOR ?= vcs
