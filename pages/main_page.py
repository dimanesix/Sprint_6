import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import test_data


class MainPage:
    order_button_nav = [By.XPATH, './/button[contains(@class, "Button_Button") and text()="Заказать"]']
    order_button_middle = [By.XPATH, './/button[contains(@class, "Button_Middle")]']
    yandex_logo = [By.XPATH, './/a[contains(@class, "LogoYandex")]']
    scooter_logo = [By.XPATH, './/a[contains(@class, "LogoScooter")]']
    important_question_reg = [By.XPATH, './/div[@data-accordion-component="Accordion"]']
    question_buttons = [By.XPATH, './/div[@data-accordion-component="AccordionItemButton"]']
    answers_to_questions = [By.XPATH, './/div[@data-accordion-component="AccordionItemPanel"]']
    cookie_button = [By.ID, 'rcc-confirm-button']

    def __init__(self, driver):
        self.driver = driver

    def click_on_button_accept_cookie(self):
        self.driver.find_element(*self.cookie_button).click()

    def wait_for_cookie_is_accept(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.invisibility_of_element_located(self.cookie_button))

    def accept_cookie(self):
        if self.driver.find_element(*self.cookie_button).is_displayed():
            self.click_on_button_accept_cookie()
            self.wait_for_cookie_is_accept()

    def wait_for_load_order_button_nav(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.order_button_nav))

    def click_on_order_button_nav(self):
        self.driver.find_element(*self.order_button_nav).click()

    @allure.step('Проверяем точку входа с кнопки "Заказать" в шапке')
    def check_url_from_order_button_nav(self):
        self.wait_for_load_order_button_nav()
        self.click_on_order_button_nav()
        return self.driver.current_url == test_data.ORDER_PAGE_URL

    def wait_for_load_order_button_middle(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.order_button_middle))

    def scroll_to_order_button_middle(self):
        self.driver.execute_script(test_data.SCROLL_SCRIPT, self.driver.find_element(*self.question_buttons))

    def click_on_order_button_middle(self):
        self.driver.find_element(*self.order_button_middle).click()

    @allure.step('Проверяем точку входа с кнопки "Заказать" в середине экрана')
    def check_url_from_order_button_middle(self):
        self.wait_for_load_order_button_middle()
        self.scroll_to_order_button_middle()
        self.click_on_order_button_middle()
        return self.driver.current_url == test_data.ORDER_PAGE_URL

    def wait_for_load_yandex_logo(self):  # main_scooter_page, dzen_page
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.yandex_logo))

    @allure.step('Кликаем на логотип Яндекса')
    def click_on_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    def wait_for_redirect(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.current_url != test_data.DZEN_REDIRECT_PAGE_URL)

    @allure.step('Проверяем редирект на страницу Дзена')
    def check_yandex_logo_redirect(self):
        self.wait_for_load_yandex_logo()
        self.click_on_yandex_logo()
        return self.wait_for_redirect()

    def wait_for_load_scooter_logo(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.scooter_logo))

    @allure.step('Кликаем на логотип сервиса Яндекс Самокат')
    def click_on_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    @allure.step('Проверяем переход на главную страницу')
    def check_scooter_logo_url(self):
        self.wait_for_load_scooter_logo()
        self.click_on_scooter_logo()
        return self.driver.current_url == test_data.MAIN_PAGE_URL

    def wait_for_load_important_questions(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.important_question_reg))

    @allure.step('Переходим к вопросу')
    def scroll_to_important_question(self, question_number):
        questions = self.driver.find_elements(*self.question_buttons)
        self.driver.execute_script(test_data.SCROLL_SCRIPT, questions[question_number - 1])

    @allure.step('Кликаем на вопрос')
    def click_on_important_question(self, question_number):
        questions = self.driver.find_elements(*self.question_buttons)
        questions[question_number - 1].click()

    @allure.step('Проверяем, что появляется ответ')
    def check_roll_down_answer_to_the_question(self, question_number):
        return self.driver.find_elements(*self.answers_to_questions)[question_number - 1].get_attribute('hidden')

    def interaction_with_important_question(self, question_number):
        self.wait_for_load_important_questions()
        self.scroll_to_important_question(question_number)
        self.click_on_important_question(question_number)
        self.check_roll_down_answer_to_the_question(question_number)
