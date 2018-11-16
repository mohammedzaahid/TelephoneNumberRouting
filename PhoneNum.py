import pandas as pd		 											                   #package used to implement data frames for operator and price lists.
import math             											                   #This library is used to split telephone number into its prefixes to match with operator lists
import unittest			 											                   #package imported for performing unit tests with regards to code and data provided
from pandas.util.testing import assert_frame_equal					                   #function to conduct unit tests and match my dataframes with expected dataframes


def first_n_digits(num1, n):
    return num1 // 10 ** (int(math.log(num1, 10)) - n + 1)		                        #Telephone Number is split with formula to obtain respective prefixes to match with data given


class DFTests(unittest.TestCase):								                      	#defining functions for unit tests to conduct on code
    def setUp(self, df1, df2):
        try:													                        #try used to catch and handle exceptions during unit tests after matching data i.e. Operator and price lists
            my_df1 = df1									                	    	#command statement for my_df1, my_df2 as data to match with given data in code
            my_df2 = df2
            #expected_df1=pd.read_csv("filepath",sep='\t')			                    #command to import excel file as CSV with operators and price lists
            #expected_df2=pd.read_csv("filepath",sep='\t')			                    #remove hashtag and paste path of file in place of filepath
            expected_df1 = pd.DataFrame({'Prefix': [1, 268, 46, 4620, 468, 4631, 4673, 46732], 'Cost-OperatorA': [0.9, 5.1, 0.17, 0.0, 0.15, 0.15, 0.9, 1.1]})	#expected_df1 defines data which is to be matched with data in body of code
            expected_df2 = pd.DataFrame({'Prefix': [1, 44, 46, 467, 48], 'Cost-OperatorB': [0.92, 0.5, 0.2, 1.3, 1.2]})
            pd.testing.assert_frame_equal(my_df1, expected_df1)                     	#match dataframes in body of code with expected dataframes
            pd.testing.assert_frame_equal(my_df2, expected_df2)
        except Exception as e:									                     	#handle case when data is not matched with data in body of code
            print("UNIT TEST FAILED", e)				           		            	#print output as unit test failed with percentage amount of error


if __name__ == '__main__':
    DFTests1 = DFTests()
    num1 = input("Enter the Telephone Number ")					                        #assigning input as num1 which is telephone number
    if num1.startswith('+'):									                	    #if statement where case is input given with +
        num1 = num1[1:]										                  	    	#statement to disregard + if input given as +TelephoneNumber
    else:
        num1 = num1
    num1 = int(num1)
    m = len(str(num1))  										                  	    #length of string num1 assigned to m
    a = 1               											                    #assigning variable a which enables string to start from 1 and not 0
    f = []															                    #assigning variable to give output with datatype as object
    g = []														                      	#assigning variable to give output in different case
    for a in range(0, m + 1):  									              	        #iteration run to find match of prefix in input
            n = first_n_digits(num1, a) 						          	            #after iteration done, splitting the matched prefix from Telephone Number as input
            df1 = pd.DataFrame({'Prefix': [1, 268, 46, 4620, 468, 4631, 4673, 46732], 'Cost-OperatorA': [0.9, 5.1, 0.17, 0.0, 0.15, 0.15, 0.9, 1.1]})	    #assigned dataframes as Prefixes and Price Lists in pandas package
            df2 = pd.DataFrame({'Prefix': [1, 44, 46, 467, 48], 'Cost-OperatorB': [0.92, 0.5, 0.2, 1.3, 1.2]})
            DFTests1.setUp(df1, df2)													#calling DFTests function to conduct test with expected and my dataframes
            df = pd.merge(df1, df2, how='outer', on='Prefix',) 						    #merging current dataframes together in outer way so all values are merged
            df['Minimum-Price'] = df[['Cost-OperatorA', 'Cost-OperatorB']].min(axis=1)	#calculating Minimum price in dataframes, and axis=1 for rows which are the costs in Operators
            if not df.loc[df['Prefix'] == n].empty:  				                    #if not statement to assign minimum price in both operators
                f = df.loc[df['Prefix'] == n]				    		                #assigning f as dataframe matching prefix with costs
                g = df.loc[df['Prefix'] == n, 'Minimum-Price']   	                    #assign g with value of Minimum price
                continue											                    #continue if not loop without termination
    if len(f) == 0:												                    	#statement to find length of object f for no match case
        print("Telephone Number Not Found in Any Operator")
    try:
        print(f)												                    #Respective operator can be understood as f is dataframe containing operator details
        print("Minimum price is", float(g))     					                    #Print Final MINIMUM PRICE OF TELEPHONE NUMBER, as g, float because g can be null value
    except Exception as e:											                    #giving error case as No match again for try operator
        print("Not Routed")
