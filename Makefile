VENV           = .venv
VENV_PYTHON    = $(VENV)/bin/python
SYSTEM_PYTHON  = $(or $(shell which python3), $(shell which python))
PYTHON         = $(or $(wildcard $(VENV_PYTHON)), $(SYSTEM_PYTHON))
PIP            = ./venv/bin/pip

venv/bin/activate: requirements.txt
	$(PYTHON) -m venv venv
	chmod +x venv/bin/activate
	. ./venv/bin/activate
	$(PIP) install -r requirements.txt

venv: venv/bin/activate
	. ./venv/bin/activate

run_nameserver: venv
		$(PYTHON) -m Pyro5.nameserver

run_server: venv
	flask --app ./server/app.py run

run_client: venv
	$(PYTHON) ./client/client.py

run_w_server: 
	flask --app ./server/app.py run

run_w_client: 
	$(PYTHON) ./client/client.py

clean:
	$(shell rm -r venv)
