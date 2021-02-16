my_dict = {'x':500,'y':5874,'z':8502}
key_min =min(my_dict.keys(), key=(lambda k: my_dict[k]))
print('minimum value: ',my_dict[key_min])