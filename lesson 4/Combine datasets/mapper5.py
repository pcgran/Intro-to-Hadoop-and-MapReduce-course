#!/usr/bin/python
import sys, csv, string

# Mapper - combining forum posts with its user data

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
   #if it has 19 columns, then it is a post
   if len(line) == 19:
	post_id = line[0]
	title = line[1]
	tags = line[2]
	author_id = line[3]
	node_type = line[5]
	parent = line[6]
	abs_parent = line[7]
	added = line[8]
	score = line[9]
	if post_id != "id":
		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}".format(author_id,"B", post_id, title, tags, node_type, parent, abs_parent, added, score)

   if len(line) == 5:
	user_ptr_id = line[0]
	reputation = line[1]
	gold = line[2]
	silver = line[3]
	bronze = line[4]
	if user_ptr_id != "user_ptr_id":
		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(user_ptr_id, "A", reputation, gold, silver, bronze)

