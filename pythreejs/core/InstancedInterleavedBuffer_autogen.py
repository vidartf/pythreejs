from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget


class InstancedInterleavedBuffer(ThreeWidget):
    """InstancedInterleavedBuffer
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:59:18 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Core/InstancedInterleavedBuffer 
    """

    def __init__(self, **kwargs):
        super(ThreeWidget, self).__init__(**kwargs)

    _view_name = Unicode('InstancedInterleavedBufferView').tag(sync=True)
    _model_name = Unicode('InstancedInterleavedBufferModel').tag(sync=True)


