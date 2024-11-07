#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title 
        self.page_count = page_count
    
    @property
    def page_count(self):
        '''The page_count property'''
        return self._page_count 

    @page_count.setter
    def page_count(self, page_count):
        '''page_count must be an integer'''
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print('page_count must be an integer')

    def turn_page(self):
        print('Flipping the page...wow, you read fast!')

book = Book('Blossoms', 124)
book.turn_page()





    
