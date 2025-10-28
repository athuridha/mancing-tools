"""Version information for auto-update system."""

__version__ = "2.0.0"
VERSION_INFO = {
    "major": 2,
    "minor": 0,
    "patch": 0,
}

def get_version() -> str:
    """Returns current version string."""
    return __version__

def get_version_tuple() -> tuple:
    """Returns version as tuple (major, minor, patch)."""
    return (VERSION_INFO["major"], VERSION_INFO["minor"], VERSION_INFO["patch"])
