# -*- coding:utf-8 -*-
# !/usr/bin/python
""""
该页面主要保存一些公用的方法
"""
__author__='wancaihong'
__date__='2018/9/27 21:32'

from selenium import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote import switch_to

class PublicMethod(object):
    """
    the main class of wubot framework, the web automate test framework bassed
    on selenium, making easy to use.
    """

    def __init__(self, browser='firefox'):
        """
        Run class initialization method, the default driver is Firefox browser
        Also, you can pass the parameter to other browser, i.e. "Chrome", "internet explorer"
         or "ie", "Opera" and so on.
        """
        if browser == 'firefox' or browser == 'ff':
            driver = webdriver.Firefox()
        elif browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'internet explorer' or browser == 'ie':
            driver = webdriver.Ie()
        elif browser == 'opera':
            driver = webdriver.Opera()
        elif browser == 'safari':
            driver = webdriver.Safari()
        elif browser == 'phantomjs':
            driver = webdriver.PhantomJS()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s browser, you should enter 'firefox','ff','chrome','internet explorer','ie','opera','safari'." % browser)

    def wait_element_by_name(self, name, timeout=5):
        """
       Wait.
       """
        try:
            element = WebDriverWait(self, timeout).until(
                lambda x: x.find_element_by_name(name))
        except TimeoutException:
            element = None
        return element

    def wait_elements_by_name(self, name, timeout=5):
        """
       Wait.
       """
        try:
            elements = WebDriverWait(self, timeout, ignored_exceptions=NoSuchElementException).until(
            lambda e: e.find_elements_by_name(name)
            if e.find_elements_by_name(name)[0].is_displayed() else False)
        except TimeoutException:
            elements = []
        return elements

    def get_element(self, selector):
        """
        find the the element, and return the element
        Usage:
        driver.get_element("id>>>username")
        """
        _wait_element_localed(self.driver, selector)
        element = self.driver.find_element(*_selector_to_by(selector))

        return element

    def get_elements(self, selector):
        """
        find the the element, and return the element
        Usage:
        driver.get_element("id>>>username")
        """
        _wait_element_localed(self.driver, selector)
        elements = self.driver.find_elements(*_selector_to_by(selector))

        return elements

    def open_link(self, url):
        """
        open target url
        Usage:
        driver.open_link("172.0.0.1:8000")
        """
        self.driver.get(url)

    def max_window(self):
        """
        Set browser window maximize
        Usage:
        driver.max_window
        """
        self.driver.maximize_window()

    def set_window(self, wide, high):
        """
        Set browser window winde and high
        Usage:
        driver.set_window(wide, high)
        """
        self.driver.set_window_size(wide, high)

    def enter(self, selector, text):
        """
        type text into the selected element。
        Usage:
        driver.type("id>>>username", "test")
        """
        try:
            _wait_element_localed(self.driver, selector)
            element = self.get_element(selector)
            element.send_keys(text)
        except:
            raise NoSuchElementException("未找到对应的元素")

    def clear(self, selector):
        """
        Clear the content of the input box
        Usage:
        driver.clear("id>>>username")
        """
        _wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        element.clear()

    def clear_enter(self, selector, text):
        """
        Clear text and enter new text into element
        Usage:
        driver.cleat_enter("id>>>username", "test")
        """
        _wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        element.clear()
        element.click()
        element.send_keys(text)

    def click(self, selector):
        """
        click the ang element can be clicked, like: text, image, check box, button. radio button etc...
        Usage:
        driver.click("id>>>username")
        """
        _wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        element.click()

    def right_click(self, selector):
        """
        Right clcik element
        Usage:
        driver.right_click("id>>>username")
        """
        _wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        ActionChains(self.driver).context_click(element).perform()

    def double_click(self, selector):
        """
        Double click element
        Usage:
        driver.double_click("id>>>username")
        """
        _wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        ActionChains(self.driver).double_click(element)

    def clik_link_text(self, text):
        """
        click the link text element
        Usage:
        driver.click_text("测试")
        """
        self.driver.find_element_by_partial_link_text(text)

    def drag_and_drop(self, source_selector, target_selector):
        """
        Drags the source_selector element a certain distance and then drop it.
        Usage:
        driver.drag_and_drop("id>>>username", "id>>>password")
        """
        _wait_element_localed(self.driver, source_selector)
        source = self.get_element(source_selector)
        _wait_element_localed(self.driver, target_selector)
        target = self.get_element(target_selector)
        ActionChains(self.driver).drag_and_drop(source, target)

    def close(self):
        """
        close the window
        Usage:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        Quit the driver and close all the windows
        Usage:
        driver.quit
        """
        self.driver.quit()

    def submit(self, selector):
        """
        Submit the form
        Usage:
        driver.submit("class>>>submit")
        """
        _wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        element.submit()

    def F5(self):
        """
        Refresh the current page
        Usage:
        driver.F5()
        """
        self.driver.refresh()

    def execute_js(self, script):
        """
        Execute JavaScript script in the current window/frame
        Usage:
        driver.execute_js("var q=document.documentElement.scrollTop=0")
        """
        self.driver.execute_script(script)

    def get_attribute(self, selector, attribute):
        """
        Get the value of an element attribute

        Usage:
        driver.get_attribute("id>>>username", "class")
        """
        _wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        attr = element.get_attribute(attribute)
        return attr

    def get_text(self, selector):
        """
        Get the text information of the element
        Usage:
        driver.get_text("id>>>username")
        """
        _wait_element_localed(self.driver, selector)
        element = self.get_element(selector)
        text = element.text
        return text

    def get_title(self):
        """
        Get current window title
        Usage:
        driver.get_title()
        """
        title = self.driver.title
        return title

    def get_url(self):
        """
        Get the URL address of the current page
        Usage:
        driver.get_url()
        """
        url = self.driver.current_url
        return url

    def is_element_display(self, selector):
        """
        Check the element Whether the element is visible to a user.
        Usage:
        driver.is_element_display("id>>>username")
        """
        return True if self.get_element(selector).is_displayed() else False

    def wait(self, seconds):
        """
        Implicitly wait.All elements on the page.
        Usage:
        driver.wait(10)
        """
        self.driver.implicitly_wait(seconds)

    def accept_alert(self):
        """
        Accept warning box
        Usage:
        driver.accept_alert()
        """
        self.driver.switch_to_alert().accept()

    def dismiss_alert(self):
        """
        Dismiss the alert
        Usage:
        driver.dismiss_alert()
        """
        self.driver.switch_to_alert().dismiss()

    def switch_to_frame(self, selector):
        """
        Switch to the specified frame
        Usage:
        driver.switch_to_frame("id>>>username")
        """
        _wait_element_localed(self.driver, selector)
        iframe_element = self.get_element(selector)
        self.driver.switch_to_frame(iframe_element)

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        Usage:
        driver.switch_to_frame_out()
        """
        self.driver.switch_to.default_content()

    def open_new_window(self, selector):
        """
        Open the new window and switch to the newly opened windows
        Usage:
        driver.open_new_window("id>>>username")
        """
        current_window = self.driver.current_window_handle
        element = self.get_element(selector)
        element.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_window:
                self.driver.switch_to_window(handle)

    def open_new_tab_for_Windows(self, url):
        """
        For Windows system method , open a new tab to open new url and switch to the newly tab.
        Usage:
        driver.open_new_tab_for_Windows("https://www.baidu.com/")
        """
        ActionChains(self.driver).send_keys(Keys.CONTROL + 't').perform()
        self.driver.get(url)

    def open_new_table_for_Mac(self, url):
        """
        For MacOS method , open a new tab to open new url and switch to the newly tab.
        Usage:
        driver.open_new_tab_for_Mac("https://www.baidu.com/")
        """
        ActionChains(self.driver).send_keys(Keys.COMMAND + 't').perform()
        self.driver.get(url)

    def take_screenshot(self, filepath):
        """
        Get the current window screenshot.
        Usage:
        driver.take_screenshot('../test.png')
        """
        self.driver.get_screenshot_as_file(filepath)

    @property
    def wd(self):
        """
        Return the original driver,Can use webdriver API.
        Usage:
        driver.wd
        """
        return self.driver


def _selector_to_by(selector):
    """
    Change the selector to ('by', 'value') mode
    :param selector: "id>>>username"
    :return: ('by', 'value')
    """
    if ">>>" not in selector:
        raise NameError("selector syntax errors, lack of '>>>'")

    by = selector.split('>>>')[0]
    value = selector.split('>>>')[1]

    if by == "id":
        by = By.ID
    elif by == "name":
        by = By.NAME
    elif by == "link_text":
        by = By.LINK_TEXT
    elif by == "css" or by == "css_selector":
        by = By.CSS_SELECTOR
    elif by == "xpath":
        by = By.XPATH
    elif by == "tag" or by == "tag_name":
        by = By.TAG_NAME
    elif by == "class" or by == "class_name":
        by = By.CLASS_NAME
    elif by == "text" or by == "partial_link_text":
        by = By.PARTIAL_LINK_TEXT
    else:
        raise NameError("please enter correct element attribute, 'id','name','xpath','css','tag','class','text','link_text'.")

    return by, value


def _wait_element_localed(driver, selector, time_out=5, interval=0.2):
    """
    Wait for an element localed on DOM.
    """
    WebDriverWait(driver, time_out, interval).until(
        EC.presence_of_element_located(_selector_to_by(selector)))

if __name__ == "__main__":
    driver = PublicMethod('firefox')
