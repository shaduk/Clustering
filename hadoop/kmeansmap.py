#!/usr/bin/env python
import sys
import math


#Calculate euclidean distance between two points
def calculate_euclidean_distance(x, m):
	distance = 0
	for i in range(len(x)):
		distance = distance + math.sqrt(math.pow(float(x[i]) - float(m[i]), 2))
	return distance

#get the index of nearest cluster
def get_nearest_cluster(centroid, x):
	closestTo = -1
	mindist = sys.maxint
	for j in range(0, len(centroid)):
		euc_distance = calculate_euclidean_distance(centroid[j], x)
		if(euc_distance < mindist):
			mindist = euc_distance
			closestTo = j
	return closestTo

#create a text file of initial random clusters
def get_centroids():
	f = open("centroid.txt", 'r')
	data = f.read()
	centroid = []
	for i in data.strip().split("\n"):
		row = i.strip().split("\t")
		centroid.append(row)
	return centroid
		
centroids = get_centroids()

#Emit the closestTo id, gene id and all the attributes of input data as key value pairs
for line in sys.stdin:
	line = line.strip()
	data = line.split('\t')
	gen_id = data[0]
	ground_truth = data[1]
	attributes = data[2:]
	closestTo = get_nearest_cluster(centroids, attributes)
	attr_str = '#'.join(attributes)
	print '%s\t%s\t%s' % (closestTo, gen_id, attr_str)
