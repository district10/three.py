all:
	@echo nothing special

lint:
	yapf -ir .

prepare:
	python3 -m pip install -r requirements.txt

install:
	@cp pre_commit.sh .git/hooks/pre-commit || true
	@python3 setup.py install

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf __pycache__
	rm -f *.pyc
