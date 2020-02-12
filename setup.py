import io
import re
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("pybash/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)

setup(
    name="pybash",
    version=version,
    url="https://gioorgi.com/2020/pybash/",
    project_urls={
        "Documentation": "https://github.com/daitangio/pybash",
        "Code": "https://github.com/daitangio/pybash",
        "Issue tracker": "https://github.com/daitangio/pybash/issues",
    },
    license="BSD-3-Clause",
    author="Giovanni Giorgi",
    author_email="jj@gioorgi.com",
    maintainer="Giovanni Giorgi",
    maintainer_email="jj@gioorgi.com",
    description="Idempotent and *minimal* python 3 library for rapid scripting.",
    long_description=readme,
    packages=["pybash"],
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)