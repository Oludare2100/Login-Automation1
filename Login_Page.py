from playwright.sync_api import expect
class LoginPage:
    def __init__(self, page):
        self.page = page
        
    def validlogin(self, page, username, password): 
        self.page = page
        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.get_by_role("textbox", name="Username").dblclick()
        page.get_by_role("textbox", name="Username").fill("student")
        page.get_by_role("textbox", name="Username").press("Tab")
        page.get_by_role("textbox", name="Password").fill("Password123")
        page.get_by_role("button", name="Submit").click()
        
        
    def verifylogin(self, page):
        url = page.url
        assert url == "https://practicetestautomation.com/logged-in-successfully/"  
        expect(page.get_by_text("Congratulations student. You")).to_be_visible()
        expect(page.get_by_role("link", name="Log out")).to_be_visible()
        
    def invalidloginU(self, page, username, password):
        self.page = page
        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.get_by_role("textbox", name="Username").click()
        page.get_by_role("textbox", name="Username").click()
        page.get_by_role("textbox", name="Username").fill("IncorrectUser")
        page.get_by_role("textbox", name="Username").press("Tab")
        page.get_by_role("textbox", name="Password").fill("Password123")
        page.get_by_role("button", name="Submit").click()
        
        
    def verify_invalidloginU(self, page):
        self.page = page
        URL = page.url
        expect(page.locator("#error")).to_be_visible()
        expect(page.locator("#error")).to_have_text("Your username is invalid!")
        
        
    def invalidloginPSW(self, page, username, password):
        self.page = page
        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.get_by_role("textbox", name="Username").click()
        page.get_by_role("textbox", name="Username").fill("student")
        page.get_by_role("textbox", name="Password").click()
        page.get_by_role("textbox", name="Password").fill("IcorrectPassword")
        page.get_by_role("button", name="Submit").click()
        
    def verify_invalidloginPSW(self, page):
        self.page = page
        URL = page.url
        expect(page.locator("#error")).to_be_visible()
        expect(page.locator("#error")).to_have_text("Your password is invalid!")