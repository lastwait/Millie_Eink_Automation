class LoginPage_Resource_Class:
    def __init__(self, driver):
        self.driver = driver
        
        self.IdField_ID = "kr.co.millie.eink:id/textField_login_identifier"
        self.PwField_ID = "kr.co.millie.eink:id/textField_login_password"
        self.LoginBtn_ID = "kr.co.millie.eink:id/button_login"