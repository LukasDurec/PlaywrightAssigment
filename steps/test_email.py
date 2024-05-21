import pytest
from playwright.sync_api import sync_playwright,expect
from pytest_bdd import scenarios, given, when, then
from pageObjects.loginPageObjects import LoginPage
from pageObjects.emailPageObjects import EmailPage

scenarios('../features/email.feature')

mail :str = "test.playwpyt@gmail.com"
password :str = "Heslo1234"
sendToMail :str = "lukasdurec2@gmail.com"
file :str = "smile.jpg"

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

@pytest.fixture(scope="function")
def email_page(page_context):
    return EmailPage(page_context)

@given('the user is logged into Gmail')
def user_logged_into_gmail(login_page):
    login_page.navigate()
    login_page.login(mail, password)
    login_page.is_logged_in()

@when('the user composes a new email')
def user_composes_new_email(email_page):
    email_page.compose_new_email()

@when('the user attaches a file')
def user_attaches_file(email_page):
    email_page.attach_file(file)

@when('the user sends the email to "me"')
def user_sends_email(email_page):
    email_page.send_email(sendToMail, "Test Subject", "Test Body")

@then('the email should be sent successfully')
def email_sent_successfully(email_page):
    email_page.is_email_sent()
