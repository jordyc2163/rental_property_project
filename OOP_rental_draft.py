class HashTable:
    def __init__(self):
        self.MAX = 10
        self.array = [None for i in range(self.MAX)]

    def getHash(self, key):
        h = 0
        for letter in key:
            h += ord(letter)
        return h % self.MAX
    
    def addValue(self, instance):
        h = self.getHash(instance.name)
        
        self.array[h] = instance
#         found = False
#         for idx, element in enumerate(self.array[h]):
#             if element[0].keys() == key:
#                 self.array[h][idx] = (key, value)
#                 found = True
#                 break   
                
#         if not found:
#             self.array[h].append((key, value))
    
    def getValue(self, instance):
        return f"Here is all the information for {instance.name} | income: {instance.income}, expenses: {instance.expenses}, total investment: {instance.total_investment}"
                
    
    def deleteItem(self, instance):
        h = self.getHash(instance.name)
        print(f"You have successfully removed {instance.name} from your watchlist!")
        del self.array[h]
        return

class Properties:
    def __init__(self, name):
        self.name = name
        self.income = {}
        self.expenses = {}
        self.total_investment = {"down payment": 0,
                               "closing cost": 0,
                               "renovation": 0}
    def __repr__(self):
        return self.name

class RentalPropertyCalc(HashTable):
    def __init__(self):
        super().__init__()
        self.prop_list = []
        
        
    def addProperty(self):
        unit = input("What is the name of your property? ")
        prop = Properties(unit)
        self.addValue(prop)
        self.prop_list.append(unit)
        print(f"{unit} added.")
    
    
    def addIncome(self):
        unit = input("Which property is this for? ")
        h = self.getHash(unit)
        
        Exit = False
        while not Exit:
            incometype = input("What type of income will you be recieving? (Ex: Rent) ")
            incomeval = int(input(f"How much will you recieve monthly from {incometype}? $"))

            self.array[h].income[incometype] = incomeval

            keepadd = input("Would you like to add more income sources? (y/n) ").lower().strip()
            if keepadd == 'y':
                continue
            else:
                print(f"Monthly Income source towards {unit} have been added.")
                Exit = True
        
        new_prop_add = input("Would you like to add income sources to other properties? (y/n) ").lower().strip()
        if new_prop_add == "y":
            self.addIncome()
            
        
    def totalIncome(self, instance):
        
        total_sum = 0
        for prices in instance.income.values():
            total_sum += prices
        
        return total_sum
    
    
    def addExpenses(self):
        unit = input("Which property are you adding expenses for? ")
        h = self.getHash(unit)
        
        Exit = False
        while not Exit:
            expensetype = input("What type of expense will you have monthly? (Ex: Tax, Insurance, Mortgage) ")
            cost = int(input(f"How much will you be paying monthly for {expensetype}? $"))

            self.array[h].expenses[expensetype] = cost

            keepadd = input("Would you like to add more expenses? (y/n) ").lower().strip()
            if keepadd == 'y':
                continue
            else:
                print(f"Monthly Expenses towards {unit} have been added.")
                Exit = True
        
        new_prop_add = input("Would you like to add Expenses to other properties? (y/n) ").lower().strip()
        if new_prop_add == "y":
            self.addExpenses()
            
            
    def totalExpenses(self, instance):

        total_sum = 0
        for prices in instance.expenses.values():
            total_sum += prices
        
        return total_sum
    
    
    def calcROI(self, instance):
        roi = ((self.calcCashFlow(instance) * 12) / self.totalInvestment(instance)) * 100
        return roi
    
    
    def calcCashFlow(self, instance):
        return self.totalIncome(instance) - self.totalExpenses(instance)
    
    
    def addInitialInvestment(self):
        unit = input("Which property are you adding initial investment info to? ")
        h = self.getHash(unit)
        
        investment = self.array[h].total_investment
        downp = int(input(f"What will the down payment be on {unit}? "))
        closing_cost = int(input(f"What will your closing cost be for {unit} give or take? "))
        renovation = int(input(f"Please add what you believe will be the renovation costs for {unit}. "))
        
        investment["down payment"] = downp
        investment["closing cost"] = closing_cost
        investment["renovation"] = renovation
        
        print(f"Foreseeable Initial Investment for {unit} has been added.")
        
        
    def totalInvestment(self, instance):
        investment = instance.total_investment
        total = 0
        for key in investment:
            total += investment[key]
        
        return total
    
            
    def viewWatchlist(self):
        print(f"Your Watchlist | {self.prop_list}")
    
    
    def update(self, instance):
        attribute = input(f"Which component of {instance.name} are you updating? (income | expenses | investment OR delete property) ").lower().strip()
        
        if attribute == "delete property":
            confirm = input(f"Are you sure you want to remove {instance.name} from watchlist? (y/n) ").lower().strip()
            if confirm == 'y':
                self.deleteItem(instance)
                self.prop_list.remove(instance.name)
        elif attribute == "income":
            adding_income = input("Are you adding an income source? (y/n) ")
            if adding_income == "y":
                self.addIncome()
            else:
                for k, v in instance.income.items():
                    print(f"{k} - {v}", end = " | ")
                updated = input(f"Which income source are you updating for {instance.name}? ").lower().strip()
                new_amount = int(input("Enter the new amount of income expected for this property: $"))
                instance.income[updated] = new_amount
                print(f"{instance.income} update successful")
            
        elif attribute == "expenses":
            adding_expense = input("Are you adding an source of expense? (y/n) ")
            if adding_expense == "y":
                self.addExpenses()
            else:
                for k, v in instance.expenses.items():
                    print(f"{k} - {v}", end = " | ")
                updated = input(f"Which expenses source are you updating for {instance.name}? ").lower().strip()
                new_amount = int(input("Enter the new amount of expenses expected for this property: $"))
                instance.expenses[updated] = new_amount
                print(f"{instance.expenses} update successful")
        
        elif attribute == "investment":
            key_select = input("Please select which to update: down payment | closing cost | renovation ").lower().strip()
            new_amount = int(input(f"Enter the new amount for {instance.name}'s {key_select}: $"))
            instance.total_investment[key_select] = new_amount
            print(f"{instance.total_investment} update successful")
            
            
            
    def run(self):
        if self.prop_list:
            print("Welcome Back!")
        else:
            print("To begin calculating ROI, we need to gather some information from you first")
            self.addProperty()
            self.addIncome()
            self.addExpenses()
            self.addInitialInvestment()
            print("Now that we've acquired valuable info, we can present you an ROI for these expected properties!")
            
        while True:
            for prop in self.prop_list:
                print(prop + " | " )
            unit = input("Please choose your Property from Watchlist to work with OR type 'quit' to return - ")
            if unit == 'quit':
                break
            else:
                h = self.getHash(unit)
                instance = self.array[h]
            
            while True:
                print("Things you can do here")
                print("Calculate ROI | View Total Income | View Total Expenses | Cash Flow | Update an Existing Property | View Watchlist | Add Property | Quit")
                selection = input("What would you like to do? ").lower().strip()
                if selection == "calculate roi":
                    print(f"Here is the ROI for {unit}: {self.calcROI(instance)}")
                elif selection == "view total income":
                    print(f"Here is the Total Income for {unit}: {self.totalIncome(instance)}")
                elif selection == "view total expenses":
                    print(f"Here is the Total Expenses for {unit}: {self.totalExpenses(instance)}")
                elif selection == "cash flow":
                    print(f"Here is the Cash Flow for {unit}: {self.calcCashFlow(instance)}")
                elif selection == "update" or selection == "update an existing property":
                    self.update(instance)
                elif selection == "view watchlist":
                    self.viewWatchlist()
                elif selection == "add property":
                    self.addProperty()
                elif selection == "quit":
                    break

