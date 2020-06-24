from setuptools import setup, find_packages
import io
import re
import os

"""
Remember to:
    Set app_name
    Set description 
    Set install_requires
    Set entry_points
    Set keywords
"""

app_name = 'myapp'

with io.open(f"./{app_name}/__init__.py", encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name=app_name,
    version=version,
    author='Rafael Padilha',
    author_email='rafaelpadilha@hotmail.com.br',
    packages=find_packages(exclude='tests'),
    long_description=long_description,
    url="",
    description=" Description for the app. ",
    install_requires=['pytest', 'click'],
    entry_points={
        'console_scripts': [
            'myapp = myapp.main:start',
        ],
    },
    classifiers=[
        'Intended Audience :: Information Technology',
    #    'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
    #    'Topic :: Software Architecture',
    ],
    keywords=(
        'Python simple app',
        'Template',
        'Container'
    )
)
