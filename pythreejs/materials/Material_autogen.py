from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget

from ..math.Plane_autogen import Plane

class Material(ThreeWidget):
    """Material
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:59:18 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Materials/Material 
    """

    def __init__(self, **kwargs):
        super(ThreeWidget, self).__init__(**kwargs)

    _view_name = Unicode('MaterialView').tag(sync=True)
    _model_name = Unicode('MaterialModel').tag(sync=True)

    uuid = Unicode("").tag(sync=True)
    name = Unicode("").tag(sync=True)
    opacity = CFloat(1).tag(sync=True)
    transparent = Bool(False).tag(sync=True)
    blending = Enum(BlendingMode, "NormalBlending").tag(sync=True)
    blendSrc = Enum(BlendFactors, "SrcAlphaFactor").tag(sync=True)
    blendDst = Enum(BlendFactors, "OneMinusSrcAlphaFactor").tag(sync=True)
    blendEquation = Enum(Equations, "AddEquation").tag(sync=True)
    depthTest = Bool(True).tag(sync=True)
    depthFunc = Enum(DepthMode, "LessEqualDepth").tag(sync=True)
    depthWrite = Bool(True).tag(sync=True)
    polygonOffset = Bool(False).tag(sync=True)
    polygonOffsetFactor = CFloat(0).tag(sync=True)
    polygonOffsetUnits = CFloat(0).tag(sync=True)
    alphaTest = CFloat(0).tag(sync=True)
    clippingPlanes = Tuple().tag(sync=True, **widget_serialization)
    clipShadows = Bool(False).tag(sync=True)
    overdraw = CFloat(0).tag(sync=True)
    visible = Bool(True).tag(sync=True)
    side = Enum(Side, "FrontSide").tag(sync=True)
    fog = Bool(True).tag(sync=True)
    lights = Bool(True).tag(sync=True)

