'''
Created on 28 Apr 2016

@author: Gregory
@organization: stbedeslanchester
@summary: Implementation to solve problem three in homework task one.
'''
class task3:
    def __init__(self):
        """
        Constructor for the class "task3".
        """
        self.main()

    def main(self):
        """
        Method for getting two inputs from a user and congregating them into one string.
        """
        first_name = input("What is your first name? ")
        last_name = input("What is your last name? ")
        print("Your full name is {0} {1}".format(first_name, last_name))
        
# used for testing class
# task3()
