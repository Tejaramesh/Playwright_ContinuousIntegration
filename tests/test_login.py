from playwright.sync_api import sync_playwright,expect
import pytest


@pytest.mark.parametrize("pw_browser",["chromium","firefox","webkit"])
def test_login(pw_browser):
    with sync_playwright() as p:
        browser=getattr(p,pw_browser).launch(headless=False,slow_mo=0)
        page=browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        page.fill('input[id="email"]',"demo@demo.com")
        page.fill('input[id="password"]',"demo")
        login_btn=page.locator("button[id='loginBtn']")
        expect(login_btn).to_be_visible()
        expect(login_btn).to_be_enabled()
        login_btn.click()
        browser.close()