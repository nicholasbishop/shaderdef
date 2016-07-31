#! /usr/bin/env python

from __future__ import print_function

from subprocess import check_call
import sys

from tools.version_util import load_version_as_list, format_version_string


def run_cmd(*cmd):
    """Run a command via subprocess."""
    print(' '.join(cmd))
    check_call(cmd)


def run_tests():
    """Run the unit tests."""
    run_cmd(sys.executable, '-m', 'unittest', 'discover', '-v')


def bump_minor_version():
    """Bump the minor version in version.py."""
    version = load_version_as_list()
    print('current version: {}'.format(format_version_string(version)))
    version[-1] += 1
    print('new version: {}'.format(format_version_string(version)))

    contents = "__version__ = '{}'".format(format_version_string(version))

    # with open(VERSION_PATH, 'w') as wfile:
    #     wfile.write(contents)


def commit_setup_py():
    pass


def push_branch():
    pass


def sdist_and_upload():
    pass


def main():
    run_tests()
    bump_minor_version()
    commit_setup_py()
    push_branch()
    sdist_and_upload()


if __name__ == '__main__':
    main()
