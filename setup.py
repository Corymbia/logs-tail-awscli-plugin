#!/usr/bin/env python
import sys
from os import path
from setuptools import setup

requires = ['awscli>=1.14.0',
            'botocore>=1.8.35',
            'colorama>=0.3.2',
            'python-dateutil>=1.4']

project_dir = path.abspath(path.dirname(__file__))
with open(path.join(project_dir, 'VERSION'), 'rb') as version:
    version = version.read().decode('UTF-8').strip()
with open(path.join(project_dir, 'README.md'), 'rb') as readme:
    long_description = readme.read().decode('UTF-8')

setup(
    name='awscli-plugin-logs-tail',
    packages=['awscli_plugin_logs_tail'],
    version=version,
    description='CloudWatch Logs tail command plugin for AWS CLI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Steve Jones',
    author_email='steve@iaascream.cloud',
    url='https://github.com/corymbia/logs-tail-awscli-plugin',
    keywords=['awscli', 'cloudwatch'],
    install_requires=requires,
    license='BSD (Simplified)',
    classifiers=['Development Status :: 4 - Beta',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Internet']
)


