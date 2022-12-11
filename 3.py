#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file = open("file2.txt", "r")

content1 = file.readline()
content2 = file.readline()

print(content1)
print(content2)

file.close()