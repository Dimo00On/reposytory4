import unittest
import parser
from bot import get_text_messages


class TestBot(unittest.TestCase):
    def test_error(self):
        message = ""
        with self.assertRaises(AttributeError):
            get_text_messages(message)


class TestParser(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(KeyError):
            parser.getTemperature("what", "it")

    def test_size_1(self):
        s = parser.getTemperature(parser.towns[parser.name[0]], parser.time[0])
        self.assertEqual(len(s), 1)

    def test_size_2(self):
        s = parser.getTemperature(parser.towns[parser.name[1]], parser.time[1])
        self.assertEqual(len(s), 24)

    def test_name(self):
        self.assertEqual(parser.name[1], 'Долгопрудный')


if __name__ == "__main__":
    unittest.main()
