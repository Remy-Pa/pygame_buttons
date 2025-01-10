from setuptools import setup, find_packages

setup(
    name='pygame_buttons',
    version='0.1.0',
    author='Remy-Pa',
    author_email='remy.paquette@gmail.com',
    description='Adds different types of buttons to use with pygame',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Remy-Pa/pygame_buttons/',
    packages=find_packages(where = 'source'),
    package_dir={'': 'source'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pygame'
    ],
)
