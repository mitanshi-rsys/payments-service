import unittest

from refund_service import process_refund, to_cents


class RefundTests(unittest.TestCase):
    def test_two_decimals(self):
        self.assertEqual(to_cents("10.50"), 1050)

    def test_whole_number(self):
        self.assertEqual(to_cents("10"), 1000)

    def test_refund_ok(self):
        self.assertEqual(process_refund(5000, "10.50")["cents"], 1050)

    def test_refund_too_big(self):
        with self.assertRaises(ValueError):
            process_refund(1000, "20.00")

    def test_three_decimals_rounds_to_cents(self):
        # JIRA-123: 10.999 should round to 11.00 (1100 cents), not crash.
        self.assertEqual(to_cents("10.999"), 1100)


if __name__ == "__main__":
    unittest.main()
