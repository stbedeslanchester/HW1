'''
Created on 28 Apr 2016

@author: Gregory
@organization: stbedeslanchester
@summary: Implementation to solve problem one in homework task one.
'''
class task1:
    def __init__(self):
        """
        Constructor for the class "task1".
        """
        self.main()
            
    def is_number(self, s):
        """
        Method to test if a number is a valid number (float).
        @rtype: boolean
        @return: true if a valid float, else false.
        """
        try:
            float(s)
            return True
        except ValueError:
            return False

    def get_float_input(self, prompt):
        """
        Method to get a float value from a user with the given prompt.
        @param prompt: The message to be sent to the player prompting them to enter a number.
        @rtype: float
        @return: The float value of the users input once it is validated.
        """
        temp = input(prompt)
        while not self.is_number(temp):
            print("{0} is not recognised as a number!".format(temp))
            temp = input(prompt)
        return float(temp)
            
    def main(self):
        """
        Method to start the logic of the program and get all the required inputs.
        """
        num_1 = self.get_float_input("Please enter a number: ")
        num_2 = self.get_float_input("Please enter a second number: ")
        num_3 = self.get_float_input("Please enter a third number: ")
        num_4 = self.get_float_input("Please enter a fourth number: ")
        print("Sum: {0}".format((num_1 + num_2 + num_3 + num_4)))

# used for testing class
# task1()
