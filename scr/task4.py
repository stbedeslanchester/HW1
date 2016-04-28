'''
Created on 28 Apr 2016

@author: Gregory
@organization: stbedeslanchester
@summary: Implementation to solve problem four in homework task one.
'''
class task4:    
    def __init__(self, address):
        """
        Constructor for the class "task4".
        """
        self.main(address)

    def main(self, address):
        """
        Method for printing a users address in a set format.
        """
        print("{0} {1}\n{2}\n{3}\n{4}\n{5}".format(address.get("house_name"), 
                                                   address.get("house_number"), 
                                                   address.get("street"), 
                                                   address.get("town"), 
                                                   address.get("region"), 
                                                   address.get("country")))
# used for testing class
# task4({"house_name" : "My House",
#        "house_number" : "3", 
#        "street" : "123 lane", 
#        "town" : "Lanchester", 
#        "region" : "Durham", 
#        "country" : "UK"})
