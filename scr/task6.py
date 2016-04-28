'''
Created on 28 Apr 2016

@author: Gregory
@organization: stbedeslanchester
@summary: Implementation to solve problem six in homework task one.
'''
class task6:
    
    _to_fix = []
    _fixed = []
    
    def __init__(self, to_fix):
        """
        Constructor for the class "task6".
        """
        self._to_fix = to_fix
        self.main()
    
    def main(self):
        """
        Method for fixing the list of email addresses.
        """
        for s in self._to_fix:
            temp = s.replace("#", "@")
            print ("{0} --> {1}".format(s, temp))
            self._fixed.append(temp)
            
    def get_fixed(self):
        """
        Method to get the email addresses that have been fixed.
        @return: The list of fixed email addresses.
        """
        return self._fixed
        
        
# used for testing class
# task6(["me#example.com", "you#example.com", "him#example.com", "her#example.com"])
