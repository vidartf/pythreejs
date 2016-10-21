from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget

from .Vector3_autogen import Vector3

class Spline(ThreeWidget):
    """Spline
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:59:18 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Math/Spline 
    """

    def __init__(self, points=[], **kwargs):
        kwargs['points'] = points
        super(ThreeWidget, self).__init__(**kwargs)

    _view_name = Unicode('SplineView').tag(sync=True)
    _model_name = Unicode('SplineModel').tag(sync=True)

    points = Tuple().tag(sync=True, **widget_serialization)

