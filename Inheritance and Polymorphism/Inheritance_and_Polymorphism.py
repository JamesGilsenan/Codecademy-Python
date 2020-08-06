class SortedList(list):

    def __init__(self, list):
        super().__init__(list)
        self.sort()

    def append(self, value):
        super().append(value)
        self.sort()
        return self


class FallbackDict(dict):
    
    def get(self, key):
        fallback_value = "Key does not exist"
        super().get(key, fallback_value)
        if key in self:
            return key
        else:
            return fallback_value        


mylist = SortedList([1,5,3,9])
#print(mylist)
mylist.append(2)
#print(mylist)

mydict = FallbackDict({"Mary": 20, "George": 18, "Jack": 12})
print(mydict.get("John"))
