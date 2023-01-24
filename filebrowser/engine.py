def initialize(server, state, ctrl, vtk_pipeline, **kwargs):
    state.attribute = "Value"

    @state.change("attribute")
    def set_attribute_value(attribute, **kwargs):
        # vtk_pipeline.setAttribute(attribute)
        ctrl.view_update()

    # add any other engine functions
