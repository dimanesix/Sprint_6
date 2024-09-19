import allure
from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage


class MainPage(BasePage):
    order_button_nav = [By.XPATH, './/button[contains(@class, "Button_Button") and text()="Заказать"]']
    order_button_middle = [By.XPATH, './/button[contains(@class, "Button_Middle")]']
    yandex_logo = [By.XPATH, './/a[contains(@class, "LogoYandex")]']
    scooter_logo = [By.XPATH, './/a[contains(@class, "LogoScooter")]']
    important_question_reg = [By.XPATH, './/div[@data-accordion-component="Accordion"]']
    question_buttons = [By.XPATH, './/div[@data-accordion-component="AccordionItemButton"]']
    answers_to_questions = [By.XPATH, './/div[@data-accordion-component="AccordionItemPanel"]']
    cookie_button = [By.ID, 'rcc-confirm-button']

    @allure.step('Принять cookie')
    def accept_cookie(self):
        if self.find_element(self.cookie_button).is_displayed():
            self.click_on_element(self.cookie_button)
            self.wait_for_element_hide(self.cookie_button)

    @allure.step('Кликнуть по кнопке "Заказать" в шапке')
    def click_on_order_button_nav(self):
        self.wait_for_load_element(self.order_button_nav)
        self.click_on_element(self.order_button_nav)

    @allure.step('Проверка точки входа с кнопки "Заказать" в шапке')
    def check_url_from_order_button_nav(self):
        self.click_on_order_button_nav()
        return self.get_current_url() == test_data.ORDER_PAGE_URL

    @allure.step('Кликнуть по кнопке "Заказать" в середине экрана')
    def click_on_order_button_middle(self):
        self.wait_for_load_element(self.order_button_middle)
        self.execute_script(test_data.SCROLL_SCRIPT, self.find_element(self.order_button_middle))
        self.click_on_element(self.order_button_middle)

    @allure.step('Проверка точки входа с кнопки "Заказать" в середине экрана')
    def check_url_from_order_button_middle(self):
        self.click_on_order_button_middle()
        return self.get_current_url() == test_data.ORDER_PAGE_URL

    @allure.step('Получить адрес редиректа Дзена')
    def get_redirect_page(self, windows):
        self.go_to_window(windows[1])
        self.wait_url_to_be(test_data.DZEN_REDIRECT_PAGE_URL)
        return self.get_current_url()

    @allure.step('Проверить редирект на страницу Дзена при клике на логотип Яндекса')
    def check_yandex_logo_redirect(self):
        self.wait_for_load_element(self.yandex_logo)
        self.click_on_element(self.yandex_logo)
        windows = self.get_windows()
        dzen_url = self.get_redirect_page(windows)
        self.go_to_window(windows[0])
        return dzen_url == test_data.DZEN_REDIRECT_PAGE_URL

    @allure.step('Проверить переход на главную страницу при клике на логотип Яндекс Самокат')
    def check_scooter_logo_url(self):
        self.wait_for_load_element(self.scooter_logo)
        self.click_on_element(self.scooter_logo)
        return self.get_current_url() == test_data.MAIN_PAGE_URL

    @allure.step('Пролистать до важного вопроса')
    def scroll_to_important_question(self, question_number):
        questions = self.find_elements(self.question_buttons)
        self.execute_script(test_data.SCROLL_SCRIPT, questions[question_number - 1])

    @allure.step('Кликнуть на вопрос')
    def click_on_important_question(self, question_number):
        questions = self.find_elements(self.question_buttons)
        questions[question_number - 1].click()

    @allure.step('Проверить, что появляется ответ')
    def check_roll_down_answer_to_the_question(self, question_number):
        return self.find_elements(self.answers_to_questions)[question_number - 1].get_attribute('hidden')

    @allure.step('Повзаимодействовать с важным вопросом')
    def interaction_with_important_question(self, question_number):
        self.wait_for_load_element(self.important_question_reg)
        self.scroll_to_important_question(question_number)
        self.click_on_important_question(question_number)
        self.check_roll_down_answer_to_the_question(question_number)
