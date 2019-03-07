#Thomas Devery
# import client & purchase csv files
import csv
import operator

def links():
    print(" ")
 
    # Open CSV Files
    with open('file1.csv') as fileone, open('file2.csv') as filetwo:

        # DictReader to access the information by numbers
        csv_one = csv.DictReader(fileone)
        csv_two = csv.DictReader(filetwo)
        
        num_dict = {row['id']:row['last_name'] for row in csv_one}
        link_dict = {row['id']:row['loyalty_points'] for row in csv_two}  
 
        
        # Header information
        print("Client Retention Tool")
        print("Top Loyalty Card Clients")
        print(" ")
        print('--------------------------------------------')
        print(" ")
        
        # Sort file1.csv by client last_name
        sample = open('file1.csv', 'r')
        csv1 = csv.reader(sample,delimiter=',')
        sort = sorted(csv1, key=operator.itemgetter(4), reverse=True)   
        
        for eachline1 in sort:
            print eachline1
        
        print(" ")
        print('--------------------------------------------')
        print(" ")
        
        # Sort file2.csv by Loyalty_points
        sample = open('file2.csv', 'r')
        csv1 = csv.reader(sample,delimiter=',')
        sort = sorted(csv1, key=operator.itemgetter(3), reverse=True)
        
        for eachline in sort:
            print eachline

links()


# Output:

# client.csv & purchase.csv data imported
# Sorted - Descending order on Loyalty attribute