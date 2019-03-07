# Merging data test
# (1) Clients Data (2) Purchase Data
# Merge data (1) & (2) into one string


def mergeTest(clients, purchase): 
    return(purchase.update(clients)) 
      

#Enter data vlaues
clients = {'id': 101, 'first_name': 'Tom'} 
purchase = {'id': 101, 'loyalty_points': 450} 
  

print(mergeTest(clients, purchase)) 
  

print(purchase) 


# Output:

# manually entered data is printed in a single string
# id attribute is the common attribute between both data sets