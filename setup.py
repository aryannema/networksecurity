'''
This setup.py is an essential part of packaging and distributing Python projects.
It is used by setuptools to define the configuration of your project, such as metadata, dependencies 
and more.
'''


from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    """
    This fuction will return the list of requirements.
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file:
            lines = file.readlines()

            # process each line:

            for line in lines:
                requirement = line.strip()
                #ignore the empty lines and -e . 

                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found.")
    

    return requirement_lst

print(get_requirements())


setup(
    name = "Network Security",
    version= "0.0.1",
    author= "Aryan Nema",
    author_email= "aaryan.techy@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)