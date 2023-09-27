from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    include_package_data=True,
    name='main_cd',  
    version='0.0.1',   
    description='Optimization of the parameters of a protocol for continuous delivery (CD) of entanglement in a quantum network.',
    author='Álvaro G. Iñesta',
    license='MIT',
    packages=find_packages(),
    install_requires=requirements
)