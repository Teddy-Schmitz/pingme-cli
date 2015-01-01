PingMe-cli
======
Command line client for PingMe android app.

[![Build Status](http://img.shields.io/travis/teddy-schmitz/pingme-cli/master.svg)](https://travis-ci.org/teddy-schmitz/pingme-cli)
[![Coverage Status](http://img.shields.io/coveralls/teddy-schmitz/pingme-cli/master.svg)](https://coveralls.io/r/teddy-schmitz/pingme-cli)
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/teddy-schmitz/pingme-cli.svg)](https://scrutinizer-ci.com/g/teddy-schmitz/pingme-cli/?branch=master)
[![PyPI Version](http://img.shields.io/pypi/v/PingMeCli.svg)](https://pypi.python.org/pypi/PingMeCli)
[![PyPI Downloads](http://img.shields.io/pypi/dm/PingMeCli.svg)](https://pypi.python.org/pypi/PingMeCli)


Getting Started
===============

Requirements
------------

* Python 2.7+

Installation
------------

PingMe-cli can be installed with pip:

```
$ pip install pingme
```

or directly from the source code:

```
$ git clone https://github.com/teddy-schmitz/pingme-cli.git
$ cd pingme-cli
$ python setup.py install
```

Basic Usage
===========

To send a message use the following syntax

```
$ pingme -d <device id> <message>
```

Devices can be a comma separated list.  You can also define a config file in 

~/.pingme_config

```
[Default]
devices=deviceid1,deviceid2
message=Example
```
This will allow you to specify defaults for the command, but any arguments passed in will override these values.


For Contributors
================

Requirements
------------

* Make:
    * Windows: http://cygwin.com/install.html
    * Mac: https://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make (likely already installed)
* virtualenv: https://pypi.python.org/pypi/virtualenv#installation

Installation
------------

Create a virtualenv:

```
$ make env
```

Run the tests:

```
$ make test
$ make tests  # includes integration tests
```

Build the documentation:

```
$ make doc
```

Run static analysis:

```
$ make pep8
$ make pep257
$ make pylint
$ make check  # includes all checks
```

Prepare a release:

```
$ make dist  # dry run
$ make upload
```
