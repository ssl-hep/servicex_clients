# setuptools loads some plugins necessary for use here.
from setuptools import find_packages  # noqa: F401
from distutils.core import setup
import os

# Use the readme as the long description.
with open("README.md", "r") as fh:
    long_description = fh.read()

version = os.getenv('servicex_clients_version')
if version is None:
    version = '0.1a1'
else:
    version = version.split('/')[-1]

setup(name="servicex_clients",
      version=version,
      packages=[],
      scripts=[],
      description="Install ServiceX Common Clients",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="G. Watts (IRIS-HEP/UW Seattle)",
      author_email="gwatts@uw.edu",
      maintainer="Gordon Watts (IRIS-HEP/UW Seattle)",
      maintainer_email="gwatts@uw.edu",
      url="https://github.com/ssl-hep/servicex_clients",
      license="TBD",
      install_requires=[
          "func_adl_servicex==1.1.3",
          "tcut-to-qastle==0.5",
      ],
      classifiers=[
          # "Development Status :: 3 - Alpha",
          "Development Status :: 4 - Beta",
          # "Development Status :: 5 - Production/Stable",
          # "Development Status :: 6 - Mature",
          "Intended Audience :: Developers",
          "Intended Audience :: Information Technology",
          "Programming Language :: Python",
          "Topic :: Software Development",
          "Topic :: Utilities",
      ],
      platforms="Any",
      )
