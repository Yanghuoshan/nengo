"""Nengo version information.

We use semantic versioning (see http://semver.org/).
and conform to PEP440 (see https://www.python.org/dev/peps/pep-0440/).
'.devN' will be added to the version unless the code base represents
a release version. Release versions are git tagged with the version.
"""

# pylint: disable=consider-using-f-string

name = "nengo"
version_info = (3, 2, 0)  # (major, minor, patch)
dev = 0

# use old string formatting, so that this can still run in Python <= 3.5
version = "{v}{dev}".format(
    v=".".join(str(v) for v in version_info),
    dev=(".dev%d" % dev) if dev is not None else "",
)
