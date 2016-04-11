__all__ = ['__version__']

def test():
    print "ok"

# Load the Clinica package version
import pkgutil
__version__ = pkgutil.get_data(__package__, 'VERSION').decode('ascii').strip()
version = __version__

# import pkg_resources
# version = pkg_resources.require("Clinica")[0].version
# __version__ = version

# python 2.7 minimum version is required
import sys
if sys.version_info < (2, 7):
    print("clinica %s requires Python 2.7" % __version__)
    sys.exit(1)