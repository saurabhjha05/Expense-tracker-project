# # #Create a simple personal expense tracker that allows users to log their daily expenses and view summaries.
#  # ek file jisma tabular data form ma sab save hoga 3 columns ma 

# #---------------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np 
import os
import matplotlib.pyplot as plt 

class expense():

    def __init__(Self,category,amount,description): 
        Self.category = category
        Self.amount = amount
        Self.description = description
    def store_data(self):
        df = pd.DataFrame(data=exp_dict)
        file_path = 'expenses.csv'      
        file_exists = os.path.isfile(file_path)   #if file exist it will not add header again and again 
        df.to_csv("expenses.csv" , index = False , mode="a", header= not file_exists)
        print("Data Stored Successfully 🥳")
        print("-"*70)

#---------------------------------------------------------------------------------------------------------------           

def full_summary(): # to read file and show its data 
        pt = pd.read_csv("expenses.csv")
        print(pt) #prints complete dataframe

        #it will include only numeric datatype excluding nan and string .sum()to take sum of each colum
        total = pt.select_dtypes(include=[np.number]).sum() 
        print("-"*70)
        print("TOTAL MONEY💸 SPENT TILL NOW IS RS.",total.sum())           #returning total spent in all category
        print("YOU SPENT MAXIMUM ON",total.idxmax(),"= Rs.",total.max())   #returning category with maximum expenditure
        print("-"*70)

        graph = input("Do You Want To View Category-Wise Pie Chart Distribution\nThen Enter 'Y' else Enter Any Value to exit : ")
        if graph.lower() == "y" :
            col_name = pt.select_dtypes(include=[np.number]).columns       #selecting only column with integer value
            s = pt[col_name].sum()
            color_pallete = ["#ef476f","#ffd166","#06d6a0","#118ab2","#073b4c"]
            plt.pie(s,labels=["Food","Clothes","Grocery","Bills and Dues","Miscellaneous"],colors= color_pallete)
            plt.title("CATEGORY WISE EXPENDITURE DISTRIBUTION")
            plt.show()                                                     #plotting pie chart categorywise
        else:
            pass

def category_summary(): # show complete data of a perticular category
        pt = pd.read_csv("expenses.csv")
        select_category = int(input("Select A Category : - \n 1.FOOD \n 2.CLOTHES \n 3.GROCERY \n 4.BILLS AND DUES \n 5.OTHER MISCELLANEOUS EXPENSE : "))

        if select_category==1 :
            col = "Food"
        elif select_category==2:
            col = "Clothes"
        elif select_category==3:
            col = "Grocery"
        elif select_category==4:
            col = "Bills_Dues"   
        elif select_category==5:
            col = "Miscellaneous"
        else:
            print("⛔ Invalid Choice")
            
        print(pt.loc[:,[col]]) #printing all rows and selected column

#---------------------------------------------------------------------------------------------------------------

#dictionary with category as key and empty list as value 
exp_dict = {
    "Food" : [] , "Clothes" : [] , "Grocery" : [] , "Bills_Dues" : [] ,"Miscellaneous" : [] ,
    "Description" : []
} 

#---------------------------------------------------------------------------------------------------------------

def add_expense(): # add expense in dictionary and store it in file
    
    a = int(input("Enetr Amount Of Expense : "))

    b=int(input("Select A Category : - \n 1.FOOD \n 2.CLOTHES \n 3.GROCERY \n 4.BILLS AND DUES \n 5.OTHER MISCELLANEOUS EXPENSE : "))

    #category wise addition of expenditure
    if b==1 :
        exp_dict["Food"].append(a)
    elif b==2:
        exp_dict["Clothes"].append(a) 
    elif b==3:
        exp_dict["Grocery"].append(a)
    elif b==4:
        exp_dict["Bills_Dues"].append(a)     
    elif b==5:
        exp_dict["Miscellaneous"].append(a)
    else:
        print("⛔ Invalid Choice")

    #adding description of expense
    print("-"*70)
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
    view = int(input("Do You Want To View Full Summary Of Expenses Or \nWant to know category Wise Expense\nEnter 1 For Full Summary And \nEnter 2 For Category Wise Expense : "))
    print("-"*70)
    if view == 1:
        full_summary()
    elif view == 2:
        category_summary()
    else:
        print("⛔ Enter A Valid Input\n")
        view_expense()

#---------------------------------------------------------------------------------------------------

#starting user interface

def starting_interface():
    print("="*70)
    print("                    WELCOME TO EXPENSE TRACKER 🙏 ")
    print("="*70)
    user = int(input("\nPress 1 To Add A New Expense \nPress 2 To View Expense :  "))
    print("-"*70)

    if user == 1:
        add_expense()
    elif user == 2:
        view_expense()
    else:
        print("Enter A Valid Input")
        starting_interface()
        

#-----------------------------------------------------------------------------------------------

starting_interface()


