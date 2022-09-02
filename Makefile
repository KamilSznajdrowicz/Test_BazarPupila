.PHONY: deps tests
deps:
	pip install -r requirements.txt

tests:
	py.test Tests/test_registration.py
	py.test Tests/test_contact.py

