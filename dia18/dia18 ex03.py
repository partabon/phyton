import re

def is_valid_variable(w):
    regex_pattern = r'^[_a-zA-Z]+'
    matches =re.findall(regex_pattern, w)
    print(w)
    if len(matches) == 0:
        return False
    else:
        w2 = w[1:]
        #print(w2)
        reg_pat2 = r'\W' #Revisa si no hay carácteres de palabra
        matches2= re.findall(reg_pat2,w2)
        #print(matches2)
        if len(matches2)==0:
            return True
        else:
            return False

print(is_valid_variable('first_name') )# True
print(is_valid_variable('first-name') )# False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname') )# True
print(is_valid_variable('_firstname') )# True
print(is_valid_variable('Firstname') )# True
print(is_valid_variable('_') )# True