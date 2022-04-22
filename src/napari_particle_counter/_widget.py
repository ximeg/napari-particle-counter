"""
GUI for particle counting
"""
from magicgui import magicgui

import numpy as np


def particle_counting_dock():
    return _gui


@magicgui(
    threshold=dict(widget_type="Slider", min=0, max=65536, readout=False),
    number_of_particles=dict(widget_type="Label"),
    plot=dict(widget_type="PushButton"),
    call_button=False,
)
def _gui(
    viewer: "napari.viewer.Viewer",
    img_layer: "napari.layers.Image",
    threshold=65536,
    use_ROI=True,
    number_of_particles="<h3>5125</h3>",
    info_box="",
    plot=True,
):
    ...


@_gui.img_layer.changed.connect
def on_img_layer_changed(img_layer):
    if img_layer:
        _min, _max = img_layer.contrast_limits
        _gui.threshold.min = _min
        _gui.threshold.max = _max

        _gui.threshold.value = auto_threshold(img_layer.data)


def auto_threshold(image_data, nsd=8):
    v = _gui.viewer.value
    # get a single image from the 3D stack
    if v.dims.ndim == 3:
        frame_id = v.dims.current_step[0]
        frame = image_data[frame_id]
    elif v.dims.ndim > 3:
        raise NotImplemented("Only 2D or 3D images are supported.")
    else:
        frame = image_data

    print("Shape of the frame: ", frame.shape)
    return frame.mean() + nsd * frame.std()


def get_current_frame():
    v = _gui.viewer.value
    if v.dims.ndim == 2:
        return _gui.img_layer.value.data
    if v.dims.ndim == 3:
        return _gui.img_layer.value.data[v.dims.current_step[0]]


def update_mask_layer():
    """Create a preview mask."""
    img_layer = _gui.img_layer.value
    if img_layer:

        mask = get_current_frame() > _gui.threshold.value

        v = _gui.viewer.value
        if "mask" in v.layers:
            v.layers["mask"].data = mask
            # rearrange, making sure the mask is on top
            v.layers.append(v.layers.pop("mask"))
            count_particles(mask)
        else:
            v.add_image(mask, colormap="bop purple", opacity=0.5)
            v.dims.events.connect(update_mask_layer)


def count_particles(mask):
    _gui.number_of_particles.value = f"<h3>{mask.sum()}</h3>"


@_gui.threshold.changed.connect
def on_threshold_changed(threshold):
    update_mask_layer()


@_gui.called.connect
def my_callback(value: str):
    print(f"Your function was called! The result is: {value}")


@_gui.plot.clicked.connect
def on_plot_clicked():
    raise NotImplemented("Result plotting is not implemented yet")


### Known bugs
# * everything falls apart when a layer gets deleted, because the signals and slots are still connected
#
#
#
#
