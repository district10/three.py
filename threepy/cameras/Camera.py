import numpy as np
from threepy.core import *
from threepy.mathutils import MatrixFactory


class Camera(Object3D):

    def __init__(self):
        super().__init__()
        self.projectionMatrix = MatrixFactory.makeIdentity()

    def getProjectionMatrix(self):
        return self.projectionMatrix

    def getViewMatrix(self):
        return np.linalg.inv(self.transform.matrix)
