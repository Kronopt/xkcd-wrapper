#!python
# coding: utf-8

"""
xkcd-wrapper setup
"""

import xkcd_wrapper


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md', encoding='utf-8') as readme_md,\
        open('docs/history.md', encoding='utf-8') as history_md,\
        open('requirements.txt', encoding='utf-8') as requirements_txt:
    README = readme_md.read()
    HISTORY = history_md.read()

    REQUIREMENTS = []
    REQUIREMENTS_EXTRA = {}
    for req in requirements_txt.readlines():
        req = req[:req.find('#')].rstrip()  # remove comments
        if req.startswith("requests"):
            REQUIREMENTS_EXTRA["requests"] = req
        elif req.startswith("aiohttp"):
            REQUIREMENTS_EXTRA["aiohttp"] = req
        else:
            REQUIREMENTS.append(req)

setup(
    name='xkcd-wrapper',
    version=xkcd_wrapper.__version__,
    description='A wrapper for the xkcd API',
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type='text/markdown',
    license=xkcd_wrapper.__license__,
    author=xkcd_wrapper.__author__,
    url='https://github.com/Kronopt/xkcd-wrapper',
    project_urls={'Documentation': 'https://xkcd-wrapper.readthedocs.io/en/latest/'},
    packages=['xkcd_wrapper'],
    package_dir={'xkcd_wrapper': 'xkcd_wrapper'},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    extras_require={
        "sync":  [REQUIREMENTS_EXTRA["requests"]],
        "async": [REQUIREMENTS_EXTRA["aiohttp"]],
    },
    zip_safe=False,
    keywords='xkcd wrapper xkcd-wrapper',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
