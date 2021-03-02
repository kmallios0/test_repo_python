import json
file = open(input("ΔΩΣΕ ΟΝΟΜΑ ΑΡΧΕΙΟΥ"), 'r')
cont = file.read()
dic = json.loads(cont)
file.close()
# Python3 Program to find depth of a dictionary
def dict_depth(dic, level = 1):

    str_dic = str(dic)
    counter = -1
    for i in str_dic:
        if (i == "{") or (i == "[") :
            counter += 1
    return(counter)


print(dict_depth(dic))
