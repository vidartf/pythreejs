from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ...core.BufferGeometry_autogen import BufferGeometry


class PlaneBufferGeometry(BufferGeometry):
    """PlaneBufferGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:59:19 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/PlaneBufferGeometry 
    """

    def __init__(self, width=10, height=10, widthSegments=1, heightSegments=1, **kwargs):
        kwargs['width'] = width
        kwargs['height'] = height
        kwargs['widthSegments'] = widthSegments
        kwargs['heightSegments'] = heightSegments
        super(BufferGeometry, self).__init__(**kwargs)

    _view_name = Unicode('PlaneBufferGeometryView').tag(sync=True)
    _model_name = Unicode('PlaneBufferGeometryModel').tag(sync=True)

    width = CFloat(10).tag(sync=True)
    height = CFloat(10).tag(sync=True)
    widthSegments = CInt(1).tag(sync=True)
    heightSegments = CInt(1).tag(sync=True)

