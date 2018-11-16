import pandas as pd		 											#package used to implement data frames for operator and price lists.
import math             											#This library is used to split telephone number into its prefixes to match with operator lists
import unittest			 											#package imported for performing unit tests with regards to code and data provided
from pandas.util.testing import assert_frame_equal					#function to conduct unit tests and match my dataframes with expected dataframes


def first_n_digits(num1, n):
    return num1 // 10 ** (int(math.log(num1, 10)) - n + 1)			#Telephone Number is split with formula to obtain respective prefixes to match with data given


class DFTests(unittest.TestCase):									#defining functions for unit tests to conduct on code
    def setUp(self, df1, df2):
        try:														#try used to catch and handle exceptions during unit tests after matching data i.e. Operator and price lists
            my_df1 = df1											#command statement for my_df1, my_df2 as data to match with given data in code
            my_df2 = df2
            #expected_df1=pd.read_csv("filepath",sep='\t')			#command to import excel file as CSV with operators and price lists 
            #expected_df2=pd.read_csv("filepath",sep='\t')			#remove hashtag and paste path of file in place of filepath
            expected_df1 = pd.DataFrame({'Operator': [1, 268, 46, 4620, 468, 4631, 4673, 46732], 'Cost': [0.9, 5.1, 0.17, 0.0, 0.15, 0.15, 0.9, 1.1]})	#expected_df1 defines data which is to be matched with data in body of code
            expected_df2 = pd.DataFrame({'Operator': [1, 44, 46, 467, 48], 'Cost': [0.92, 0.5, 0.2, 1.3, 1.2]})
            pd.testing.assert_frame_equal(my_df1, expected_df1)		#match dataframes in body of code with expected dataframes
            pd.testing.assert_frame_equal(my_df2, expected_df2)
        except Exception as e:										#handle case when data is not matched with data in body of code
            print("UNIT TEST FAILED", e)							#print output as unit test failed with percentage amount of error


def func2(dat):
    try:
        for key, value in dat.items():
            for name, values in value.iterrows():
                if values.Operator == first_n_digits(num1, 1):       #checking and matching prefix value till 1st digit
                    a = values.Cost
                elif values.Operator == first_n_digits(num1, 2):     #checking and matching prefix value till 2nd digit
                    a = values.Cost
                elif values.Operator == first_n_digits(num1, 3):     #checking and matching prefix value till 3rd digit
                    a = values.Cost
                elif values.Operator == first_n_digits(num1, 4):     #checking and matching prefix value till 4th digit
                    a = values.Cost
                elif values.Operator == first_n_digits(num1, 5):     #checking and matching prefix value till 5th digit
                    a = values.Cost


        return a, key
    except Exception as e:
        print("Not "+key)


if __name__ == '__main__':
    DFTests1 = DFTests()
    num1 = input('Enter the Telephone Number ')						 #assigning input as num1 which is telephone number
    if num1.startswith('+'):										 #if statement where case is input given with +
        num1 = num1[1:]												 #statement to disregard + if input given as +TelephoneNumber
    else:
        num1 = num1
    num1 = int(num1)                                                #assigning num1 as integer for matching prefix
    df1 = pd.DataFrame({'Operator': [1, 268, 46, 4620, 468, 4631, 4673, 46732], 'Cost': [0.9, 5.1, 0.17, 0.0, 0.15, 0.15, 0.9, 1.1]})       #assigned dataframes as Operators and Price Lists in pandas package
    df2 = pd.DataFrame({'Operator': [1, 44, 46, 467, 48], 'Cost': [0.92, 0.5, 0.2, 1.3, 1.2]})
    dfs1 = {'Routed by Operator A': df1}                            #assigning names as per required output to dataframes to conduct tests
    dfs2 = {'Routed by Operator B': df2}
    DFTests1.setUp(df1, df2)                                        #calling DFTests function to perform test to match prefix in dataframes
    y = func2(dfs1)                                                 #assigning y and z variable to defined dataframes
    z = func2(dfs2)
    if y is None:                                                   #statement to find out match in dfs1, Operator A
        c = z
    elif z is None:                                                 #statement to find out match in dfs2, Operator B
        c = y
    else:                                                           #when match is found in both operators
        c = min(y, z)                                               #to calculate minimum of both matches

    print("Minimum price is", c)
