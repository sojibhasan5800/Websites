class Stock:
    product={}
    default_product={}
    default_product_list={}
    user_product={}
    add=True
    def __init__(self,store,id):
        if isinstance(store,dict):
            for item,quantity in store.items():
                # check default product and store this product
                if not isinstance(item,str) and not isinstance (quantity,int):
                    print(f"check to recoded your product is-> {item} is not vaild")
                    self.default_product[id]={}
                    self.default_product[id][quantity]=item
                    add=False
            
            if(self.add):
                for item,quantity in store.items():

                    self.product[item]= self.product.get(item,0)+quantity
                    
    if(add):
        def __repr__(self)->str:

            print(f"your product store add in sucessfully id number is->{id}")                    
    
