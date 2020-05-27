from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='apple music api',
    url='https://github.com/heyannag/ETL_Project_Group_4/applemusic',
    version='1.0.3',
    packages=['applemusicpy'],
    license='LICENSE.txt',
    author='Lisa Reed Preston',
    author_email='josh@joshpreston.com',
    description='A python wrapper for the Apple Music API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests>=2.20.1',
        'pyjwt>=1.6.4',
        'cryptography>=2.4.2'
    ],
)
