from math import sin, cos, pi, sqrt
import random
from threepy.core import *
from threepy.cameras import *
from threepy.geometry import *
from threepy.material import *
import colorsys

import os
pwd = os.path.abspath(os.path.dirname(__file__))


class TestPointGeometry(Base):

    def initialize(self):

        self.setWindowTitle('Point Geometry and Materials')
        self.setWindowSize(800, 800)

        self.renderer = Renderer()
        self.renderer.setViewportSize(800, 800)
        self.renderer.setClearColor(0.25, 0.25, 0.25)

        self.scene = Scene()

        self.camera = PerspectiveCamera()
        self.cameraControls = FirstPersonController(self.input, self.camera)

        pointTexture = OpenGLUtils.initializeTexture(
            f"{pwd}/images/particle-star.png")

        gridTexture = OpenGLUtils.initializeTexture(
            f"{pwd}/images/color-grid.png")
        gridMaterial = SurfaceBasicMaterial(texture=gridTexture)
        floorMesh = Mesh(QuadGeometry(10, 10, 1, 1), gridMaterial)
        floorMesh.transform.rotateX(-3.14 / 2, Matrix.LOCAL)
        self.scene.add(floorMesh)

        vertexPositionData = []
        vertexColorData = []
        # generate random points on surface of sphere
        #  and random colors
        for i in range(5000):
            z = random.uniform(-1, 1)
            r = sqrt(1 - z**2)
            angle = random.uniform(0, 2 * pi)
            x = r * cos(angle)
            y = r * sin(angle)
            s = random.uniform(0.95, 1.05)
            point = [s * x, s * y, s * z]
            vertexPositionData.append(point)
            color = colorsys.hsv_to_rgb(i / 5000, 1, 1)
            vertexColorData.append(color)

        pointGeo = PointGeometry(vertexPositionData)
        pointGeo.setAttribute("vec3", "vertexColor", vertexColorData)
        pointMat = PointBasicMaterial(
            texture=pointTexture, size=0.1, useVertexColors=True)
        self.pointMesh = Mesh(pointGeo, pointMat)
        self.pointMesh.transform.translate(0, 1, 0)
        self.scene.add(self.pointMesh)

        self.camera.transform.setPosition(0, 2, 7)

    def update(self):

        self.cameraControls.update()

        if self.input.resize():
            size = self.input.getWindowSize()
            self.camera.setAspectRatio(size["width"] / size["height"])
            self.renderer.setViewportSize(size["width"], size["height"])

        self.pointMesh.transform.rotateY(0.005, Matrix.LOCAL)

        self.renderer.render(self.scene, self.camera)


# instantiate and run the program
TestPointGeometry().run()
