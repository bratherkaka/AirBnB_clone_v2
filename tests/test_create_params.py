# tests/test_create_params.py

import unittest
from console import HBNBCommand
from io import StringIO
import sys
from unittest.mock import patch
from models import storage

class TestCreateParams(unittest.TestCase):

    def setUp(self):
        self.hbnb_console = HBNBCommand()

    def test_create_with_params(self):
        with patch('sys.stdout', new=StringIO()) as output:
            sys.stdin = StringIO('create State name="California"\n')
            self.hbnb_console.cmdloop()
            state_id = output.getvalue().strip()
        
        state = storage.get("State", state_id)
        self.assertIsNotNone(state)
        self.assertEqual(state.name, "California")

        # Add more tests for other attributes and classes as needed

if __name__ == '__main__':
    unittest.main()
