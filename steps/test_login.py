import pytest
from playwright.sync_api import sync_playwright,expect
from pytest_bdd import scenarios, given, when, then
from pageObjects.loginPageObjects import LoginPage

scenarios('../features/login.feature')

mail :str = "test.playwpyt@gmail.com"
password: str = "Heslo1234"
invalidUsernameMsg :str = "Váš účet Google sa nepodarilo nájsť"
invalidPasswdMsg :str  =  "Chybné heslo. Skúste to znova alebo kliknite na „Zabudli ste heslo?“ a heslo si resetujte."

@pytest.fixture(scope="function")
def page_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def login_page(page_context):
    return LoginPage(page_context)

@given('the user is on the login page')
def user_on_login_page(login_page):
    login_page.navigate()

@when('the user enters a valid email')
def user_enters_valid_email(login_page):
    login_page.enter_email(mail)

@when('the user enters a valid password')
def user_enters_valid_password(login_page):
    login_page.enter_password(password)

@then('the user should be redirected to the inbox')
def user_redirected_to_inbox(login_page):
    login_page.is_logged_in()

@when('the user enters an invalid email')
def user_enters_invalid_email(login_page):
    login_page.enter_email("invalid-email@gmail.com")

@when('the user enters an invalid password')
def user_enters_invalid_password(login_page):
    login_page.enter_password("invalid-password")

@then('an invalid username error message should be displayed')
def error_message_displayed(login_page):
    login_page.get_error_message(invalidUsernameMsg)
    expect(login_page.email_input).to_be_visible()


@when('the user enters an incorrect password')
def user_enters_incorrect_password(login_page):
    login_page.enter_password("incorrect-password")

@then('an invalid password error message should be displayed')
def incorrect_password_message_displayed(login_page):
    login_page.get_error_message(invalidPasswdMsg)

@given('the user is logged in')
def user_is_logged_in(login_page):
    login_page.navigate()
    login_page.login(mail, password)

@when('the user clicks on the profile icon')
def user_clicks_profile_icon(login_page):
    login_page.profile_icon.click()

@when('the user clicks on the "Sign out" button')
def user_clicks_sign_out_button(login_page):
    login_page.sign_out_button.click()

@then('the user should be redirected to the logout page')
def user_redirected_to_logout_page(login_page):
    login_page.assert_url("https://www.google.com/intl/sk/gmail/about/")
