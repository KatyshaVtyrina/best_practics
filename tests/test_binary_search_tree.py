from src.binary_search_tree import BinarySearchTree
import pytest


@pytest.fixture()
def bst():
    bst = BinarySearchTree()
    bst.insert({'id': 40})
    return bst


def test_bst_empty():
    """В пустом дереве root ссылаетcя на None"""
    bst = BinarySearchTree()
    assert bst.root is None


def test_bst_insert_root(bst):
    """При добавлении 1 узла он хранится в root"""
    assert bst.root.data == {'id': 40}


def test_bst_insert_left(bst):
    """Добавляет первый элемент слева"""
    bst.insert({'id': 30})
    assert bst.root.left.data == {'id': 30}


def test_bst_insert_right(bst):
    """Добавляет первый элемент слева"""
    bst.insert({'id': 50})
    assert bst.root.right.data == {'id': 50}
