from setuptools import setup

setup(name='mypackage',
	  version='0.1',
	  description='My package description.',
	  url='https://github.com/Michael-Signorotti/example-python-package',
	  author='Michael Signorotti',
	  author_email='my_email_here',
	  license='Apache License, Version 2.0',
	  packages=['mypackage', 'mypackage/mysubpackage'],
	  zip_safe=False)
