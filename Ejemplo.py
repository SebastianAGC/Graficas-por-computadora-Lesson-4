from sr4 import *


glInit()
glCreateWindow(1000, 1000)
glViewPort(0, 0, 1000, 1000)
glClearColor(1, 1, 1)
glClear()
glColor(1, 1, 1)
glLoad("model.obj", 500, 500, 500, 0)
glDraw()
glFinish()

