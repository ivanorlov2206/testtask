import unittest

from app.validation import validate_fields_for_operation, preprocess_argument


class TestValidation(unittest.TestCase):
    def test_fields_validation(self):
        val_res, val_msg = validate_fields_for_operation("sort", "bonus")
        self.assertTrue(val_res)
        val_res, val_msg = validate_fields_for_operation("sort", "column1")
        self.assertFalse(val_res)
        val_res, val_msg = validate_fields_for_operation("sort", None)
        self.assertFalse(val_res)

    def argument_preprocessing(self):
        res = preprocess_argument("")
        self.assertIsNone(res)
        res = preprocess_argument("column")
        self.assertEquals(res, "column")
        res = preprocess_argument("451.1")
        self.assertEquals(res, 451.1)
