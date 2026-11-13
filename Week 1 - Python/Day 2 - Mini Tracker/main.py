class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return ("{} | {} | {}".format(self.amount, self.category, self.description))
    

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    def add_expense(self, expense_object):
        self.expenses.append(expense_object)
    def get_total(self):
        total=0
        for expense in self.expenses:
            total += expense.amount
        return total
    def show_expense(self):
        print("\n======== Expense Report ========\n")
        for expense in self.expenses:
            print("{}                     : ₹{}".format(expense.category, expense.amount))
        print("\nTotal Spent              : ₹{}\n".format(self.get_total()))
        print("================================")
    def get_category_total(self, category):
        category_total=0
        for expense in self.expenses:
            if category == expense.category:
                category_total += expense.amount
        if category_total == 0:
            return "Expense is zero"
        else:
            return category_total
            

a=Expense(250,"Food","Lunch")
b=Expense(750,"Travel","Delhi")
tracker=ExpenseTracker()
tracker.add_expense(a)
tracker.add_expense(b)
tracker.show_expense()
print(tracker.get_category_total("Food"))



        

        
        
