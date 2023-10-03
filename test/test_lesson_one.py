import unittest

import lesson_one


class TestLessonOne(unittest.TestCase):
    def test_sum_a_b_normal(self):
        self.assertEqual(lesson_one.sum_a_b(3,4), 7)

    def test_data_type_lesson_one(self):
        self.assertEqual(lesson_one.data_type_lesson(), "")

    def test_factorial_lesson_one(self):
        self.assertEqual(lesson_one.factorial_lesson(3), 6)

    def test_average_lesson_one(self):
        self.assertEqual(lesson_one.average_lesson(3,3,3,3), 3.0)

    def test_calculate_lesson_one(self):
        self.assertEqual(lesson_one.calculate_lesson(3,4,1, 2), 2.0)