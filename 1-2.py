# Given two strings, write a method to decide if one is a permutation of the other

# Examples
# permu("there", "their") = False
# permu("god", "dog") = True


def permu(str1, str2):

    # Check the length of the two strings. if not equal return false.
    if len(str1) != len(str2):
        return False

    # Create a dict containing the letters of str1
    str1_bag = {}
    
    # For each character in str1, pop the character into the bag
    ## If a character 'key' already exists in the dictionary, increment the value
    for char in str1:
        if char in str1_bag:
            str1_bag[char] += 1
        else:
            str1_bag[char] = 1
    # bag is now populated with chars from str1

    # for each of the letters in str2, check the char exists in the dict and decrement it.     
    ## if it doesn't exist, we can return false immediately.
    ## if we hit zero, delete the key from the dict.
    
    for char in str2:
        if not str1_bag.get(char):
            print(f'didnt find {char}')
            return False
        else:
            str1_bag[char] -= 1
            if(str1_bag[char] == 0):
                del str1_bag[char]

    # If there are no keys left in the "bag", then we have a permutation.
    return len(str1_bag) == 0

    ### DOES NOT HANDLE EXTRA LETTERS IN str2
    ### New solution - 2 bags of words


def permu2(str1, str2):

    # Check the length of the two strings. if not equal return false.
    if len(str1) != len(str2):
        return False

    # Create a dict containing the letters of str1
    str1_bag = {}
    
    # For each character in str1, pop the character into the bag
    ## If a character 'key' already exists in the dictionary, increment the value
    for char in str1:
        if char in str1_bag:
            str1_bag[char] += 1
        else:
            str1_bag[char] = 1
    # bag is now populated with chars from str1

    # Create a dict containing letters of str2
    str2_bag = {}
    for char in str2:
        if char in str2_bag:
            str2_bag[char] += 1
        else:
            str2_bag[char] = 1


    # after populating bag2, compare size and return false if different.
    # continue by iterate keys of one and start comparing vals
    ### HANDY CHECK FOR KEYS HERE! python3...
    if str1_bag.keys() != str2_bag.keys():
        return False

    for key in str1_bag:
        if str1_bag[key] != str2_bag[key]:
            return False

    # Looks like all the key/values are equal. return True!
    return True

print(f'permu("there", "their)" = {permu("there", "there")}')
print(f'permu("god", "dog") = {permu("god", "dog")}')

print(f'permu2("there", "their)" = {permu2("there", "their")}')
print(f'permu2("god", "dog") = {permu2("god", "dog")}')

print(f'permu2("FFFFDSAFDSA", "ASDFASDFFFF") = {permu2("FFFFDSAFDSA", "ASDFASDFFFF")}')


### Things I missed:
# ask about - encoding ASCII, UTF8 (size implications)
# ask about - case, whitespace (do they count?) 
# EASY SOLUTION - SORT THE STRINGS and compare!
# subtle improvements - create a dict with all values from dict1 (# ASCII char space i.e. 128), decrement for each char in dict2, and then check for negative values