import time
import cv2
import os

from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Automation_Resource import LoginPage_Resource
from Automation_Resource import AllBookPage_Resource
from Automation_Resource import SettingPage_Resource

class Login_Pass_Class:
    # 인스턴스 생성의 초기화를 수행하며, 다른 파일에서 Login_Pass_Calss를 호출 할 때마다 초기화 작업을 수행합니다. 
    # 파이썬-객체 지향 프로그래밍이 올바르게 동작하기 위한 기본 동작 입니다.
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        
        self.LoginPage = LoginPage_Resource.LoginPage_Resource_Class(driver)
        self.AllBookPage = AllBookPage_Resource.AllBookPage_Resource_Class(driver)
        self.SettingPage = SettingPage_Resource.SettingPage_Resource_Class(driver)
        
    def Login_Pass_Automation(self):
        try:
            # 비밀번호 필드를 클릭하고, clear로 필드 값을 모두 지웁니다.
            self.wait.until(EC.element_to_be_clickable((MobileBy.ID, self.LoginPage.PwField_ID))).click()
            self.driver.switch_to.active_element.clear()
            # ID 필드를 클릭하고, clear로 필드 값을 모두 지웁니다.
            self.wait.until(EC.element_to_be_clickable((MobileBy.ID, self.LoginPage.IdField_ID))).click()
            self.driver.switch_to.active_element.clear()
            self.driver.switch_to.active_element.send_keys('lastwait')
            # 비밀번호 필드를 클릭하고 비밀번호를 입력합니다.
            self.wait.until(EC.element_to_be_clickable((MobileBy.ID, self.LoginPage.PwField_ID))).click()
            self.driver.switch_to.active_element.send_keys('Wlgus!7220')
            # ID와 비밀번호 필드를 입력 후 [로그인] 버튼을 클릭 합니다.
            self.wait.until(EC.element_to_be_clickable((MobileBy.ID, self.LoginPage.LoginBtn_ID))).click()
            # presence_of_element_located로 "kr.co.millie.eink:id/btn_settings" = [설정] 버튼이 등장할 때 까지 대기하고 찾습니다.
            if self.wait.until(EC.presence_of_element_located((MobileBy.ID, self.AllBookPage.GNB_Setting_Btn_ID))):
                print ("\n로그인에 성공하여 [설정]버튼(톱니바퀴)를 찾았습니다.")
                # [설정] 버튼을 클릭 합니다.
                self.wait.until(EC.element_to_be_clickable((MobileBy.ID, self.AllBookPage.GNB_Setting_Btn_ID))).click()
                # 설정 화면에 입장 후 "kr.co.millie.eink:id/tv_account_title"의 텍스트가 "계정"인지 확인 합니다. 이는 설정/계정 정보 화면에 성공적으로 진입 했음을 나타냅니다.
                self.wait.until(EC.presence_of_element_located((MobileBy.ID, self.SettingPage.AccountTitle_ID)))
                if self.driver.find_element(MobileBy.ID, self.SettingPage.AccountTitle_ID).text == "계정":
                    print ("\n'계정' 정보를 노출하는 Element ID가 확인 되었습니다.")
                    # 아이디 노출 frame의 XPATH값이 로그인 아이디 'lastwait'인지 확인 합니다.
                    if self.driver.find_element(MobileBy.XPATH, self.SettingPage.AccountNickname_XPATH).text == "lastwait":
                        print("\n계정의 아이디 정보가 'lastwait'로 확인 되었습니다.")
                    # 현재 시간을 구해서 login_Pass_Time 지정합니다.
                    Login_Pass_Time = time.strftime("%Y%m%d_%H%M%S")    
                    # 현재 화면을 png로 저장합니다. 이 때 png 파일에 login_Pass_Time 파일명에 포함합니다.
                    Login_Pass_Screenshot_Path = f"/Users/younjihyun/Desktop/Millie_Eink_Automation/Login_Result/Login_Pass_Test_{Login_Pass_Time}.png"
                    self.driver.save_screenshot(Login_Pass_Screenshot_Path)

                    # adb logcat을 txt로 저장합니다. 이 때 logcat을 txt 파일에 login_Pass_Time 파일명에 포함합니다.
                    Login_Pass_Logcat_Path = f"/Users/younjihyun/Desktop/Millie_Eink_Automation/Login_Result/Login_Pass_Test_{Login_Pass_Time}.txt"
                    os.system(f"adb logcat -d > {Login_Pass_Logcat_Path}")

                    # 기존에 저장된 Login Pass 상황의 원본 이미지 경로를 지정합니다. = Login_Pass_Original_Screenshot_Path
                    Login_Pass_Original_Screenshot_Path = f"/Users/younjihyun/Desktop/Millie_Eink_Automation/Login_Result/Login_Pass_Test_Original.png"
                    # open cv로 Login_Pass_Original_Screenshot_Path의 이미지를 읽고 Original_Login_Pass_Image로 저장 합니다.
                    Original_Login_Pass_Image = cv2.imread(Login_Pass_Original_Screenshot_Path)
                    # open cv로 Login_Pass_Screenshot_Path의 이미지를 읽고 Current_Login_Pass_image로 저장합니다.
                    Current_Login_Pass_image = cv2.imread(Login_Pass_Screenshot_Path)

                    # cv2.subtract() 함수를 사용하여 Original_Login_Pass_Image에서 Current_Login_Pass_image를 뺀 차이 이미지를 생성합니다.
                    Login_Pass_Difference = cv2.subtract(Original_Login_Pass_Image, Current_Login_Pass_image)
                    # cv2.split() 함수를 사용하여 Login_Pass_Difference 이미지를 각 채널 (파란색, 초록색, 빨간색)로 분할합니다.
                    b, g, r = cv2.split(Login_Pass_Difference)
                    # cv2.countNonZero(b), cv2.countNonZero(g), cv2.countNonZero(r): 각각 파란색 채널 (b), 초록색 채널 (g), 빨간색 채널 (r)에서 0이 아닌 픽셀의 수를 합산 합니다.
                    # Original_Login_Pass_Image.size / 3으로 rgb의 평균적으로 사용되는 픽셀 수를 계산 합니다.
                    Login_Pass_Diff_Percentage = (cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)) / (Original_Login_Pass_Image.size / 3) * 100
                    # 100-(오리지널 픽셀 수-rgb가 0이 아닌 픽셀) = 이미지 일치율을 계산 합니다.
                    Login_Pass_Diff_Percentage_Result = 100 - Login_Pass_Diff_Percentage
                    # 이미지 일치율이 90% 이상이라면 코드 실행 합니다.
                    # 코드 조건이 만족하지 않은 경우 코드를 종료 합니다.
                    if Login_Pass_Diff_Percentage_Result >= 90:
                        print(f"\n원본 이미지와 비교한 결과 {Login_Pass_Diff_Percentage_Result}% 일치율로 로그인 성공을 확인했습니다. logcat을 확인합니다.")
                    # logcat txt 파일을 열고 "Toast already killed."로 토스트 메시지가 사라진 기록이 있는지 확인 합니다.
                    # 'r' = 읽기 모드로 파일 오픈 합니다.
                    # 인코딩 'UTF-8'에서 에러 발생하여 latin-1으로 인코딩 합니다.
                    with open(Login_Pass_Logcat_Path, 'r', encoding='latin-1') as Login_Fail_Logcat_File:
                        # 파일 전체 내용을 Login_Fail_Logcat_File.read로 읽어오고 파일에 "Toast already killed."가 포함된 경우 다음 코드를 실행 합니다.
                        # 코드 조건이 만족하지 않은 경우 코드를 종료 합니다.
                        if "BookshelfActivity" in Login_Fail_Logcat_File.read():
                            print(f"\nlogcat 에서도 'BookshelfActivity'가 확인되어 최종적으로 로그인에 성공 했음을 확인하였습니다.\n(BookshelfActivity는 LoginActivity에서 화면이 전환되었음을 나타내며 로그인 성공 상황임으로 추정 합니다.)")
        except Exception as e:
            print("에러가 발생 했습니다. : ", e)