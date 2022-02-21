The Work consists entirely of:

i) 2 .py files with python3.7 implementation language
ii) 3 csv output files 'predicted.csv', 'new_representation.csv' and 'output'
iii) 4 input files 'nn_representation.csv', 'actual.csv', the neural network 'WindDenseNN.h5' and the cluster.conf
iv) The source files cluster.cpp, hashtable.cpp and the cluster.h, hashtable.h header files used in Clustering-Project to generate the output file with the silhuette results.

A) In order to create the csv predicted file type:
 'python3.7 predict.py -i inputfile'
The predict.py file receives as input the WindDenseNN.h5 neural network and creates
a dataframe that will store the input file (In our case nn_representation.csv) which we will use
to predict and produce the desired result in the result variable (line 23).
Then in lines 28-39 we make the transformations required to calculate the required errors. Finally,
we export csv with the results.

B) In order to create the csv new_representation file, type:
'python3.7 new_representation.py -i inputfile'
Respectively here we first load the neural network WindDenseNN.h5.
In line 21 we initialize the weights of the first layer of the model and then in the lines
26-29 we do some transformations and compilation to properly configure the levels and the
new dimensions that are requested. Then we load the result of the new base and export it to csv.

C) Execution command './cluster -i new_representation.csv -c cluster.conf -o output'
Here the program is about clustering using algorithms such as LSH, Lloyd etc, with the only difference that the input file is different
and the separator for the name and the coords is the comma (,).In addition,now the total points are 23988 making the programm slow  to export the results, so in line 53-54 of cluster.cpp we have put a condition to read the first 5000. If we want everything to be read then we just have to put these 2 lines in comments. We export the results through Silhuette and in the name of centroid we put the timestamp.

Execute the commands in questions A, B and C sequentially.

Implementation language of .py files: python3.7
File implementation language in c: C++

Regarding C: 'make' command for compilation and 'make clean' for cleaning object files.
Tested in Linux environment.