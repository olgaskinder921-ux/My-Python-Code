import time

inventory = ["coconut", "pineapple", "Samsung Galaxy A36 5G", "laptop Lenovo", "3000 tenge", "Itel S26 Super Ultra", "Google Plus", "Googi", "Ginger Sahur", "Samsung Galaxy A23 4G", "Samsung Galaxy S25 Ultra"]

if inventory[0] == "coconut":
    print(inventory)
    time.sleep(1.5)
    print("фу, говно етот ваш ибучий кокос🤮")
    time.sleep(1.5)
    inventory.pop(0)
    print(f"Saut выкинул кокос🥥, осталось: {inventory}")