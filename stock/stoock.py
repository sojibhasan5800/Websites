class Stock:
    total_product={}
    def __init__(self,items):
        self.product={}
        if isinstance(items,dict):
            for element,quantity in items.items():
                self.product[element] = self.product.get(element,0)+ quantity
                self.total_product[element] = self.total_product.get(element,0)+ quantity
        print((f"your product added suffcessfully"))
    def __repr__(self):
        pass


supplier_lement = {
    'rice' : 10,
    'oil' :20,
    'tomato' :50
}
grouping ={
    'matrial' : 40,
    'oil':12
}

supplier =Stock(supplier_lement)
ms_group = Stock(grouping)

if __name__ =="stocks":

    print(supplier.total_product)

