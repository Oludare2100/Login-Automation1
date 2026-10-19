
#THIS CODES USUE (from playwright.sync_api import sync_playwright)
#O ACCESS WEBPAGE
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from Login_Page import LoginPage
import pytest


@pytest.mark.smoke
def test_autovalid():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        Login_Page = LoginPage(page)
        Login_Page.validlogin(page, "student", "password")
        Login_Page.verifylogin(page)
        #page.pause()
        
@pytest.mark.regression
def test_autoinvalidU():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        Login_Page = LoginPage(page)
        Login_Page.invalidloginU(page, "IncorrectUser", "Password123")
        Login_Page.verify_invalidloginU(page)
        
        
@pytest.mark.regression
def test_autoinvalidPSW():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        Login_Page = LoginPage(page)
        Login_Page.invalidloginPSW(page, "student", "IcorrectPassword")
        Login_Page.verify_invalidloginPSW(page)
        
        
        
# #THIS CODES USUE (import pytest)TO ACCESS WEBPAGE
# #from playwright.sync_api import sync_playwright
# from playwright.sync_api import expect
# from Login_Page import LoginPage
# import pytest


# @pytest.mark.smoke
# def test_autovalid(page):
#         Login_Page = LoginPage(page)
#         Login_Page.validlogin(page, "student", "password")
#         Login_Page.verifylogin(page)
#         #page.pause()
        
# @pytest.mark.regression
# def test_autoinvalidU(page):
#         LoginPage(page)
#         Login_Page = LoginPage(page)
#         Login_Page.invalidloginU(page, "IncorrectUser", "Password123")
#         Login_Page.verify_invalidloginU(page)
        
        
# @pytest.mark.regression
# def test_autoinvalidPSW(page):
#         Login_Page = LoginPage(page)
#         Login_Page.invalidloginPSW(page, "student", "IcorrectPassword")
#         Login_Page.verify_invalidloginPSW(page)
#         page.pause()
               
               
    
        
