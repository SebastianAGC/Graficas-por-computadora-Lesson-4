from sr4 import *


glInit()
glCreateWindow(1000, 1000)
glViewPort(0, 0, 1000, 1000)
glClearColor(1, 1, 1)
glClear()
glColor(1, 1, 1)
glLoad("PenguinBaseMesh.obj", 700, 500, 100, 0)
glDraw()
glFinish()

