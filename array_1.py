#1D array (Just warming up)
arr = [1,2,3,4,5,6,7,8,9,10]

#Accessing array: Usage of index O(1)
def pos_num(ind):
    return arr[ind]

def add_array():
    arr.insert(11,len(arr)+1)
    return arr

print(pos_num(1))
print(add_array())
