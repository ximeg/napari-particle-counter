"""
This module is an example of a barebones sample data provider for napari.

It implements the "sample data" specification.
see: https://napari.org/plugins/stable/guides.html#sample-data

Replace code below according to your needs.
"""
from __future__ import annotations
from skimage.io import imread
import importlib.resources as importlib_resources
import numpy

_data_dir = importlib_resources.files("napari_particle_counter") / "data"


def load_sample_data_1():
    """Loads a sample dataset"""
    return (
        [
            imread(_data_dir / "dataset_1_ERASE_switch.tif"),
            {"name": "Dataset 1", "contrast_limits": [500, 3000]},
            "image",
        ],
    )
