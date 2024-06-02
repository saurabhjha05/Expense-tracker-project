# #Create a simple personal expense tracker that allows users to log their daily expenses and view summaries.
 # ek file jisma tabular data form ma sab save hoga 3 columns ma 

#---------------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np 

class expense():

    def __init__(Self,category,amount,description): 
        Self.category = category
        Self.amount = amount
        Self.description = description
    def store_data(self):
           df = pd.DataFrame(data=exp_dict) #error
           df.to_csv("expenses.csv" , index = False)
           print("Data Stored Successfully 🥳")
           print("Total Expense Till Now Is : ",sum(total))
           print("-"*50)
           
    def full_summary(self): # to read file and show its data 
        pass

    def category_summary(self): # just add list of category wise expense
        pass

#---------------------------------------------------------------------------------------------------------------

exp_dict = {
    "Food" : [] , "Clothes" : [] , "Grocery" : [] , "Bills_Dues" : [] ,"Miscellaneous" : [] ,
    "Description" : []
}

total = [] # stores total expense

#---------------------------------------------------------------------------------------------------------------

def add_expense(): # add expense in list and store it in file
    print("-"*50)
    a = int(input("Enetr Amount Of Expense : "))
    total.append(a) #first adding expenditure to a list of total expense
    b=int(input("Select A Category : - \n 1.FOOD \n 2.CLOTHES \n 3.GROCERY \n 4.BILLS AND DUES \n 5.OTHER MISCELLANEOUS EXPENSE : "))

    #category wise addition of expenditure
    if b==1 :
        exp_dict["Food"].append(a)
    elif b==2:
        exp_dict["Clothes"].append(a) 
    elif b==3:
        exp_dict["Grocery"].append(a)
    elif b==4:
        exp_dict["Bills_dues"].append(a)     
    elif b==5:
        exp_dict["Miscellaneous"].append(a)
    else:
        print("invalid choice")
        add_expense()

    #adding description of expense
    print("-"*50)
    c=input("Enter Description Of Your Expense :  ")
    exp_dict["Description"].append(c)

    
    #to fill missing data with nan value so it doesnt throw an error while creating a datframe

    max_len = max(len(v) for v in exp_dict.values())  #maximum length of value list 

    for key in exp_dict:
        exp_dict[key] = exp_dict[key] + [np.nan]*(max_len-(len(exp_dict[key])))


    exp = expense(a,b,c)  #taking instance of exp class
    exp.store_data()

#---------------------------------------------------------------------------------------------------

def view_expense():
    view = input("Do You Want To View Full Summary Of Expenses Or Want to know category Wise Expense\n Enter 1 for full summary and 2 for category wise expense")
    if view == 1:
        pass# exp.full_summary()
    elif view == 2:
        pass# exp.category_summary()
    else:
        print("Enter A Valid Input")
        view_expense()

#---------------------------------------------------------------------------------------------------

#starting user interface

def starting_interface():
    print("="*50)
    print("WELCOME TO EXPENSE TRACKER 🙏 ")
    print("="*50)
    user = int(input("Press 1 To Add A New Expense \nPress 2 To View Expense :  "))

    if user == 1:
        add_expense()
    elif user == 2:
        view_expense()
    else:
        print("Enter A Valid Input")
        starting_interface()

#-----------------------------------------------------------------------------------------------

starting_interface()


