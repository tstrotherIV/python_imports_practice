from appliances import DishWasher
from appliances import Dryer
from appliances import Washer
from appliances import Refrigerator
from appliances import CoffeeMaker
from appliances import CanOpener

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

Can_O_Tuna = CanOpener("Green")
Can_O_Tuna.open_can()
