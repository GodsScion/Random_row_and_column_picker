# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:51:36 2021

@author: saivign
    
"""

#imports
import random


mr = 25   #max no of rows
mc = 15   #max no of columns
x = (0,0) #current random number
ch = ""   #choice


def regen():
    l=getWatchedList()
    x = (random.randint(1,mr) , random.randint(1,mc))
    while x in l:
        x = (random.randint(1,mr) , random.randint(1,mc))
    return x



def getWatchedList():    
    WatchedList=[] 
    file = open("A1Watched.txt","r")  #Read file content
    content = file.read()
    content = content.replace(" ","")
    content = content[1:len(content)-2]
    content = content.replace("(","")
    tempL = list(content.split("),"))
    file.close()    
    if tempL not in [[''],[]]:    
        for x in tempL:
            xt = tuple(map(int,x.split(",")))
            WatchedList.append(xt)
    return WatchedList



def addToWatchedList(r,c):
    l=getWatchedList()
    if (r,c) not in l:
        l.append((r,c))
    file = open("A1Watched.txt","w")
    file.write(str(l))
    file.close()



def delFromWatchedList(r,c):
    l=getWatchedList()
    l.remove((r,c))
    file = open("A1Watched.txt","w")
    file.write(str(l)) 
    file.close()       


try:  
    print("\n     Hi, Welcome to random generator! \n")
    print("     Simply close the window to stop the programm \n\n\n")
    while True:
        if ch in ["","1","2","3","4","5"]:
           
            if ch=="1" or ch=="":
                x = regen()
                print("          -->  ",x,"  <--   \n\n")
            
            elif ch=="2":
                addToWatchedList(x[0],x[1])
                print(getWatchedList(),"\n\n        is your updated Watched List. \n\n")
            
            elif ch=="3":
                
                print(getWatchedList(),"\n\n        is your current Watched List.\n\n        Would you like to edit it?:")
                ch1=input("            1) No (Press Enter or Type 1)\n            2) Yes (Type Anything except 1)\n")
                if ch1 not in ["1",""]:
                    ch1a=input("        What would you like to do?: \n            1) Cancel (Hit Enter or Type Anything) \n            2) Add to the list (Type 2) \n            3) Delete an element (Type 3) \n")                    
                    if ch1a in ["2","3"]:
                        while ch1a=="2":
                            try:
                                print("        NOTE: Only Natural numbers are allowed\n            Enter the row number r: (must be <= ",mr,")")
                                rn1=int(input())
                                print("\n            Enter the column number c: (must be <= ",mc,")")
                                cn1=int(input())
                                if rn1>0 and rn1<=mr and cn1>0 and cn1<=mc:
                                    addToWatchedList(rn1,cn1)
                                    print("        Added successfully, your updated Watched list is: \n ",getWatchedList())
                                    break
                                else:
                                    print("        Unsuccessful, Values are not in limits, Try again \n")
                            except:
                                print("        Invalid input or inputs, Try again\n")
                        while ch1a=="3":
                            try:
                                print("        NOTE: Only Natural numbers are allowed\n            Enter the row number r: (must be <= ",mr,")")
                                rn1=int(input())
                                print("\n            Enter the column number c: (must be <= ",mc,")")
                                cn1=int(input())
                                if rn1>0 and rn1<=mr and cn1>0 and cn1<=mc:
                                    if (rn1,cn1) in getWatchedList():
                                        delFromWatchedList(rn1,cn1)
                                        print("        Deleted successfully, your updated Watched list is: \n ",getWatchedList())
                                        break
                                    else:
                                        print("        Given element (",rn1,",",cn1,") is not in the list, Try again later\n")
                                else:
                                    print("        Unsuccessful, Values are not in limits, Try again \n")
                            except:
                                print("        Invalid input or inputs, Try again\n")
                
            elif ch=="4":
                print("        Your current max rows are: ",mr,"\n and current max columns are: ",mc)
                ch2a=input("        Would you like to edit?\n            1) No (Press Enter or Type 1)\n            2) Yes (Type Anything except 1)\n")
                while ch2a not in ["1",""]:
                    try:
                        rn1=int(input("        NOTE: Only Natural numbers are allowed\n     Enter the Max number of rows: "))
                        cn1=int(input("\n        Enter the Max number of columns: "))
                        if rn1>0 and cn1>0:
                            mr=rn1
                            mc=cn1
                            print("        Updated max values for rows = ",mr," and columns = ",mc,"\n")
                            break
                        else:
                            print("        Unsuccessful, Invalid values or value ( less than 0 or too big numbers) , Try again \n")
                    except:
                        print("        Invalid input or inputs, Try again\n")
            
            else:
                print("        Invalid input, Try again \n\n")
            ch = input("        What next?:\n        1) Regenerate again? (press Enter key or Type 1) \n        2) Add to current values to Watched list (Type 2) \n        3) Show or Edit current Watched list (Type 3) \n        4) Show no of rows and columns and Edit (Type 4) \n")
            print("-----------------------------------------------\n\n\n")

        else:
            ch="5"
            
                
            
except:
    print("     Sorry some error occured! Try the below solutions:\n")
    print("        1) Create an empty file named 'A1Watched.txt' in the same location of this program only if it does not exist. \n")
    print("        2) Check the data in A1Watched.txt file format must be like [(1,2),(1,9),(3,8)]   spaces dont matter. \n")
    print("        3) If not sure, then delete the A1Watched.txt file and create an new empty A1Watched.txt file, Name is Case sensitive\n")
    print("        4) The A1RandomGenerator.py program and A1Watched.txt file must be in same folder or location.")
    
