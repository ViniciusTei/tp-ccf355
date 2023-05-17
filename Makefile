VENV           = .venv
VENV_PYTHON    = $(VENV)/bin/python
SYSTEM_PYTHON  = $(or $(shell which python3), $(shell which python))
PYTHON         = $(or $(wildcard $(VENV_PYTHON)), $(SYSTEM_PYTHON))

VENV_ACTIVATE  = ./scripts/run.sh

all:
	$(VENV_ACTIVATE)

run_server:
	$(PYTHON) ./server/server.py

run_client:
	$(PYTHON) ./client/client.py

clean:
	$(shell rm -r venv)
