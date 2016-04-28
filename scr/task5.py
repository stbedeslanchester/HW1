'''
Created on 28 Apr 2016

@author: Gregory
@organization: stbedeslanchester
@summary: Implementation to solve problem five in homework task one.
'''
from datetime import datetime
class task5:    
    def __init__(self):
        """
        Constructor for the class "task5".
        """
        self.main()

    def is_valid_date(self, test, _format):
        """
        Method to verify a that a string can be parsed to a datetime object.
        @param test: The string to attempt to parse into a datetime object.
        @param _format: The format that the users message will be tested against.
        @return: True if the input is valid, else False.
        """
        try:
            datetime.strptime(test, _format)
            return True
        except ValueError:
            return False

    def get_date_input(self, prompt, _format='%d/%m/%Y'):
        """
        Get a datetime object from a users inputted string.
        @param prompt: The message that will be displayed to prompt the user to enter data.
        @param _format: The format that the users message will be tested against.
        @return: A validated datetime object from a users input.
        """
        error_format = _format.replace("%b", "Month_Name_Short").replace("%B", "Month_Name").replace("%d", "DD").replace("%j", "Day_Of_Year").replace("%m", "MM").replace("%U", "Week_Number").replace("%W", "Week_Number").replace("%y", "YY").replace("%Y", "YYYY")
        temp = input(prompt)
        while not self.is_valid_date(temp, _format):
            print("{0} is not recognised as a valid date!\nPlease use the date format {1}".format(temp, error_format))
            temp = input(prompt)
        return datetime.strptime(temp, _format)

    def main(self):
        """
        Method for getting three dates from a users input and then outputting the year of each of these dates.
        """
        date1 = self.get_date_input("Please enter the first date: ")
        date2 = self.get_date_input("Please enter the second date: ")
        date3 = self.get_date_input("Please enter the third date: ")
        print("Year 1: {0}\nYear 2: {1}\nYear 3: {2}".format(date1.strftime("%Y"), date2.strftime("%Y"), date3.strftime("%Y")))
# used for testing class
task5()