"""Version utilities that don't rely on importing shaderdef."""

import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
VERSION_PATH = os.path.join(SCRIPT_DIR, '../shaderdef/version.py')

def parse_version_string(version_string):
    """Parse dotted version string into a list of ints."""
    parts = version_string.split('.')
    return [int(part) for part in parts]


def format_version_string(version):
    """Format a list of version components."""
    return '.'.join(str(part) for part in version)


def load_version_as_string():
    """Get the current version from version.py as a string."""
    with open(VERSION_PATH, 'r') as rfile:
        contents = rfile.read().strip()

    _, version = contents.split('=')
    version = version.strip()

    # Remove quotes
    return version.strip('"\'')


def load_version_as_list():
    """Get the current version from version.py as a list of ints."""
    return parse_version_string(load_version_as_string())
