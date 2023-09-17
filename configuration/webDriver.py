from appium import webdriver

desired_cap = {
  "appium:deviceName": "RF9RA010KYW",
  "platformName": "Android",
  "appium:appPackage": "it.feio.android.omninotes",
  "appium:appActivity": "it.feio.android.omninotes.MainActivity"
}

def cal():
  wd = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
  wd.implicitly_wait(10)
  return wd


