#!/home/virtual_envs/fake_data/bin/python3

@profile
def func_numeric(type_str):
    print(f"\n\n>>>>>>>>>>{type_str}<<<<<<<<<<<")
    lst = []
    for i in range(int(input(f"How many {type_str} column you need? "))):
        print("\n")
        min=int(input("Min: "))
        max=int(input("Max: "))
        if max <= min:
            max=int(input(f"Please enter number grter then {min} "))
        name=input("Column name: (press Enter to auto generation) ")
        distribution=input("Distribution: ")
        lst.append([min,max,distribution])
    return lst
@profile
def func_date(type_str):
    print(f"\n\n>>>>>>>>>>{type_str}<<<<<<<<<<<")
    lst = []
    for i in range(int(input(f"How many {type_str} column you need? "))):
        print("\n")
        min=input("Min: ")
        max=input("Max: ")
        
        if max <= min:
            max=int(input(f"Please enter number grter then {min} "))
        name=input("Column name: (press Enter to auto generation) ")
        distribution=input("Distribution: ")
        lst.append([min,max,distribution])
    return lst
# Integer
# list_INTEGER = func_numeric("INTEGER")
# list_FLOAT = func_numeric("FLOAT")
list_DATE = func_date("DATE")
list_DATE_TIME = func_date("DATE-TIME")
# breakpoint()

from faker import Faker
import numpy as np
import pandas as pd
import os
import sys
import numpy as np

dict_to_csv = {'Type': {0: 'Integer', 1: 'Float', 2: 'Date', 3: 'DateTime'},'Min': {0: ' ', 1: ' ', 2: ' ', 3: ' '},'Max': {0: ' ', 1: ' ', 2: ' ', 3: ' '},'Distribution': {0: ' ', 1: ' ', 2: ' ', 3: ' '},'Count': {0: ' ', 1: ' ', 2: ' ', 3: ' '}}

n_rows = int(input("nrows: "))

df = pd.DataFrame(dict_to_csv)
df.to_csv("/tmp/dict_to_csv.csv", index=False)
os.system("gopen /tmp/dict_to_csv.csv")


input("\n\nFill the file and then press any button here ....... ")
df2 = pd.read_csv("/tmp/dict_to_csv.csv")
if df.eq(df2).all().all():
    print("\nYou didn't fill any number. \nExiting ..........")
    sys.exit()




df2 = df2[df2.Count.ne(" ") & ~df2.Count.isin(["FLOAT", "DATETIME", "STRING", "OTHER"])][['INTEGER', 'Count']]
dict_ = df2.set_index("INTEGER").to_dict()['Count']
# dict_ = {'random_digit': '5', 'random_int': '3', 'random_number': '1', 'date': '3'}


Faker.seed(4321)
fake = Faker('en_US')
data = {}
for k, count in dict_.items():
    for i in range(int(count)):
        com = f"fake.{k}()"
        random_ganerated_vals = [eval(com) for _ in range(n_rows)]
        data[f"{k}-{i}"] = random_ganerated_vals
df = pd.DataFrame(data)

orig_name = "/home/amir/fake_data"
name = orig_name
n = 1
while os.path.exists(name + ".csv"):
    name = f"{orig_name}_{n}"
    n += 1
df.to_csv(name+".csv", index=False)
print(f"\n\nYou fake data saved as {name+'.csv'}\n")
