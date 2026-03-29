from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->list[str]:
    requirements =[]
    with open(file_path) as file_obj:
        requirements=[req.replace('\n'," ").strip()    for req in file_obj.readlines()]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    
    return requirements

setup(
    name= 'data science project',
    version= '0.0.1',
    author= 'van',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)

