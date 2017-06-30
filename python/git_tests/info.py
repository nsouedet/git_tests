#! /usr/bin/env python

# Current version
version_major = 1
version_minor = 1
version_micro = 6
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

# Main setup parameters
NAME = "git_tests"
ORGANISATION = "CEA"
#MAINTAINER = ""
#MAINTAINER_EMAIL = "antoine.grigis@cea.fr"
#DESCRIPTION = description
#LONG_DESCRIPTION = long_description
#URL = ""
#DOWNLOAD_URL = ""
LICENSE = "CeCILL-B"
#CLASSIFIERS = CLASSIFIERS
AUTHOR = "BrainVISA team"
AUTHOR_EMAIL = "support@brainvisa.info"
PLATFORMS = "OS Independent"
ISRELEASE = ""
VERSION = __version__

