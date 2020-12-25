machine = {
    'c' : {
            1: "Espresso Coffee", 
            2: "Cappuccino Coffee", 
            3: "Latte Coffee"
        },
    
    't' : {
            1: "Plain Tea",
            2:"Assam Tea",
            3: "Ginger Tea",
            4: "Cardamom Tea",
            5: "Masala Tea",
            6: "Lemon Tea",
            7: "Green Tea",
            8: "Organic Darjeeling Tea"
        },
    
    's' : {
            1: "Hot and Sour Soup",
            2: "Veg Corn Soup",
            3: "Tomato Soup",
            4: "Spicy Tomato Soup"
    },

    'b' : {
            1: "Hot Chocolate Drink",
            2: "Badam Drink",
            3: "Badam-Pista Drink"
    }
}

menu = input()
sub_menu = int(input())
print("Welcome to CCD!")
try:
    print("Enjoy your {}!".format(machine[menu][sub_menu]))
except: 
    print("INVALID OUTPUT!")