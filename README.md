# python-packaging-gitlab

## Description

Demonstrate Python packaging features in combination
with GitLab continuous integration capabilities:

- packaging
  - non-redundant package dependencies in setup.py and requirements.txt
  - Git-based versioning via setuptools-scm
  - inclusion of executable script
  - Makefile to install/test/document package
- documentation
  - sphinx to create package documentation
  - sphinx-gallery to create gallery examples
- testing
  - pytest for unit testing
  - testing of docstings doctest
  - fixture, mocking, image output comparison
  - coverage reports via pytest-cov
- GitLab
  - run continuous integration
  - use GitLab container registry to exploit Docker caching
  - install private GitLab Python repository using Deploy Tokens
  - deploy documentation as GitLab Pages
  - include pipeline and coverage badges

## Links

Many links are given directly in the comments in the Python packages.
Two general sources on Python packaging that were very helpful are:

- https://www.pypa.io/en/latest/

- https://python-packaging.readthedocs.io/en/latest/about.html
