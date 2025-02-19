from data import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_page import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):

        # no modificar
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        from_value = routes_page.wait_for_element(routes_page.from_field).get_property('value')
        to_value = routes_page.wait_for_element(routes_page.to_field).get_property('value')
        assert from_value == data.address_from
        assert to_value == data.address_to

    def test_set_comfort_option(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort_option()
        assert routes_page.get_text(routes_page.comfort_option_button) in "Comfort"

    def test_set_phone_number(self):
        self.test_set_comfort_option()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_phone_number(data.phone_number)
        phone_shown_on_the_button = routes_page.get_text(routes_page.phone_number_button)
        phone_number = data.phone_number
        assert phone_shown_on_the_button == phone_number

    def test_add_payment_method(self):
        self.test_set_phone_number()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_payment_method(data.card_number, data.card_code)
        pay_method = routes_page.get_text(routes_page.payment_method_button)
        assert pay_method == "Tarjeta"

    def test_set_comment_field(self):
        self.test_add_payment_method()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comment_field(data.message_for_driver)
        comment_shown_on_comment_field = routes_page.wait_for_element(routes_page.comment_field).get_property('value')
        comment_for_driver = data.message_for_driver
        assert comment_shown_on_comment_field in comment_for_driver

    def test_ask_for_a_blanket_and_tissues(self):
        self.test_set_comment_field()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_blanket_and_tissues_slider()
        switch = self.driver.find_element(By.CSS_SELECTOR, '.switch-input')
        assert switch.is_selected() == True

    def test_oder_two_ice_creams(self):
        self.test_ask_for_a_blanket_and_tissues()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_two_ice_creams()
        counter_value = self.driver.find_element(By.CSS_SELECTOR, '.counter-value').text
        assert counter_value == "2"

    def test_ordering_a_taxi(self):
        self.test_oder_two_ice_creams()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_a_taxi()
        ordering_a_taxi_modal_appears = routes_page.wait_for_element(routes_page.ordering_a_taxi_modal)
        assert ordering_a_taxi_modal_appears.is_displayed() == True

    def test_drivers_information(self):
        self.test_ordering_a_taxi()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_licence_plate()
        wait_driver_information = routes_page.wait_extended_for_element(routes_page.license_plate)
        assert wait_driver_information.is_displayed() == True


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()