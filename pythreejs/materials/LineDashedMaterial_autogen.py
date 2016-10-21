from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .Material_autogen import Material


class LineDashedMaterial(Material):
    """LineDashedMaterial
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:59:18 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Materials/LineDashedMaterial 
    """

    _view_name = Unicode('LineDashedMaterialView').tag(sync=True)
    _model_name = Unicode('LineDashedMaterialModel').tag(sync=True)

    color = Unicode("#ffffff").tag(sync=True)
    linewidth = CFloat(1).tag(sync=True)
    scale = CFloat(1).tag(sync=True)
    dashSize = CFloat(3).tag(sync=True)
    gapSize = CFloat(1).tag(sync=True)
    vertexColors = Enum(Colors, "NoColors").tag(sync=True)

