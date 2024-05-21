from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.get_by_role("textbox", name="E-mail alebo telefón")
        self.password_input = page.get_by_role("textbox", name="Zadajte svoje heslo")
        self.next_button = page.get_by_role("button", name="Ďalej")
        self.inbox_locator = page.get_by_label("Inbox", exact=True)
        self.profile_icon = page.get_by_label("Google Account: ")
        self.sign_out_button = page.frame_locator('iframe[name="account"]').get_by_text("Sign out")

    def navigate(self):
        self.page.goto("https://mail.google.com")

    def enter_email(self, email_: str):
        self.email_input.fill(email_)
        self.next_button.click()

    def enter_password(self, password_: str):
        self.password_input.fill(password_)
        self.next_button.click()

    def login(self, email_: str, password_: str):
        self.enter_email(email_)
        self.enter_password(password_)
        self.is_logged_in()

    def is_logged_in(self):
        expect(self.inbox_locator).to_be_visible
        expect(self.profile_icon).to_be_visible

    def get_error_message(self,message_: str):
        expect(self.page.get_by_text(message_)).to_be_visible() #cant find better locator dot error message

    def assert_url(self, expected_url_: str):
        expect(self.page).to_have_url(expected_url_)

    def logout(self):
        expect(self.profile_icon).to_be_visible()
        self.profile_icon.click()
        expect(self.sign_out_button).to_be_visible()
        self.sign_out_button.click()
