class SettingPage_Resource_Class:
    def __init__(self, driver):
        self.driver = driver
        
        self.AccountTitle_ID = "kr.co.millie.eink:id/tv_account_title"
        self.AccountNickname_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]"