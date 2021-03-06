def show_menu():
    print("\nSelect an option")
    print("1. Insert ₹5")
    print("2. Insert ₹20")
    print("3. Buy Gumball")
    print("4. Withdraw money")

def get_x():
    x = int(input("\nPlease enter your choice: "))
    if x not in range(1,5):
        print("\nInvalid choice")
        get_x()
    return x

def state_diagram(states,inputs):
    print("\nThe Final State Diagram for the above Transactions are as follows: ")
    print("(0)",end="")
    for (state,input) in zip(states,inputs):
        print(" --"+str(input)+"--> ("+ str(state) + ")",end="")

states = []
inputs = []
dfa = 0
def balance(dfa,x):
    if dfa == 0:
        if x == 1:
            dfa = 5
            states.append(dfa)
            inputs.append("5")
            print("\nYou have inserted ₹5")
            print("Current balance is ₹" + str(dfa))
        elif x == 2:
            dfa = 20
            states.append(dfa)
            inputs.append("20")
            print("\nYou have inserted ₹20")
            print("Current balance is ₹" + str(dfa))
        elif x == 3:
            states.append(dfa)
            inputs.append('Buy')
            print("Insufficient amount")
            print("Current balance is ₹" + str(dfa))
        elif x == 4:
            print("\nYou have withdrawn ₹"+str(dfa))
            dfa = 0
            states.append(dfa)
            inputs.append('Withdrawn')
            print("Current balance is ₹" + str(dfa))
            state_diagram(states,inputs)
            return dfa

        show_menu()
        x = get_x()
        balance(dfa,x)

    elif dfa == 5:
        if x == 1:
            dfa = 10
            states.append(dfa)
            inputs.append("5")
            print("\nYou have inserted ₹5")
            print("Current balance is ₹" + str(dfa))
        elif x == 2:
            dfa = 25
            states.append(dfa)
            inputs.append("20")
            print("\nYou have inserted ₹20")
            print("Current balance is ₹" + str(dfa))
        elif x == 3:
            states.append(dfa)
            inputs.append('Buy')
            print("Insufficient amount")
            print("Current balance is ₹" + str(dfa))
        elif x == 4:
            print("\nYou have withdrawn ₹"+str(dfa))
            dfa = 0
            states.append(dfa)
            inputs.append('Withdrawn')
            print("Current balance is ₹" + str(dfa))
            state_diagram(states,inputs)
            return dfa

        show_menu()
        x = get_x()
        balance(dfa,x)

    elif dfa == 10:
        if x == 1:
            dfa = 15
            states.append(dfa)
            inputs.append("5")
            print("\nYou have inserted ₹5")
            print("Current balance is ₹" + str(dfa))
        elif x == 2:
            dfa = 30
            states.append(dfa)
            inputs.append("20")
            print("\nYou have inserted ₹20")
            print("Current balance is ₹" + str(dfa))
        elif x == 3:
            states.append(dfa)
            inputs.append('Buy')
            print("Insufficient amount")
            print("Current balance is ₹" + str(dfa))
        elif x == 4:
            print("\nYou have withdrawn ₹"+str(dfa))
            dfa = 0
            states.append(dfa)
            inputs.append('Withdrawn')
            print("Current balance is ₹" + str(dfa))
            state_diagram(states,inputs)
            return dfa

        show_menu()
        x = get_x()
        balance(dfa,x)

    elif dfa == 15:
        if x == 1:
            dfa = 20
            states.append(dfa)
            inputs.append("5")
            print("\nYou have inserted ₹5")
            print("Current balance is ₹" + str(dfa))
        elif x == 2:
            dfa = 35
            states.append(dfa)
            inputs.append("20")
            print("\nYou have inserted ₹20")
            print("Current balance is ₹" + str(dfa))
        elif x == 3:
            states.append(dfa)
            inputs.append('Buy')
            print("Insufficient amount")
            print("Current balance is ₹" + str(dfa))
        elif x == 4:
            print("\nYou have withdrawn ₹"+str(dfa))
            dfa = 0
            states.append(dfa)
            inputs.append('Withdrawn')
            print("Current balance is ₹" + str(dfa))
            state_diagram(states,inputs)
            return dfa

        show_menu()
        x = get_x()
        balance(dfa,x)
    
    elif dfa == 20:
        if x == 1:
            dfa = 25
            states.append(dfa)
            inputs.append("5")
            print("\nYou have inserted ₹5")
            print("Current balance is ₹" + str(dfa))
        elif x == 2:
            dfa = 40
            states.append(dfa)
            inputs.append("20")
            print("\nYou have inserted ₹20")
            print("Current balance is ₹" + str(dfa))
        elif x == 3:
            states.append(dfa)
            inputs.append('Buy')
            print("Insufficient amount")
            print("Current balance is ₹" + str(dfa))
        elif x == 4:
            print("\nYou have withdrawn ₹"+str(dfa))
            dfa = 0
            states.append(dfa)
            inputs.append('Withdrawn')
            print("Current balance is ₹" + str(dfa))
            state_diagram(states,inputs)
            return dfa

        show_menu()
        x = get_x()
        balance(dfa,x)
        
    elif dfa == 25:
        if x == 1 or x == 2:
            dfa = 25
            states.append(dfa)
            inputs.append("5,20")
            print("\nCannot add any further amount")
            print("Current balance is ₹" + str(dfa))
        elif x == 3:
            dfa = dfa - 25
            states.append(dfa)
            inputs.append('Buy')
            print("\nYou have bought a gumball")
            print("Current balance is ₹" + str(dfa))
        elif x == 4:
            print("\nYou have withdrawn ₹"+str(dfa))
            dfa = 0
            states.append(dfa)
            inputs.append('Withdrawn')
            print("Current balance is ₹" + str(dfa))
            state_diagram(states,inputs)
            return dfa

        show_menu()
        x = get_x()
        balance(dfa,x)

    elif dfa == 30:
        if x == 1 or x == 2:
            dfa = 30
            states.append(dfa)
            inputs.append("5,20")
            print("\nCannot add any further amount")
            print("Current balance is ₹" + str(dfa))
        elif x == 3:
            dfa = dfa - 25
            states.append(dfa)
            inputs.append('Buy')
            print("\nYou have bought a gumball")
            print("Current balance is ₹" + str(dfa))
        elif x == 4:
            print("\nYou have withdrawn ₹"+str(dfa))
            dfa = 0
            states.append(dfa)
            inputs.append('Withdrawn')
            print("Current balance is ₹" + str(dfa))
            state_diagram(states,inputs)
            return dfa

        show_menu()
        x = get_x()
        balance(dfa,x)

    elif dfa == 35:
        if x == 1 or x == 2:
            dfa = 35
            states.append(dfa)
            inputs.append("5,20")
            print("\nCannot add any further amount")
            print("Current balance is ₹" + str(dfa))
        elif x == 3:
            dfa = dfa - 25
            states.append(dfa)
            inputs.append('Buy')
            print("\nYou have bought a gumball")
            print("Current balance is ₹" + str(dfa))
        elif x == 4:
            print("\nYou have withdrawn ₹"+str(dfa))
            dfa = 0
            states.append(dfa)
            inputs.append('Withdrawn')
            print("Current balance is ₹" + str(dfa))
            state_diagram(states,inputs)
            return dfa
            
        show_menu()
        x = get_x()
        balance(dfa,x)

    elif dfa == 40:
        if x == 1 or x == 2:
            dfa = 40
            states.append(dfa)
            inputs.append("5,20")
            print("\nCannot add any further amount")
            print("Current balance is ₹" + str(dfa))
        elif x == 3:
            dfa = dfa - 25
            states.append(dfa)
            inputs.append('Buy')
            print("\nYou have bought a gumball")
            print("Current balance is ₹" + str(dfa))
        elif x == 4:
            print("\nYou have withdrawn ₹"+str(dfa))
            dfa = 0
            states.append(dfa)
            inputs.append('Withdrawn')
            print("Current balance is ₹" + str(dfa))
            state_diagram(states,inputs)
            return dfa
        
        show_menu()
        x = get_x()
        balance(dfa,x)
    
    else:
        print("\nSorry Something Went Wrong")

print("\nWelcome to Gumball Machine")
print("Enter ₹25 to buy a gumball")
print("\nCurrent balance is ₹0")
# print("\nSelect an option")
# print("1. Insert ₹5")
# print("2. Insert ₹20")
# print("3. Buy Gumball")
# print("4. Withdraw money")
show_menu()
x = get_x()
balance(dfa,x)
