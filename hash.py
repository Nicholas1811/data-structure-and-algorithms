#Practice on hashing algorithm
#there are a lot of hash algorithms to choose from
def hash(val):
    word = 0
    for text in val:
        word += ord(text)
    hash_val = word % 10
    return hash_val
print(hash("Hello world"))