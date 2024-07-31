import pytest
from Appy import get_cat_img

def test_get_cat_img(mocker):
    mock_get = mocker.patch('Appy.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{'url': 'https://cdn2.thecatapi.com/images/f2.jpg'}]

    cat_img = get_cat_img()
    assert cat_img == 'https://cdn2.thecatapi.com/images/f2.jpg'

def test_get_cat_img_with_error(mocker):
    mock_get = mocker.patch('Appy.requests.get')
    mock_get.return_value.status_code = 500

    cat_img = get_cat_img()
    assert cat_img == None


