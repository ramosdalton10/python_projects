import matplotlib.pyplot as pyt

days = [1, 2, 3, 4, 5, 6]
sleeping = [3, 4, 5, 3, 14, 15]
playing = [5, 7, 8, 4, 3, 9]
wataching = [1, 2, 4, 2, 5, 2]
pyt.stackplot([], [], color='b',)
pyt.stackplot([], [], color='g', )
pyt.stackplot([], [], color='k', )
pyt.xlabel('x')
pyt.ylabel('y')
pyt.stackplot(days, sleeping, playing, wataching, color=['c', 'b', 'g', 'k'],label=['df','f','sdf','df'])

pyt.show()
