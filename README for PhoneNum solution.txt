FILE NAME: PhoneNum.py (Solution Number 2)
PROGRAM TITLE: Telephone Number routing with Operators by Zaahid Mohammed

GETTING STARTED
Delivered to alaTest.com 
Developed in python3 package.
The application functions to route a telephone number with its cheapest operator. 

RUNNING THE APPLICATION: 
Extract the ‘TelephoneNumber_Router.zip’.
Run PhoneNum.py using python3.
Install required packages; pandas, math, unittest.

EXAMPLE: 
The output for this program is given in form of a table pointing out the respective prices for all operators and then finally showing the minimum price of the telephone number that is routed.
The user may identify which Operator has the minimum price from the table. 
MANIPULATING CODE FOR FUNCTIONS:
1. Adding more operators and price lists:
"""expected_dfN=pd.read_csv("filepath",sep='\t')"""
This command can be used to add operators that will be imported from CSV Excel files, with columns as Operators and Costs. 

2. Also, Operators and price lists can be added as dataframes after code line, 55 which has df1 and df2 as Operator A and Operator B. These Operators are defined as variables dfs1 and dfs2 and are named henceforth. 
To add new operators and price lists, same format may be used. 
Format for adding Operators and Price lists:
###dfN = pd.DataFrame({'Prefix': [prefix, prefix, prefix,......], 'Cost-OperatorX': [price, price, price,......]})####
Also, the number of dataframes added have to be mentioned in line 43, as df3, and so on. 

Subsequently, these dataframes must be added in the unittest part of the code, which is after line 19. 

###expected_dfN = pd.DataFrame({'Prefix': [prefix, prefix, prefix,......], 'Cost-OperatorX': [price, price, price,......]})####
###pd.testing.assert_frame_equal(my_dfN, expected_dfN)###

This is for unittest to work, and check whether expected dfN(Prefix) is same as given dfN. 
