def balance_0(x):
    if x == 1:
        dfa = 5
    elif x == 2:
        dfa = 20
    
def balance_5(x):
    if x == 1:
        dfa = 10
    elif x == 2:
        dfa = 25
    
def balance_10(x):
    if x == 1:
        dfa = 15
    elif x == 2:
        dfa = 30
        
def balance_15(x):
    if x == 1:
        dfa = 20
    elif x == 2:
        dfa = 35

def balance_20(x):
    if x == 1:
        dfa = 25
    elif x == 2:
        dfa = 40

def balance_25(x):
    if x == 1 or x == 2:
        dfa = 25


def balance_30(x):
    if x == 1 or x==2:
        dfa = 30

def balance_35(x):
    if x == 1 or x == 2:
        dfa = 35
        
def balance_40(x):
    if x == 1 or x == 2:
        dfa = 40
        
while __name__ == "__main__":
    print("\nWelcome to Gumball Machine")
    print("\nSelect an option")
    print("1. Insert 5 rupees")
    print("2. Insert 20 rupees")
    print("3. Buy Gumball")
    print("4. Withdraw money")
    x = int(input("\nPlease enter your choice: "))

