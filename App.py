import json
import difflib
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    
    w=w.lower()

    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    
    elif len(get_close_matches(w,data.keys()))>0:

        yn= input("Did you mean %s instead ? Press Y for yes else press N for no. :  "% get_close_matches(w,data.keys())[0])
        if yn=='Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=='N':
            return "Data is not present"
        else:
            #u=u.lower()
            u=input("Given input is not valid, please give again : ")
            if u=='Y':
                return data[get_close_matches(w,data.keys())[0]]
            else:
                return "Data is not present"

    else:
        return "The word does not exists, Please double check it"
word=input("Enter word  : ")


x=translate(word)
if type(x)==list:
    for i in x:
        print()
        print('*',i)
        print()    
else:
    print(x)
    
    