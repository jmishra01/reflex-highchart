"""Reflex custom component ReflexHighchart."""
from typing import List, Dict
from reflex.vars import BaseVar, Var
import reflex as rx



class ReflexHighchart(rx.Component):
    """ReflexHighchart component."""

    # The React library to wrap.
    library = "highcharts-react-official"

    # The React component tag.
    tag = "HighchartReact"

    is_default = True

    highcharts_: rx.Var[str] =  BaseVar.create(value="{Highchart}", _var_is_local=False, _var_is_string=False)  # type: ignore

    # options flag with default value
    options  = {"series": [{"data": [[1, 30], [2, 10], [3, 6]]}]} 

    def _get_custom_code(self) -> str | None:
        return "if ((typeof Highcharts) === 'object') { HighchartsExporting(Highcharts); } "

    def _get_dependencies_imports(self) -> Dict[str, List[rx.ImportVar]]:
        return {"highcharts@11.4.8": [rx.ImportVar(tag="Highchart", render=True, is_default=True,
                                            alias="Highchart", install=True, transpile=False)]}


reflex_highchart = ReflexHighchart.create
