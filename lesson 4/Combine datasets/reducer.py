#!/usr/bin/python

import sys

# Reducer - combining forum posts with its user data

previous_author = ""
current_author = ""
post_list = []
author_info = []

def joinInformation(posts, author):
    
    reputation = author[2]
    gold = author[3]
    silver = author[4]
    bronze = author[5]

    for item in posts:
	post_id = item[2]
	title = item[3]
	tags = item[4]
	author_id = item[0]
	node = item[5]
	parent = item[6]
	abs_parent = item[7]
	added = item[8]
	score = item[9]
	print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(post_id, title, tags, author_id, node, parent, abs_parent, added, score, reputation, gold, silver, bronze)

for line in sys.stdin:
    data = line.strip().split("\t")

    if previous_author == "":
	previous_author = data[0]

    if data[0] != previous_author:
	joinInformation(post_list, author_info)
	post_list = []
	author_info = ""
	previous_author = data[0]

    if data[1] == "B":
	post_list.append(data)

    elif data[1] == "A":
	author_info = data

joinInformation(post_list, author_info)
