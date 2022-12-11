#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file = open("file2.txt", "r")
content = file.readlines()
print(content)
file.close()