
# Makefile

.PHONY: all compile_proto run_python clean

all: compile_proto run_python

compile_proto:
	protoc -I=. --python_out=. complex_message.proto
	protoc -I=. --mypy_out=. complex_message.proto

run_python:
	python create_complex_message.py

clean:
	rm -f *_pb2.py
	rm -f *.pyc
