import unittest

import lesson_two
import lesson_two_2nd


class TestLessonTwo(unittest.TestCase):
    def test_discount_greater_than_and_member(self):
        self.assertEqual(lesson_two.get_discount(200000, "y"), 20)

    def test_discount_greater_than_and_not_member(self):
        self.assertEqual(lesson_two.get_discount(200000, "n"), 10)

    def test_discount_less_than_and_member(self):
        self.assertEqual(lesson_two.get_discount(199000, "y"), 0)

    def test_discount_less_than_and_not_member(self):
        self.assertEqual(lesson_two.get_discount(199000, "n"), 0)

    def test_member_value_not_y_or_n(self):
        self.assertEqual(lesson_two.get_discount(200000, "w"), 0)

    def test_total(self):
        self.assertEqual(lesson_two.count_total(200000, "y"), 160000.0)

    def test_total_less_than(self):
        self.assertEqual(lesson_two.count_total(100000, "y"), 100000.0)

    def test_total_greater_than_not_member(self):
        self.assertEqual(lesson_two.count_total(200000, "n"), 180000.0)


class TestLessonTwoSec(unittest.TestCase):
    def test_score(self):
        self.assertEqual(lesson_two_2nd.get_score_grade(95), "A")


if __name__ == '__main__':
    unittest.main()
