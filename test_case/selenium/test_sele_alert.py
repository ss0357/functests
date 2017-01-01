import time
import sys
import pytest
import selenium
from driver import browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def setup_module(module):
    print ("setup_module      module:%s" % module.__name__)
    global dr
    dr = browser()

def teardown_module(module):
    print ("teardown_module   module:%s" % module.__name__)
    dr.quit()

def setup_function(function):
    print ("setup_function    function:%s" % function.__name__)

def teardown_function(function):
    print ("teardown_function function:%s" % function.__name__)



def test_alert_accept():
    dr.get('http://www.baidu.com/')
    setup_link = dr.find_element_by_partial_link_text('设置')

    ActionChains(dr).move_to_element(setup_link).perform()
    time.sleep(2)
    search_setup_link = dr.find_element_by_partial_link_text('搜索设置')
    search_setup_link.click()
    time.sleep(2)
    dr.find_element_by_class_name('prefpanelgo').click()
    time.sleep(2)
    dr.switch_to_alert().accept()
