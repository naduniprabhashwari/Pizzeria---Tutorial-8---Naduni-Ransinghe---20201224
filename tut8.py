global toppingsList
toppingsList = []

# show pizza toppings
def show_pizza_toppings():
           if toppingsList is None:
                      print("There are no toppings selected")
           else:
                      print("The toppings on your pizza are:")
                      for topping in toppingsList:
                                 print("      ",topping)
           


# welcome
print("Welcome to Cavendish Pizzeria - choose your toppings.")

# menu
print("When prompted, enter first letter or full word of operation.")
print("---- Operations ----")
print("a          Add a topping")
print("c          Change a topping")
print("r          Remove a topping")
print("o         Order the pizza")
print("q         Quit")
print("s          Start over")


while True:           
           # getting user input
           print("\nWhat would you like to do?")
           user_input = input("add, change, remove, order, quit, startover: ").lower()

           if user_input == 'a':
                      print("\n-----------Add Toppings-------------")
                      # get and add new toppings
                      toppingsList_input = input("Type in a topping to add: ").lower()
                      toppingsList.append(toppingsList_input)

                      # print toppings
                      show_pizza_toppings()

           elif user_input == 'c':
                      print("\n-----------Change Toppings-------------")
                      change_type = ''
                      # get topping to change
                      while change_type not in  toppingsList:
                                 change_type = input("What topping would you like to change: ").lower()

                      # get new topping
                      new_topping = input("What is the new topping: ").lower()
                      # replace the old topping with new topping
                      toppingsList[toppingsList.index(change_type)] = new_topping

                      # print toppings
                      show_pizza_toppings()

           elif user_input == 'r':
                      print("\n-----------Remove Toppings-------------")
                      # getting topping name to remove
                      remove_topping = input("What topping would you like to remove: ")
                      # remove the topping from the list
                      toppingsList.remove(remove_topping)

                      # printing toppings
                      show_pizza_toppings()

           elif user_input == 'o':
                      print("\n-----------Order Pizza-------------")
                      # printing toppings
                      show_pizza_toppings()

                      # thaking the user
                      print("Thanks for your order!")

                      # seeting the topping list empty
                      toppingsList = []

                      # asking leave or make another pizza order
                      status = input("\nWould you like another pizza (y/n) ?").lower()
                      if status == 'n':
                                 break
                      
           elif user_input == 's':
                      print("\n-----------Start Over-------------")
                      # start again
                      # making the list empty and start again
                      toppingsList = []
                      continue
                      
           elif user_input == 'q':
                      print("\n-----------Quit-------------")
                      # quit from the proccess
                      break

           else:
                      # if wrong work type
                      print("I\'m not sure what you said, please try again.")

                      # printing toppings
                      show_pizza_toppings()
                      continue

           
print("\nThank you!")
                    
                      
                      

           

           
                      
                      
                      
                      
                      
                      

           

           

           

           

           


