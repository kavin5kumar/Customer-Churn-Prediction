from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    This fn gets the requirements from the given file
    '''

    req = []

    with open(file_path) as f:
        req = f.readlines()
        req = [r.replace("\n", "") for r in req]

        if HYPHEN_E_DOT in req:
            req.remove(HYPHEN_E_DOT)
        
    return req



setup(
    name='Customer Churn Prediction',
    version='0.0.1',
    author='Kavin Kumar',
    author_email='pkavin2161@gmail.com',
    packages=find_packages(),
    install_required=get_requirements('requirements.txt')
)

