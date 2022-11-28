"""
`Pyfx`'s model.

It applies and completes given JSONPath query on the current loaded JSON data.

* query directly uses :mod:`jsonpath_ng`
* auto-completion is achieved by home-made :mod:`~pyfx.model.autocomplete`
"""
from .model import Model
