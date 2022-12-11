#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file = open("newfile1.txt", "x")
print(file)
if file:
    print("File created successfully")
file.close()