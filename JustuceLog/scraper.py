from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def fetch_case_details_playwright(case_type, case_number, filing_year):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Go to the search page
        page.goto("https://dhccaseinfo.nic.in/pcase/guiCaseWise.php")
        page.wait_for_selector('select[name="type"]', timeout=90000)  


        # Fill in form fields
        page.select_option('select[name="type"]', case_type)
        page.fill('input[name="num"]', str(case_number))
        page.fill('input[name="year"]', str(filing_year))

        # Click the submit button
        page.click('input[type="submit"]')

        # Wait for navigation and load content
        page.wait_for_load_state('networkidle')
        content = page.content()
        browser.close()

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    parties_tag = soup.find('div', id='parties')
    parties = parties_tag.text.strip() if parties_tag else "Parties info not found"

    hearing_tag = soup.find('span', id='hearingDate')
    hearing = hearing_tag.text.strip() if hearing_tag else "Hearing date not found"

    pdf_tag = soup.find('a', string='Download Order')
    pdf_link = pdf_tag['href'] if pdf_tag else "PDF link not found"

    return {
        'parties': parties,
        'hearing': hearing,
        'pdf_link': pdf_link
    }


