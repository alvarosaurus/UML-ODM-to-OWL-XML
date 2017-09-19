#! /bin/bash
export PYTHONPATH=${PYTHONPATH}:../src
green -vvv --run-coverage -u */odm2owl/*,*/zargo/* --clear-omit
