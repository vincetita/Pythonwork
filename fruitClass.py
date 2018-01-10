class fruit:
    
    def __init__(self, type,color,weight_in_grams, price_per_kilo):
        self.type=type
        self.color=color
        self.weight_in_grams=weight_in_grams
        self.price_per_kilo=price_per_kilo
       

    def get_total_price(self,weight_in_grams,price_per_kilo):
       # return weight_in_grams=weight_in_grams/1000*price_per_kilo
        print("The calculate_price is",(self.weight_in_grams/1000*self.price_per_kilo), "Eur")
        
    def print_info(self):
        print("The fruit type is {}, color is {}, weight_in_grams is {} and price_per_kilo is {} Eur".format(self.type,self.color,self.weight_in_grams,self.price_per_kilo))
                                           

orange= fruit("orange", "yellow",100,2.30)
orange.get_total_price(100,2.30)
orange.print_info()

