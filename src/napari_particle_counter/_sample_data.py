"""
This module is an example of a barebones sample data provider for napari.

It implements the "sample data" specification.
see: https://napari.org/plugins/stable/guides.html#sample-data

Replace code below according to your needs.
"""
from __future__ import annotations
import numpy


def load_sample_data_1():
    """Generates an image"""
    return (
        [
            numpy.random.rand(512, 512),
            {"name": "Dataset 1", "contrast_limits": [0, 0.9]},
            "image",
        ],
    )


def load_sample_data_2():
    """Generates an image"""
    return (
        [
            numpy.random.rand(512, 512),
            {
                "name": "Dataset 2",
                "contrast_limits": [0, 1.9],
                "colormap": "viridis",
            },
            "image",
        ],
    )
