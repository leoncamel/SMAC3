import setuptools


setuptools.setup(
    name="smac",
    version="0.0.1dev",
    author="Marius Lindauer, Matthias Feurer, Katharina Eggensperger, Aaron Klein, Stefan Falkner and Frank Hutter",
    author_email="fh@cs.uni-freiburg.de",
    description=("SMAC3, a python implementation of 'Sequential Model-based "
                 "Algorithm Configuration'."),
    license="BSD",
    keywords="machine learning algorithm configuration hyperparameter "
             "optimization tuning",
    url="",
    packages=setuptools.find_packages(exclude=['test']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    platforms=['Linux'],
    install_requires=['setuptools',
                      'numpy>=0.16.2',
                      'scipy>=0.9.0',
                      'pysmac'],
    test_suite = 'nose.collector'
)