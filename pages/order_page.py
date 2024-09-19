import allure
from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage


class OrderPage(BasePage):
    first_order_form = [By.XPATH, './/div[contains(@class, "Order_Header") and text() = "Для кого самокат"]/parent::*']
    name_field = [By.XPATH, './/input[contains(@placeholder, "Имя")]']
    surname_field = [By.XPATH, './/input[contains(@placeholder, "Фамилия")]']
    address_field = [By.XPATH, './/input[contains(@placeholder, "Адрес")]']
    metro_station_button = [By.XPATH, './/button[contains(@class, "Order_SelectOption")]']
    metro_station_field = [By.XPATH, './/input[contains(@placeholder, "метро")]']
    telephone_field = [By.XPATH, './/input[contains(@placeholder, "Телефон")]']
    next_button = [By.XPATH, './/button[contains(@class, "Button_Button") and text()="Далее"]']

    second_order_form = [By.XPATH, './/div[contains(@class, "Order_Header") and text() = "Про аренду"]/parent::*']
    delivery_date_field = [By.XPATH, './/input[contains(@placeholder, "Когда привезти")]']
    rental_period_list_button = [By.XPATH, './/div[contains(text(), "Срок аренды")]/parent::*']
    rental_period_list = [By.XPATH, './/div[@class="Dropdown-option"]']
    required_day = [By.XPATH, './/div[contains(@class, "react-datepicker") and contains(@class, "day") and '
                              '@tabindex="0"]']
    color_checkbox_black = [By.XPATH, './/input[@id="black" and @type = "checkbox"]']
    color_checkbox_grey = [By.XPATH, './/input[@id="grey" and @type = "checkbox"]']
    comment_field = [By.XPATH, './/input[contains(@placeholder, "Комментарий")]']
    make_order_button = [By.XPATH, './/button[contains(@class, "Button_Middle") and text()="Заказать"]']

    confirm_order_window = [By.XPATH, './/div[contains(@class, "Order_ModalHeader")]/parent::*']
    yes_button = [By.XPATH, './/button[contains(@class, "Button_Middle") and text()="Да"]']

    successful_order_window = [By.XPATH,
                               './/div[contains(@class, "Order_ModalHeader") and text()="Заказ оформлен"]/parent::*']

    @allure.step('Выбрать станцию метро')
    def select_metro_station(self, metro_station):
        self.click_on_element(self.metro_station_field)
        self.set_data_to_element(self.metro_station_field, metro_station)
        self.wait_for_load_element(self.metro_station_button)
        self.click_on_element(self.metro_station_button)

    @allure.step('Нажать на кнопку "Далее"')
    def click_on_next_button(self):
        self.click_on_element(self.next_button)

    @allure.step('Заполнить первую часть формы')
    def fill_first_form(self, name, surname, address, metro_station, telephone):
        self.wait_for_load_element(self.first_order_form)
        self.set_data_to_element(self.name_field, name)
        self.set_data_to_element(self.surname_field, surname)
        self.set_data_to_element(self.address_field, address)
        self.select_metro_station(metro_station)
        self.set_data_to_element(self.telephone_field, telephone)

    @allure.step('Выбрать дату доставки')
    def select_delivery_date(self, delivery_date):
        self.click_on_element(self.delivery_date_field)
        self.set_data_to_element(self.delivery_date_field, delivery_date)
        self.click_on_element(self.required_day)

    @allure.step('Прокрутить список до нужного срока аренды')
    def scroll_to_rental_period(self, rental_period):
        periods = self.find_elements(self.rental_period_list)
        self.execute_script(test_data.SCROLL_SCRIPT, periods[rental_period - 1])

    @allure.step('Выбрать количество дней аренды из списка')
    def click_on_rental_period(self, rental_period):
        periods = self.find_elements(self.rental_period_list)
        periods[rental_period - 1].click()

    @allure.step('Выбрать срок аренды')
    def select_rental_period(self, rental_period):
        self.click_on_element(self.rental_period_list_button)
        self.scroll_to_rental_period(rental_period)
        self.click_on_rental_period(rental_period)

    @allure.step('Выбрать чёрный цвет')
    def select_color_black(self):
        self.click_on_element(self.color_checkbox_black)

    @allure.step('Выбрать серый цвет')
    def select_color_grey(self):
        self.click_on_element(self.color_checkbox_grey)

    @allure.step('Выбрать оба цвета')
    def select_both_color(self):
        self.select_color_black()
        self.select_color_grey()

    @allure.step('Выбрать цвет самоката, если выбран')
    def select_color(self, color):
        if color != "":
            color = color.split(',')
            if len(color) == 2:
                self.select_both_color()
            else:
                if color[0] == test_data.BLACK_PERL:
                    self.select_color_black()
                else:
                    self.select_color_grey()

    @allure.step('Указать комментарий, если указан')
    def set_comment(self, comment):
        if comment != "":
            self.set_data_to_element(self.comment_field, comment)

    @allure.step('Заполнить вторую часть формы')
    def fill_second_form(self, delivery_date, rental_period, color, comment):
        self.wait_for_load_element(self.second_order_form)
        self.select_delivery_date(delivery_date)
        self.select_rental_period(rental_period)
        self.select_color(color)
        self.set_comment(comment)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_on_make_order_button(self):
        self.click_on_element(self.make_order_button)

    @allure.step('Подтвердить, что хотим сделать заказ')
    def confirm_order(self):
        self.wait_for_load_element(self.confirm_order_window)
        self.click_on_element(self.yes_button)

    @allure.step('Проверить появление сообщения об успешном создании заказа')
    def check_appearance_successful_order_window(self):
        self.wait_for_load_element(self.successful_order_window)
        return test_data.SUCCESSFUL_ORDER_MESSAGE in self.find_element(self.successful_order_window).text



