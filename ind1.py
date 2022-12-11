#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Написать программу, которая считывает текст из файла и выводит на экран все его
#предложения в обратном порядке.

if __name__ == "__main__":

    with open('text1.txt',encoding='utf-8')as f:
        for text in reversed(f.readlines()):
            print(text1, end='')
