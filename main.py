import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    request_a_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_option_button = (By.CSS_SELECTOR, '[alt="Comfort"]')

    phone_number_button = (By.CLASS_NAME, 'np-button')
    phone_number_field = (By.ID, 'phone')
    phone_next_button = (By.XPATH, '//button[text() = "Siguiente"]')
    code_field = (By.ID, "code")
    submit_button = (By.XPATH, "//button[text()='Confirmar']")

    payment_method_button = (By.CLASS_NAME, 'pp-button')
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


    def __init__(self, driver):
        self.driver = driver

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.request_a_taxi_button)
        )

    def click_on_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_option_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.comfort_option_button)
        )

    def click_on_comfort_option_button(self):
        self.get_comfort_option_button().click()

    def set_comfort_option(self):
        self.click_on_request_taxi_button()
        self.click_on_comfort_option_button()

    def get_phone_number_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.phone_number_button)
        )

    def click_on_phone_number_button(self):
        self.get_phone_number_button().click()

    def get_phone_number_field(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.phone_number_field)
        )

    def fill_in_phone_number(self):
        self.get_phone_number_field().send_keys(data.phone_number)

    def get_phone_next_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.phone_next_button)
        )

    def click_on_phone_next_button(self):
        self.get_phone_next_button().click()

    def get_code_field(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.code_field)
        )

    def set_code_field(self):
        self.get_code_field().send_keys(retrieve_phone_code(self.driver))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.submit_button)
        )

    def click_on_submit_button(self):
        self.get_submit_button().click()

    def set_phone_number(self):
        self.click_on_phone_number_button()
        self.fill_in_phone_number()
        self.click_on_phone_next_button()
        self.set_code_field()
        self.click_on_submit_button()

    def get_payment_method_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.payment_method_button)
        )

    def click_on_payment_method_button(self):
        self.get_payment_method_button().click()

    def get_add_card_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_card_button)
        )

    def click_on_add_card_button(self):
        self.get_add_card_button().click()

    def get_card_number_field(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.card_number_field)
        )

    def set_card_number_field(self):
        self.get_card_number_field().send_keys(data.card_number)

    def get_card_code_field(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.card_code_field)
        )

    def set_card_code_field(self):
        self.get_card_code_field().send_keys(data.card_code)

    def get_card_wrapper(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.card_wrapper)
        )

    def click_on_card_wrapper(self):
        self.get_card_wrapper().click()

    def get_add_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_button)
        )

    def click_on_add_button(self):
        self.get_add_button().click()

    def get_form_close_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.form_close_button)
        )

    def click_on_form_close_button(self):
        self.get_form_close_button().click()

    def add_payment_method(self):
        self.click_on_payment_method_button()
        self.click_on_add_card_button()
        self.set_card_number_field()
        self.set_card_code_field()
        self.click_on_card_wrapper()
        self.click_on_add_button()
        self.click_on_form_close_button()

    def get_comment_field(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.comment_field)
        )

    def set_comment_field(self):
        self.get_comment_field().send_keys(data.message_for_driver)

    def get_blanket_and_tissues_slider(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.blanket_and_tissues_slider)
        )

    def click_on_blanket_and_tissues_slider(self):
        self.get_blanket_and_tissues_slider().click()

    def get_ice_cream_counter_plus_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.ice_cream_counter_plus_button)
        )

    def double_click_on_ice_cream_counter_plus_button(self):
        self.get_ice_cream_counter_plus_button().click()
        self.get_ice_cream_counter_plus_button().click()

    def get_ordering_a_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.ordering_a_taxi_button)
        )

    def click_on_ordering_a_taxi_button(self):
        self.get_ordering_a_taxi_button().click()

    def get_ordering_a_taxi_modal(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.ordering_a_taxi_modal)
        )

    def get_licence_plates(self):
        return WebDriverWait(self.driver,60).until(
            expected_conditions.presence_of_element_located(self.license_plate)
        )

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_comfort_option(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort_option()
        assert routes_page.get_comfort_option_button().text in "Comfort"

    def test_set_phone_number(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort_option()
        routes_page.set_phone_number()
        phone_shown_on_the_button = routes_page.get_phone_number_button().text
        phone_number = data.phone_number
        assert phone_shown_on_the_button == phone_number

    def test_add_payment_method(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort_option()
        routes_page.set_phone_number()
        routes_page.add_payment_method()
        pay_method = self.driver.find_element(By.CSS_SELECTOR, '.pp-value-text').text
        assert pay_method == "Tarjeta"

    def test_set_comment_field(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort_option()
        routes_page.set_phone_number()
        routes_page.add_payment_method()
        routes_page.set_comment_field()
        comment_shown_on_comment_field = routes_page.get_comment_field().get_property('value')
        comment_for_driver = data.message_for_driver
        assert comment_shown_on_comment_field in comment_for_driver

    def test_ask_for_a_blanket_and_tissues(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort_option()
        routes_page.set_phone_number()
        routes_page.add_payment_method()
        routes_page.set_comment_field()
        routes_page.click_on_blanket_and_tissues_slider()
        switch = self.driver.find_element(By.CSS_SELECTOR, '.switch-input')
        assert switch.is_selected() == True

    def test_oder_two_ice_creams(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort_option()
        routes_page.set_phone_number()
        routes_page.add_payment_method()
        routes_page.set_comment_field()
        routes_page.click_on_blanket_and_tissues_slider()
        routes_page.double_click_on_ice_cream_counter_plus_button()
        counter_value = self.driver.find_element(By.CSS_SELECTOR, '.counter-value').text
        assert counter_value == "2"

    def test_ordering_a_taxi(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort_option()
        routes_page.set_phone_number()
        routes_page.add_payment_method()
        routes_page.set_comment_field()
        routes_page.click_on_blanket_and_tissues_slider()
        routes_page.double_click_on_ice_cream_counter_plus_button()
        routes_page.click_on_ordering_a_taxi_button()
        ordering_a_taxi_modal_appears = routes_page.get_ordering_a_taxi_modal()
        assert ordering_a_taxi_modal_appears.is_displayed() == True

    def test_drivers_information(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort_option()
        routes_page.set_phone_number()
        routes_page.add_payment_method()
        routes_page.set_comment_field()
        routes_page.click_on_blanket_and_tissues_slider()
        routes_page.double_click_on_ice_cream_counter_plus_button()
        routes_page.click_on_ordering_a_taxi_button()
        wait_driver_information = routes_page.get_licence_plates()
        assert wait_driver_information.is_displayed() == True


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
