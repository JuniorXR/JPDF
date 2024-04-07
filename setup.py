from setuptools import setup, find_packages

setup(
    name='junior',
    version='v1.0',
    packages=find_packages(),
    package_data={'junior': ['*.py']},
    install_requires=["fpdf2","sympy"],
)