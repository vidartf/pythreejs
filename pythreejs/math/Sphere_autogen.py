from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget


class Sphere(ThreeWidget):
    """Sphere
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:59:18 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Math/Sphere 
    """

    def __init__(self, center=[0,0,0], radius=0, **kwargs):
        kwargs['center'] = center
        kwargs['radius'] = radius
        super(ThreeWidget, self).__init__(**kwargs)

    _view_name = Unicode('SphereView').tag(sync=True)
    _model_name = Unicode('SphereModel').tag(sync=True)

    center = Vector3(default=[0,0,0]).tag(sync=True)
    radius = CFloat(0).tag(sync=True)

