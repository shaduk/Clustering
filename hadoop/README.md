# Parallel-text-processing-using-MapReduce-MR-and-Hadoop-Distributed-File-System-HDFS

This problem was provided by researchers in the Classics department at UB. They have provided
two classical texts and a lemmatization file to convert words from one form to a standard or
normal form. In this case several passes through the documents were done. 


Pass 1: Lemmetization using the lemmas.csv file


Pass 2: Identify the words in the texts by <word <docid, [chapter#, line#]> for two documents>.


Pass 3: Repeat this for multiple documents.

1) Start hadoop
```
 start-hadoop.sh
```
2) Run chmod
```
chmod +x ./mapper3.py
chmod +x ./reducer3.py
```
2) Put the input files to the hadoop directory :-
```
hdfs dfs -put $HOME/Activity3/act3input act3input
```
3) Run hadoop mapreduce:
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.4.jar -mapper $HOME/Activity3/mapper3.py -reducer $HOME/Activity3/reducer3.py -input act3input -output act3out
```
4) Read output:
```
hdfs dfs -cat act3out/*
```
