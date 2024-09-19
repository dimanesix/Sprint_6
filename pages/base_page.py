import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_page(self, page_url: str):
        self.driver.get(page_url)

    @allure.step('Перейти в окно')
    def go_to_window(self, window):
        self.driver.switch_to.window(window)

    @allure.step('Получить список открытых окон')
    def get_windows(self):
        return self.driver.window_handles

    @allure.step('Найти элемент')
    def find_element(self, page_object: list[str, str]):
        return self.driver.find_element(*page_object)

    @allure.step('Найти элементы')
    def find_elements(self, page_object: list[str, str]):
        return self.driver.find_elements(*page_object)

    @allure.step('Выполнить скрипт')
    def execute_script(self, script: str, args):
        self.driver.execute_script(script, args)

    @allure.step('Вернуться на предыдущую страницу')
    def go_back(self):
        self.driver.back()

    @allure.step('Получить URL активной страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Дождаться появления элемента')
    def wait_for_load_element(self, page_object: list[str, str]):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(page_object))

    @allure.step('Дождаться когда элемент пропадёт')
    def wait_for_element_hide(self, page_object: list[str, str]):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.invisibility_of_element_located(page_object))

    @allure.step('Дождаться, когда появится страница')
    def wait_url_to_be(self, page_url: str):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be(page_url))

    @allure.step('Кликнуть по элементу')
    def click_on_element(self, page_object: list[str, str]):
        self.driver.find_element(*page_object).click()

    @allure.step('Заполнить элемент данными')
    def set_data_to_element(self, page_object: list[str, str], data: str):
        self.driver.find_element(*page_object).send_keys(data)

    @allure.step('Удалить все cookie')
    def delete_all_cookie(self):
        self.driver.delete_all_cookies()
