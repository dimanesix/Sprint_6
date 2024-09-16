import pytest
from selenium import webdriver
import test_data
from pages.main_page import MainPage


class TestImportantQuestionArea:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @pytest.mark.parametrize('question', ['1 question', '2 question', '3 question', '4 question', '5 question', '6 question', '7 question', '8 question'])
    def test_appearance_answer(self, question):
        question_number = int(question.split(' ')[0])
        self.driver.get(test_data.MAIN_PAGE_URL)
        main_page = MainPage(self.driver)
        hidden = main_page.interaction_with_important_question(question_number)
        assert hidden is None, f'Ответ на вопрос номер {question_number} не появляется!'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
