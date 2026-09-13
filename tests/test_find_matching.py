#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from src.find_matching import find_matching


class TestFindMatching(unittest.TestCase):

    def test_first(self):
        result = find_matching(
            ["sensitive", "engine", "rubbish", "comment"], "en")
        self.assertIsInstance(
            result, list,
            msg=f"find_matching should return a list. Got {type(result)}.")
        self.assertEqual(
            result, [0, 1, 3],
            msg="find_matching(['sensitive','engine','rubbish','comment'], "
                "'en') should be [0, 1, 3]: 'sensitive', 'engine', and "
                "'comment' all contain 'en'; 'rubbish' does not.")

    def test_calls(self):
        words = ["sensitive", "engine", "rubbish", "comment"]
        with patch('builtins.enumerate',
                   return_value=enumerate(words)) as p:
            find_matching(words, "en")
            p.assert_called_once()

    def test_empty(self):
        result = find_matching([], "en")
        self.assertEqual(
            result, [],
            msg="find_matching([], 'en') should be an empty list: an "
                "empty list cannot contain any matches!")


if __name__ == '__main__':
    unittest.main()
