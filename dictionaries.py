my_dict={'item':'soap','quantity':2,'price':20.9}
h=my_dict.keys()
j=my_dict.values()
print(j)
print(h)

#update
dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }



dict.update(dict2)
print ("updated dict : ", dict)

#items
dict = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" %  dict.items())

#length
print ("Length : %d" % len (dict))