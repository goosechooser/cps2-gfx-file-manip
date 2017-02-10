from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cps2-file-manip-unstable',
    version='1.1',
    description='allows you to (de)interleave CPS2 files',
    long_description=readme,
    author='M B',
    author_email='dont@me',
    license=license,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'unfman=cps2_file_manip.cli:unfman_main',
            'bswap=cps2_file_manip.cli:bswap_main'],
        }
    )
