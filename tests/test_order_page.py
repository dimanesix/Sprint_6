import pytest
from selenium import webdriver
import test_data
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestScooterOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_order_entry_points_equality(self):
        self.driver.get(test_data.MAIN_PAGE_URL)
        main_page = MainPage(self.driver)
        main_page.accept_cookie()
        first_entry_point = main_page.check_url_from_order_button_nav()
        self.driver.back()
        second_entry_point = main_page.check_url_from_order_button_middle()
        assert first_entry_point == second_entry_point, 'Точки входа не совпадают!'
        self.driver.delete_all_cookies()

    @pytest.mark.parametrize('test_set', [test_data.TEST_SET_FIRST_ORDER, test_data.TEST_SET_SECOND_ORDER,
                                          test_data.TEST_SET_THIRD_ORDER])
    def test_successful_scooter_order(self, test_set):
        self.driver.get(test_data.MAIN_PAGE_URL)
        main_page = MainPage(self.driver)
        main_page.accept_cookie()
        main_page.click_on_order_button_nav()
        order_page = OrderPage(self.driver)
        order_page.fill_first_form(test_set["name"],
                                   test_set["surname"],
                                   test_set["address"],
                                   test_set["metro_station"],
                                   test_set["telephone"])
        order_page.click_on_next_button()
        order_page.fill_second_form(test_set["delivery_date"],
                                    test_set["rental_period"],
                                    test_set["color"],
                                    test_set["comment"])
        order_page.click_on_make_order_button()
        order_page.confirm_order()
        order_page.wait_for_load_successful_order_window()
        is_appeared = order_page.check_appearance_successful_order_window()
        assert is_appeared == True, 'Окно об успешном создании заказа не появляется!'
        self.driver.back()
        is_main_page = main_page.check_scooter_logo_url()  # до этого все работает!
        assert is_main_page == True, 'Клик по логотипу сервиса не ведёт на главную страницу!'
        is_dzen_redirect = main_page.check_yandex_logo_redirect()
        assert is_dzen_redirect == True, 'По клику на логотип Яндекса не происходит редиректа на станицу Дзена!'
        self.driver.delete_all_cookies()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
