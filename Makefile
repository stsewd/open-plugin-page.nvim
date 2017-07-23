PYTHON=python3

test:
	cd rplugin/python3/ && \
	${PYTHON} -m unittest -v
