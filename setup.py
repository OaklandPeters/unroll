from setuptools import setup

setup(
    name='unroll',
    version=open('VERSION').read().strip(),
    author='Oakland John Peters',
    author_email='oakland.peters@gmail.com',

    description='Tool for multi-line and advanced list/dict/generator comprehensions.',
    long_description=open('README.rst').read(),
    url='http://bitbucket.org/OPeters/unroll',
    license='MIT',
    packages=['unroll'],

    classifiers=[
        'Development Status :: 3 - Alpha'
        #'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
