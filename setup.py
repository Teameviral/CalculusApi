from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='calcuap',
    version='0.0.1',
    author='wbavishek',
    author_email='wbavishek@gmail.com',
    description='A package for integration and differentiation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Teameviral/Calculusapi',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'tensorflow',
        'numpy',
        'flask',
    ],
)
