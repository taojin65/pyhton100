#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

for file in os.listdir('/Users/jinmingnan'):
    if os.path.splitext(file)[1] != '':
        print '/Users/jinmingnan' + os.sep + file