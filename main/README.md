# main

[![pipeline](https://gitlab.com/davidbreuer/main/badges/master/pipeline.svg)](https://gitlab.com/davidbreuer/main/pipelines)

[![coverage](https://gitlab.com/davidbreuer/main/badges/master/coverage.svg)](https://davidbreuer.gitlab.io/main)

## Description

This Python package is part of a repository to demonstrates various Python
packaging features in combination with GitLab continuous  integration
capabilities.

See README in parent directory for explanations of the purpose of the project.

See comments in the files of this package for details.

## Instructions

Install package development version via:

```bash
make install
```

Create documentation:

```bash
make docs
```

Run unit tests via:

```bash
make tests
```

Run all of the above steps and open in browser:

```bash
make all
```

Alternatively build self-contained docker container and open Python console:

```bash
make docker
```

## Style

Please use PEP for writing standardized and readable Python code:

https://www.python.org/dev/peps/pep-0008/

Conform to conventions for writing docstrings:

https://www.python.org/dev/peps/pep-0257/

Use code tags when helpful:

https://www.python.org/dev/peps/pep-0350/

Using appropriate versioning also for git tags:

https://www.python.org/dev/peps/pep-0440/
