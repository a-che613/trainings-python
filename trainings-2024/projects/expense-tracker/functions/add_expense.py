from models.expense_class import Expense
from utils.new_expense_fields import newExpenseFields
from utils.expense_csv_handler import save_expenses


expenses = [];




def add_expense():
  
    # extracted the input fetching logic incase i might
    # need to create a new expense
    # along the line elsewhere
    newExpense = newExpenseFields();
    
    
    expense = Expense(category=newExpense['category'], date=newExpense['date'], amount=newExpense['amount'])
    
    expenseDetails = expense.getExpenseDetails();
    expenses.append(expenseDetails)
    
    
    addAnother = input('Will you like to add another expense? (y/n): ')
    if addAnother == 'y':
      add_expense()
    else:
      # calling the save_expenses function of our
      # csv helper file
      save_expenses(expenses)
      print("Expense(s) added successfully!")