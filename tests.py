import unittest
from myencoder import convertToHex
from myencoder import encodeToBase64
from myencoder import decodeFromBase64

class TestConvertions(unittest.TestCase):
    def test_convertToHex(self):
        data = 'test string'
        lowercase_expected_result = '7465737420737472696e67'
        uppercase_expected_result = '5445535420535452494e47'

        lowercase_actual_result = convertToHex(data)
        self.assertEqual(lowercase_expected_result, lowercase_actual_result)

        uppercase_actual_result = convertToHex(data.upper())
        self.assertEqual(uppercase_expected_result, uppercase_actual_result)

    def test_convert_to_hex_with_empty_string(self):
        data = ''
        expected_result = ''
        actual_result = convertToHex(data)
        self.assertEqual(expected_result, actual_result)

    def test_convert_to_hex_white_space(self):
        data = '            '
        expected_result = '202020202020202020202020'
        actual_result = convertToHex(data)
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()
