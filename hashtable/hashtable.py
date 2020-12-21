from linkedList import LinkedList
from linkedList import Node
# class HashTableEntry:
#     """
#     Linked List hash table key/value pair
#     """
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
#     def __str__(self):
#         return f'{self.key}, {self.value}'

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity if capacity > 8 else MIN_CAPACITY
        self.list = [LinkedList()] * self.capacity
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.list)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.count / len(self.list)

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #find the slot for the key
        slot = self.hash_index(key)

        #search the linked list for the key
        searchResult = self.list[slot].find(key)
        #if the result is not None update the value othwerise make a new node with the entry
        if searchResult is not None:
            searchResult.value = value
        else:
            self.count += 1
            self.list[slot].insert(Node(key, value))

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        #find the slot for the key
        slot = self.hash_index(key)

        #search the linked list for the key
        searchResult = self.list[slot].find(key)
        
        if searchResult is not None:
            self.count -= 1
            return self.list[slot].delete(searchResult)
        #else return none
        else:
            return searchResult
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        #find the slot for the key
        slot = self.hash_index(key)

        #search the linked list for the key
        searchResult = self.list[slot].find(key)
        if searchResult is not None:
            return searchResult.value
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        #make a new list with the new capacity
        new_list = [LinkedList()] * new_capacity
        self.count = 0
        #loop through the old list
        for i in self.list:
            #get a reference to the linked list
            ll = i
            #traverse the linked list
            current = ll.head
            while current is not None:
                #rehash all the keys
                slot = self.djb2(current.key) % new_capacity
                #insert into new list
                self.count += 1
                new_list[slot].insert(Node(current.key, current.value))
                current = current.next
        #update the capcity
        self.capacity = new_capacity
        #make self.list = new_list
        self.list = new_list

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")


     
    ht.delete("line_1")
    ht.delete("line_2")
    ht.delete("line_3")
    ht.delete("line_4")
    ht.delete("line_5")

    ht.get("line_1")
    ht.get("line_2")
    ht.get("line_3")
    ht.get("line_4")
    ht.get("line_5")
    ht.get("line_6")
    ht.get("line_7")
    ht.get("line_8")
    ht.get("line_9")
    ht.get("line_10")
    ht.get("line_11")
    ht.get("line_12")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
