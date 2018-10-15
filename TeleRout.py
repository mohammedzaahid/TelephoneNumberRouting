import pandas as pd     #package used to implement data frames for operator and price lists.
import math             #This library is used to split telephone number into its prefixes to match with operator lists
import unittest         #package imported for performing unit tests with regards to code and data provided


class DFTests(unittest.TestCase):
    def setUp(self, df):
        try:
            my_df1 = df1
            my_df2 = df2
            expected_df1 = pd.DataFrame({'Operator': [1, 268, 46, 4620, 468, 4631, 4673, 46732], 'Cost': [0.9, 5.1, 0.17, 0.0, 0.15, 0.15, 0.9, 1.1]})
            expected_df2 = pd.DataFrame({'Operator': [1, 44, 46, 467, 48], 'Cost': [0.92, 0.5, 0.2, 1.0, 1.2]})
            """addition of data frames in 'main' leading to more expected data frames for unit tests"""
            pd.testing.assert_frame_equal(my_df1, expected_df1)             #matching data frame to data frame in 'main'
            pd.testing.assert_frame_equal(my_df2, expected_df2)
        except Exception as e:
            print("Unit Test failed ", e)


def first_n_digits(num1, n):
    return num1 // 10 ** (int(math.log(num1, 10)) - n + 1)


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
        print("Not Found in "+key)


if __name__ == '__main__':
    DFTests1 = DFTests()
    num1 = input("Enter the Telephone Number ")
    if num1.startswith('+'):        #if user inputs telephone number with +, it is disregarded
        num1 = num1[1:]
    else:
        num1 = num1
    num1 = int(num1)

    df1 = pd.DataFrame({'Operator': [1, 268, 46, 4620, 468, 4631, 4673, 46732], 'Cost': [0.9, 5.1, 0.17, 0.0, 0.15, 0.15, 0.9, 1.1]})
    df2 = pd.DataFrame({'Operator': [1, 44, 46, 467, 48], 'Cost': [0.92, 0.5, 0.2, 1.0, 1.2]})
    """Operator and price list can be added here."""
    dfs1 = {'Operator A ': df1}         #naming data frames as particular operators
    dfs2 = {'Operator B ': df2}
    DFTests1.setUp(df1)
    DFTests1.setUp(df2)
    y = func2(dfs1)
    z = func2(dfs2)

    if y is None:
        c = z
    elif z is None:
        c = y
    else:
        c = min(y, z)

    print(c)
