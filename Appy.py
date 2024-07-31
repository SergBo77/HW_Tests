import requests

def get_cat_img():
    url = 'https://api.thecatapi.com/v1/images/search'  # Используем API для получения изображения
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # Получаем JSON-ответ
        return data[0]['url']  # Возвращаем URL первого изображения
    else:
        return None

