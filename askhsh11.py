import json
file = open(input("ΔΩΣΕ ΟΝΟΜΑ ΑΡΧΕΙΟΥ"), 'r')
cont = file.read()
js = json.loads(cont)
file.close()
sum={}
def get_all_keys(leksiko):
    for k, value in leksiko.items():
        if type(value) is dict:
            get_all_keys(value)
            if (k in sum):
                sum[k] += 1
            else:
                sum[k]=1
        elif (k in sum):
            sum[k] += 1
        else:
            sum[k]=1
        if type(value) is list:
            for i in range(len(value)):
                if type(value[i]) is dict:
                    get_all_keys(value[i])
get_all_keys(js)
maxkey = max(sum.items(), key=lambda x: x[1])
listmaxkey = list()
for key, value in sum.items():
    if value == maxkey[1]:
        listmaxkey.append(key)
print(listmaxkey)
