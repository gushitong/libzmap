
from setuptools import find_packages
from setuptools import setup

# requirements
install_requires = []

setup(name="libzmap",
      version="v0.0.1",
      description="zmap binding for python",
      author="gushitong",
      author_email="gushitong@gmail.com",
      packages=find_packages(),
      url="https://github.com/gushitong/python-libzmap",
      install_requires=install_requires)
