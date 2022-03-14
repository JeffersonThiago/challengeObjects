from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

class rpachallenge():
    firstName = (By.XPATH,".//label[text() = 'First Name']/following-sibling::input")
    lastName = (By.XPATH,".//label[text() = 'Last Name']/following-sibling::input")
    address = (By.XPATH,".//label[text() = 'Address']/following-sibling::input")
    phoneNumber = (By.XPATH,".//label[text() = 'Phone Number']/following-sibling::input")
    roleInCompany = (By.XPATH,".//label[text() = 'Role in Company']/following-sibling::input")
    companyName = (By.XPATH,".//label[text() = 'Company Name']/following-sibling::input")
    email = (By.XPATH,".//label[text() = 'Email']/following-sibling::input")
    submit = (By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input")
    start = (By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button")
    result_text_one = (By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[1]")
    result_text_two = (By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[2]")


    def __init__(self, driver: Chrome):
        self.webdriver = driver
        
    def accessSystem(self):
        self.webdriver.get("https://www.rpachallenge.com/")

    def startChallenge(self):
        self.webdriver.find_element(*self.start).click()

    def fillForm(self,firstName,lastName,companyName,roleInCompany,address,email,phoneNumber):
        self.webdriver.find_element(*self.firstName).send_keys(firstName)
        self.webdriver.find_element(*self.lastName).send_keys(lastName)
        self.webdriver.find_element(*self.address).send_keys(address)
        self.webdriver.find_element(*self.phoneNumber).send_keys(str(phoneNumber))
        self.webdriver.find_element(*self.roleInCompany).send_keys(roleInCompany)
        self.webdriver.find_element(*self.companyName).send_keys(companyName)
        self.webdriver.find_element(*self.email).send_keys(email)
        self.webdriver.find_element(*self.submit).click()

    def getResults(self):
        msg = []
        textone = self.webdriver.find_element(*self.result_text_one).text
        texttwo = self.webdriver.find_element(*self.result_text_two).text
        msg.append([textone])
        msg.append([texttwo])
        return msg
