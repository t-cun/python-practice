# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

def oneAway(str1, str2):
    numChgs = 0

    # the 'replace' case
    if len(str1) == len(str2):
        str2pos = 0
        for char in str1:
            if char != str2[str2pos]:
                numChgs += 1
                str2pos += 1
                if numChgs > 1:
                    return False
            else:
                str2pos += 1
        
        return numChgs <= 1

    # the 'insert/remove' case
    elif abs(len(str1) - len(str2)) == 1:
        longword, shortword = ((str1, str2), (str2, str1))[len(str2) > len(str1)]

        strpos = 0
        for char in longword:
            if strpos >= len(shortword) or char != shortword[strpos]:
                numChgs += 1
            else:
                strpos += 1
        
        return numChgs <= 1
    else:
        return False


print(f'oneAway("dig", "dog")\t\t= {oneAway("dig", "dog")}')
print(f'oneAway("hound", "pround")\t= {oneAway("hound", "pround")}')
print(f'oneAway("sdig", "dig")\t\t= {oneAway("sdig", "dig")}')
print(f'oneAway("horses", "hoorses")\t= {oneAway("horses", "hoorses")}')
print(f'oneAway("dig", "digs")\t\t= {oneAway("dig", "digs")}')
print(f'oneAway("xxx", "xx")\t\t= {oneAway("xxx", "xx")}')
print(f'oneAway("xxx", "xixx")\t\t= {oneAway("xxx", "xixx")}')
print(f'oneAway("xxx", "ixx")\t\t= {oneAway("xxx", "ixx")}')
print(f'oneAway("asdf", "fads")\t\t= {oneAway("asdf", "fads")}')
print(f'oneAway("read", "rade")\t\t= {oneAway("read", "rade")}')

# Solution notes
# runs in O(n) of short word (long word in case of my solution above)
# could simplify the logic above and create a insert/remove and replace cases
# can check len diff case first to return immediately
# numChgs could be a boolean since we only allow 1