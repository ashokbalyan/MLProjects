from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(filepath:str)->List[str]:
    '''
      this function will return a list of requirements
    '''
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements      


setup(
    name='MLProjects',
    version="1.0",
    author="Ashok Kumar Balyan",
    author_email="ashok.balyan@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)