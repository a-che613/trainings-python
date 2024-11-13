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


def update_contact(phoneNumber):
  with open('trainings-2024/projects/expense-tracker/expenses.csv', 'r') as contacts_file:
    reader = csv.DictReader(contacts_file, delimiter='\t')

    contacts = list(reader)

    contactToUpdate = {}
    foundContact = False

    for contact in contacts:
      if contact['number'] == phoneNumber:
        foundContact = True
        contactToUpdate = contact
        break
      else:
        foundContact = False

    return {
      "success": foundContact,
      "message": f"trying to update {contactToUpdate}" if foundContact else f"Didn't find a contact with the number {phoneNumber}",
      "data": contactToUpdate
    }


def delete_contact(phoneNumber):
  with open('trainings-2024/projects/expense-tracker/expenses.csv', 'r') as contacts_file:
    reader = csv.DictReader(contacts_file, delimiter='\t')

    contacts = list(reader)
    foundNumber = True

    for contact in contacts:
      if contact['number'] == phoneNumber:
        print(f'Deleting {contact}')
        contacts.remove(contact)
        foundNumber = True
        break
      else:
        foundNumber = False

    return {"success": foundNumber, "message": f"{phoneNumber} deleted successfully" if foundNumber else f"Didn't find a contact with the number {phoneNumber}", "data": contacts}