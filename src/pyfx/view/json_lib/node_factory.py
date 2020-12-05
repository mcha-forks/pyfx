from .array import array_node
from .object import object_node
from .primitive import StringNode, IntegerNode, BooleanNode, NullNode, NumericNode


class NodeFactory:
    """
    Factory to create :py:class:`pyfx.view.json_lib.json_simple_node.JSONSimpleNode`.

    Currently only supports:
    * :py:class:`pyfx.view.json_lib.primitive.primitive_node.PrimitiveNode` for (str, numeric, None)
    * :py:class:`pyfx.view.json_lib.array.array_node.ArrayNode` for list
    * :py:class:`pyfx.view.json_lib.object.object_node.ObjectNode` for dict
    """

    node_map = {
        list: array_node.ArrayNode,
        dict: object_node.ObjectNode,
        str: StringNode,
        int: IntegerNode,
        bool: BooleanNode,
        float: NumericNode,
        type(None): NullNode
    }

    @staticmethod
    def create_node(key, value, **kwargs):
        return NodeFactory.node_map[type(value)](key, value, **kwargs)
