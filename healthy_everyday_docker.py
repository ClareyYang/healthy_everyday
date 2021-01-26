#!/home/fang/anaconda3/bin/python
# -*- coding: utf-8 -*-
import os
import random
import sys
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from out_every_day import click_select_list


def upload(username, password):
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    # login
    driver = webdriver.Chrome(options=option)
    # 打开网站，未登录，跳转到数字北林登陆
    driver.get(address)
    wait = WebDriverWait(driver, 60)

    # 输入账号密码，点击登陆
    elem = driver.find_element_by_id('un')
    elem.send_keys(username)
    elem = driver.find_element_by_id('pd')
    elem.send_keys(password)
    elem = wait.until(EC.element_to_be_clickable((By.ID, 'index_login_btn')))
    elem.click()

    # 登陆完成，重新输入地址进入报平安页面
    driver.get(address)

    wait.until(EC.frame_to_be_available_and_switch_to_it('formIframe'))

    click_select_list(driver, "TW1", 1)
    click_select_list(driver, "TW2", 1)
    click_select_list(driver, "TW3", 1)

    click_select_list(driver, "TW1", random.randint(2, 6))
    click_select_list(driver, "TW2", random.randint(2, 6))
    click_select_list(driver, "TW3", random.randint(2, 6))

    driver.switch_to.default_content()

    commit = wait.until(EC.element_to_be_clickable((By.ID, 'commit')))
    commit.click()
    # time.sleep(1000)
    driver.close()


if __name__ == '__main__':
    dir_name = os.path.dirname(sys.argv[0])
    address = open(os.path.join(dir_name, 'address.txt')).readline()
    user_info = open(os.path.join(dir_name, 'user_info.txt'))
    print(datetime.today())
    for i in user_info:
        p = user_info.readline().strip('\n') + '\n'
        try:
            upload(i, p)
            print(i + "uploaded")
        except UnexpectedAlertPresentException:
            print(i + "had uploaded")
