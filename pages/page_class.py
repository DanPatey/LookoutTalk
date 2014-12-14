from page_components.text_field_controls import TextFieldControls
from page_components.drop_down_controls import DropDownControls
from page_components.calendar_controls import CalendarControls
from selenium.webdriver.common.by import By


class MyPageClass(object):

    def __init__(self, driver):
        self.driver = driver

    def load_page(self, env):
        self.driver.get("https://" + env + ".MyWebsite.com/SignUpPage/")
    
    def _select_from_dropdown(self, element_id, option):
        dropdown = DropDownControls(self.driver.find_element(By.ID, element_id))
        dropdown.select_option_by_autocomplete(option)

    def _type_into_text_field(self, element_id, value):
        textfield = TextFieldControls(self.driver.find_element(By.ID, element_id))
        textfield.submit_text(value)

    def _select_from_calendar(self, element_id, value):
        calendar = CalendarControls(self.driver.find_element(By.ID, element_id), self.driver.find_element(By.ID, 'ui-datepicker-div'))
        calendar.set_date(value)

    def submit_form(self, form_fields, form_data):
        for field_name, options in form_fields:
            getattr(self, options['input_function'])(
                    options['element_id'], 
                    form_data.get(field_name, options['default_value']))
        self.driver.find_element(By.ID, 'submit-id-save').click()
