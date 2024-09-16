import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import test_data


class OrderPage:
    first_order_form = [By.XPATH, './/div[contains(@class, "Order_Header") and text() = "Для кого самокат"]/parent::*']
    name_field = [By.XPATH, './/input[contains(@placeholder, "Имя")]']
    surname_field = [By.XPATH, './/input[contains(@placeholder, "Фамилия")]']
    address_field = [By.XPATH, './/input[contains(@placeholder, "Адрес")]']
    metro_station_button = [By.XPATH, './/button[contains(@class, "Order_SelectOption")]']
    metro_station_field = [By.XPATH, './/input[contains(@placeholder, "метро")]']
    telephone = [By.XPATH, './/input[contains(@placeholder, "Телефон")]']
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

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_first_order_form(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.first_order_form))

    def set_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    def click_on_metro_station_field(self):
        self.driver.find_element(*self.metro_station_field).click()

    def set_metro_station(self, metro_station):
        self.driver.find_element(*self.metro_station_field).send_keys(metro_station)

    def wait_for_load_metro_station_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.metro_station_button))

    def click_on_metro_station_button(self):
        self.driver.find_element(*self.metro_station_button).click()

    def select_metro_station(self, metro_station):
        self.click_on_metro_station_field()
        self.set_metro_station(metro_station)
        self.wait_for_load_metro_station_button()
        self.click_on_metro_station_button()

    def set_telephone(self, telephone):
        self.driver.find_element(*self.telephone).send_keys(telephone)

    def click_on_next_button(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step('Заполняем первую часть формы')
    def fill_first_form(self, name, surname, address, metro_station, telephone):
        self.wait_for_load_first_order_form()
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.select_metro_station(metro_station)
        self.set_telephone(telephone)

    def wait_for_load_second_order_form(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.second_order_form))

    def click_on_delivery_date_field(self):
        self.driver.find_element(*self.delivery_date_field).click()

    def set_delivery_date(self, delivery_date):
        self.driver.find_element(*self.delivery_date_field).send_keys(delivery_date)

    def click_on_delivery_date(self):
        self.driver.find_element(*self.required_day).click()

    def select_delivery_date(self, delivery_date):
        self.click_on_delivery_date_field()
        self.set_delivery_date(delivery_date)
        self.click_on_delivery_date()

    def click_on_rental_period_list_button(self):
        self.driver.find_element(*self.rental_period_list_button).click()

    def scroll_to_rental_period(self, rental_period):
        periods = self.driver.find_elements(*self.rental_period_list)
        self.driver.execute_script(test_data.SCROLL_SCRIPT, periods[rental_period - 1])

    def click_on_rental_period(self, rental_period):
        periods = self.driver.find_elements(*self.rental_period_list)
        periods[rental_period - 1].click()

    def select_rental_period(self, rental_period):
        self.click_on_rental_period_list_button()
        self.scroll_to_rental_period(rental_period)
        self.click_on_rental_period(rental_period)

    def select_color_black(self):
        self.driver.find_element(*self.color_checkbox_black).click()

    def select_color_grey(self):
        self.driver.find_element(*self.color_checkbox_grey).click()

    def select_both_color(self):
        self.select_color_black()
        self.select_color_grey()

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

    def set_comment(self, comment):
        if comment != "":
            self.driver.find_element(*self.comment_field).send_keys(comment)

    @allure.step('Заполняем вторую часть формы')
    def fill_second_form(self, delivery_date, rental_period, color, comment):
        self.wait_for_load_second_order_form()
        self.select_delivery_date(delivery_date)
        self.select_rental_period(rental_period)
        self.select_color(color)
        self.set_comment(comment)

    @allure.step('Нажимаем на кнопку сделать заказ')
    def click_on_make_order_button(self):
        self.driver.find_element(*self.make_order_button).click()

    def wait_for_load_confirm_order_window(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.confirm_order_window))

    def click_on_button_yes(self):
        self.driver.find_element(*self.yes_button).click()

    @allure.step('Подтверждаем, что хотим сделать заказ')
    def confirm_order(self):
        self.wait_for_load_confirm_order_window()
        self.click_on_button_yes()

    def wait_for_load_successful_order_window(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.successful_order_window))

    @allure.step('Проверяем появление сообщения об успешном создании заказа')
    def check_appearance_successful_order_window(self):
        self.wait_for_load_successful_order_window()
        return test_data.SUCCESSFUL_ORDER_MESSAGE in self.driver.find_element(*self.successful_order_window).text



