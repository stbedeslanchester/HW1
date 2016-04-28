'''
Created on 28 Apr 2016

@author: Gregory
@organization: stbedeslanchester
@summary: Implementation to solve problem seven in homework task one.
'''
class task7:    
    def __init__(self):
        """
        Constructor for the class "task7".
        """
        self.main()
    
    def is_integer(self, s):
        """
        Method to test if a number is a valid number (integer).
        @rtype: boolean
        @return: true if a valid integer, else false.
        """
        try:
            int(s)
            return True
        except ValueError:
            return False
    
    def main(self):
        """
        Method for getting a users name and age, then printing them.
        """
        name = input("What is your name? ")
        age = input("What is your age {0}? ".format(name))
        while not self.is_integer(age):
            print("{0} is not a valid age!\nAn age value must be an integer.".format(age))
            age = input("What is your age {0}? ".format(name))
        print("Hello {}, {} isn’t too old!!".format(name, age))
        
# used for testing class
# task7()
