from threepy.core import *
from threepy.cameras import *
from threepy.geometry import *
from threepy.material import *
from threepy.lights import *
from threepy.helpers import *

import os
pwd = os.path.abspath(os.path.dirname(__file__))


class TestDirectionalLight(Base):

    def initialize(self):

        self.setWindowTitle('Directional Light')
        self.setWindowSize(800, 800)

        self.renderer = Renderer()
        self.renderer.setViewportSize(800, 800)
        self.renderer.setClearColor(0.25, 0.25, 0.25)

        self.scene = Scene()

        self.camera = PerspectiveCamera()
        self.camera.transform.setPosition(0, 1, 7)
        self.camera.transform.lookAt(0, 0, 0)
        self.cameraControls = FirstPersonController(self.input, self.camera)

        ambientLight = AmbientLight(color=[0.1, 0.1, 0.2])
        self.scene.add(ambientLight)

        directionalLight = DirectionalLight(
            position=[4, 4, -2], direction=[-1, -1, -1])
        self.scene.add(directionalLight)
        self.scene.add(DirectionalLightHelper(directionalLight))

        gridTexture = OpenGLUtils.initializeTexture(
            f"{pwd}/images/color-grid.png")
        lightMaterial = SurfaceLightMaterial(
            color=[1, 1, 1], texture=gridTexture)

        self.cube = Mesh(BoxGeometry(), lightMaterial)
        self.cube.transform.translate(1.5, 0, 0, Matrix.LOCAL)
        self.scene.add(self.cube)

        self.sphere = Mesh(SphereGeometry(), lightMaterial)
        self.sphere.transform.translate(-1.5, 0, 0, Matrix.LOCAL)
        self.scene.add(self.sphere)

    def update(self):

        self.cameraControls.update()

        if self.input.resize():
            size = self.input.getWindowSize()
            self.camera.setAspectRatio(size["width"] / size["height"])
            self.renderer.setViewportSize(size["width"], size["height"])

        self.cube.transform.rotateX(0.02, Matrix.LOCAL)
        self.cube.transform.rotateY(0.03, Matrix.LOCAL)

        self.sphere.transform.rotateY(0.025, Matrix.LOCAL)

        self.renderer.render(self.scene, self.camera)


# instantiate and run the program
TestDirectionalLight().run()
