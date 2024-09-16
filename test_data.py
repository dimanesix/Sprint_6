MAIN_PAGE_URL = "https://qa-scooter.praktikum-services.ru/"
ORDER_PAGE_URL = f"{MAIN_PAGE_URL}order"
DZEN_REDIRECT_PAGE_URL = "https://dzen.ru/?yredirect=true"

BLACK_PERL = "чёрный жемчуг"
SUCCESSFUL_ORDER_MESSAGE = "Заказ оформлен"

TEST_SET_FIRST_ORDER = {"name": "Василий",
                        "surname": "Пупкин",
                        "address": "г. Москва ул. Тёплый стан д. 11",
                        "metro_station": "Тёплый Стан",
                        "telephone": "+7123456789",
                        "delivery_date": "12.09.2024",
                        "rental_period": 1,
                        "color": "",
                        "comment": ""}
TEST_SET_SECOND_ORDER = {"name": "Тамара",
                         "surname": "Васильева",
                         "address": "г. Москва ул. Ельнинская д. 1",
                         "metro_station": "Молодёжная",
                         "telephone": "+7987654321",
                         "delivery_date": "11.09.2024",
                         "rental_period": 3,
                         "color": "чёрный жемчуг",
                         "comment": "постарайтесь успеть вовремя"}
TEST_SET_THIRD_ORDER = {"name": "Денис",
                         "surname": "Беленький",
                         "address": "г. Москва ул. Ломоносовский проспект",
                         "metro_station": "Университет",
                         "telephone": "+7987654321",
                         "delivery_date": "14.09.2024",
                         "rental_period": 7,
                         "color": "чёрный жемчуг,серая безысходность",
                         "comment": ""}

SCROLL_SCRIPT = "arguments[0].scrollIntoView();"
