
#Thomas Devery
# import CSV data
# using DictReader to convert CSV data into dictonaries

import csv
import operator

def links():

    # Open CSV files
    with open('file1.csv') as clients, open('file2.csv') as purchase:

        # DictReader to read the CSV data
        csv_clients = csv.DictReader(clients)
        csv_purchase = csv.DictReader(purchase)

         # Convert CSV data into dictonaires
        purchase_dict = {row['id']:row['loyalty_points'] for row in csv_purchase}
        client_dict = {row['id']:row['first_name'] for row in csv_clients}  

    # Header info
    print("ID", "Loyalty Points")

    # Print information from dictonaries
    for num, status in purchase_dict.items():


        # Calling purchase_dict.get() - values pulled from the dictonaries
        # To return a default value of a empty string - To avoid an exception
        print(num, status)
        

links()