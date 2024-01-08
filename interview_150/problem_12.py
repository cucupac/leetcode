import random


class RandomizedSet:
    def __init__(self):
        self.list = list()
        self.set_dict = dict()

    def insert(self, val: int) -> bool:
        val_index = self.set_dict.get(val)
        if val_index is None:
            # Add to dict
            insert_index = len(self.list)
            self.set_dict[val] = insert_index

            # Add to list
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        val_index = self.set_dict.get(val)
        if val_index is not None:
            # remove from dict no matter what
            del self.set_dict[val]

            # remove from list -- swap if list has more than 1 element
            if len(self.list) > 1:
                if self.list[val_index] != self.list[-1]:
                    self.list[val_index], self.list[-1] = (
                        self.list[-1],
                        self.list[val_index],
                    )
                    # update index of swapped elem to val_index, thereby maintaining index order
                    self.set_dict[self.list[val_index]] = val_index
            self.list.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)


"""
Learnings:
>> random.choice allows for equal probability choices between elements in a list.

>> in this case, elems are always appended to the end of the list, so we know the insertion index -> len(my_list)

>> an element can be removed from a list via O(1) by swapping it with the last elem my_list[-1]
   and my_list.pop()
"""
