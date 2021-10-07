from setuptools import setup, find_packages
from codecs import open

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='websitesmetricscollectorbeta',
    version='1.0.2',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=["requests","confluent-kafka-producers-wrapper","aiohttp"],
    url='',
    license='',
    python_requires='>=3.6',
    author='Antonio Di Mariano',
    author_email='antonio.dimariano@gmail.com',
    description='An application that collects metrics from websites and produce results as messages to Kafka',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
