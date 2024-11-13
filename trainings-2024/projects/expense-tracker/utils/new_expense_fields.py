import datetime

def newExpenseFields():
  date = input("Enter date (DD/MM/YYYY): ")
  date_obj = None
  
  while date_obj is None:
    try:
      date_obj = datetime.datetime.strptime(date, "%d/%m/%Y")
      break
    except Exception as e:
      print('Invalid date!')
    date = input("Please enter a valid date (DD/MM/YYYY) e.g. 04/11/2023: ")
      
      
  category = input("Enter category: ")
  while not category:
    category = input("Please enter a category: ")
  
  amount = input("Enter amount: ")
  
  while not amount.isnumeric():
    amount = input("Please enter a valid amount e.g 100000: ");
  
  
  return {'date': date_obj.strftime("%d-%m-%Y"), 'category': category.capitalize(), 'amount': float(amount)}