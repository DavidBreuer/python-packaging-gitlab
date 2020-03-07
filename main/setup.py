from pip._internal.req import parse_requirements
from setuptools import setup, find_packages


# load dependencies from requirements.txt in order to leverage docker caching
def load_requirements(fname):
    reqs = parse_requirements(fname, session='test')
    return [str(req.req) for req in reqs]


# set package parameters
setup(name='main',
      description='Package description',
      author='author <info@info.com>',
      setup_requires=['setuptools_scm'],
      use_scm_version=True,
      url='http://www.info.com/',
      packages=find_packages(),
      include_package_data=True,
      scripts=['bin/run_main.py'],
      python_requires='==3.*',
      install_requires=load_requirements('requirements.txt'),
      extras_require={
            'dev': [load_requirements('requirements_dev.txt')]
      }
)
