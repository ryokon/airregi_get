import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select

args = sys.argv
year = args[1]
month = args[2].zfill(2)
date_start = args[3]
date_end = args[4]

driver = webdriver.Chrome(executable_path="/Users/ryokon/Desktop/dev/chromedriver")

login_url = "https://connect.airregi.jp/login?client_id=ARG&redirect_uri=https%3A%2F%2Fconnect.airregi.jp%2Foauth%2Fauthorize%3Fclient_id%3DARG%26redirect_uri%3Dhttps%253A%252F%252Fairregi.jp%252FCLP%252Fview%252FcallbackForPlfLogin%252Fauth%26response_type%3Dcode"
login_user_name = os.environ["air_user"]
login_user_passwd = os.environ["air_pass"]

#go to login website
driver.get(login_url)

#go to username form
user_name = driver.find_element_by_id('account')
user_name.send_keys(login_user_name)

#go to password form
user_passwd = driver.find_element_by_id('password')
user_passwd.send_keys(login_user_passwd)

#click login button
try:
  driver.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div[2]/div[4]/input').click()
  driver.implicitly_wait(2)
except:
  print('airレジへのログインに失敗しました。処理を終了します。')
  sys.exit(-1)
else:
  print('airレジへのログインに成功しました。')

#日別売上タブクリック
try:
  driver.find_element_by_xpath('//*[@id="btn-sales-day"]/a').click()
  driver.implicitly_wait(2)
except:
  print('日別売上タブのクリックに失敗しました。処理を終了します。')
  sys.exit(-1)

#時間別に変更
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[2]/div').click()
element = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[2]/div/select')
Select(element).select_by_value("H")
driver.implicitly_wait(2)

#年を選択
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[3]/div[1]').click()
element = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[3]/div[1]/select')
Select(element).select_by_value(year)
driver.implicitly_wait(2)

#月を選択
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[3]/div[2]').click()
element = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[3]/div[2]/select')
Select(element).select_by_value(month)
driver.implicitly_wait(2)

#選択した日付の間をループ
date_start_int = int(date_start)
date_end_int = int(date_end) + 1
date_now = date_start

for date in range(date_start_int, date_end_int):
    date_now = date_now.zfill(2)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[3]/div[3]').click()
    sleep (1)

    element = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[3]/div[3]/select')
    Select(element).select_by_value(date_now)
    sleep (1)
    #driver.implicitly_wait(5)

    #「表示する」ボタンクリック
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[4]/button').click()
    sleep (1)
    #driver.implicitly_wait(5)

    #「csvデータをダウンロードする」ボタンクリック
    driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/button').click()
    sleep (1)
    #driver.implicitly_wait(5)

    #「売上集計」ボタンクリック
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/button').click()
    sleep (1)
    #driver.implicitly_wait(5)

    date_now = int(date_now) + 1
    date_now = str(date_now)


driver.close()
driver.quit()
