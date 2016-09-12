#!/bin/bash

apt-get update

apt-get install -y vim cmake build-essential libgtest-dev python

cd /usr/src/gtest

cmake CMakeLists.txt

make

cp *.a /usr/lib
export GTEST_OUTPUT=xml:/autograder/source/out.xml
echo 'GTEST_OUTPUT="xml:/autograder/source/out.xml"' >> $HOME/.profile
