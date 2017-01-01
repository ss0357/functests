import time
import sys
from driver import browser
from selenium.webdriver.common.keys import Keys


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




def test_find_element_by_id():
    dr.get('http://www.youdao.com/')

    input_box = dr.find_element_by_id('translateContent')
    input_box.send_keys('apple')
    input_box.send_keys(Keys.ENTER)
    time.sleep(3)
    assert '苹果' in dr.page_source


def test_find_element_by_name():
    dr.get('http://www.youdao.com/')

    input_box = dr.find_element_by_name('q')
    input_box.send_keys('apple')
    input_box.send_keys(Keys.ENTER)
    time.sleep(3)
    assert '苹果' in dr.page_source


def test_find_element_by_class():
    dr.get('http://fanyi.youdao.com/?keyfrom=dict2.index')

    input_box = dr.find_element_by_class_name('text')
    input_box.send_keys('apple')
    input_box.send_keys(Keys.ENTER)
    time.sleep(3)
    assert '苹果' in dr.page_source


def test_find_element_by_link_text():
    dr.get('http://www.youdao.com/')

    trans_link = dr.find_element_by_link_text('翻译')
    trans_link.click()
    time.sleep(3)
    assert dr.current_url == 'http://fanyi.youdao.com/?keyfrom=dict2.index'


def test_find_element_by_xpath():
    dr.get('http://fanyi.youdao.com/?keyfrom=dict2.index')

    input_box = dr.find_element_by_class_name('text')
    input_box.send_keys('apple')
    input_box.send_keys(Keys.ENTER)
    time.sleep(3)

    result = dr.find_element_by_xpath("//div[@class='smart_result']/p")
    assert '苹果' in result.text
