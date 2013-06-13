#!/bin/bash
set -ex

VERSION=$(python -c "from confluence.version import __version__ ; print __version__")
echo Preparing to release version $VERSION

#source tox
# --upgrade
pip install --user pep8 autopep8 docutils sphinx Sphinx-PyPI-upload

echo === Building documentation ===
#make html singlehtml text
if ! python setup.py build_sphinx; then
	echo "The documentation build suite failed. Fix it!"
    cd ..
	exit 1
fi

echo === Testings ===
if ! python setup.py test; then
	echo "The test suite failed. Fix it!"
	exit 1
fi

echo === Chechink that all changes are commited and pushed ===
hg pull
hg update

hg diff
# Disallow unstaged changes in the working tree
if [ -n "$(hg status -mar)" ]
then
    echo >&2 "error: your index contains uncommitted changes."
    exit 1
fi

echo "Please don't run this as a user. This generates a new release for PyPI. Press ^C to exit or Enter to continue."
read


# Clear old distutils stuff
rm -rf build dist MANIFEST &> /dev/null

# Build installers, etc. and upload to PyPI
# python setup.py register sdist bdist_wininst upload

#python setup.py register sdist build_sphinx upload upload_sphinx
python setup.py register sdist upload upload_sphinx

hg tag -f -a $VERSION -m "Version $VERSION"
hg tag -f -a RELEASE -m "Current RELEASE"

hg push origin --tags

echo "done."
