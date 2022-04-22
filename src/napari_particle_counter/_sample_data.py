"""
This module is an example of a barebones sample data provider for napari.

It implements the "sample data" specification.
see: https://napari.org/plugins/stable/guides.html#sample-data

Replace code below according to your needs.
"""
from __future__ import annotations
import numpy


def make_sample_data():
    """Generates an image"""
    return (
        [
            numpy.random.rand(512, 512),
            {"name": "random image 1", "contrast_limits": [0, 0.9]},
            "image",
        ],
        [
            numpy.random.rand(512, 512),
            {
                "name": "random image 2",
                "contrast_limits": [0, 1.9],
                "colormap": "viridis",
            },
            "image",
        ],
        [
            numpy.random.rand(512, 512),
            {
                "name": "random image 3",
                "contrast_limits": [0, 1.0],
                "colormap": "red",
            },
            "image",
        ],
    )
