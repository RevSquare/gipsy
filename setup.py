#! /usr/bin/env python
from distutils.core import setup
import sys
reload(sys).setdefaultencoding('Utf-8')


setup(
    name='gipsy_tools',
    version='0.0.1',
    author='Guillaume Pousseo',
    author_email='guillaumepousseo@revsquare.com',
    description='Manages common libraries to use accross the gipsy\
                 applications.',
    long_description=open('README.rst').read(),
    url='http://www.revsquare.com',
    license='BSD License',
    platforms=['OS Independent'],
    packages=['gipsy_tools'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 0.0.1 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Documentation',
    ],
    install_requires=[
        'Django>=1.4',
    ],
)
