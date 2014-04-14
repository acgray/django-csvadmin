from setuptools import find_packages
from setuptools import setup

setup(name='django-csvadmin',
      version='0.1',
      description='CSV admin',
      author='Adam Gray',
      author_email='acgray@me.com',
      packages=find_packages(),
      package_data={},
      include_package_data=True,
)
