from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ...core.Geometry_autogen import Geometry


class ExtrudeGeometry(Geometry):
    """ExtrudeGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:59:18 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/ExtrudeGeometry 
    """

    def __init__(self, **kwargs):
        super(Geometry, self).__init__(**kwargs)

    _view_name = Unicode('ExtrudeGeometryView').tag(sync=True)
    _model_name = Unicode('ExtrudeGeometryModel').tag(sync=True)


