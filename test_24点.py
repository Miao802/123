import unittest
from unittest.mock import patch
from 24点 import *

class Test24Game(unittest.TestCase)

    def test_card_map(self):
        self.assertEqual(card_map['A'], 1)
        self.assertEqual(card_map['J'], 11)
        self.assertEqual(card_map['Q'], 12)
        self.assertEqual(card_map['K'], 13)

    def test_generate_cards(self):
        cards = generate_cards()
        self.assertEqual(len(cards), 4)
        for card in cards:
            self.assertTrue(1 <= card <= 13)

    @patch('builtins.input', side_effect=['A 5 J 8'])
    def test_input_cards_valid(self, mock_input):
        """测试有效输入"""
        cards = input_cards()
        self.assertEqual(cards, [1, 5, 11, 8])

    def test_display_cards(self):
        """测试牌面显示"""
        self.assertEqual(display_cards([1, 5, 11, 8]), ['A', '5', 'J', '8'])
        self.assertEqual(display_cards([12, 13, 10, 2]), ['Q', 'K', '10', '2'])

    def test_evaluate_expression(self):
        """测试表达式求值"""
        self.assertTrue(evaluate_expression("8/(3-8/3)"))
        self.assertTrue(evaluate_expression("6*6-6-6"))
        self.assertFalse(evaluate_expression("1+2+3+4"))
        self.assertFalse(evaluate_expression("1/0"))

    def test_find_24_expressions_known_solutions(self):
        """测试已知有解的情况"""
        # 测试 3,3,8,8
        solutions = find_24_expressions([3, 3, 8, 8])
        self.assertTrue(len(solutions) > 0)
        self.assertTrue(any("8/(3-8/3)" in expr for expr in solutions))


    def test_find_24_expressions_no_solution(self):
        """测试无解的情况"""
        solutions = find_24_expressions([1, 1, 1, 1])
        self.assertEqual(len(solutions), 0)

        solutions = find_24_expressions([1, 1, 1, 2])
        self.assertEqual(len(solutions), 0)

    def test_find_24_expressions_multiple_solutions(self):
        """测试多解情况"""
        solutions = find_24_expressions([1, 2, 3, 4])
        self.assertTrue(len(solutions) >= 1)
