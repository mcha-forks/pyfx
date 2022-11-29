import json
import pathlib

from jsonpath_ng import parse
from loguru import logger

from .autocomplete import autocomplete


class Model:
    """
    Pyfx model entry point, which processes JSON data.

    Currently it manages the following actions:
     * parses JSONPath query and returns new data
     * performs auto-completion with given JSONPath query
    """

    def __init__(self, data):
        self._data = data
        self._current = data

    # noinspection PyBroadException
    def save(self, file_path):
        try:
            path = pathlib.Path(file_path)
            # Create the file if not exists
            path.touch()
            with path.open('w') as f:
                json.dump(self._current, f)
            return True
        except Exception as e:
            logger.opt(exception=True) \
                .error("Failed to save the current data into {}", file_path, e)
            return False

    def query(self, text):
        if self._data is None:
            logger.debug("Data is None.")
            return None

        result = self._query(text)
        self._current = result[0] if len(result) == 1 else result
        return self._current

    def complete(self, text):
        if self._data is None:
            logger.debug("Data is None.")
            return False, "", []
        return autocomplete(text, self.query)

    # noinspection PyBroadException
    def _query(self, text):
        try:
            jsonpath_expr = parse(text)
            return [match.value for match in jsonpath_expr.find(self._data)]
        except Exception as e:
            logger.opt(exception=True) \
                .error("JSONPath query '{}' failed with: {}", text, e)
            return []
