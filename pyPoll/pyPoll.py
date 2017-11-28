#import modules 

import os
import csv



# define path and opening csv reader

csvpath = os.path.join("/Users/pooja/Documents/python-challenge/pyPoll", "election_data_1.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headerline = next(csvreader)
    rowcount=0
    mylist=[]
    candidate=[]
    test=[]
    percents=[]

  # looping through the rows of the csv file to get the number of votes ,list of candidtaes and their voting ratios  
    
    
    for row in csvreader:
        rowcount=rowcount+1
        mylist.append(row[2])
        if row[2] not in candidate:
            candidate.append(row[2])

    for y in candidate:
        test.append(mylist.count(y))

    for z in test:
        percents.append((z/rowcount)*100)


    best= test.index(max(test))
    print ( best)



        
    print ("Election Results")
    print("----------------------------------")
    print("The Total Number of votes are:"+ str(rowcount))
    print ("---------------------------------")
    #print(candidate)
    #print(test)
    #print(percents)
    print("-----------------------------------")

    # combining all three lists to define the winner  based on the maximum votes 
    
    for (a,b,c) in zip(candidate,percents,test):
        print (str(a) +":"+ str(b) +"%"+ "(" + str(c)+ ")")

    print ("-----------------------------------")
    print ("winner is:"+ candidate[best])


res=[rowcount,candidate, percents,test]
output_file = os.path.join("/Users/pooja/Documents/python-challenge/pyPoll","election_data_new.csv")
with open(output_file, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in res:
        writer.writerow([val])    





    