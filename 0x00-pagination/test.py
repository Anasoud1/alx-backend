#!/usr/bin/env python3
"""
Main file
"""
import csv


with open('Popular_Baby_Names.csv') as f:
    reader = csv.reader(f)
    data = [row for row in reader]
    page = 1
    page_size = 3
    start = (page - 1) * page_size
    end = start + page_size
    count = 0
    print(start, end)
    lis = []
    for line in data:
        if count >= start and count <= end:
            lis.append(line)
        count += 1
    print(lis)
