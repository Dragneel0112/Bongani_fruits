#!/usr/bin/python3
"""
Contains the TestFruitDocs classes
"""

from datetime import datetime
import inspect
import models
from models import fruit
from models.base_model import BaseModel
import pep8
import unittest
Fruits = fruit.Fruits


class TestFruitsDocs(unittest.TestCase):
    """Tests to check the documentation and style of Fruits class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.Fruits_f = inspect.getmembers(Fruits, inspect.isfunction)

    def test_pep8_conformance_Fruits(self):
        """Test that models/fruits.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/fruit.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_fruits(self):
        """Test that tests/test_models/test_fruit.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_fruit.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_fruit_module_docstring(self):
        """Test for the fruit.py module docstring"""
        self.assertIsNot(Fruits.__doc__, None,
                         "fruit.py needs a docstring")
        self.assertTrue(len(Fruits.__doc__) >= 1,
                        "fruit.py needs a docstring")

    def test_fruit_class_docstring(self):
        """Test for the Fruits class docstring"""
        self.assertIsNot(Fruits.__doc__, None,
                         "Fruits class needs a docstring")
        self.assertTrue(len(Fruits.__doc__) >= 1,
                        "Fruits class needs a docstring")

    def test_Fruits_func_docstrings(self):
        """Test for the presence of docstrings in Fruits methods"""
        for func in self.Fruits_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFruits(unittest.TestCase):
    """Test the Fruits class"""
    def test_is_subclass(self):
        """Test that Fruits is a subclass of BaseModel"""
        fruits = Fruits()
        self.assertIsInstance(fruits, BaseModel)
        self.assertTrue(hasattr(fruits, "id"))
        self.assertTrue(hasattr(fruits, "created_at"))
        self.assertTrue(hasattr(fruits, "updated_at"))

    def test_name_attr(self):
        """Test that Fruits has attribute name, and it's an empty string"""
        fruits = Fruits()
        self.assertTrue(hasattr(fruits, "name"))
        if models.storage_t == 'db':
            self.assertEqual(fruits.name, None)
        else:
            self.assertEqual(fruits.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        f = Fruits()
        new_d = f.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in f.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        f = Fruits()
        new_d = f.to_dict()
        self.assertEqual(new_d["__class__"], "Fruits")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], f.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], f.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        fruits = Fruits()
        string = "[Fruits] ({}) {}".format(fruits.id, fruits.__dict__)
        self.assertEqual(string, str(fruits))
