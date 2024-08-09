import pytest
from Appy import get_cat_img


def test_get_cat_img(mocker):
    # Создаем мок для метода requests.get из модуля Appy
    mock_get = mocker.patch('Appy.requests.get')

    # Устанавливаем статус-код ответа на 200 (успех)
    mock_get.return_value.status_code = 200

    # Устанавливаем возврат JSON-ответа с URL изображения кота
    mock_get.return_value.json.return_value = [{'url': 'https://cdn2.thecatapi.com/images/f2.jpg'}]

    # Вызываем тестируемую функцию
    cat_img = get_cat_img()

    # Проверяем, что функция возвращает ожидаемый URL изображения кота
    assert cat_img == 'https://cdn2.thecatapi.com/images/f2.jpg'


def test_get_cat_img_with_error(mocker):
    # Создаем мок для метода requests.get из модуля Appy
    mock_get = mocker.patch('Appy.requests.get')

    # Устанавливаем статус-код ответа на 500 (ошибка сервера)
    mock_get.return_value.status_code = 500

    # Вызываем тестируемую функцию
    cat_img = get_cat_img()

    # Проверяем, что функция возвращает None в случае ошибки
    assert cat_img == None


