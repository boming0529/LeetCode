class Algorithm(object):
    def binary_search(self, data ,key, lower = 0, upper = None):
        if upper is None : upper = (len(data) - 1)
        mid = (len(data)) // 2
        q = data[mid]
        if data[mid] == key:
            return mid 

        
        data = data[mid:] if data[mid] < key else data[:mid]
        
        return self.binary_search(data, key, lower, upper)

x = [1,2,7,9,7,5,6,4,7]
mid = len(x) // 2 
L = x[:mid]
R = x[mid:]
mid2 = len(R) // 2
L2 = x[:mid2]
R2 = x[mid2:]
print('')


input = [1,2,3,4,5,6,7,8,9,10]
al = Algorithm()
indexs = al.binary_search(input, 8)
print(input)
print(indexs)