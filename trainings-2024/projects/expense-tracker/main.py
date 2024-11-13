from functions.add_expense import add_expense
from functions.view_expenses import view_expenses
from utils.expense_csv_handler import get_expenses


print(get_expenses() if get_expenses().__len__() > 0 else 'No expense found')
    
    
# expense1 = Expense(category='Transportation', date='11/02/2022', amount='20000')


# print('ljlj', type(expense1.getExpenseDetails()))

        
         
def calculate_total_expenses():
  expenses = get_expenses()
  total = sum(float(expense['amount']) for expense in expenses)
  print(f"Total Expenses: {total:.2f}")


while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        calculate_total_expenses()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
        
        
