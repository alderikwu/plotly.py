import _plotly_utils.basevalidators


class SelectedValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='selected', parent_name='scatterpolargl', **kwargs
    ):
        super(SelectedValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Selected',
            data_docs="""
            marker
                plotly.graph_objs.scatterpolargl.selected.Marke
                r instance or dict with compatible properties
            textfont
                plotly.graph_objs.scatterpolargl.selected.Textf
                ont instance or dict with compatible properties""",
            **kwargs
        )
