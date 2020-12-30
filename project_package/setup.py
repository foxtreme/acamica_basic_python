from setuptools import find_packages, setup

setup(
    name="my_package",
    version="0.1.0",
    author="Chris Charry",
    author_email="chriseth@gmail.com",
    packages=find_packages(),
    url="https://github.com/foxtreme/my_package.git",
    license="MIT",
    description="This is my package",
    long_description=open("README.rst").read(),
    install_requires=[]
)

