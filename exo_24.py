def anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    
    string_list1 = list(str1)
    string_list2 = list(str2)
    string_list1.sort()
    string_list2.sort()
    if string_list1 == string_list2:
        return True
    else:
        return False
print(anagram("listen","silent"))