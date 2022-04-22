"""
GUI for particle counting
"""
from magicgui import magicgui

import numpy as np


def particle_counting_dock():
    return _gui


@magicgui(threshold=dict(min=0, max=65536))
def _gui(
    viewer: "napari.viewer.Viewer",
    img_layer: "napari.layers.Image",
    threshold=65536,
    use_ROI=True,
    number_of_particles=0,
    info_box="",
):
    print(img_layer)


@_gui.img_layer.changed.connect
def on_img_layer_changed(img_layer):
    _gui.info_box.value = img_layer
    print(f"img_layer changed! New layer: {img_layer}")


@_gui.threshold.changed.connect
def on_threshold_changed(threshold):
    _gui.info_box.value = str(threshold)
    print(f"threshold changed! New threshold: {threshold}")


@_gui.called.connect
def my_callback(value: str):
    print(f"Your function was called! The result is: {value}")
