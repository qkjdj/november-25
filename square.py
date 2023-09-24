# def sqare_num(a):
#     return a**2
import pandas as pd
import logging

logging.basicConfig(
    filename = 'result.log',
    level= logging.INFO,
    filemode= 'w',
    format= '%(name)s - %(levelname)s - %(message)s')

def find_file(file_path):
    try:
       df = pd.read_csv(file_path)
       logging.info("Success: Your file has been read successfully.")
       logging.info(f"The number of row is {df.shape}")
       return df
    except FileNotFoundError:
        logging.error("Error: Given file not found")

df = find_file('data/test.csv')