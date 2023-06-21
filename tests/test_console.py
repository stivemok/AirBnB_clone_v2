#!/usr/bin/python3
""" Unit test for console """
import os
import json
import MySQLdb
import unittest
import sqlalchemy
from io import StringIO
from models import storage
from unittest.mock import patch
from console import HBNBCommand
from models.user import User
from tests import clear_stream
from models.base_model import Basemodel


class TestHBNBCommand(unittest.TestCase):
    """ test class for HBNBCommand class """

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_create(self):
        """ Tests create command with database storage"""
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()

            # create model with none null attribute
            with self.assertRaises(sqlalchemy.exc.OperationalError):
                cons.onecmd('create User')
            # create User instance
            clear_stream(cout)
            cons.onecmd('create User email="stive@gmail.com" password="mok"')
            _id = cout.getvalue().strip()
            dbconnect = MySQLdb.connect(
                host=os.getenv('hbnb_localhost'),
                port=3306,
                user=os.getenv('hbnb_user'),
                passwd=os.getenv('hbnb_pwd'),
                db=os.getenv('hbnb_db'))

            cursor = dbc.cursor()
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(_id))
            result = cursor.fetchone()
            self.assertTrue(result is not None)
            self.assertIn('stive@gmail.com', result)
            self.assertIn('mok', result)
            cursor.close()
            dbc.close()

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_fs_create(self):
        """Tests create command with file storage"""
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            cons.onecmd('create City name="Addis"')
            _id = cout.getvalue().strip()
            clear_stream(cout)
            self.assertIn('City.{}'.format(_id), storage.all().keys())
            cons.onecmd('show City {}'.format(_id))
            self.assertIn("'name': 'Addis'", cout.getvalue().strip())
            clear_stream(cout)
            cons.onecmd('create User name="Stive" age=20 height=174')
            _id = cout.getvalue().strip()
            self.assertIn('User.{}'.format(_id), storage.all().keys())
            clear_stream(cout)
            cons.onecmd('show User {}'.format(_id))
            self.assertIn("'name': 'Stive'", cout.getvalue().strip())
            self.assertIn("'age': 20", cout.getvalue().strip())
            self.assertIn("'height': 174", cout.getvalue().strip())
