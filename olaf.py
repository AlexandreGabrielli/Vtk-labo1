import vtk
import time

# create vtk object

legs = vtk.vtkSphereSource()
legs.SetRadius(5.0)

body = vtk.vtkSphereSource()
body.SetRadius(3)
body.SetCenter(-10, 0, 0)

nose = vtk.vtkConeSource()
nose.SetHeight(2.0)
nose.SetRadius(0.5)
nose.SetResolution(10)
nose.SetCenter(10, 0, 0)
nose.SetDirection(0, -1, 0)

eyesRight = vtk.vtkSphereSource()
eyesRight.SetRadius(0.5)
eyesRight.SetCenter(-1, 8, 3)

eyesLeft = vtk.vtkSphereSource()
eyesLeft.SetRadius(0.5)
eyesLeft.SetCenter(1, 8, 3)

# Mapper

legsMapper = vtk.vtkPolyDataMapper()
legsMapper.SetInputConnection(legs.GetOutputPort())

bodyMapper = vtk.vtkPolyDataMapper()
bodyMapper.SetInputConnection(body.GetOutputPort())

noseMapper = vtk.vtkPolyDataMapper()
noseMapper.SetInputConnection(nose.GetOutputPort())

eyesRightMapper = vtk.vtkPolyDataMapper()
eyesRightMapper.SetInputConnection(eyesRight.GetOutputPort())

eyesLeftMapper = vtk.vtkPolyDataMapper()
eyesLeftMapper.SetInputConnection(eyesLeft.GetOutputPort())

#
# Create actor
#
legsActor = vtk.vtkActor()
legsActor.SetMapper(legsMapper)
legsActor.GetProperty().SetInterpolationToGouraud()

bodyActor = vtk.vtkActor()
bodyActor.SetMapper(bodyMapper)
bodyActor.GetProperty().SetInterpolationToGouraud()

noseActor = vtk.vtkActor()
noseActor.SetMapper(noseMapper)
noseActor.GetProperty().SetColor(1,0.6,0)
noseActor.GetProperty().SetInterpolationToGouraud()


eyesRightActor = vtk.vtkActor()
eyesRightActor.SetMapper(eyesRightMapper)
eyesRightActor.GetProperty().SetColor(0, 0, 0)
eyesRightActor.GetProperty().SetInterpolationToGouraud()


eyesLeftActor = vtk.vtkActor()
eyesLeftActor.SetMapper(eyesLeftMapper)
eyesLeftActor.GetProperty().SetColor(0, 0, 0)
eyesLeftActor.GetProperty().SetInterpolationToGouraud()


#
# Create the Renderer and assign actors to it.
#
ren1 = vtk.vtkRenderer()
ren1.AddActor(legsActor)
ren1.AddActor(bodyActor)
ren1.AddActor(noseActor)

ren1.SetBackground(1, 0.8, 0.6)

#  we create the render window
#
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(300, 300)

renWin.Render()

# move body to the top
for i in range(0, 90):
    time.sleep(0.03)
    bodyActor.RotateZ(-1)
    renWin.Render()

# go down body
for i in range(0, 6):
    time.sleep(0.03)
    bodyActor.AddPosition(0, -0.5, 0)
    renWin.Render()

# move nose to the front
for i in range(0, 18):
    time.sleep(0.03)
    noseActor.RotateY(-5)
    renWin.Render()

# move up and rotate the nose
x = 0
y = -1
for i in range(0, 20):
    time.sleep(0.03)
    noseActor.AddPosition(0, 0.35, 0)
    y += 0.05
    x += 0.05
    nose.SetDirection(x, y, 0)
    renWin.Render()

# move down the nose
for i in range(0, 13):
    time.sleep(0.03)
    noseActor.AddPosition(0, 0, -0.5)
    renWin.Render()

# Add eyes
ren1.AddActor(eyesRightActor)
ren1.AddActor(eyesLeftActor)
renWin.Render()

# do a barel rol
for i in range(0, 360):
    time.sleep(0.01)
    renWin.Render()
    ren1.GetActiveCamera().Roll(1)

# camera movement
for i in range(0, 360):
    time.sleep(0.01)
    renWin.Render()
    ren1.GetActiveCamera().Azimuth(1)

# camera movement
for i in range(0, 90):
    time.sleep(0.03)
    renWin.Render()
    ren1.GetActiveCamera().Elevation(1)

# camera movement
for i in range(0, 90):
    time.sleep(0.03)
    renWin.Render()
    ren1.GetActiveCamera().Elevation(-1)


time.sleep(2000)
