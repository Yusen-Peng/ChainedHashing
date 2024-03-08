"""
    developed hashtables for test cases
"""
from hashtable import HashTable 

def table_1():
    table = HashTable()
    table.__init__()
    return table

def table_2():
    table = HashTable()
    table.__init__(table_size=15)
    return table

def table_3():
    hashtable = HashTable()
    hashtable.__init__(table_size=6)
    hashtable.insert(3, "React")
    hashtable.insert(20, "Vue")
    return hashtable

def table_4():
    hashtable = HashTable()
    hashtable.__init__(table_size=6)
    hashtable.insert(3, "React")
    hashtable.insert(20, "Vue")
    hashtable.insert(5, 'Angular')
    return hashtable

def table_5():
    hashtable = HashTable()
    hashtable.__init__(table_size=6)
    hashtable.insert(3, "React")
    hashtable.insert(20, "Vue")
    hashtable.insert(5, 'Angular')
    hashtable.insert(39, 'Express')
    return hashtable

def table_6():
    hashtable = HashTable()
    hashtable.__init__(table_size=6)
    hashtable.insert(3, "React")
    hashtable.insert(20, "Vue")
    hashtable.insert(5, 'Angular')
    hashtable.insert(39, 'Express')
    return hashtable, hashtable.retrieve(3)

def table_7():
    hashtable = HashTable()
    hashtable.__init__(table_size=6)
    hashtable.insert(3, "React")
    hashtable.insert(20, "Vue")
    hashtable.insert(5, 'Angular')
    hashtable.insert(39, 'Express')
    return hashtable, hashtable.retrieve(39)

def table_8():
    hashtable = HashTable()
    hashtable.__init__(table_size=6)
    hashtable.insert(3, "React")
    hashtable.insert(20, "Vue")
    hashtable.insert(5, 'Angular')
    hashtable.insert(39, 'Express')
    return hashtable, hashtable.retrieve(5)

def table_9():
    hashtable = HashTable()
    hashtable.__init__(table_size=6)
    hashtable.insert(3, "React")
    hashtable.insert(20, "Vue")
    hashtable.insert(5, 'Angular')
    hashtable.insert(39, 'Express')
    return hashtable, hashtable.member(20)


def table_10():
    hashtable = HashTable()
    hashtable.__init__(table_size=6)
    hashtable.insert(3, "React")
    hashtable.insert(20, "Vue")
    hashtable.insert(5, 'Angular')
    hashtable.insert(39, 'Express')
    return hashtable, hashtable.member(39)

def table_11():
    hashtable = HashTable()
    hashtable.__init__(table_size=6)
    hashtable.insert(3, "React")
    hashtable.insert(20, "Vue")
    hashtable.insert(5, 'Angular')
    hashtable.insert(39, 'Express')
    return hashtable, hashtable.member(1024)

developed_table_1 = table_1()
developed_table_2 = table_2()
developed_table_3 = table_3()
developed_table_4 = table_4()
developed_table_5 = table_5()
developed_table_6, developed_return_6 = table_6()
developed_table_7, developed_return_7 = table_7()
developed_table_8, developed_return_8 = table_8()
developed_table_9, developed_return_9 = table_9()
developed_table_10, developed_return_10 = table_10()
developed_table_11, developed_return_11 = table_11()