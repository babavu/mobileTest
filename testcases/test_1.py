from configuration import webDriver
from selenium.webdriver.common.by import By
import time

wd = webDriver.cal()
delay_seconds = 2  # 딜레이를 주고 싶은 경우
time.sleep(delay_seconds)  # 지정된 시간 동안 프로그램을 일시 중지

#홈까지
wd.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageButton").click()
wd.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageButton").click()
wd.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageButton").click()
wd.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageButton").click()
wd.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageButton").click()
wd.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageButton").click()


#햄버거 버튼
wd.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="drawer open"]').click()

#언어 모음
languages = ["العربية (Arabic)", "Asturianu (Asturian)", "Euskara (Basque)", "မြန်မာစာ (Burmese)", "Català (Catalan)", "中文 (Chinese Simplified)", "臺灣話 (Chinese Traditional)","Hrvatski (Croatian)","Čeština (Czech)","Nederlands (Dutch)","English (English)","Suomi (Finnish)","Français (French)","ភាសាខ្មែរ (Khmer)","Deutsch (German)","Galego (Galician)","ελληνικά (Greek)","עברית (Hebrew)","हिंदी (Hindi)","Magyar (Hungarian)","Bahasa Indonesia (Indonesian)","Italiano (Italian)","日本語 (Japanese)","ສ​ປ​ປ​ລາວ (Lao)","Latviešu valoda (Latvian)","فارسی (Persian)","Polszczyzna (Polish)","Português (Portuguese Brazil)","Português (Portuguese Portugal)","Românește (Romanian)","Русский (Russian)","Српски (Serbian Cyrillic)","Slovenčina (Slovak)","Slovenščina (Slovenian)","Español (Spanish)","Svenska (Swedish)","Türkçe (Turkish)","Українська (Ukrainian)","اُردُو‎ (Urdu)"]


#언어종류 반복
for language in languages:
    
#셋팅
    wd.find_element(By.ID, "it.feio.android.omninotes:id/settings").click()

#인터페이스
    wd.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout').click()

#언어
    wd.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout').click()

#현재 지정된 언어로 바꾸기
    wd.find_element(By.XPATH, f"//android.widget.CheckedTextView[@text='{language}']").click()

# 1회성 동의
    if language == "العربية (Arabic)":
        time.sleep(delay_seconds)  # 작업 간  딜레이
        wd.find_element(By.ID, "it.feio.android.omninotes:id/md_buttonDefaultPositive").click()


#다시 영어로


#wd.find_element(By.ID, "it.feio.android.omninotes:id/settings").click()

#wd.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout').click()

#wd.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout').click()

#wd.find_element(By.XPATH, f"//android.widget.CheckedTextView[@text='English (English)']").click()

        




