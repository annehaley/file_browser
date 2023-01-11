from .vtk_pipeline import VtkPipeline


def initialize(server, **kwargs):
    state, ctrl = server.state, server.controller
    state.trame__title = "File Browser"
    state.attribute = "Value"

    vtk_pipeline = VtkPipeline(kwargs['dataset_path'])

    @state.change("attribute")
    def set_attribute(newValue, **kwargs):
        # vtk_pipeline.setAttribute(newValue)
        ctrl.view_update()

    @ctrl.set("get_render_window")
    def get_render_window():
        return vtk_pipeline.render_window

    # add any other engine functions
