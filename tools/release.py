#! /usr/bin/env python

from __future__ import print_function

import os
from subprocess import check_call
import sys

from tools.version_util import (SCRIPT_DIR, VERSION_PATH,
                                load_version_as_list,
                                format_version_string)


def run_cmd(*cmd):
    """Run a command via subprocess."""
    print(' '.join(cmd))
    check_call(cmd)


def test_and_lint():
    """Run the unit tests and pylint."""
    run_cmd('make', 'test')
    run_cmd('make', 'lint')


def bump_minor_version():
    """Bump the minor version in version.py."""
    version = load_version_as_list()
    print('current version: {}'.format(format_version_string(version)))
    version[-1] += 1
    print('new version: {}'.format(format_version_string(version)))

    contents = "__version__ = '{}'\n".format(format_version_string(version))

    with open(VERSION_PATH, 'w') as wfile:
        wfile.write(contents)


def commit_version():
    run_cmd('git', 'commit', VERSION_PATH,
            '--message', 'Bump minor version number')


def push_branch():
    run_cmd('git', 'push')


def sdist_and_upload():
    setup_py_path = os.path.join(SCRIPT_DIR, '../setup.py')
    run_cmd(sys.executable, setup_py_path, 'sdist', 'upload')


def main():
    test_and_lint()
    bump_minor_version()
    commit_version()
    push_branch()
    sdist_and_upload()


if __name__ == '__main__':
    main()
