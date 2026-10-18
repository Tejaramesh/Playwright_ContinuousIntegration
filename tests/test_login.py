from playwright.sync_api import sync_playwright,expect

def test_login():
    with sync_playwright() as p:
        browser=p.chromium.launch()
        page=browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        page.fill('input[id="email"]',"demo@demo.com")
        page.fill('input[id="password"]',"demo")
        login_btn=page.locator("button[id='loginBtn']")
        expect(login_btn).to_be_visible()
        expect(login_btn).to_be_enabled()
        login_btn.click()
        browser.close()