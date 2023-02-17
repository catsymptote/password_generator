
build:
	/usr/bin/python3 download_words.py short

buildlong:
	/usr/bin/python3 download_words.py long

buildhuge:
	/usr/bin/python3 download_words.py huge

clean:
	rm -rf assets
	rm -rf report
	rm -rf __pycache__
	rm -rf .pytest_cache

test:
	/usr/bin/python3 -m pytest test_generate_password.py
	/usr/bin/python3 entropy.py
