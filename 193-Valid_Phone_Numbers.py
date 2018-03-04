#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: nemo_chen
# https://leetcode.com/problems/valid-phone-numbers/description/
# http://blog.csdn.net/qq_18952073/article/details/70236230
'''
Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.
You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)
You may also assume each line in the text file must not contain leading or trailing white spaces.
For example, assume that file.txt has the following content:
987-123-4567
123 456 7890
(123) 456-7890
Your script should output the following valid phone numbers:
987-123-4567
(123) 456-7890
'''
egrep '^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$|^[0-9]{3}-[0-9]{3}-[0-9]{4}$' file.txt

awk '$0 ~ /^((([0-9]{3}-)|(\([0-9]{3}\) ))[0-9]{3}-[0-9]{4})$/ {print $0}' file.txt
