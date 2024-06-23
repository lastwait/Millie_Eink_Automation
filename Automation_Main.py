import time
import unittest
import warnings
import subprocess
import pytest
import cv2
import os

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.appium_service import AppiumService

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Automation_Modules import Login_Fail
from Automation_Modules import Login_Pass

# iTerm2 실행 후 Appium 2.0 명령을 수행하는 코드
appium_command = 'osascript -e \'tell application "iTerm" to activate\' -e \'tell application "System Events" to tell process "iTerm" to keystroke "appium --address 127.0.0.1 -p 4723 --base-path /wd/hub"\' -e \'tell application "System Events" to tell process "iTerm" to keystroke return\''
subprocess.Popen(appium_command, shell=True)

# iTerm2 실행 및 Appium 실행까지의 대기 명령어
time.sleep(5)

# 자동화 실행 환경
cap = {
  "appium:appPackage": "kr.co.millie.eink",
  "appium:appActivity": "kr.co.millie.eink.user.LoginActivity",
  "platformName": "Android",
  "appium:deviceName": "galaxy_s10",
  "appium:udid": "R39M10EC2RZ",
  "automationName": "UiAutomator2"
}

# 코드에서 Appium 2.0 접속 설정 및 실행
Appium = AppiumService()
DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 4723
Appium.start(args=['--address', DEFAULT_HOST, '-p', str(DEFAULT_PORT), '--base-path', '/wd/hub'])
warnings.filterwarnings("ignore", category=DeprecationWarning)

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap, keep_alive=False)
time.sleep(5)

# 클래스 정의, 파이썬 내장 테스트 프레임 워크 unittest를 사용 합니다.
class Test01_MillieEink_Automation_Login(unittest.TestCase):
    @classmethod
    # setup class 정의함으로 테스트 실행 전 셋업을 위한 class 입니다.
    def setUpClass(self):
        # driver라는 변수를 self.driver에 할당하여 클래스 내에서 사용 가능하도록 합니다.
        self.driver = driver
        # WebDriverWait는 driver를 사용해서 최대 15초까지 대기하는 기능입니다. 
        self.wait = WebDriverWait(driver, 15)
        
        # Login_Fail 모듈에서 Login_Fail_Class 클래스를 인스턴스화하여 self.Login_Fail_Modules에 할당합니다. 그리고 driver 객체를 전달 합니다.
        self.Login_Fail_Modules = Login_Fail.Login_Fail_Class(driver)
        # Login_Pass 모듈에서 Login_Pass_Class 클래스를 인스턴스화하여 self.Login_Pass_Modules에 할당합니다. 그리고 driver 객체를 전달 합니다.
        self.Login_Pass_Modules = Login_Pass.Login_Pass_Class(driver)

    # test01 login Fail 메서드를 정의 합니다. self는 클래스의 인스턴스를 참조하게 됩니다.
    def test01_MillieEink_Login_Fail(self):
        # Login_Fail_Modules 클래스 인스턴스의 Login_Fail_Automation 메서드를 실행 합니다.
        self.Login_Fail_Modules.Login_Fail_Automation()
    
    # test02 login Pass 메서드를 정의 합니다. self는 클래스의 인스턴스를 참조하게 됩니다.
    def test02_MillieEink_Login_Pass(self):
        # Login_Pass_Modules 클래스 인스턴스의 Login_Pass_Automation 메서드를 실행 합니다.
        self.Login_Pass_Modules.Login_Pass_Automation()

  
    @classmethod
    # 드라이버 인자를 받을 필요가 없는 class입니다.
    # tesrdown으로 driver종료 및 appium을 정지하여 테스트를 종료 합니다.
    def tearDownClass(cls):
        driver.quit()
        Appium.stop()

