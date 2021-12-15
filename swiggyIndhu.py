Swiggy = {"Saravanabavan":{"Idly":30,"Dosa":80,"Poori":40,"Parotta":30,"Curd rice":90,"Ice cream":40},
"SS foods":{"Mushroom biriyani":150,"Veg biriyani":100,"Veg gravy":90,"Milk shake":60,"Juice":50},
"Street foods":{"Egg rice":50,"Chicken chilli":80,"soup":50,"Veg rice":40,"Parota":40},
"Buhari":{"Chicken bIriyani":250,"Mutton biriyani":300,"Fish biriyani":200,"Chicken gravy":120,"Mutton gravy":150}}

order={}
class Hotels:
    print("Swiggy!!")

    def __init__(self):
        print("List Of Hotels :")
        print("1.Hotelname:Saravanabavan  Location:Thambaram   RecommendedFood:Parotta            Rating:4.6")
        print("2.Hotelname:SS foods       Location:Adyar       RecommendedFood:Mushroom biriyani  Rating:4.5")
        print("3.Hotelname:Street foods   Location:Guindy      RecommendedFood:Egg rice           Rating:4.7")
        print("4.Hotelname:Buhari         Location:Anna nagar  RecommendedFood:Mutton biriyani    Rating:4.8")
        self.hotelname=input("Enter hotel name : ")
        
    def menu(self):
        if isinstance(self.hotelname,str):
            if self.hotelname in Swiggy:
                hotel=self.hotelname
                value=Swiggy.get(self.hotelname)
                for i,j in value.items():
                    print(f"{i} : {j}")
                    
            else:
                raise ValueError("Details unavailable")

        else:
            raise TypeError("invalid")

    def order(self):
        print("Order References")
        inpt=input("Proceed to order : yup or Nope:")
        if inpt == "yup":
            items=input("Dishes : ")
            if int(items)>0 and int(items)<30:
                for i in range(int(items)):
                    dish=input("Enter the dish name : ")
                    if(dish in Swiggy[self.hotelname]):
                        quantity=input(f"Enter the Quantity : ")
                        order[dish]=quantity
                    else:
                        raise ValueError("Error")
            else:
                raise ValueError("invalid")
        else:
            print("Thank you")

    def bill(self):
        amount=0
        for i,j in order.items():
            val=Swiggy[self.hotelname]
            amount=val[i]*int(j)
            print("ordered confirmed")
            print(f"total bill : {amount}")
            print("Thank you for using swiggy.Enjoy your food")
              
            
        
            
        
            
        
food=Hotels()
food.menu()
food.order()
food.bill()
