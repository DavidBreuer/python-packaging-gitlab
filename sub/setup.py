from pip._internal.req import parse_requirements
from setuptools import setup, find_packages


def load_requirements(fname):
    reqs = parse_requirements(fname, session='test')
    return [str(req.req) for req in reqs]


setup(name='sub',
      description='Package description',
      author='info <info@info.com>',
      url='http://www.info.com/',
      packages=find_packages(),
      include_package_data=True,
      python_requires='==3.*',
      install_requires=load_requirements('requirements.txt')
)
