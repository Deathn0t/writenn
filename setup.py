from setuptools import setup, find_packages

# Package meta-data.
NAME = "writenn"
DESCRIPTION = "Generate code from handwritten neural networks"
URL = "https://github.com/Deathn0t/writenn"
EMAIL = "romain.egele@polytechnique.edu, andrei.plekhanov@polytechnique.edu"
AUTHOR = "Romain Egele, Andrei Plekhanov"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = None

# What packages are required for this module to be executed?
REQUIRED = [
    "numpy",
    "scikit-learn",
    "tqdm",
    "tensorflow==2.0.0",
    "keras",
    "networkx",
    "pydot",
    "Pillow",
    "h5py",
]


setup(
    name=NAME,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    # If your package is a single module, use this instead of 'packages':
    install_requires=REQUIRED,
    include_package_data=True,
    license="BSD-2",
    classifiers=[
        # Trove classifiers
        # https://pypi.org/classifiers/
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)

