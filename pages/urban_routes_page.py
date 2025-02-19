from utils.helpers import retrieve_phone_code
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class UrbanRoutesPage(BasePage):
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    request_a_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_option_button = (By.CSS_SELECTOR, '[alt="Comfort"]')

    phone_number_button = (By.CLASS_NAME, 'np-button')
    phone_number_field = (By.ID, 'phone')
    phone_next_button = (By.XPATH, '//button[text() = "Siguiente"]')
    code_field = (By.ID, "code")
    submit_button = (By.XPATH, "//button[text()='Confirmar']")

    payment_method_button = (By.CLASS_NAME, 'pp-value-text')
    add_card_button = (By.CSS_SELECTOR, '.pp-plus-container')
    card_number_field = (By.CLASS_NAME, 'card-input')
    card_code_field = (By.XPATH, '//div[@class="card-code-input"]//input[@class="card-input"]')
    card_wrapper = (By.CLASS_NAME, 'card-wrapper')
    add_button = (By.XPATH, '//button[text()="Agregar"]')
    form_close_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")

    comment_field = (By.XPATH, "//input[@placeholder='Traiga un aperitivo']")

    blanket_and_tissues_slider = (By.CSS_SELECTOR, ".slider.round")

    ice_cream_counter_plus_button = (By.CSS_SELECTOR, '.counter-plus')

    ordering_a_taxi_button = (By.CSS_SELECTOR, '.smart-button')
    ordering_a_taxi_modal = (By.CSS_SELECTOR, '.order-header')

    license_plate = (By.CSS_SELECTOR, '.number')

    def set_route(self, from_address, to_address):
        self.enter_text(self.from_field, from_address)
        self.enter_text(self.to_field, to_address)

    def set_comfort_option(self):
        self.click(self.request_a_taxi_button)
        self.click(self.comfort_option_button)

    def set_phone_number(self, phone_number):
        self.click(self.phone_number_button)
        self.enter_text(self.phone_number_field, phone_number)
        self.click(self.phone_next_button)
        self.enter_text(self.code_field, retrieve_phone_code(self.driver))
        self.click(self.submit_button)

    def add_payment_method(self, card_number, card_code):
        self.click(self.payment_method_button)
        self.click(self.add_card_button)
        self.enter_text(self.card_number_field, card_number)
        self.enter_text(self.card_code_field, card_code)
        self.click(self.card_wrapper)
        self.click(self.add_button)
        self.click(self.form_close_button)

    def set_comment_field(self, message):
        self.enter_text(self.comment_field, message)

    def set_blanket_and_tissues_slider(self):
        self.click(self.blanket_and_tissues_slider)

    def request_two_ice_creams(self):
        self.click(self.ice_cream_counter_plus_button)
        self.click(self.ice_cream_counter_plus_button)

    def request_a_taxi(self):
        self.click(self.ordering_a_taxi_button)
        self.wait_for_element(self.ordering_a_taxi_modal)

    def get_licence_plate(self):
        self.wait_extended_for_element(self.license_plate)
