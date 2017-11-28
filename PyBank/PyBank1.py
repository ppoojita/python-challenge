# import modules 

import os
import csv

# define path and opening csv reader

csvpath = os.path.join("/Users/pooja/Documents/python-challenge/PyBank", "budget_data_2.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headerline = next(csvreader)
    revenue=0
    rowcount=0
    avgrev=[]
    revch=[]
    datescsv=[]
    
    
    for row in csvreader:
        revenue= revenue + int(row[1])
        rowcount=rowcount+1
        #month,day=row[0].split('-')
        avgrev.append(row[1])
        #print(avgrev)
        datescsv.append(row[0])
        #print(datescsv)
        
        
          
    #calculating the total number of months
    print("The Total Number of Months are:"+str(rowcount))
    # calculating the revenue over the entire period
    print("The total revenue over the period is:"+str(revenue))
    #print(avgrev)
    revch=[int(t) - int(s) for s, t in zip(avgrev, avgrev[1:])]
    #print(revch)
    count=len(revch)
    revchtotal=sum(revch)
    average=revchtotal/count
    print ("The average change by month over the period of time is:"+str(average))
    
   
    maxi=max(revch)
    mini=min(revch)
    
    mxin=revch.index(maxi)
    mnin=revch.index(mini)
    
    #print(datescsv[mxin+1])
    #print(datescsv[mnin+1])
    
    
    print("The greatest increase in revenue over a period of time is:"+str(max(revch))+"and date is:"+str(datescsv[mxin+1]))
    print("The greatest decrease in revenue over a period of time is:"+str(min(revch))+"and date is:"+str(datescsv[mnin+1]))
     
    
    
            