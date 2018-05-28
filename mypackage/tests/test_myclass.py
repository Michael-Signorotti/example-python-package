import unittest
from mypackage.mysubpackage import MyClass

class TestMyClass(unittest.TestCase):
	"""This class contains tests for the myclass module."""

	def __init__(self, *args, **kwargs):
		"""
		Construct a TestMyClass object.

		The constructor defined in the unittest.TestCase class can be
		overridden in order to instantiate variables that are used
		throughout the different unit test methods. For instance,
		suppose that all unit test methods refer to the same file or
		database name. We can define a variable for that name below
		after performing logic contained within the constructor of
		the super class.
		"""
		super(TestMyClass, self).__init__(*args, **kwargs)
		print("Constructor")

	def setUp(self):
		"""
		Configure dependencies before each unit test method is run.

		The setup method exists in unittest.TestCase, and we can override
		it below with our own functionality. The setup method is run before
		every unit test method. Dependencies can be configured here.

		For example, suppose that one of our unit test methods queries
		information from a table in a database. If the table does not exist
		in the database and we execute a query, an error will be thrown. In
		order to avoid this, we can create that table and load it with data
		in the setup method.
		"""
		print("setup")

	def test_my_method(self):
		"""Test my_method in MyClass."""
		myclass = MyClass(1)

		self.assertEqual(myclass.my_method(2), 2)



	def tearDown(self):
		"""
		Configure dependencies after each unit test method is run.

		The tearDown method exists in unittest.TestCase, and we can override
		it below with our own functionality. The tearDown method is run after
		each unit test method completes. If dependencies need to be removed,
		that logic can be implemented here.

		For instance, suppose that the unit test methods create a file, and
		ideally, we do not want this file to exist on our system after the
		tests complete. We can first check if this file exists, and delete it
		if necessary.
		"""
		print("tearDown")
