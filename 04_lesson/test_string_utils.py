# test_string_utils.py
import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


class TestStringUtils:
    """Тесты для класса StringUtils."""

    # Тесты для capitalize
    @pytest.mark.positive
    @pytest.mark.parametrize("input_str,expected", [
        ("skypro", "Skypro"),  # обычная строка
        ("123", "123"),        # числа как строка
        ("04 апреля 2023", "04 апреля 2023"),  # строка с пробелами
        ("тест", "Тест"),      # кириллица
    ])
    def test_capitalize_positive(self, string_utils, input_str, expected):
        """Позитивные тесты для метода capitalize."""
        assert string_utils.capitalize(input_str) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize("input_str,expected", [
        ("", ""),              # пустая строка
        (" ", " "),            # строка с пробелом
        (None, None),          # None (должен вызывать исключение)
    ])
    def test_capitalize_negative(self, string_utils, input_str, expected):
        """Негативные тесты для метода capitalize."""
        if input_str is None:
            with pytest.raises(Exception):
                string_utils.capitalize(input_str)
        else:
            assert string_utils.capitalize(input_str) == expected

    # Тесты для trim
    @pytest.mark.positive
    @pytest.mark.parametrize("input_str,expected", [
        ("   skypro", "skypro"),
        ("04 апреля 2023  ", "04 апреля 2023  "),
        ("\t\n текст", "текст"),  # разные пробельные символы
    ])
    def test_trim_positive(self, string_utils, input_str, expected):
        """Позитивные тесты для метода trim."""
        assert string_utils.trim(input_str) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize("input_str,expected", [
        ("", ""),              # пустая строка
        (" ", ""),             # строка из одного пробела
        ("  \t\n  ", ""),      # разные пробельные символы
        (None, None),          # None
    ])
    def test_trim_negative(self, string_utils, input_str, expected):
        """Негативные тесты для метода trim."""
        if input_str is None:
            with pytest.raises(Exception):
                string_utils.trim(input_str)
        else:
            assert string_utils.trim(input_str) == expected

    # Тесты для contains
    @pytest.mark.positive
    @pytest.mark.parametrize("string,symbol,expected", [
        ("Тест", "е", True),  # кириллица
        ("123", "2", True),    # цифры
        ("04 апреля 2023", " ", True),  # пробел
    ])
    def test_contains_positive(self, string_utils, string, symbol, expected):
        """Позитивные тесты для метода contains."""
        assert string_utils.contains(string, symbol) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize("string,symbol,expected", [
        ("", "a", False),      # пустая строка
        (" ", "", True),       # поиск пустой строки
        (None, "a", False),    # None
        ("текст", None, False),  # None в symbol
    ])
    def test_contains_negative(self, string_utils, string, symbol, expected):
        """Негативные тесты для метода contains."""
        if string is None or symbol is None:
            with pytest.raises(Exception):
                string_utils.contains(string, symbol)
        else:
            assert string_utils.contains(string, symbol) == expected

    # Тесты для delete_symbol
    @pytest.mark.positive
    @pytest.mark.parametrize("string,symbol,expected", [
        ("Тест", "Т", "ест"),  # кириллица
        ("12345", "3", "1245"),  # цифры
        ("a b c d", " ", "abcd"),  # пробелы
    ])
    def test_delete_symbol_positive(
        self, string_utils, string, symbol, expected
    ):
        """Позитивные тесты для метода delete_symbol."""
        assert string_utils.delete_symbol(string, symbol) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize("string,symbol,expected", [
        ("", "a", ""),         # пустая строка
        ("текст", "", "текст"),  # пустой symbol
        (None, "a", None),     # None в string
        ("текст", None, "текст"),  # None в symbol
    ])
    def test_delete_symbol_negative(
        self, string_utils, string, symbol, expected
    ):
        """Негативные тесты для метода delete_symbol."""
        if string is None or symbol is None:
            with pytest.raises(Exception):
                string_utils.delete_symbol(string, symbol)
        else:
            assert string_utils.delete_symbol(string, symbol) == expected
