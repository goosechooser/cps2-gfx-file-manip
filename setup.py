from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cps2-file-manip',
    version='1.0',
    description='allows you to (de)interleave CPS2 graphics files',
    long_description=readme,
    author='M B',
    author_email='dont@me',
    license=license,
    modules=['cps2_file_manip'],
    entry_points={
        'console_scripts': [
            'cps2-file-manip=cps2_file_manip:main'],
        }
    )
