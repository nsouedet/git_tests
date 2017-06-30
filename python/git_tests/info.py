#! /usr/bin/env python

# Current version
version_major = 1
version_minor = 1
version_micro = 0
version_extra = ""

# The following variables are here for backward compatibility in order to
# ease a transition for bv_maker users. They will be removed in a few days.
_version_major = version_major
_version_minor = version_minor
_version_micro = version_micro
_version_extra = version_extra

# Expected by setup.py: string of form "X.Y.Z"
__version__ = "{0}.{1}.{2}{3}".format(
    version_major, version_minor, version_micro, version_extra)


