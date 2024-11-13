import csv


def save_expenses(expenses):
  try:
    with open('trainings-2024/projects/expense-tracker/expenses.csv', 'w') as expenses_file:
      fieldnames = ['category', 'date', 'amount']

      writer = csv.DictWriter(expenses_file, fieldnames=fieldnames, delimiter='\t')

      writer.writeheader()

      writer.writerows(expenses);
  except Exception as e:
    print("Couldn't save expenses")
    raise e
  # end try


def get_expenses():
  with open('trainings-2024/projects/expense-tracker/expenses.csv', 'r') as expenses_file:
    reader = csv.DictReader(expenses_file, delimiter='\t')

    contacts = list(reader)


    return contacts


