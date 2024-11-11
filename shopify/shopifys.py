import sys
import os
sys.path.append(os.path.abspath("e:/CSE/Python/oop/Websites"))
from stockk.stoock import Stock

def avaiable(purches_product):
    flag = True
    not_enough = {}
    total = Stock.total_product.copy()  # Assume total_product is a dictionary with available stock
    
    for mal, kg in purches_product.items():
        if total.get(mal, 0) >= kg:
            pass
        else:
            flag = False
            not_enough[mal] = total.get(mal, 0)
    
    if flag:
        return True
    else:
        return not_enough


class Shoping:
    def __init__(self, itemss):
        if isinstance(itemss, dict):
            self.getted_product = {}  # Initialize self.getted_product as an empty dictionary
            
            # Populate self.getted_product with the required quantities
            for pro, quan in itemss.items():
                self.getted_product[pro] = self.getted_product.get(pro, 0) + quan
            
            # Check availability
            haven = avaiable(self.getted_product)
            if haven is True:
                print("Products are available")
            else:
                print("Below products are not available in sufficient quantity:")
                for prod, not_q in haven.items():
                    print(f"{prod}: only {not_q} available")
    def call(self):
        print('calling someone i know')

# Sample data
ab_di = {'rice': 20, 'oil': 10}
abdulla = Shoping(ab_di)
abdulla.call()
