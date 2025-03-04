# playwright install - Chromium, Firefox, Webkit
# playwright codegen url - inspector
# locator - Role, Text, Label, Placeholder, AltText, Title, TestId
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright : Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    expect(page.get_by_text("Student Registration Form")).to_be_visible()
    firstName = page.get_by_role("textbox", name="First Name")
    firstName.click()
    firstName.type("Wooyoung")
    lastName=page.get_by_role("textbox", name="Last Name")
    lastName.click()
    lastName.type("CHOI")
    email = page.get_by_role("textbox", name="name@example.com")
    email.click()
    email.type("email@naver.com")
    expect(email).to_have_value("email@naver.com")
    page.locator("#dateOfBirthInput").click()
    page.get_by_role("option", name="Choose Wednesday, March 12th,").click()

    time.sleep(3)
    context.close()
    browser.close()
#
# with sync_playwright() as playwright:
#     test_run(playwright)
