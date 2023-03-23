import unittest
import MySQLdb
from console import HBNBCommand
from io import StringIO
import sys


class TestCreateState(unittest.TestCase):

    def setUp(self):
        self.db = MySQLdb.connect(user='hbnb_test', passwd='hbnb_test_pwd', db='hbnb_test_db', host='localhost')
        self.cursor = self.db.cursor()
        self.hbnb_console = HBNBCommand()

    def tearDown(self):
        self.db.close()

    def test_create_state(self):
        # Get the current number of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Execute the console command to create a new State
        sys.stdin = StringIO('create State name="California"\n')
        sys.stdout = StringIO()
        self.hbnb_console.cmdloop()

        # Get the updated number of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        updated_count = self.cursor.fetchone()[0]

        # Check if the difference is +1
        self.assertEqual(updated_count, initial_count + 1)


if __name__ == '__main__':
    unittest.main()
