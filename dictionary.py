#first way
dictionary = {'key_1':1,'key_2':2}
print (dictionary)
#second way
dictionary = {}
dictionary['key_1']=1
dictionary['key_2']=2
print(dictionary)

dictionary = {'key_1': 100,'key_2': 200}
print(dictionary['key_1'])
print(dictionary['key_2'])

dictionary = {'key_1': 100,'key_2': 200}
'key_1' in dictionary
'key_5' in dictionary
100 in dictionary

dictionary = {'key_1': 100,'key_2': 200}
dictionary['key_1'] += 600
dictionary['key_2'] =400
print(dictionary)
