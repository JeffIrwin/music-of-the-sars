#!/bin/bash

inputs=./*genome.txt

frames=()

exebase=sars
outdir=.
expectedoutdir=./expected-output
outputext=mid
use_stdin="false"
use_python="true"

#===============================================================================

source ./submodules/bat/test.sh

