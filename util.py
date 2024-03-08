from hashtable import HashTable
"""
    a bunch of utility functions to simplify the test benchmark.

"""

"""
    write a test case description header
"""
def description(num_case: int, method: str, table_size: int = 10, input_param=None):
    print(f"\nThis is test case #{num_case}")
    print(f"The method being tested: {method}")
    print(f"The size of the hashtable: {table_size}")
    if input_param != None: print(f"The test input: {input_param}")

"""
    print and compare two hashtables
"""
def print_and_compare(table1: HashTable, table2: HashTable, num_case: int, method: str, data1=None, data2=None):
    if(_table_compare(table1, table2) and _return_compare(method, data1, data2)):
        print(f"CONGRATS! test case #{num_case} passed.")
    else:
        print(f"ERROR! test case #{num_case} failed!")
        print("Loser, try it again!")

"""
    print a developed hashtable
"""
def _table_developed_print(hashtable: HashTable):
    for entry in range(len(hashtable.table)):
        print(f"entry{entry}: {hashtable.table[entry]}")

"""
    print an expected hashtable
""" 
def _table_expected_print(hashtable: list):
    for entry in range(len(hashtable)):
        print(f"entry{entry}: {hashtable[entry]}") 

"""
    compare two hashtables
"""
def _table_compare(table1: HashTable, table2: list):
    print("-----------------------------------------------")
    print("developed table:")
    _table_developed_print(table1)
    print("-----------------------------------------------")
    print("expected table:")
    _table_expected_print(table2)

    if table1.size != len(table2):
        return False
    else:
        for i in range(table1.size):
            list1 = table1.table[i]
            list2 = table2[i]
            if len(list1) != len(list2):
                return False
            else:
                for j in range(len(list1)):
                    if list1[j] != list2[j]:
                        return False
        return True

"""
    compare data returned
"""
def _return_compare(method, data1, data2):
    if method != "retrieve" and method != "member":
        return True
    else:
        print("-----------------------------------------------")
        print("developed return:")
        print(data1)
        print("-----------------------------------------------")
        print("expected return:")
        print(data2)
        print("-----------------------------------------------")
        return data1 == data2