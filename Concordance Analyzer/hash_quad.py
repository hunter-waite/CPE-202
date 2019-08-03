
class HashTable:

    def __init__(self, table_size=191):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index,
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number that the word appears on.
        If the key is not already in the table, then the key is inserted, and the value is used as the first
        line number in the list of line numbers. If the key is in the table, then the value is appended to that
        key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        #gets the index of where the value should go
        index = self.horner_hash(key)
        #if the index is empty just insert that mf and the value
        if self.hash_table[index] == None:
            self.hash_table[index] = [key,value]
            #increases the number of items after insertion
            self.num_items += 1
        #if the index isn't empty but it has the same key insert just the new value
        elif key in self.hash_table[index]:
            self.hash_table[index].append(value)
        #this handles the quadratic probing
        else:
            #start for the probe index is 1
            i = 1
            #variable for the while loop
            t = False
            #saves the initial index
            init_index = index
            #loops until the probing is sucessful
            while not t:
                #creates the new index based on the probe
                index = init_index + i**2
                #if the new index is greater than the table size then loop back around to the beginning
                while index >= self.table_size:
                    index = index - self.table_size
                #if the index is empty just insert that mf and the value
                if self.hash_table[index] == None:
                    self.hash_table[index] = [key,value]
                    #exits the while loop because probe was sucessful
                    t = True
                    #increases the number of items after insertion
                    self.num_items += 1
                #if the index isn't empty but it has the same key insert just the new value
                elif key in self.hash_table[index]:
                    self.hash_table[index].append(value)
                    #exits the while loop because probe was sucessful
                    t = True
                #otherwise keep the while loop going
                else:
                    i += 1
        #handles the change of table size(when it becomes greater then 1/2)
        if self.get_load_factor() > .5:
            #list the will store all the data from the hash table
            values = []
            #adds all the data into the list
            for i in range(self.table_size):
                if not self.hash_table[i] == None:
                    values.append(self.hash_table[i])
            #creates the new table size
            self.table_size = (self.table_size*2)+1
            #sets everything back to None
            self.hash_table = [None]*self.table_size
            #returns the number of items to 0
            self.num_items = 0
            #inserts all the old data into the newly sized hash table
            for i in range(len(values)):
                for j in range(1,len(values[i])):
                    self.insert(values[i][0],values[i][j])


    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        hash_key = 0
        min = len(key)
        if len(key) >= 8:
            min = 8
        i = 0
        while i < min:
            hash_key += (ord(key[i])*(31**(min-1-i)))
            i+=1
        return hash_key%(self.table_size)

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        index = self.horner_hash(key)
        init_index = index
        i = 1
        while not self.hash_table[index] == None and not key == self.hash_table[index][0]:
            index = init_index + i**2
            while index >= self.table_size:
                index = index - self.table_size
            i += 1
        if self.hash_table[index] == None:
            return False
        return True

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key.
        If there is not an entry with the provided key, returns None."""
        index = self.horner_hash(key)
        init_index = index
        i = 1
        while not self.hash_table[index] == None and not key == self.hash_table[index][0]:
            index = init_index + i**2
            while index >= self.table_size:
                index = index - self.table_size
            i += 1
        if self.hash_table[index] == None:
            return None
        return index

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        ret_list = []
        for i in range(len(self.hash_table)):
            if not self.hash_table[i] == None:
                ret_list.append(self.hash_table[i][0])
        return ret_list

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key.
        If key is not in hash table, returns None."""
        if not self.in_table(key):
            return None
        return self.hash_table[self.get_index(key)][1:]

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size
'''
h = HashTable(7)
h.insert('cat',11)
h.insert('cat',31)
h.insert('dog',11)
h.insert('mouse',11)
h.insert('elephant',11)
print(h.hash_table)
'''