from playwright.sync_api import Page, expect

class EmailPage:
    def __init__(self, page: Page):
        self.page = page
        self.compose_button = page.get_by_text("Compose")
        self.to_input = page.get_by_label("To recipients")
        self.subject_input = page.locator("input[name='subjectbox']")
        self.body_input = page.locator("div[aria-label='Message Body']")
        self.attach_input = page.locator("input[name='Filedata']")
        self.send_button = page.locator("div[role='button'][aria-label='Send ‪(Ctrl-Enter)‬']")
        self.sent_confirmation = page.get_by_text("Message sent")

    def compose_new_email(self):
        self.compose_button.click()

    def attach_file(self, file_path: str):
        self.attach_input.set_input_files(file_path)


    def send_email(self, to: str, subject: str, body: str):
        self.to_input.fill(to)
        self.subject_input.fill(subject)
        self.body_input.fill(body)
        self.send_button.click()

    def is_email_sent(self):
        expect(self.sent_confirmation).to_be_visible()
