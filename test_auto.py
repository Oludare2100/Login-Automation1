
#THIS CODES USUE (from playwright.sync_api import sync_playwright)
#TO ACCESS WEBPAGE
# from playwright.sync_api import sync_playwright
# from playwright.sync_api import expect
# from Login_Page import LoginPage
# import pytest


# @pytest.mark.smoke
# def test_autovalid():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         Login_Page = LoginPage(page)
#         Login_Page.validlogin(page, "student", "password")
#         Login_Page.verifylogin(page)
#         #page.pause()
        
# @pytest.mark.regression
# def test_autoinvalidU():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         Login_Page = LoginPage(page)
#         Login_Page.invalidloginU(page, "IncorrectUser", "Password123")
#         Login_Page.verify_invalidloginU(page)
        
        
# @pytest.mark.regression
# def test_autoinvalidPSW():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         Login_Page = LoginPage(page)
#         Login_Page.invalidloginPSW(page, "student", "IcorrectPassword")
#         Login_Page.verify_invalidloginPSW(page)
        
        
        
#THIS CODES USUE (import pytest)TO ACCESS WEBPAGE
#from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from Login_Page import LoginPage
import pytest


@pytest.mark.smoke
def test_autovalid(page):
        Login_Page = LoginPage(page)
        Login_Page.validlogin(page, "student", "password")
        Login_Page.verifylogin(page)
        #page.pause()
        
@pytest.mark.regression
def test_autoinvalidU(page):
        LoginPage(page)
        Login_Page = LoginPage(page)
        Login_Page.invalidloginU(page, "IncorrectUser", "Password123")
        Login_Page.verify_invalidloginU(page)
        
        
@pytest.mark.regression
def test_autoinvalidPSW(page):
        Login_Page = LoginPage(page)
        Login_Page.invalidloginPSW(page, "student", "IcorrectPassword")
        Login_Page.verify_invalidloginPSW(page)
        #page.pause()
               
               
        # page.goto("https://practicetestautomation.com/practice-test-login/")
        # page.get_by_role("textbox", name="Username").dblclick()
        # page.get_by_role("textbox", name="Username").fill("student")
        # page.get_by_role("textbox", name="Username").press("Tab")
        # page.get_by_role("textbox", name="Password").fill("Password123")
        # page.get_by_role("button", name="Submit").click()
        # url = page.url
        # assert url == "https://practicetestautomation.com/logged-in-successfully/"  
        # expect(page.get_by_text("Congratulations student. You")).to_be_visible()
        # expect(page.get_by_role("link", name="Log out")).to_be_visible()

        #page.pause()
        
# def test_autoinvalidU():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         Login_Page = LoginPage(page)
#         Login_Page.invalidloginU(page, "IncorrectUser", "Password123")
#         #Login_Page.verify_login(page)
        
        # page.goto("https://practicetestautomation.com/practice-test-login/")
        # page.get_by_role("textbox", name="Username").click()
        # page.get_by_role("textbox", name="Username").click()
        # page.get_by_role("textbox", name="Username").fill("IncorrectUser")
        # page.get_by_role("textbox", name="Username").press("Tab")
        # page.get_by_role("textbox", name="Password").fill("Password123")
        # page.get_by_role("button", name="Submit").click()
        # expect(page.locator("#error")).to_be_visible()
        # expect(page.locator("#error")).to_have_text("Your username is invalid!")
        #page.pause()
        
# def test_autoinvalidPSW():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         page.goto("https://practicetestautomation.com/practice-test-login/")
#         page.get_by_role("textbox", name="Username").click()
#         page.get_by_role("textbox", name="Username").fill("student")
#         page.get_by_role("textbox", name="Password").click()
#         page.get_by_role("textbox", name="Password").fill("IcorrectPassword")
#         page.get_by_role("button", name="Submit").click()
#         expect(page.locator("#error")).to_be_visible()
#         expect(page.locator("#error")).to_have_text("Your password is invalid!")
      

#         #page.pause()