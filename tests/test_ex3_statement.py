import unittest
from ex3_statement.ex3_statement import statement


class TestStatement(unittest.TestCase):
    def test_statement_wrong_play_type(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 55
                }
            ]
        }
        plays = {
            "hamlet": {"name": "Hamlet", "type": "something"}
        }
        with self.assertRaises(ValueError):
            statement(invoice, plays)

    def test_statement_tragedy_less_equal_than_30_people(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 29
                },
                {
                    "playID": "macbeth",
                    "audience": 28
                }
            ]
        }
        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "macbeth": {"name": "Macbeth", "type": "tragedy"}
        }
        response = "Statement for BigCo\n" \
                   " Hamlet: $400.00 (29 seats)\n" \
                   " Macbeth: $400.00 (28 seats)\n" \
                   "Amount owed is $800.00\n" \
                   "You earned 0 credits\n"
        self.assertEqual(statement(invoice, plays), response)

    def test_statement_tragedy_greater_than_30_people(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 67
                }
            ]
        }
        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"}
        }
        response = "Statement for BigCo\n" \
                   " Hamlet: $770.00 (67 seats)\n" \
                   "Amount owed is $770.00\n" \
                   "You earned 37 credits\n"
        self.assertEqual(statement(invoice, plays), response)

    def test_statement_comedy_less_equal_than_20_people(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "as-like",
                    "audience": 18
                }
            ]
        }
        plays = {
            "as-like": {"name": "As You Like It", "type": "comedy"}
        }
        response = "Statement for BigCo\n" \
                   " As You Like It: $354.00 (18 seats)\n" \
                   "Amount owed is $354.00\n" \
                   "You earned 3 credits\n"
        self.assertEqual(statement(invoice, plays), response)

    def test_statement_comedy_greater_than_20_people(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "as-like",
                    "audience": 53
                }
            ]
        }
        plays = {
            "as-like": {"name": "As You Like It", "type": "comedy"}
        }
        response = "Statement for BigCo\n" \
                   " As You Like It: $724.00 (53 seats)\n" \
                   "Amount owed is $724.00\n" \
                   "You earned 33 credits\n"
        self.assertEqual(statement(invoice, plays), response)


if __name__ == '__main__':
    unittest.main()
