## TASK_1
# 🏛️ Court-Data Fetcher & Mini-Dashboard
Get Indian court case metadata and orders with just a few clicks. This web app scrapes public court portals based on user input and renders structured results on a clean dashboard.

# ⚙️ Court Target
Delhi High Court → https://delhihighcourt.nic.in

Chosen for consistent structure and scrape-ability. If layout issues occur, we fail gracefully with helpful feedback.

# 🚀 Features
- 🔍 Case Search: Input Case Type, Number, Filing Year — we do the rest
- 📁 Metadata Extraction: Get parties, filing date, next hearing, and case status
- 📎 Order Links: Shows latest PDF order/judgment file with download button
- 📊 Dashboard: Neat results layout — built for clarity, not court complexity
- 🧾 Storage: Every query is logged in SQLite along with raw HTML responses
- 🛠️ Robust Error Handling: Friendly alerts for invalid cases or site downtime


## 🏛️ Court-Data Fetcher & Mini-Dashboard

A lightweight tool to fetch case metadata and latest judgments from the Delhi High Court website using Playwright automation and a simple web dashboard.

---

### 🚀 Setup Instructions

#### 1. Clone the Repository
git clone https://github.com/ShubhamBhosale0264/Internship_Task_TAR.git
cd court-data-fetcher

# 2. Create & Activate Virtual Environment
python -m venv jenv
jenv/bin/activate

#### 3. Install Dependencies
pip install -r requirements.txt

#### 4. Install Playwright Browsers
playwright install

# ▶️ Run the Project
python app.py

Visit `http://localhost:5000` in your browser to access the dashboard.

---

### 📦 Features
- Form-based input for Case Type, Number, and Filing Year
- Scrapes metadata and latest judgment/order link
- Stores queries and raw HTML in SQLite
- Displays parsed results with download option
- Handles errors and CAPTCHA gracefully

---

Let me know if you'd like a version with badges, screenshots, or a longer description for GitHub!



# Add .env:
BASE_URL=https://delhihighcourt.nic.in
DB_PATH=./db/court_queries.db


# Run:
python app.py



# 🧠 CAPTCHA Bypass Strategy
Delhi High Court uses hidden token fields but no image CAPTCHA.:
- Emulate tokens via Playwright’s form autofill
- Wait for async DOM renders before parsing
- Retry failed attempts with randomized user-agents
No illegal bypasses — just smart automation.

# 🧯 Debug Log
| Issue | Diagnosis | Fix | 
| Page stalls or goes blank | Dynamic JS loads block scraping | Added wait_for_selector() and fallback retries | 
| Case not found | Incorrect form field name | Validated input fields and improved error message | 
| PDF links missing | AJAX content not available via raw HTML | Used Playwright to capture full page before parsing | 
| SQLite locked error | Multiple threads clashed on insert | Implemented connection pooling and mutex locking | 



# 🌈 Tech Stack
- Frontend uses HTML and Bootstrap for layout and styling.
- Backend relies on Python Flask to handle routes and logic.
- Scraping is performed using Playwright for automation and BeautifulSoup for content parsing.
- Database stores data in SQLite for lightweight management.
- Additional tools include dotenv for managing environment variables, logging for debugging, and a PDF parser to extract information from documents.
## note 

I utilized Microsoft Copilot as a development aid to troubleshoot issues and structure the application in a professional manner. I also leveraged its suggestions to create a clear and engaging README file, incorporating relevant emoticons for better presentation. This process not only enhanced the overall quality and presentation of the project but also helped me strengthen my prompt engineering skills and accelerate the rapid development of the application.


# 📹 Demo Video
Watch full end-to-end flow: [https://1drv.ms/v/c/d24deb8ce0c645ad/Eejkhc5rGFpMhmGO53oIiuoBCVgf_bYK9qC6FT4rjM56hA]
# 🖼️ SnapShot
![Dashboard Preview](SnapShot.png)






TASK2
# 📎 Note:
This task may not behave exactly as described, due to WhatsApp media token expiry or sandbox limitations.
📦 I’ve attached the workflow.json for reference 
I was Not able to complete this task as i Was not familier with n8n . but ill surely learn the n8n automation to help organisation as required 
I have also added snapshot and My Workflow.josn file of the Workflow which i have created as per my understanding
