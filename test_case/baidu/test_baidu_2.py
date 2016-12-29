import time
import sys
from driver import browser


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




def test_baidu_2_case1():
    dr.get('http://www.baidu.com')
    input_box = dr.find_element_by_id('kw')
    input_box.send_keys('pytest')
    input_box.submit()
    time.sleep(3)
    try:
        dr.find_element_by_partial_link_text('pytest: helps you write better programs')
    except:
        assert 0

def test_baidu_2_case2():
    text = dr.find_element_by_id('cp').text
    print(text)
    assert '京公网安备11000002000001号' in text
