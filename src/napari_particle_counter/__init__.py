try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"


from ._sample_data import *
from ._widget import ExampleQWidget, example_magic_widget
