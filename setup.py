import io
from setuptools import find_packages, setup

# Read in the README for the long description on PyPI
def long_description():
    with io.open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
    return readme


setup(
    name="simpleoptics",
    version="0.1",
    description="Simple optics tool",
    long_description=long_description(),
    url="https://github.com/GyeonghunKim/simple-optics",
    author="Gyeonghun Kim",
    author_email="gyeonghun.kim@duke.edu",
    license="",
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3"],
    zip_safe=False,
)
