
# from square import sqare_num


# def test_square_2():
#     assert(sqare_num(2) == 4)
    

# def test_square_3():
#     assert(sqare_num(3) == 9)
    


# def test_square_4():
#     assert(sqare_num(4) == 16)
    


# def test_square_5():
#     assert(sqare_num(5) == 25)

# File: test_mylibrary.py
# Pytest filename starts with "test_...."
import pytest
import pandas as pd
import logging
##################################
"""
Function to test
"""
def import_data(pth):
    df = pd.read_csv(pth)
    return df
##################################
"""
Fixture - The test function test_import_data() will 
use the return of path() as an argument
"""
@pytest.fixture(scope="module")
def path():
    return "data/test.csv"

##################################
"""
Test method
"""
def test_import_data(path):
    try:
        df = import_data(path)
        
    except FileNotFoundError as err:
        logging.error("File not found")
        raise err
        
	# Check the df shape
    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0

    except AssertionError as err:
        logging.error(
            "Testing import_data: The file doesn't appear to have rows and columns")
        raise err
    return df
##################################