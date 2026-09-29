import unittest

from app import get_debt, get_expenses, get_payments
from expenses import expenses
from payments import payments


class JuicePayTests(unittest.TestCase):
	def test_get_expenses(self):
		expenses.clear()
		expenses["28.9.2026"] = 5
		expenses["29.9.2026"] = 5
		expenses["30.9.2026"] = 5
		self.assertEqual(get_expenses(), 15)

	def test_get_payments(self):
		payments.clear()
		payments["1.10.2026"] = 10
		payments["2.10.2026"] = 10
		self.assertEqual(get_payments(), 20)

	def test_debt_is_expenses_minus_payments(self):
		expenses.clear()
		expenses["2.10.2026"] = 10
		payments.clear()
		payments["3.10.2026"] = 5
		self.assertEqual(get_debt(), 5)


if __name__ == "__main__":
	unittest.main()
