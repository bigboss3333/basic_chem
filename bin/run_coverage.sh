#!/bin/bash
# Run tests for jenkins
pushd ..
pylint core_chem tests
coverage run --source=. -m unittest discover ./tests/
coverage report
popd