class kettle(object):

    power_source = 'Electricity'
    def __init__(self, make, price):
        self.price = price
        self.make = make
        self.on = False
        self.cake = False
    def switchon (self):
        self.on = True

bajaj = kettle('bajaj', 2500)
philips = kettle('philips',3000)
print 'the model is {0} and the price is {1}' .format(bajaj.make,bajaj.price)
print 'the model is {0.make} and the price is {0.price}' .format(bajaj)
print 'the model is {0.make} and the price is {0.price}' .format(philips)
philips.switchon()
print philips.on
print philips.cake

philips.power = 4


print philips.power
print kettle.power_source
print bajaj.power_source
print 'switch power to solar'
kettle.power_source = 'Solar '
print philips.power_source

print philips.__dict__
print kettle.__dict__