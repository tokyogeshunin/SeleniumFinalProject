from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        cur_url = self.browser.current_url
        assert "login" in cur_url, "There is no login in current url"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS_CONFIRM)
        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_password_input.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_btn.click()
