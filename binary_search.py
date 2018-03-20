#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: nemo_chen
# 二分查找

def binary_search(arr, key):
    start = arr[0]
    end = arr[-1]
    while start <= end:
        mid = start + (end - start) / 2
        if arr[mid] > key:
            start = mid -1
        elif arr[mid] < key:
            start = mid + 1
        else:
            return mid

