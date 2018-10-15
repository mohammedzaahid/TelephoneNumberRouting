# TelephoneNumberRouting
PROJECT TITLE: Telephone Number Routing with Operators by Zaahid Mohammed

GETTING STARTED
Delivered to alaTest.com 
Developed in python3 package.
The application functions to route a telephone number with its cheapest operator. 

RUNNING THE APPLICATION: 
Extract the ‘TelephoneNumber_Router.zip’.
Run phoneNum.py using python3.
Install required packages; pandas, math, unittest.


MANIPULATING CODE FOR FUNCTIONS:
1. Adding more operators and price lists:
Operators and price lists can be added as dataframes after code line, 55 which has df1 and df2 as Operator A and Operator B. These Operators are defined as variables dfs1 and dfs2 and are named henceforth. 
To add new operators and price lists, same format may be used. 
Format for adding Operators and Price lists:
###dfN = pd.DataFrame({'Operator': [prefix, prefix, prefix,......], 'Cost': [price, price, price,......]})####
###dfsN = {'Operator X ': dfN}###

Subsequently, these dataframes must be added in the unittest part of the code, which is after line 14. 

###expected_dfN = pd.DataFrame({'Operator': [prefix, prefix, prefix,......], 'Cost': [price, price, price,......]})####
###pd.testing.assert_frame_equal(my_dfN, expected_dfN)###

This is for unittest to work, and check whether expected dfN(operator) is same as given dfN. 
