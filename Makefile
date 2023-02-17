clean:
	rm -rf report
	rm -rf __pycache__
	rm -rf .pytest_cache

test:
	/usr/bin/python3 -m pytest test_generate_password.py
	/usr/bin/python3 entropy.py
