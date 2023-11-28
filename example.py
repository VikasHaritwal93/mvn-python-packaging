#!/usr/bin/env python2
# Copyright 2020 Sean Busbey
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# place in src/main/python/example.py

""" Example python use in a maven build. echos args """

import sys
sys.dont_write_bytecode = True
print("By default the stdout/stderr from the script will go to the maven logger")
print("\tif you want to change that there's a config on the exec-maven-plugin")
print("Exit with 0 means the build goes on. anything else fails the build")
print("\tif you need to allow for other non-0 exit codes there's a config on the exec-maven-plugin")
print("This invocation was called as follows:")
print('\n\t* '.join(sys.argv))
