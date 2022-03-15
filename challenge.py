from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

class rpa_challenge():
    first_name_locator = (By.XPATH,".//label[text() = 'First Name']/following-sibling::input")
    last_name_locator = (By.XPATH,".//label[text() = 'Last Name']/following-sibling::input")
    address_locator = (By.XPATH,".//label[text() = 'Address']/following-sibling::input")
    phone_number_locator = (By.XPATH,".//label[text() = 'Phone Number']/following-sibling::input")
    role_in_company_locator = (By.XPATH,".//label[text() = 'Role in Company']/following-sibling::input")
    company_name_locator = (By.XPATH,".//label[text() = 'Company Name']/following-sibling::input")
    email_locator = (By.XPATH,".//label[text() = 'Email']/following-sibling::input")
    submit_form_locator = (By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input")
    start_challenge_locator = (By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button")
    result_text_one_locator = (By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[1]")
    result_text_two_locator = (By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[2]")


    def __init__(self, driver: Chrome):
        self.webdriver = driver
        
    def open_system(self):
        self.webdriver.get("https://www.rpachallenge.com/")

    def start_challenge(self):
        self.webdriver.find_element(*self.start_challenge_locator).click()

    def fill_form(
            self, first_name, last_name, 
            company_name, role_in_company, address, 
            email, phone_number):

        self.webdriver.find_element(*self.first_name_locator).send_keys(first_name)
        self.webdriver.find_element(*self.last_name_locator).send_keys(last_name)
        self.webdriver.find_element(*self.address_locator).send_keys(address)
        self.webdriver.find_element(*self.phone_number_locator).send_keys(str(phone_number))
        self.webdriver.find_element(*self.role_in_company_locator).send_keys(role_in_company)
        self.webdriver.find_element(*self.company_name_locator).send_keys(company_name)
        self.webdriver.find_element(*self.email_locator).send_keys(email)
        self.webdriver.find_element(*self.submit_form_locator).click()

    def get_result(self):
        msg = []
        text_one = self.webdriver.find_element(*self.result_text_one_locator).text
        text_two = self.webdriver.find_element(*self.result_text_two_locator).text
        final_msg = f'{text_one}{text_two}'
        msg.append([final_msg])
        return msg
