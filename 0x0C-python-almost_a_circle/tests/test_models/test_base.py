#!/usr/bin/python3
"""
Unittest for base.py
"""


import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """tests instances, methods from base class"""
    def setUp(self):
        """sets variable everytime"""
        Base._Base__nb_objects = 0

    def test_type_class(self):
        """tests if class exists"""
        self.assertEqual(str(type(Base())), "<class 'models.base.Base'>")

    def test_create_id_default(self):
        """tests whether id is being created correctly or not"""
        b1 = Base()
        b2 = Base()
        self.assertEqual((b1.id), 1)
        self.assertEqual((b2.id), 2)

    def test_create_id_custom(self):
        """id custom"""
        b1 = Base(14)
        b3 = Base(35)
        self.assertEqual((b1.id), 14)
        self.assertEqual((b3.id), 35)

    def test_args(self):
        with self.assertRaises(TypeError) as e:
            b1 = Base(12, 23)

    def test_negative(self):
        b5 = Base(-5)
        self.assertEqual((b5.id), (-5))

    def test_empty_json(self):
        """tests if list is empty"""
        lis = Base.to_json_string([])
        self.assertEqual(lis, "[]")

    def test_emptydict_json(self):
        """tests for empty dict"""
        dic = Base.to_json_string([{}])
        self.assertEqual(dic, "[{}]")

    def test_nonefile(self):
        """tests for none file"""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_from_string_set(self):
        """tests func from_json with set"""
        with self.assertRaises(TypeError) as e:
            Base.from_json_string({1, 2})
        self.assertEqual("the JSON object must be str, not 'set'",
                         str(e.exception))

    def test_empty_list_to_file(self):
        """tests empty list for save_to_file method"""
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_json_list_dicts(self):
        """tests for multiple dicts in to_json_string."""
        lis = Base.to_json_string([{"a": 1}, {"b": 2}])
        self.assertEqual(type(lis), str)

    def test_from_json_string_list(self):
        """tests for list from_json_method."""
        with self.assertRaises(TypeError) as e:
            Base.from_json_string([1, 2, 3])
        self.assertEqual("the JSON object must be str, not 'list'",
                         str(e.exception))

    def test_jsonstringerror(self):
        """Test for from_json_method with int."""
        with self.assertRaises(TypeError):
            Base.from_json_string(39)

    def test_jsonstring_emptydict(self):
        """Test json with empty dict"""
        list_input = [{}]
        json_list_input = Base.to_json_string(list_input)
        listob = Base.from_json_string(json_list_input)
        self.assertEqual(listob, [{}])

    def test_json_from_none(self):
        """test a none in a json string"""
        ans = Base.to_json_string(None)
        self.assertEqual(ans, "[]")

    def test_saves_empty_list_in_file(self):
        """test to save an empty list to a file"""
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

if __name__ == '__main__':
    unittest.main()
