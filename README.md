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

## Instructions

1. Download or fork and clone this repository
2. Create new GitLab project for 'sub' Python package
3. Generate Deploy Token for 'sub'
  - Settings -> CI/CD -> Deploy Tokens -> create and store user and token
4. Push 'sub' package to GitLab project
5. Set tag to be used during installation of 'main' package
  - Repository -> Tags -> New tag -> v0.0.2 or similar
6. Create new GitLab project for 'main' Python package
7. Adjust GitLab address and tag of 'sub' package in main/requirements.txt
8. Set Deploy Token as environment variables for CI
  - Settings -> CI/CD -> Variables -> define SUB_USER and SUB_TOKEN, enable 'masked' option
9. Enable test coverage parsing
  - Settings -> CI/CD -> General Pipelines -> Test coverage parsing -> '^TOTAL.+?(\d+\%)$' as shown for pytest-cov below
10. Enable 'GitLab Pages' for 'main'
  - Settings -> General -> Visibility... -> enable Pages and select who can view them
11. Push 'main' package to GitLab project to trigger CI pipeline which will:
  - build package in a Docker container (with its 'sub' dependency) or load cached parts from GitLab registry
  - push Docker image to GitLab registry
  - run unit tests and compute test coverage
  - publish documentation and coverage report as GitLab Pages
  - clean up
12. Please feel free to create pull requests if there are any:
  - issues
  - ideas for extensions/improvements
  - questions
13. Have fun!

## Links

Many links are given directly in the comments in the Python packages.
Two general sources on Python packaging that were very helpful are:

- https://www.pypa.io/en/latest/

- https://python-packaging.readthedocs.io/en/latest/about.html
