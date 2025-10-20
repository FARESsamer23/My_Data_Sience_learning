#- -- we use module call re search and findAll
# search() => Search A string For A match and return a first Match Only
# findall() => Search A string For A match and return all Matches

# [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
#  span is the position of the element matched
 

import re  

my_Search = re.search(r"[A-Z]{2}","FFaresSamer")
print(my_Search.group())
print(my_Search.string)
print(my_Search.span())

# is_email = re.search(r'[A-z0-9\.]+@[A-z0-9]+\.com|net|org|info',"os@fares.com")

# if is_email :
#     print(is_email)
#     print("Email is valid")
# else :
#     print("this is not a valide email")
    
    
# my_input = input('please entre your email')    

# result = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)",my_input)    
        

# if result :
#     print("Email is valid  ",result)
# else :
#     print("this is not a valide email")
    
# split and sub 