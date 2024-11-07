#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand 
        self.size = size 

    @property 
    def size(self):
        '''size property'''
        return self._size

    @size.setter 
    def size(self, size):
        '''size must be an integer'''
        if isinstance(size, int):
            self._size = size 
        else:
            print('size must be an integer')
        self.condition = ''

    def cobble(self):
        print('Your shoe is as good as new!')
        self.condition = 'New'


adidas = Shoe('Adidas', 8)
adidas.cobble()