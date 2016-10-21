from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ...core.BufferGeometry_autogen import BufferGeometry


class RingBufferGeometry(BufferGeometry):
    """RingBufferGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:59:19 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/RingBufferGeometry 
    """

    def __init__(self, innerRadius=0, outerRadius=50, thetaSegments=8, phiSegments=8, thetaStart=0, thetaLength=6.283185307179586, **kwargs):
        kwargs['innerRadius'] = innerRadius
        kwargs['outerRadius'] = outerRadius
        kwargs['thetaSegments'] = thetaSegments
        kwargs['phiSegments'] = phiSegments
        kwargs['thetaStart'] = thetaStart
        kwargs['thetaLength'] = thetaLength
        super(BufferGeometry, self).__init__(**kwargs)

    _view_name = Unicode('RingBufferGeometryView').tag(sync=True)
    _model_name = Unicode('RingBufferGeometryModel').tag(sync=True)

    innerRadius = CFloat(0).tag(sync=True)
    outerRadius = CFloat(50).tag(sync=True)
    thetaSegments = CInt(8).tag(sync=True)
    phiSegments = CInt(8).tag(sync=True)
    thetaStart = CFloat(0).tag(sync=True)
    thetaLength = CFloat(6.283185307179586).tag(sync=True)

