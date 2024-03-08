"""
    Hashtable implementation with chained hashing

    table: 
        the internal hashtable represented by a list of lists
    size: 
        the hashtable size
"""

"""
    calculate the hash value of the key
"""
def _hash_function(key: int, table_size: int):
    return key % table_size

class HashTable():
    """
        initialize the hashtable (default table_size = 10)
    """
    def __init__(self, table_size=10):
        #assign the table size
        self.size = table_size

        #empty table initialzation
        self.table = [None] * table_size
        for i in range(table_size):
            self.table[i] = []
        
    """
        insert a key-data pair to the hashtable
    """
    def insert(self, key: int, data):
        entry_num = _hash_function(key, self.size)
        self.table[entry_num].append((key, data))

    """
        retrieve the data of the given key
    """
    def retrieve(self, key: int):
        for i in range(self.size):
            for (k, data) in self.table[i]:
                if k == key:
                    return data
        return None
    
    """
        Check if a given key is in the hashtable
    """
    def member(self, key: int):
        for i in range(self.size):
            for (k, data) in self.table[i]:
                if k == key:
                    return True
        return False

    