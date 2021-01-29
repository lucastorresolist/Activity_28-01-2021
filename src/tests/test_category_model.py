import sys
sys.path.append('.')
from pytest import raises
from src.models.base_model import BaseModel
from src.models.category import Category


def test_instance():
    obj = Category('Televisores', "Equipamentos maravilhos para sua casa.")

    assert isinstance(obj, BaseModel)
    assert isinstance(obj, Category)


def test_name_valid():
    name_ = 'Televisores'
    description_ = 'Equipamentos maravilhos para sua casa.'
    obj = Category(name_, description_)

    assert isinstance(obj.name, str)
    assert obj.name == name_


def test_validate_name_isNone():
    with raises(TypeError):
        Category(None, "Equipamentos maravilhos para sua casa.")


def test_validate_name_type():
    with raises(TypeError):
        Category(2, "Equipamentos maravilhos para sua casa.")


def test_validate_name_empty():
    with raises(ValueError):
        Category(' ', 'Equipamentos maravilhos para sua casa.')


def test_validate_name_length():
    with raises(ValueError):
        Category("Eletrodomésticos"*30,
                 "Equipamentos maravilhos para sua casa.")


def test_description_valid():
    name_ = 'Televisores'
    description_ = 'Equipamentos maravilhos para sua casa.'
    obj = Category(name_, description_)

    assert isinstance(obj.description, str)
    assert obj.description == description_


def test_validate_description_type():
    with raises(TypeError):
        Category("Eletrodomésticos", 30)


def test_validate_description_length():
    with raises(ValueError):
        Category("Eletrodomésticos",
                 "Equipamentos maravilhos para sua casa."*300)
