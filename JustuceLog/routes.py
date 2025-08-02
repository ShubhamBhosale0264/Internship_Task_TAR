from flask import Flask, render_template, request
from scraper import fetch_case_details_playwright
from db import log_query

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    data = fetch_case_details_playwright(case_type, case_number, filing_year)
    log_query(case_type, case_number, filing_year, data['raw_html'])

    return render_template('result.html', data=data)