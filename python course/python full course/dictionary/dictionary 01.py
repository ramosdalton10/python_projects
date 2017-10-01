fruits = { 'orange':'a sweet,orange, citrus fruit',
           'apple':'good for making ceder',
            'lemon':'sour, good for melonade',
            'grape':'sweet, small as balls',
            'mango':'sweet, can mkae mango shakes',}
fruits['gover'] = 'round shape, sweet fruit'
# for fruit in fruits.values():
#     print fruit

# frutas = []
# for item in fruits.keys():
#     frutas.append(item)
frutas = [item for item in fruits.keys()]
# print frutas
print fruits.get('oranged','there is no fruit')
print fruits.has_key('apple')

f_tuple = tuple(fruits.items())
# print f_tuple
for snack in f_tuple:
    jack, des = snack
    print jack+'       '+des

veg  = fruits.copy()
print veg