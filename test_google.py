from selene.support.shared import browser
from selene import be, have


def test_yashaka(open_start_google):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(
        have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_wrong_string(open_start_google):
    browser.element('[name="q"]').should(be.blank).type('vmbndiovjsokjk').press_enter()
    browser.element('#extabar #result-stats').should(
        have.text('Результатов: примерно 0')), "Подходящая страница не найдена"


# @pytest.mark.parametrize(
#    "search_string", ["yashaka/selene", "vmbndiovjsokjk", ]
# )
# def test_search_different_strings(open_google, search_string):
#    browser.element('[name="q"]').should(be.blank).type(search_string).press_enter()
#    assert browser.element('.GyAeWb #search').should(have.attribute(name='childElementCount', value='1')), "нет"
#    ...
