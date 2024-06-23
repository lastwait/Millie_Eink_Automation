import time
import cv2
import os

from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Automation_Resource import LoginPage_Resource

class Login_Fail_Class:
    # 인스턴스 생성의 초기화를 수행하며, 다른 파일에서 Login_Fail_Calss를 호출 할 때마다 초기화 작업을 수행합니다. 
    # 파이썬-객체 지향 프로그래밍이 올바르게 동작하기 위한 기본 동작 입니다.
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        
        self.LoginPage = LoginPage_Resource.LoginPage_Resource_Class(driver)

    def Login_Fail_Automation(self):
        try:
            # 아이디 입력 칸을 클릭합니다.
            self.wait.until(EC.element_to_be_clickable((MobileBy.ID, self.LoginPage.IdField_ID))).click()
            # 아이디 입력 칸에 로그인에 실패하는 아이디를 입력합니다.
            self.driver.switch_to.active_element.send_keys('lastwai')
            # 비밀번오 입력 칸을 클릭 합니다.
            self.wait.until(EC.element_to_be_clickable((MobileBy.ID, self.LoginPage.PwField_ID))).click()
            # 비밀번호 입력 칸에 로그인에 실패하는 비밀번호를 입력합니다.
            self.driver.switch_to.active_element.send_keys('Wlgus!')
            # 로그인 버튼을 클릭합니다.
            self.wait.until(EC.element_to_be_clickable((MobileBy.ID, self.LoginPage.LoginBtn_ID))).click()
            # 로그인 버튼을 MillieEink_Login_Btn로 지정합니다.
            MillieEink_Login_Btn = self.driver.find_element(MobileBy.ID, "kr.co.millie.eink:id/button_login")
            # 만약 MillieEink_Login_Btn = self.driver.find_element(MobileBy.ID, "kr.co.millie.eink:id/button_login")이 화면에 남아 있다면 다음 코드를 실행합니다.
            # 코드 조건이 만족하지 않은 경우 코드를 종료 합니다.
            if MillieEink_Login_Btn:
                # 아이디 입력 칸의 텍스트를 Id_Text에 저장합니다.
                Id_Text = self.driver.find_element(MobileBy.ID, self.LoginPage.IdField_ID).text
                # 비밀번호 입력 칸의 아스타 처리된 텍스트를 Pw_Text에 저장 합니다.
                Pw_Text = self.driver.find_element(MobileBy.ID, self.LoginPage.PwField_ID).text
                # 아이디와 비밀번호가 모두 공백인 경우 print를 출력 합니다.
                if Id_Text == "" and Pw_Text == "":
                    print("\n ID와 비밀번호 모두 공백 입니다.")
                # 아이디가 테스트 아이디가 아니고, 비밀번호가 공백인 경우 print를 출력 합니다.
                elif Id_Text != "lastwait" and Pw_Text == "":
                    print("\n ID가 테스트를 위한 아이디가 아니며, 비밀번호가 공백 입니다.")
                # 아이디는 테스트 아이디지만, 비밀번호가 공백인 경우 print를 출력 합니다.
                elif Id_Text == "lastwait" and Pw_Text == "":
                    print("\n ID는 정상 입력 되었으나(lastwait), 비밀번호가 공백 입니다.")
                # 아이디는가 테스트 아이디가 아니고, 비밀번호가 테스트를 위한 비밀번호 자리 수와 다르다면 print를 출력 합니다.
                elif Id_Text != "lastwait" and len(Pw_Text) != 8:
                    print("\n ID가 테스트를 위한 아이디가 아니며, 비밀번호 글자 수가 테스트 계정의 비밀번호 글자 수와 맞지 않습니다.")
                # 아이디는 테스트 아이디이고, 비밀번호도 테스트를 위한 비밀번호 자리 수와 같지만 비밀번호 입력 값에 문제가 있어 로그인이 실패한 경우로 print를 출력 합니다.
                elif Id_Text == "lastwait" and len(Pw_Text) == 8:
                    print("\n ID는 정상 입력 되었으며(lastwait), 비밀번호 글자 수도 테스트 계정의 비밀번호 글자 수와 일치하나 로그인에 실패 하였습니다. 비밀번호 입력 값을 다시 확인 해주세요.")
                # 현재 시간을 구해서 login_Fail_Time 지정합니다.
                Login_Fail_Time = time.strftime("%Y%m%d_%H%M%S")    
                # 현재 화면을 png로 저장합니다. 이 때 png 파일에 login_Fail_Time 파일명에 포함합니다.
                Login_Fail_Screenshot_Path = f"/Users/younjihyun/Desktop/Millie_Eink_Automation/Login_Result/Login_Fail_Test_{Login_Fail_Time}.png"
                self.driver.save_screenshot(Login_Fail_Screenshot_Path)
                # adb logcat을 txt로 저장합니다. 이 때 logcat을 txt 파일에 login_Fail_Time 파일명에 포함합니다.
                Login_Fail_Logcat_Path = f"/Users/younjihyun/Desktop/Millie_Eink_Automation/Login_Result/Login_Fail_Test_{Login_Fail_Time}.txt"
                os.system(f"adb logcat -d > {Login_Fail_Logcat_Path}")

                # 기존에 저장된 Login Fail 상황의 원본 이미지 경로를 지정합니다. = Login_Fail_Original_Screenshot_Path
                Login_Fail_Original_Screenshot_Path = f"/Users/younjihyun/Desktop/Millie_Eink_Automation/Login_Result/Login_Fail_Test_Original.png"
                # open cv로 Login_Fail_Original_Screenshot_Path의 이미지를 읽고 Original_Login_Fail_Image로 저장 합니다.
                Original_Login_Fail_Image = cv2.imread(Login_Fail_Original_Screenshot_Path)
                # open cv로 Login_Fail_Screenshot_Path의 이미지를 읽고 Current_Login_Fail_image로 저장합니다.
                Current_Login_Fail_image = cv2.imread(Login_Fail_Screenshot_Path)

                # cv2.subtract() 함수를 사용하여 Original_Login_Fail_Image에서 Current_Login_Fail_image를 뺀 차이 이미지를 생성합니다.
                Login_Fail_Difference = cv2.subtract(Original_Login_Fail_Image, Current_Login_Fail_image)
                # cv2.split() 함수를 사용하여 Login_Fail_Difference 이미지를 각 채널 (파란색, 초록색, 빨간색)로 분할합니다.
                b, g, r = cv2.split(Login_Fail_Difference)
                # cv2.countNonZero(b), cv2.countNonZero(g), cv2.countNonZero(r): 각각 파란색 채널 (b), 초록색 채널 (g), 빨간색 채널 (r)에서 0이 아닌 픽셀의 수를 합산 합니다.
                # Original_Login_Fail_Image.size / 3으로 rgb의 평균적으로 사용되는 픽셀 수를 계산 합니다.
                Login_Fail_Diff_Percentage = (cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)) / (Original_Login_Fail_Image.size / 3) * 100
                # 100-(오리지널 픽셀 수-rgb가 0이 아닌 픽셀) = 이미지 일치율을 계산 합니다.
                Login_Fail_Diff_Percentage_Result = 100 - Login_Fail_Diff_Percentage
                # 이미지 일치율이 90% 이상이라면 코드 실행 합니다.
                # 코드 조건이 만족하지 않은 경우 코드를 종료 합니다.
                if Login_Fail_Diff_Percentage_Result >= 90:
                    print(f"\n원본 이미지와 비교한 결과 {Login_Fail_Diff_Percentage_Result}% 일치율로 로그인 실패를 확인했습니다. logcat을 확인합니다.")
                # logcat txt 파일을 열고 "Toast already killed."로 토스트 메시지가 사라진 기록이 있는지 확인 합니다.
                # 'r' = 읽기 모드로 파일 오픈 합니다.
                # 인코딩 'UTF-8'에서 에러 발생하여 latin-1으로 인코딩 합니다.
                with open(Login_Fail_Logcat_Path, 'r', encoding='latin-1') as Login_Fail_Logcat_File:
                    # 파일 전체 내용을 Login_Fail_Logcat_File.read로 읽어오고 파일에 "Toast already killed."가 포함된 경우 다음 코드를 실행 합니다.
                    # 코드 조건이 만족하지 않은 경우 코드를 종료 합니다.
                    if "Toast already killed." in Login_Fail_Logcat_File.read():
                        print(f"\nlogcat 에서도 'Toast already killed.'가 확인되어 최종적으로 로그인에 실패했음을 확인하였습니다.")
        # 위 조건을 만족하지 못하는 경우 에러 내용을 프린트 합니다.
        except Exception as e:
            print(f"테스트 실행 중 오류 발생: {str(e)}")