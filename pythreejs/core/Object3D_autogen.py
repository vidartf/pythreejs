from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget


class Object3D(ThreeWidget):
    """Object3D
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:59:18 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Core/Object3D 
    """

    def __init__(self, **kwargs):
        super(ThreeWidget, self).__init__(**kwargs)

    _view_name = Unicode('Object3DView').tag(sync=True)
    _model_name = Unicode('Object3DModel').tag(sync=True)

    uuid = Unicode("").tag(sync=True)
    name = Unicode("").tag(sync=True)
    type = Unicode("").tag(sync=True)
    parent = This().tag(sync=True, **widget_serialization)
    children = Tuple().tag(sync=True, **widget_serialization)
    up = Vector3(default=[0,1,0]).tag(sync=True)
    position = Vector3(default=[0,0,0]).tag(sync=True)
    rotation = Vector3(default=[0,0,0]).tag(sync=True)
    quaternion = Vector4(default=[0,0,0,1]).tag(sync=True)
    scale = Vector3(default=[1,1,1]).tag(sync=True)
    modelViewMatrix = Matrix4(default=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1]).tag(sync=True)
    normalMatrix = Matrix3(default=[1,0,0,0,1,0,0,0,1]).tag(sync=True)
    matrix = Matrix4(default=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1]).tag(sync=True)
    matrixWorld = Matrix4(default=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1]).tag(sync=True)
    matrixAutoUpdate = Bool(True).tag(sync=True)
    matrixWorldNeedsUpdate = Bool(False).tag(sync=True)
    visible = Bool(True).tag(sync=True)
    castShadow = Bool(False).tag(sync=True)
    receiveShadow = Bool(False).tag(sync=True)
    frustumCulled = Bool(True).tag(sync=True)
    renderOrder = CInt(0).tag(sync=True)

