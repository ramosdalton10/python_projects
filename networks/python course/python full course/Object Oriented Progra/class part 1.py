class kentle(object):
    power_source = 'Electricity'
    def __init__(self,price,brand):
        self.price = price
        self.brand = brand

bajaj = kentle(2345,'bajaj')
# print bajaj.price
# print bajaj.brand

philips = kentle('1234', 'philips')
# print philips.price
# print philips.brand
print 'the brand is {0.brand} and price {0.price} and model {1.brand} and price {1.price}' .format(bajaj,philips)
print kentle.power_source
print bajaj.power_source
print philips.power_source
print '*'*60
print kentle.__dict__