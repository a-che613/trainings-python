from utils.expense_csv_handler import get_expenses
import datetime


months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


# Looking for methods to reduce the loops

def view_expenses():
    expenses = get_expenses()
    total_per_category = 0
    all_category_total = 0
    
    if not expenses:
        print("No expenses found.")
    else:
      method = input('Enter 1 to view all, or 2 to view by category or 3 to view for a month: ')
      if method == '1':
        displayExpenses(arr=expenses, total=all_category_total)
      elif method == '2':
        expense_categories = []
        
        # trying to display just a single category name for categories 
        # that occur more than once. 
        for expense in expenses:
          if expense['category'] not in expense_categories:
            expense_categories.append(expense['category'])
        
        for expense in expense_categories:
          print('-', expense)
            
        category = input('Enter your category: ')
        
        expensesList = [expense for expense in expenses if expense['category'] == category.capitalize()] 
        
        
        displayExpenses(arr=expensesList, total=total_per_category)
      elif method == '3':
        month = input('Enter the month you wish to check: ')
        
        
        for expense in expenses:
          date_obj = datetime.datetime.strptime(expense['date'], "%d-%m-%Y")
          
          # users can enter the number representation of the month
          # or the month string itself
          if month.isnumeric():
            while  int(month) < 0 or int(month) > 12:
              month = input('Please enter a valid month e.g (1 or \'January\'): ')
            if(int(date_obj.month) == int(month)):
              print(expense)
            else:
              print('No expense found for that month')
          else:
            if int(months[month.capitalize()]) == int(date_obj.month):
              print(expense)
            else:
              print('No expense found for that month')
      else:
        print('invalid choice')
              
        



def displayExpenses(arr, total):       
  for expense in arr:
    total += float(expense['amount'])
    print('-----------------------')
    print(f'Category: {expense['category']}\nDate: {expense['date']}\nAmount: {expense['amount']}')
    print('-----------------------')
  print(f'This is your total expenses -- {total}')