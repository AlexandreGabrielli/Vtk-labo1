import vtk
import time

#
# Next we create vtk object
#
legs = vtk.vtkSphereSource()
legs.SetRadius(5.0)

body = vtk.vtkSphereSource()
body.SetRadius(2.5)
body.SetCenter(-10, 0, 0)

nose = vtk.vtkConeSource()
nose.SetHeight(2.0)
nose.SetRadius(0.5)
nose.SetResolution(10)
nose.SetCenter(10, 0, 0)
nose.SetDirection(0, -1, 0)

eyesRight = vtk.vtkSphereSource()
eyesRight.SetRadius(0.2)
eyesRight.SetCenter(-1, 6, 10)

eyesLeft = vtk.vtkSphereSource()
eyesLeft.SetRadius(0.2)
eyesLeft.SetCenter(1, 6, 10)

# In this example we terminate the pipeline with a mapper process object.
# (Intermediate filters such as vtkShrinkPolyData could be inserted in
# between the source and the mapper.)  We create an instance of
# vtkPolyDataMapper to map the polygonal data into graphics primitives. We
# connect the output of the cone souece to the input of this mapper.
#
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

bodyActor = vtk.vtkActor()
bodyActor.SetMapper(bodyMapper)

noseActor = vtk.vtkActor()
noseActor.SetMapper(noseMapper)

eyesRightActor = vtk.vtkActor()
eyesRightActor.SetMapper(eyesRightMapper)
eyesRightActor.GetProperty().SetColor(0, 0, 0)

eyesLeftActor = vtk.vtkActor()
eyesLeftActor.SetMapper(eyesLeftMapper)
eyesLeftActor.GetProperty().SetColor(0, 0, 0)

#
# Create the Renderer and assign actors to it.
#
ren1 = vtk.vtkRenderer()
ren1.AddActor(legsActor)
ren1.AddActor(bodyActor)
ren1.AddActor(noseActor)

ren1.SetBackground(0.1, 0.2, 0.4)

# Finally we create the render window which will show up on the screen
# We put our renderer into the render window using AddRenderer. We also
# set the size to be 300 pixels by 300
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
    print("body")

# go down body
for i in range(0, 6):
    time.sleep(0.03)
    bodyActor.AddPosition(0, -0.5, 0)
    renWin.Render()
    print("body")

# move nose to the front
for i in range(0, 18):
    time.sleep(0.03)
    noseActor.RotateY(-5)
    renWin.Render()
    print("nose")

# move up and rotate the nose
x = 0
y = -1
for i in range(0, 10):
    time.sleep(0.03)
    noseActor.AddPosition(0, 0.5, 0)
    y += 0.1
    x -= 0.1
    nose.SetDirection(x, y, 0)
    renWin.Render()
    print("nose rotation")

# move down the nose
for i in range(0, 15):
    time.sleep(0.03)
    noseActor.AddPosition(0, 0, -0.5)
    renWin.Render()
    print("nose")

# Add eyes
print("ADD EYES")
ren1.AddActor(eyesRightActor)
ren1.AddActor(eyesLeftActor)
renWin.Render()

# do a barel rol
for i in range(0, 360):
    print("degrée :" + str(i))
    time.sleep(0.03)
    renWin.Render()
    ren1.GetActiveCamera().Roll(1)
    print("should have move one")

# camera movement
for i in range(0, 9):
    time.sleep(0.03)
    renWin.Render()
    ren1.GetActiveCamera().Azimuth(10)
    print("camera")

print("FIN")