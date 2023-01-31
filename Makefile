.PHONY: deps tests
deps:
	pip install -r requirements.txt

tests:
	run Tests/test_registration.py
	run Tests/test_contact.py

