import csv
import operator

sample = open('file1.csv', 'r')

csvTest = csv.reader(sample,delimiter=',')

sort = sorted(csvTest, key=operator.itemgetter(1))

for eachline in sort:
    print eachline