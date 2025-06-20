import streamlit as st
from datetime import datetime
import base64
from PIL import Image
import io
import os

# Page configuration
st.set_page_config(
    page_title="Healthcare Organization Operations - Coursera",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 🎯 CUSTOMIZE YOUR DETAILS HERE ONLY
# ==========================================
# Replace with your details:

YOUR_NAME = "Ranjana Jha"
YOUR_COMPLETION_DATE_SPEC = "June 15, 2025"
YOUR_COMPLETION_DATE_1 = "June 13, 2025"
YOUR_COMPLETION_DATE_2 = "June 14, 2025"
YOUR_COMPLETION_DATE_3 = "June 15, 2025"
YOUR_COMPLETION_DATE_4 = "June 15, 2025"
DEFAULT_CERTIFICATE_PATH = "ranjanaHealthCare.png"
RUTGERS_LOGO_PATH = "rutgers_university_logo.png"

# Certificate upload section
st.sidebar.title("🎓 Certificate Options")
st.sidebar.markdown("Choose how to display your certificate:")

certificate_option = st.sidebar.radio(
    "Certificate Display Option",
    ["Use Default Certificate", "Upload New Certificate"],
    help="Choose to use your default certificate or upload a new one"
)

uploaded_certificate = None
if certificate_option == "Upload New Certificate":
    uploaded_certificate = st.sidebar.file_uploader(
        "Choose your certificate PNG file", 
        type=['png', 'jpg', 'jpeg'],
        help="Upload your certificate image (PNG/JPG format)"
    )

# Function to load default certificate
@st.cache_data
def load_default_certificate():
    """Load the default certificate image"""
    try:
        if os.path.exists(DEFAULT_CERTIFICATE_PATH):
            return Image.open(DEFAULT_CERTIFICATE_PATH)
        else:
            return None
    except Exception as e:
        return None

# Function to load Rutgers logo
@st.cache_data
def load_rutgers_logo():
    """Load the Rutgers university logo"""
    try:
        if os.path.exists(RUTGERS_LOGO_PATH):
            return Image.open(RUTGERS_LOGO_PATH)
        else:
            return None
    except Exception as e:
        return None

# Custom CSS for fully responsive Coursera styling
st.markdown("""
<style>
    /* Hide Streamlit default elements and warnings */
    .main > div {
        padding-top: 0rem;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAlert {display: none;}
    .stSuccess {display: none;}
    .stInfo {display: none;}
    .stWarning {display: none;}
    .stError {display: none;}
    
    /* Base responsive variables */
    :root {
        --max-width: 1200px;
        --sidebar-width: 280px;
        --border-radius: 8px;
        --primary-blue: #0056D3;
        --rutgers-red: #CC0033;
        --success-green: #00C851;
        --text-primary: #1f1f1f;
        --text-secondary: #666;
        --border-color: #e1e1e1;
        --background-light: #fafafa;
        --gradient-bg: linear-gradient(135deg, #e8f4fd 0%, #d1e7f8 100%);
    }
    
    .main-header {
        background: var(--primary-blue);
        padding: 12px 0;
        margin: -1rem -1rem 0rem -1rem;
        position: relative;
        z-index: 100;
    }
    
    .header-content {
        max-width: var(--max-width);
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 24px;
    }
    
    .coursera-logo {
        color: white;
        font-size: 28px;
        font-weight: bold;
        font-family: 'Source Sans Pro', sans-serif;
    }
    
    .header-nav {
        display: flex;
        align-items: center;
        gap: 30px;
        color: white;
        font-size: 16px;
    }
    
    .header-search {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.3);
        border-radius: 4px;
        padding: 8px 16px;
        color: white;
        width: 300px;
    }
    
    .nav-menu {
        background: white;
        padding: 8px 0;
        border-bottom: 1px solid var(--border-color);
        margin: 0rem -1rem 0rem -1rem;
    }
    
    .nav-items {
        max-width: var(--max-width);
        margin: 0 auto;
        display: flex;
        justify-content: flex-start;
        padding: 0 24px;
        gap: 40px;
        font-size: 16px;
        color: var(--text-secondary);
        font-weight: 400;
    }
    
    .nav-item {
        padding: 8px 0;
        border-bottom: 3px solid transparent;
        cursor: pointer;
        white-space: nowrap;
    }
    
    .nav-item.active {
        border-bottom: 3px solid var(--primary-blue);
        color: var(--primary-blue);
        font-weight: 500;
    }
    
    .main-content {
        max-width: var(--max-width);
        margin: 0 auto;
        padding: 40px 24px;
        background: white;
    }
    
    .breadcrumb {
        font-size: 14px;
        color: var(--text-secondary);
        margin-bottom: 16px;
    }
    
    .specialization-title {
        font-size: 48px;
        font-weight: 400;
        color: var(--text-primary);
        margin-bottom: 40px;
        font-family: 'Source Sans Pro', sans-serif;
        line-height: 1.1;
    }
    
    /* Desktop Layout - Side by side */
    .completion-section {
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 40px;
        margin-bottom: 40px;
        align-items: flex-start;
    }
    
    .completion-left {
        width: 100%;
    }
    
    .completion-right {
        width: 100%;
        position: sticky;
        top: 20px;
    }
    
    .completion-banner {
        background: var(--gradient-bg);
        border-radius: var(--border-radius);
        padding: 32px;
        margin-bottom: 40px;
        position: relative;
        display: flex;
        align-items: flex-start;
        gap: 24px;
    }
    
    .completion-header {
        display: flex;
        align-items: center;
        margin-bottom: 16px;
    }
    
    .checkmark {
        background: var(--success-green);
        border-radius: 50%;
        width: 32px;
        height: 32px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        margin-right: 16px;
        font-size: 18px;
        flex-shrink: 0;
    }
    
    .completion-text {
        font-size: 24px;
        font-weight: 600;
        color: var(--text-primary);
    }
    
    .completion-date {
        font-size: 18px;
        color: var(--text-primary);
        margin: 10px 0 16px 0;
        font-weight: 500;
    }
    
    .completion-hours {
        font-size: 16px;
        color: var(--text-secondary);
        margin-bottom: 20px;
    }
    
    .verification-text {
        font-size: 16px;
        color: var(--text-secondary);
        line-height: 1.5;
    }
    
    .certificate-container {
        background: white;
        border-radius: var(--border-radius);
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        max-width: 100%;
        position: sticky;
        top: 20px;
    }
    
    .certificate-image {
        width: 100%;
        height: auto;
        display: block;
        border-radius: var(--border-radius);
    }
    
    .specialization-card {
        background: white;
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        padding: 0;
        margin-bottom: 40px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .university-header {
        display: flex;
        align-items: center;
        padding: 24px;
        border-bottom: 1px solid var(--border-color);
    }
    
    .university-logo {
        width: 56px;
        height: 56px;
        background: var(--rutgers-red);
        color: white;
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 24px;
        margin-right: 16px;
        font-family: 'Arial', sans-serif;
        flex-shrink: 0;
    }
    
    .university-logo img {
        width: 100%;
        height: 100%;
        object-fit: contain;
        border-radius: 4px;
    }
    
    .course-details h2 {
        color: var(--primary-blue);
        font-size: 20px;
        font-weight: 600;
        margin: 0 0 6px 0;
        text-decoration: underline;
        cursor: pointer;
    }
    
    .university-name {
        color: var(--text-secondary);
        font-size: 16px;
        margin: 0;
        font-weight: 400;
    }
    
    .rating-section {
        padding: 0 24px 20px 24px;
    }
    
    .stars {
        color: #FF9800;
        font-size: 16px;
        margin-right: 12px;
    }
    
    .rating-text {
        color: var(--text-secondary);
        font-size: 16px;
    }
    
    .enroll-btn {
        background: var(--primary-blue);
        color: white;
        padding: 14px 32px;
        border: none;
        border-radius: 4px;
        font-weight: 600;
        cursor: pointer;
        width: calc(100% - 48px);
        margin: 0 24px 24px 24px;
        font-size: 16px;
        transition: background-color 0.2s ease;
    }
    
    .enroll-btn:hover {
        background: #0043A8;
    }
    
    .skills-section {
        padding: 24px;
        border-top: 1px solid var(--border-color);
        background: var(--background-light);
    }
    
    .skills-title {
        font-size: 14px;
        font-weight: 700;
        color: var(--text-secondary);
        margin-bottom: 20px;
        letter-spacing: 0.5px;
    }
    
    .skills-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
    }
    
    .skill-tag {
        background: white;
        border: 1px solid #d1d1d1;
        padding: 8px 16px;
        border-radius: 16px;
        font-size: 14px;
        color: var(--text-secondary);
        font-weight: 400;
    }
    
    .courses-section {
        margin-top: 40px;
        grid-column: 1 / -1;
    }
    
    .courses-header {
        font-size: 32px;
        font-weight: 400;
        color: var(--text-primary);
        margin-bottom: 12px;
    }
    
    .courses-subtitle {
        font-size: 16px;
        color: var(--text-secondary);
        margin-bottom: 32px;
    }
    
    .course-item {
        background: white;
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        padding: 24px;
        margin-bottom: 24px;
        transition: box-shadow 0.2s ease;
    }
    
    .course-item:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    .course-title {
        font-size: 24px;
        font-weight: 400;
        color: var(--text-primary);
        margin-bottom: 12px;
        line-height: 1.3;
    }
    
    .course-meta {
        color: var(--text-secondary);
        font-size: 14px;
        margin-bottom: 8px;
    }
    
    .course-instructor {
        color: var(--text-secondary);
        font-size: 14px;
        margin-bottom: 8px;
    }
    
    .course-completion {
        color: var(--text-secondary);
        font-size: 14px;
        margin-bottom: 12px;
    }
    
    .course-duration {
        color: var(--text-secondary);
        font-size: 14px;
        margin-bottom: 16px;
    }
    
    .view-certificate-link {
        color: var(--primary-blue);
        font-size: 14px;
        text-decoration: underline;
        cursor: pointer;
    }
    
    .footer {
        margin-top: 80px;
        padding: 40px 0;
        text-align: center;
        color: #999;
        font-size: 12px;
        border-top: 1px solid var(--border-color);
        background: #f8f9fa;
    }
    
    .footer-content {
        max-width: var(--max-width);
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 24px;
    }
    
    .footer-social {
        display: flex;
        gap: 20px;
    }
    
    /* Tablet Layout (768px - 1024px) */
    @media (max-width: 1024px) {
        .completion-section {
            grid-template-columns: 1fr;
            gap: 30px;
        }
        
        .completion-right {
            position: static;
            order: -1;
        }
        
        .certificate-container {
            position: static;
            max-width: 400px;
            margin: 0 auto;
        }
        
        .specialization-title {
            font-size: 36px;
        }
        
        .header-search {
            width: 200px;
        }
        
        .header-nav {
            gap: 20px;
        }
        
        .nav-items {
            gap: 30px;
        }
        
        .footer-content {
            flex-direction: column;
            gap: 20px;
        }
    }
    
    /* Mobile Layout (< 768px) */
    @media (max-width: 768px) {
        .main-content {
            padding: 20px 16px;
        }
        
        .header-content, .nav-items {
            padding: 0 16px;
        }
        
        .header-nav {
            display: none;
        }
        
        .nav-items {
            gap: 20px;
            overflow-x: auto;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }
        
        .specialization-title {
            font-size: 28px;
            line-height: 1.2;
        }
        
        .completion-text {
            font-size: 20px;
        }
        
        .completion-banner {
            flex-direction: column;
            text-align: center;
            padding: 24px;
        }
        
        .completion-header {
            justify-content: center;
        }
        
        .skills-grid {
            gap: 8px;
        }
        
        .skill-tag {
            font-size: 12px;
            padding: 6px 12px;
        }
        
        .course-title {
            font-size: 20px;
        }
        
        .courses-header {
            font-size: 28px;
        }
        
        .certificate-container {
            max-width: 100%;
        }
        
        .university-header {
            padding: 16px;
        }
        
        .university-logo {
            width: 48px;
            height: 48px;
            font-size: 20px;
        }
        
        .course-details h2 {
            font-size: 18px;
        }
        
        .enroll-btn {
            width: calc(100% - 32px);
            margin: 0 16px 16px 16px;
        }
        
        .skills-section {
            padding: 16px;
        }
        
        .course-item {
            padding: 16px;
        }
    }
    
    /* Small Mobile (< 480px) */
    @media (max-width: 480px) {
        .coursera-logo {
            font-size: 24px;
        }
        
        .specialization-title {
            font-size: 24px;
        }
        
        .completion-text {
            font-size: 18px;
        }
        
        .completion-banner {
            padding: 16px;
        }
        
        .university-logo {
            width: 40px;
            height: 40px;
            font-size: 18px;
            margin-right: 12px;
        }
        
        .course-details h2 {
            font-size: 16px;
        }
        
        .university-name {
            font-size: 14px;
        }
        
        .courses-header {
            font-size: 24px;
        }
        
        .course-title {
            font-size: 18px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(f"""
<div class="main-header">
    <div class="header-content">
        <div class="coursera-logo">coursera</div>
        <div class="header-nav">
            <input type="text" class="header-search" placeholder="What do you want to learn?">
            <span>Online Degrees</span>
            <span>Careers</span>
            <span>English</span>
            <span>{YOUR_NAME[0]}</span>
        </div>
    </div>
</div>

<div class="nav-menu">
    <div class="nav-items">
        <div class="nav-item active">For Individuals</div>
        <div class="nav-item">For Businesses</div>
        <div class="nav-item">For Universities</div>
        <div class="nav-item">For Governments</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Main content container
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Breadcrumb
st.markdown('<div class="breadcrumb">Specialization Certificate</div>', unsafe_allow_html=True)

# Specialization title
st.markdown('<h1 class="specialization-title">Healthcare Organization Operations</h1>', unsafe_allow_html=True)

# Main completion section with responsive grid
st.markdown('<div class="completion-section">', unsafe_allow_html=True)

# Left column - Completion banner and course info
st.markdown('<div class="completion-left">', unsafe_allow_html=True)

# Completion banner
st.markdown(f"""
<div class="completion-banner">
    <div>
        <div class="completion-header">
            <div class="checkmark">✓</div>
            <div class="completion-text">Completed by {YOUR_NAME}</div>
        </div>
        <div class="completion-date">{YOUR_COMPLETION_DATE_SPEC}</div>
        <div class="completion-hours">Approximately 2 months at 10 hours a week to complete</div>
        <div class="verification-text">
            {YOUR_NAME}'s account is verified. Coursera certifies their successful completion of Rutgers the State University of New Jersey<br>
            <strong>Healthcare Organization Operations</strong> Specialization.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Load Rutgers logo
rutgers_logo = load_rutgers_logo()

# Specialization info card with logo handling
if rutgers_logo:
    # Convert PIL image to base64 for HTML embedding
    buffered = io.BytesIO()
    rutgers_logo.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    logo_html = f'<img src="data:image/png;base64,{img_str}" alt="Rutgers University Logo">'
else:
    logo_html = 'R'  # Fallback to text

st.markdown(f"""
<div class="specialization-card">
    <div class="university-header">
        <div class="university-logo">{logo_html}</div>
        <div class="course-details">
            <h2>Healthcare Organization Operations</h2>
            <p class="university-name">Rutgers the State University of New Jersey</p>
        </div>
    </div>
    
    <div class="rating-section">
        <span class="stars">★★★★★</span>
        <span class="rating-text">4.6 (466 ratings) | 20K Students Enrolled</span>
    </div>
    
    <button class="enroll-btn">Enroll for Free</button>
    
    <div class="skills-section">
        <div class="skills-title">SKILLS YOU WILL GAIN</div>
        <div class="skills-grid">
            <div class="skill-tag">Healthcare Industry Knowledge</div>
            <div class="skill-tag">Health Systems</div>
            <div class="skill-tag">Spreadsheet Software</div>
            <div class="skill-tag">Process Design</div>
            <div class="skill-tag">Continuous Quality Improvement (CQI)</div>
            <div class="skill-tag">Process Improvement</div>
            <div class="skill-tag">Data Collection</div>
            <div class="skill-tag">Presentations</div>
            <div class="skill-tag">Health Information Management and Medical Records</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close left column

# Right column - Certificate
st.markdown('<div class="completion-right">', unsafe_allow_html=True)

# Certificate display logic - NO STATUS MESSAGES
certificate_to_display = None

if certificate_option == "Use Default Certificate":
    certificate_to_display = load_default_certificate()
elif uploaded_certificate is not None:
    try:
        certificate_to_display = Image.open(uploaded_certificate)
    except Exception:
        certificate_to_display = None

# Display certificate silently
if certificate_to_display is not None:
    st.markdown('<div class="certificate-container">', unsafe_allow_html=True)
    st.image(certificate_to_display, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close right column

# Course Certificates section
st.markdown("""
<div class="courses-section">
    <h2 class="courses-header">Course Certificates</h2>
    <p class="courses-subtitle">Earned after completing each course in the Specialization</p>
</div>
""", unsafe_allow_html=True)

# Individual courses
courses = [
    {
        "title": "Healthcare Organizations and the Health System",
        "completion_date": YOUR_COMPLETION_DATE_1,
        "duration": "4 weeks (4 lessons); 4-6 hours of learner work per lesson; total time for the course = 16 - 24 hours"
    },
    {
        "title": "Health Care Delivery in Healthcare Organizations", 
        "completion_date": YOUR_COMPLETION_DATE_2,
        "duration": "4 weeks (4 lessons); 4-6 hours of learner work per lesson; total time for the course = 16 - 24 hours"
    },
    {
        "title": "Business Process Management in Healthcare Organizations",
        "completion_date": YOUR_COMPLETION_DATE_3, 
        "duration": "4 weeks (4 lessons); 4-6 hours of learner work per lesson; total time for the course = 16 - 24 hours"
    },
    {
        "title": "Quality Improvement in Healthcare Organizations",
        "completion_date": YOUR_COMPLETION_DATE_4,
        "duration": "4 weeks (4 lessons); 4-6 hours of learner work per lesson; total time for the course = 16 - 24 hours"
    }
]

for course in courses:
    st.markdown(f"""
    <div class="course-item">
        <h3 class="course-title">{course['title']}</h3>
        <div class="course-meta">Rutgers the State University of New Jersey</div>
        <div class="course-instructor">Taught by: Margaret Kilduff, Ph.D.</div>
        <div class="course-completion">Completed by: {YOUR_NAME} by {course['completion_date']}</div>
        <div class="course-duration">{course['duration']}</div>
        <div class="view-certificate-link">View this certificate →</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close completion section
st.markdown('</div>', unsafe_allow_html=True)  # Close main content

# Footer
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <div>© 2025 Coursera Inc. All rights reserved.</div>
        <div class="footer-social">
            <span>🌐 Facebook</span>
            <span>💼 LinkedIn</span>
            <span>🐦 Twitter</span>
            <span>📺 YouTube</span>
            <span>📸 Instagram</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar info (kept minimal to not interfere with main design)
st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 Quick Info")
st.sidebar.info(f"""
**Student Name:** {YOUR_NAME}
**Specialization:** Healthcare Organization Operations
**University:** Rutgers University
**Completion Date:** {YOUR_COMPLETION_DATE_SPEC}
**Total Courses:** 4
""")

# Hide all Streamlit messages and warnings
st.markdown("""
<script>
// Hide all status messages and warnings
const hideElements = () => {
    const elementsToHide = document.querySelectorAll('.stAlert, .stSuccess, .stInfo, .stWarning, .stError, [data-testid="stAlert"]');
    elementsToHide.forEach(el => el.style.display = 'none');
};

// Run on page load and periodically
hideElements();
setInterval(hideElements, 1000);
</script>
""", unsafe_allow_html=True)