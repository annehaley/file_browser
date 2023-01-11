from vtk import (
    vtkXMLImageDataReader,
    vtkFixedPointVolumeRayCastMapper,
    vtkColorTransferFunction,
    vtkPiecewiseFunction,
    vtkVolumeProperty,
    vtkVolume,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)
# from vtk.util.numpy_support import vtk_to_numpy
# import numpy


class VtkPipeline:
    def __init__(self, input_image):
        self.load_file(input_image)

        color_function = vtkColorTransferFunction()
        opacity_function = vtkPiecewiseFunction()

        volume_property = vtkVolumeProperty()
        volume_property.SetColor(color_function)
        volume_property.SetScalarOpacity(opacity_function)

        actor = vtkVolume()
        actor.SetProperty(volume_property)
        actor.SetMapper(self.mapper)
        renderer = vtkRenderer()
        render_window = vtkRenderWindow()
        render_window.AddRenderer(renderer)
        render_interactor = vtkRenderWindowInteractor()
        render_interactor.SetRenderWindow(render_window)
        render_interactor.GetInteractorStyle().SetCurrentStyleToTrackballCamera()
        renderer.AddVolume(actor)
        renderer.ResetCamera()

        self.color_function = color_function
        self.opacity_function = opacity_function
        self.render_window = render_window

    def load_file(self, input_image):
        self.reader = vtkXMLImageDataReader()
        self.reader.SetFileName(input_image)
        self.reader.Update()
        mapper = vtkFixedPointVolumeRayCastMapper()
        mapper.SetInputConnection(self.reader.GetOutputPort())
        self.mapper = mapper

    def setAttribute(newValue):
        print('attribute changed to', newValue)

    #  add any other pipeline functions
