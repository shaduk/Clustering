# K Means Clustering using Hadoop Mapreduce

## Implementation Details: 

Initially we stored k centroids in a text file called “centroid.txt”. We wrote 3 python scripts to run our hadoop implementation :-

1) Mapper.py - Mapper takes in the input data line by line and for each row it emits centroid id, the point which belong to this centroid and the point attributes.

		Mapper -> emits(centroid_id, gen_id, attributes 1 ...2….3..)

2) Reducer.py - Reducer gets the sorted data from the mapper. It goes through each line and sum the attributes of each line which belongs to same centroid. After that, when it parses all rows of a centroid it emits the centroid_id and the list of all gen_ids which belong to this cluster. Reducer also updates the centroid.txt file with the mean of data. This updated text file is now used by the mapper to process second iteration.

		Reducer -> emits(centroid_id, list of gen_ids)

3) bash.py - This is a driver file which runs hadoop mapreduce multiple times until we reach a convergence. This convergence is found when the text file centroid.txt does not change in any iteration. We stop our program and then write the final results into a text file called “part-00000”.

## Steps to run the program

1) Start hadoop
```
 start-hadoop.sh
```
2) Run chmod
```
chmod +x ./kmeansmap.py
chmod +x ./kmeansred.py
```
2) Put the input files to the hadoop directory :-
```
hdfs dfs -put $HOME/Activity3/act3input act3input
```
3) Run hadoop mapreduce:
```
python2.7 bash.py
```
4) Read output:
```
hdfs dfs -cat act3out/*
```
