import sys
sys.path.append('.')
from src.models.category import Category


def test_validate_name_isNone():
    try:
        Category(None, "Equipamentos maravilhos para sua casa.")
    except Exception as e:
        assert isinstance(e, TypeError)


def test_validate_name_type():
    try:
        Category(2, "Equipamentos maravilhos para sua casa.")
    except Exception as e:
        assert isinstance(e, TypeError)


def test_validate_name_empty():
    try:
        Category(' ', 'Equipamentos maravilhos para sua casa.')
    except Exception as e:
        assert isinstance(e, ValueError)


def test_validate_name_length():
    try:
        Category("Eletrodomésticos"*30, "Equipamentos maravilhos para sua casa.")
    except Exception as e:
        assert isinstance(e, ValueError)


def test_validate_description_type():
    try:
        Category("Eletrodomésticos", 30)
    except Exception as e:
        assert isinstance(e, TypeError)


def test_validate_description_length():
    try:
        Category("Eletrodomésticos", "Equipamentos maravilhos para sua casa."*300)
    except Exception as e:
        assert isinstance(e, ValueError)