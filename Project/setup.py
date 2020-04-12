#!python
# coding: utf-8

"""
Project_name setup
"""

import Project_name


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md', encoding='utf-8') as readme_md,\
        open('docs/history.md', encoding='utf-8') as history_md,\
        open('requirements.txt', encoding='utf-8') as requirements_txt:
    readme = readme_md.read()
    history = history_md.read()
    requirements = [req[:req.find('#')].rstrip() for req in requirements_txt.readlines()]

setup(
    name='Project_name',
    version=Project_name.__version__,
    description='<small description>',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    license=Project_name.__license__,
    author=Project_name.__author__,
    author_email=Project_name.__email__,
    url='<gihub_page>',
    project_urls={'Documentation': '<documentation_url>'},
    packages=['Project_name'],
    package_dir={'Project_name': 'Project_name'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='<keywords>',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        '<others>'
    ],
    test_suite='tests',
    tests_require=['<packages specifically required for testing>'],
)
