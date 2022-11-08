import re

import pytest
from transliterate import translit  # noqa skip

from ..models import Product
from ..utils import capitalize_slug, capitalize_str, get_unique_licensekey
from .factories import model_slug_test_generator


@pytest.mark.django_db
def test_get_unique_slug() -> None:
    """Test unique slug generation; conversion to ru locale"""
    test_slugs = [
        "some @ long giberish-dsfgsdfg!",
        translit("тест @ заголовок!", "ru", reversed=True),  # test-zagolovok
    ]
    for test_slug in test_slugs:
        model_slug_test_generator(Product, test_slug)


def test_capitalize_str() -> None:
    test_strings = [
        ("test title", "Test Title"),
        ("test-zagolovok", "Test-zagolovok"),
        ("тест @ заголовок!", "Тест @ Заголовок!"),
    ]
    for s, result in test_strings:
        func_res = capitalize_str(s)
        assert func_res == result


def test_capitalize_slug() -> None:
    test_slugs = [
        ("test-title", "Test Title"),
        ("test-zagolovok", "Test Zagolovok"),
        ("test-zagolovok-1", "Test Zagolovok"),
    ]
    for s, result in test_slugs:
        func_res = capitalize_slug(s)
        assert func_res == result


def test_get_unique_licensekey() -> None:
    examples = [
        [get_unique_licensekey(4), 4],
        [get_unique_licensekey(16), 16],
        [get_unique_licensekey(), 24],
    ]
    for example in examples:
        func_res, res = example
        assert len(re.match(r"^\d+$", func_res)[0]) == res
        assert isinstance(func_res, str)
