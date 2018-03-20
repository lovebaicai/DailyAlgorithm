#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: nemo_chen
# 几种常用排序Python实现
# http://blog.csdn.net/mrlevo520/article/details/77829204

# 冒泡
def bubbleSort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(l-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 选择
# method one:
def selectSort(arr):
    l = len(arr)
    for i in range(l):
        min_index = i
        for j in range(i+1, l):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[j]
    return arr
    
# method two:
def selectSort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(l - i):
            if arr[i] > arr[j+i]:
                arr[i], arr[i+j] = arr[i+j], arr[i]
    return arr

# 快速
def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        basic = arr[0]
        less = [i for i in arr[1:] if i < basic]
        more = [i for i in arr[1:] if i > basic]
        return quickSort(less) + [basic] + quickSort(more)

# 插入
def insertSort(arr):
    l = len(arr)
    for i in range(1, l):
        for j in range(i):
            if arr[i] < arr[j]:
                arr.insert(j, arr[i])
                arr.pop(i+1)
                break
    return arr

# 希尔
def shellSort(arr):
    l = len(arr)
    basic = l / 2
    while basic > 0:
        for i in range(basic, l):
            temp = arr[i]
            j = i
            while j >= basic and arr[j - basic] > temp:
                arr[j] = arr[j - basic]
                j -= basic
            arr[j] = temp
        basic = basic / 2
    return arr

# 合并
def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid_index = len(arr) / 2
    left = mergeSort(arr[:mid_index])
    right = mergeSort(arr[min_index:])
    return merge(left, right)
