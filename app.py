from expenses import expenses
from payments import payments

def get_expenses():
  return sum(expenses.values())

def get_payments():
  return sum(payments.values())

def get_debt():
  return get_expenses() - get_payments()

print(f"juicepay {get_debt()}€")