import unittest

from validation import validate_fields_for_operation, preprocess_argument


class TestValidation(unittest.TestCase):
    def test_fields_validation(self):
        columns = ["column1", "column2", "column3", "column4", "column5"]
        val_res, val_msg = validate_fields_for_operation(columns, "sort", "column5")
        self.assertTrue(val_res)
        val_res, val_msg = validate_fields_for_operation(columns, "sort", "column6")
        self.assertFalse(val_res)
        val_res, val_msg = validate_fields_for_operation(columns, "sort", None)
        self.assertFalse(val_res)

    def argument_preprocessing(self):
        res = preprocess_argument("")
        self.assertIsNone(res)
        res = preprocess_argument("column")
        self.assertEquals(res, "column")
        res = preprocess_argument("451.1")
        self.assertEquals(res, 451.1)
