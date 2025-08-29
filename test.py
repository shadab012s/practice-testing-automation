import os
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    headless = os.getenv("CI", "false").lower() == "true"
    browser = playwright.chromium.launch(headless=headless, slow_mo=500) 
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://shadab012s.github.io/PRACTISE/")
    page.get_by_role("textbox", name="Full Name").click()
    page.get_by_role("textbox", name="Full Name").fill("shsh")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("sh@yopmail.com")
    page.get_by_role("textbox", name="Department").click()
    page.get_by_role("textbox", name="Department").fill("admin")
    page.get_by_label("Role").select_option("admin")
    page.get_by_role("button", name="Submit").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
