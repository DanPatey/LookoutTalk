####### 3RD PARTY
from ddt import ddt, data

####### TELESIGN
from tsqa.backoffice.tests.ts_test_base import tsTestBase
from pages.page_class import FraudSubmissionPageClass 
from tsqa.backoffice.data.telebureau import single_submission_options
from page_components.table import Table
from selenium.webdriver.common.by import By


@ddt
class SubmissionTest(tsTestBase):
    def setUp(self):
        super(SingleSubmissionFraudTest, self).setUp()
        super(SingleSubmissionFraudTest, self).login('QA Admin')
        self.page = FraudSubmissionPageClass(self._browser)
        self.page.load_page('telemaster-qa')

    @data(single_submission_options.smoke_test)
    def test_submission(self, data):
        self.page.submit_form(single_submission_options.form_fields, data)
        page_data = Table(self.page.driver.find_element(By.ID, 'id_table_SubmissionDetail')).get_data()
        self.assertDictEqual(page_data[0], data)
        self.page.delete_user()
