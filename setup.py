#!/usr/bin/env python
# Setuptools is required for the use_2to3 option below. You should install it
# from the Distribute home page, http://packages.python.org/distribute/
import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand
from pip.req import parse_requirements

package_name = 'confluence'
module_name = package_name.replace('-', '_')

base_path = os.path.dirname(__file__)

test_suite = "py.test"
if sys.hexversion >= 0x02060000:
    # requirements.extend(['nose-machineout'])
    test_suite = "py.test"

# handle python 3
if sys.version_info >= (3,):
    use_2to3 = True
else:
    use_2to3 = False

options = {}

# class PyTest(Command):
#    user_options = []
#    def initialize_options(self):
#        pass
#    def finalize_options(self):
#        pass
#    def run(self):
#        import sys,subprocess
#        errno = subprocess.call([sys.executable, 'tox'])
#        raise SystemExit(errno)


def get_metadata(*path):
    fn = os.path.join(base_path, *path)
    scope = {'__file__': fn}

    # We do an exec here to prevent importing any requirements of this package.
    # Which are imported from anything imported in the __init__ of the package
    # This still supports dynamic versioning
    with open(fn) as fo:
        code = compile(fo.read(), fn, 'exec')
        exec(code, scope)

    if 'setup_metadata' in scope:
        return scope['setup_metadata']

    raise RuntimeError('Unable to find metadata.')


def read(fname):
    return open(os.path.join(base_path, fname)).read()


def get_requirements(*path):
    req_path = os.path.join(*path)
    reqs = parse_requirements(req_path, session=False)
    return [str(ir.req) for ir in reqs]


"""
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        pytest.main(self.test_args)
"""


class Tox(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


if __name__ == '__main__':

    setup(
        name=package_name,
        packages=[package_name],
        zip_safe=False,
        tests_require=get_requirements(base_path, 'requirements-dev.txt'),
        install_requires=get_requirements(base_path, 'requirements.txt'),
        maintainer='Sorin Sbarnea',
        platforms=['any'],
        download_url='https://bitbucket.org/phoebian/confluence/downloads',
        bugtrack_url='https://bitbucket.org/phoebian/confluence/issues',
        keywords=['confluence', 'atlassian'],
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.5',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Development Status :: 4 - Beta',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Internet',
        ],
        long_description=open('README.md').read(),
        test_suite=test_suite,
        cmdclass={'test': Tox},
        **get_metadata(base_path, module_name, 'package_meta.py'),
        **options
    )
