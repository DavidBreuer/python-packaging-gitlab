.PHONY: install docker docs tests baseplots all

# install package requirements and development version
install:
	echo "make install" \
	&& pip install -U -r requirements.txt -r requirements_dev.txt \
	&& pip install -e . --no-deps

# build docker image with enabled matplotlib support
# requires explicit plt.show() call to show graphics
# https://stackoverflow.com/a/46018699/5350621
# https://stackoverflow.com/a/18137056/5350621
docker:
	echo "make docker" \
	&& echo "set required environment variables via:" \
	&& echo "export SUB_USER=..." \
	&& echo "export SUB_TOKEN=..." \
	&& docker build --build-arg SUB_USER --build-arg SUB_TOKEN -t main . -f Dockerfile \
	&& docker run --rm -it \
   	--user=$(shell id -u) \
   	--env="DISPLAY" \
   	--workdir=/app \
   	--volume="$(shell pwd)":/app \
   	--volume="/etc/group:/etc/group:ro" \
   	--volume="/etc/passwd:/etc/passwd:ro" \
   	--volume="/etc/shadow:/etc/shadow:ro" \
   	--volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
   	--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
   	main python3

# create docs
# if the docs do not update properly,
# remove docs/build and docs/auto_examples and run:
# sphinx-apidoc -o docs main
# cd docs
# make html
docs:
	echo "make docs" \
	&& cd docs \
	&& make html \
	&& (ln -s build/html/index.html index.html || true)

# run unit tests, doctests, linters, mpl tests, and create coverage
# --pylint-error-types=EF raises exceptions only for errors and failures
tests:
	echo "make docs" \
	&& NUMBA_DISABLE_JIT='1' \
	python -m pytest tests/ \
	--doctest-modules main/ \
	--pylint main/ tests/ --pylint-error-types=EF \
	--flakes main/ tests/ \
	--mpl \
	--cov=main --cov-report term --cov-report html:docs/build/html/coverage

# create matplotlib baseline plots as comparison files for mpl tests
baseplots:
	echo "make baseplots" \
	&& python -m pytest tests/stuff --mpl-generate-path=tests/stuff/baseline

# create docs, run tests, and open documentation in browser
all:
	echo "make all" \
	&& (make docs ||true) \
	&& (make tests || true) \
	&& firefox docs/index.html
