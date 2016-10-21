from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ..._base.Three import ThreeWidget


class EdgesHelper(ThreeWidget):
    """EdgesHelper
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:59:18 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Helpers/EdgesHelper 
    """

    def __init__(self, **kwargs):
        super(ThreeWidget, self).__init__(**kwargs)

    _view_name = Unicode('EdgesHelperView').tag(sync=True)
    _model_name = Unicode('EdgesHelperModel').tag(sync=True)


