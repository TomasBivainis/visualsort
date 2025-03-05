# setup.py
from setuptools import setup, find_packages

setup(
    name='visualsort',                          # Name of your package
    version='0.1',                              # Package version
    packages=find_packages(),                   # Automatically find all packages
    install_requires=[                          # Dependencies
        'pillow',                                # Example dependency
        'random',
        'os',
        'moviepy',
        'numpy',
        'PIL',
    ],
    test_suite='tests',                         # Location of tests
    tests_require=[                             # Test dependencies
        'pytest',
        'pytest-mock',
    ],
    author='Tomas Bivainis',
    author_email='bivainis.tomas@gmail.com',
    description='A short description of your package',
    long_description=open('README.md').read(),  # Detailed description from README
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_package',  # GitHub or project URL
    classifiers=[                               # Package classifiers
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
