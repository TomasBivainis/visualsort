# setup.py
from setuptools import setup, find_packages
from setuptools.command.install import install
import os

# Import the ensure_ffmpeg function
from util.check_ffmpeg import ensure_ffmpeg

class CustomInstallCommand(install):
    """Custom installation to ensure FFMPEG is installed."""
    def run(self):
        ensure_ffmpeg()  # Call the function to check and install FFMPEG
        install.run(self)

setup(
    name='visualsort',                          # Name of your package
    version='0.1',                              # Package version
    packages=find_packages(),                   # Automatically find all packages
    install_requires=[                          # Dependencies
        'pillow',                                # Example dependency
        'moviepy',
        'numpy',
        'pytest',
        'pytest-mock',
        'urllib3',
    ],
    test_suite='tests',                         # Location of tests
    tests_require=[                             # Test dependencies
        'pytest',
        'pytest-mock',
    ],
    author='Tomas Bivainis',
    author_email='bivainis.tomas@gmail.com',
    description='Visualsort lets you write sorting algorithms with given functions and then render them to videos.',
    long_description=open('README.md').read(),  # Detailed description from README
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_package',  # GitHub or project URL
    classifiers=[                               # Package classifiers
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    cmdclass={
        'install': CustomInstallCommand,  # Use the custom install command
    },
)
