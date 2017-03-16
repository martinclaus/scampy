"""SCAMPY - SCAlable ocean Model written in PYthon.

SCAMPY is an ocean model written in Python that is designed to run on
platforms ranging from consumer laptops to large computing clusters. The idea
of using python is to have fast development cycles while accepting possible
performance issues. However, most of the number crunching will be performed via
numpy (http://www.numpy.org) and distributed computing will be managed via the
global arrays toolkit (http://hpc.pnl.gov/globalarrays/) if available. This
will ensure that most things which are critical for performance are done
natively in C/C++ with as little overhead as possible.
"""

__VERSION_MAJOR__ = 0
__VERSION_MINOR__ = 0
__VERSION_MAINT__ = 1

def get_version():
    return (__VERSION_MAJOR__, __VERSION_MINOR__, __VERSION_MAINT__)

def get_version_string():
    return "{}.{}.{}".format(*get_version())

__version__ = get_version()
