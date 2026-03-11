from assertpy import assert_that


def test_login(login_page):
    login_page.open_page()
    login_page.enter_email("test@mail.com")
    login_page.click_next()
    login_page.enter_password("testpass")
    login_page.click_next()

    assert_that(login_page.password_input.is_visible()).is_equal_to(True)
    assert_that(login_page.is_logged_in()).contains("myaccount.google.com")


def test_login_without_email(login_page):
    login_page.open_page()
    login_page.click_next()

    assert_that(login_page.hint_email.get_text()).is_equal_to(
        "Введите адрес электронной почты или номер телефона."
    )


def test_switch_language(login_page):
    login_page.open_page()
    login_page.switch_language_to_english()

    assert_that(login_page.greet.get_text()).is_equal_to("Sign in")
