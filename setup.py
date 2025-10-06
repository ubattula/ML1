from setuptools import find_packages, setup

from typing import List
hyphen_e = "-e ."
def get_requirements(get_path:str)->List[str]:
    '''
    this function return the list of requirements
    '''
    requirements = []
    with open(get_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('/n', "") for req in requirements]
        
        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
            
    return requirements


setup(
name = 'mlproject',
version ='0.0.1',
author='ubattula',
author_email='ushasri.battula@capgemini.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)