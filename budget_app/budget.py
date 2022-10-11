
class Category:
  
    def __init__(self, nameOfcatagory):
        self.nameOfcategory = nameOfcatagory
        self.ledger = []
        self.funds = 0

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description" : description})
        self.funds += amount

    def withdraw(self, wamount, description = ""):
        if self.funds > wamount:
              self.funds = self.funds - wamount
              wamount = wamount * -1
              self.ledger.append({"amount": wamount, "description" : description})
              return True
        else:
            return False

    def get_balance(self):
        return self.funds
#For this method, think of how you are going to create your class instances
#Think of how you are going to use those objects with this method
    def transfer(self, tamount, category):
        if tamount > self.funds:
            return False
        else:
            self.funds = self.funds - tamount
            tamount *= -1
            self.ledger.append({"amount": tamount, "description" : f"Transfer to {category.nameOfcategory}"})
            tamount *= -1
            self.ledger.append({"amount": tamount, "description" : f"Tranfer from {self.nameOfcategory}"})
            
    def check_funds(self, camount):
        if camount > get_balance():
            return True
        else:
            return False

    def __str__(self): #Whatever data you want to display must be on the return statement
        name_length = len(self.nameOfcategory)
        star_count = (30 - name_length) // 2
        title = "*" * star_count + self.nameOfcategory + "*" * star_count
        ledger_lst = ""
        for lst_item in self.ledger:
            amt = lst_item.get("amount")
            descr = lst_item.get("description")
            if len(descr) > 30:
                descr = descr[:15] + '& more'
              
            ledger_lst += descr + str(amt).rjust(30 - len(descr)) + "\n"
        object_lst = title + "\n" + ledger_lst + "Total: " + str(self.funds)
        return object_lst #Returned values get printed auto when the object of that particula class is     
                          #printed i.e print(food)
      

      

