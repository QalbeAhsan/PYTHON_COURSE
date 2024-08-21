

"""
coffe 
burger 
pizza 
pasta
wings 
"""

Menu = {"coffee": 20, "burger": 50, "pizza": 100, "pasta": 80, "wings": 30}

print("WELCOME TO THE PYTHON CAFE :")

reply = input("DO YOU WANT TO SEE OUR MENUE,yes/no:").lower()

if reply == "yes":
    print(
        "HERE IS OUR MENUE",
    )

    for item, price in Menu.items():  # HERE WE PRINT OUT THE MENUE BY KEY VALUE PAIR
        print(f"{item}: {price}")

    response = input("SIR DO YOU WANT TO PLACE A ORDER:").lower()

    if response == "yes":
        print("OK SIR THANKS___")
        order_total = 0
        item1 = input("PLEASE ENTER YOUR ITEM :")

        if item1 in Menu:
            order_total += Menu[item1]

            response2 = input("SIR DO YOU WANT TO ORDER ANYTHING ELSE:").upper()

            if response2 == "YES":
                item2 = input("ENTER YOUR SECOND ITEM :")

                if item2 in Menu:
                    order_total += Menu[item2]
                    print(f"SIR YOUR TOTAL BILL IS :{order_total}")
                else:
                    print("SORRY SIR THIS IS NOT AVALAIBLE:")
                    print(f"AND YOUR BILL IS : {order_total}")
            else:
                print("APKA BAHUT BAHUT SHUKRIYA")
                print(f"AND YOUR BILL IS : {order_total}")
        else:
            print("SORRY SIR THIS ITEM IS CURRENTLY NOT AVALAIBLE")
    else:
        print("PHIR HAMRA MENUE Q DEKHA ")
else:
    print("OK SIR NO PROBLEM AND HAVE A GOOD DAY")
