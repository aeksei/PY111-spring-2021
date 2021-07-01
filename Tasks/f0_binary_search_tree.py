"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple


# import networkx as nx


def create_node(key, value):
    return {
        'key': key,
        'value': value,
        'left': {},  # None
        'right': {}
    }


# дерево бинарного поиска
tree = {}


def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    global tree

    def recursion_insert(current_node: dict):
        if key > current_node["key"]:  # идем в правое поддерево
            if not current_node["right"]:  # дошли до листа
                current_node["right"] = create_node(key, value)
            else:
                recursion_insert(current_node["right"])
        elif key < current_node["key"]:  # идем в левое поддерево
            if not current_node["left"]:  # дошли до листа
                current_node["left"] = create_node(key, value)
            else:
                recursion_insert(current_node["left"])
        elif key == current_node["key"]:
            current_node["value"] = value

    if not tree:
        tree = create_node(key, value)
    else:
        recursion_insert(tree)


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    print(key)
    return None


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    def recursion_find(current_node):
        if key > current_node["key"]:  # идем в правое поддерево
            if not current_node["right"]:  # дошли до листа
                raise KeyError
            else:
                return recursion_find(current_node["right"])
        elif key < current_node["key"]:  # идем в левое поддерево
            if not current_node["left"]:  # дошли до листа
                raise KeyError
            else:
                return recursion_find(current_node["left"])
        elif key == current_node["key"]:
            return current_node["value"]

    if not tree:
        raise KeyError
    else:
        return recursion_find(tree)


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    global tree
    tree = {}  # tree.clear()
