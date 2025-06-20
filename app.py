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
        st.error(f"Error loading default certificate: {e}")
        return None

# Remove the deprecation warning with custom CSS
st.markdown("""
<style>
    /* Hide Streamlit deprecation warnings */
    .stAlert > div[data-testid="stAlert"] {
        display: none !important;
    }
    
    /* Hide the default Streamlit padding and margins */
    .main > div {
        padding-top: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    
    /* Remove default container padding */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: none;
    }
    
    .main-header {
        background: #0056D3;
        padding: 12px 0;
        margin: -1rem -1rem 0rem -1rem;
        position: relative;
    }
    
    .header-content {
        max-width: 1200px;
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
        font-family: 'OpenSans', sans-serif;
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
        border-bottom: 1px solid #e1e1e1;
        margin: 0rem -1rem 0rem -1rem;
    }
    
    .nav-items {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: flex-start;
        padding: 0 24px;
        gap: 40px;
        font-size: 16px;
        color: #666;
        font-weight: 400;
    }
    
    .nav-item {
        padding: 8px 0;
        border-bottom: 3px solid transparent;
        cursor: pointer;
    }
    
    .nav-item.active {
        border-bottom: 3px solid #0056D3;
        color: #0056D3;
        font-weight: 500;
    }
    
    .main-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 40px 24px;
    }
    
    .breadcrumb {
        font-size: 14px;
        color: #666;
        margin-bottom: 20px;
    }
    
    .specialization-title {
        font-size: 48px;
        font-weight: 400;
        color: #1f1f1f;
        margin-bottom: 40px;
        font-family: 'Source Sans Pro', sans-serif;
        line-height: 1.1;
    }
    
    .main-layout {
        display: flex;
        gap: 60px;
        align-items: flex-start;
    }
    
    .left-content {
        flex: 2;
    }
    
    .right-content {
        flex: 1;
        position: sticky;
        top: 20px;
        min-width: 400px;
    }
    
    .completion-banner {
        background: linear-gradient(135deg, #e8f4fd 0%, #d1e7f8 100%);
        border-radius: 8px;
        padding: 32px;
        margin-bottom: 40px;
        position: relative;
    }
    
    .completion-header {
        display: flex;
        align-items: center;
        margin-bottom: 16px;
    }
    
    .checkmark {
        background: #00C851;
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
    }
    
    .completion-text {
        font-size: 24px;
        font-weight: 600;
        color: #1f1f1f;
    }
    
    .completion-date {
        font-size: 18px;
        color: #1f1f1f;
        margin: 10px 0 16px 0;
        font-weight: 500;
    }
    
    .completion-hours {
        font-size: 16px;
        color: #666;
        margin-bottom: 20px;
    }
    
    .verification-text {
        font-size: 16px;
        color: #666;
        line-height: 1.5;
    }
    
    .specialization-card {
        background: white;
        border: 1px solid #e1e1e1;
        border-radius: 8px;
        padding: 0;
        margin-bottom: 40px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .university-header {
        display: flex;
        align-items: center;
        padding: 24px;
        border-bottom: 1px solid #e1e1e1;
    }
    
    .university-logo {
        width: 56px;
        height: 56px;
        background: #CC0033;
        color: white;
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 24px;
        margin-right: 16px;
        font-family: 'Arial', sans-serif;
    }
    
    .course-details h2 {
        color: #0056D3;
        font-size: 20px;
        font-weight: 600;
        margin: 0 0 6px 0;
        text-decoration: underline;
        cursor: pointer;
    }
    
    .university-name {
        color: #666;
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
        color: #666;
        font-size: 16px;
    }
    
    .enroll-btn {
        background: #0056D3;
        color: white;
        padding: 14px 32px;
        border: none;
        border-radius: 4px;
        font-weight: 600;
        cursor: pointer;
        width: calc(100% - 48px);
        margin: 0 24px 24px 24px;
        font-size: 16px;
    }
    
    .skills-section {
        padding: 24px;
        border-top: 1px solid #e1e1e1;
        background: #fafafa;
    }
    
    .skills-title {
        font-size: 14px;
        font-weight: 700;
        color: #666;
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
        color: #666;
        font-weight: 400;
    }
    
    .courses-section {
        margin-top: 40px;
    }
    
    .courses-header {
        font-size: 32px;
        font-weight: 400;
        color: #1f1f1f;
        margin-bottom: 12px;
    }
    
    .courses-subtitle {
        font-size: 16px;
        color: #666;
        margin-bottom: 32px;
    }
    
    .course-item {
        background: white;
        border: 1px solid #e1e1e1;
        border-radius: 8px;
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
        color: #1f1f1f;
        margin-bottom: 12px;
        line-height: 1.3;
    }
    
    .course-meta {
        color: #666;
        font-size: 14px;
        margin-bottom: 8px;
    }
    
    .course-instructor {
        color: #666;
        font-size: 14px;
        margin-bottom: 8px;
    }
    
    .course-completion {
        color: #666;
        font-size: 14px;
        margin-bottom: 12px;
    }
    
    .course-duration {
        color: #666;
        font-size: 14px;
        margin-bottom: 16px;
    }
    
    .view-certificate-link {
        color: #0056D3;
        font-size: 14px;
        text-decoration: underline;
        cursor: pointer;
    }
    
    .certificate-container {
        position: sticky;
        top: 20px;
    }
    
    .certificate-preview {
        border: 1px solid #d1d1d1;
        border-radius: 8px;
        overflow: hidden;
        background: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        width: 100%;
        max-width: 400px;
    }
    
    .certificate-image {
        width: 100%;
        height: auto;
        display: block;
    }
    
    .upload-placeholder {
        padding: 80px 20px;
        text-align: center;
        background: #f8f9fa;
        border: 2px dashed #dee2e6;
        border-radius: 8px;
        color: #6c757d;
        width: 100%;
        max-width: 400px;
    }
    
    .upload-icon {
        font-size: 64px;
        margin-bottom: 20px;
        color: #dee2e6;
    }
    
    .upload-text {
        font-size: 18px;
        margin-bottom: 8px;
        font-weight: 500;
    }
    
    .upload-subtext {
        font-size: 14px;
        color: #6c757d;
    }
    
    .certificate-status {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 12px 20px;
        border-radius: 4px;
        margin-bottom: 20px;
        font-size: 14px;
        text-align: center;
        width: 100%;
        max-width: 400px;
    }
    
    @media (max-width: 1024px) {
        .main-layout {
            flex-direction: column;
            gap: 40px;
        }
        
        .right-content {
            position: static;
            min-width: auto;
        }
        
        .specialization-title {
            font-size: 36px;
        }
        
        .certificate-container {
            position: static;
        }
    }
    
    @media (max-width: 768px) {
        .main-content {
            padding: 20px 16px;
        }
        
        .header-content, .nav-items {
            padding: 0 16px;
        }
        
        .specialization-title {
            font-size: 28px;
        }
        
        .completion-text {
            font-size: 20px;
        }
        
        .skills-grid {
            gap: 8px;
        }
        
        .skill-tag {
            font-size: 12px;
            padding: 6px 12px;
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

# Main content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Breadcrumb
st.markdown('<div class="breadcrumb">Specialization Certificate</div>', unsafe_allow_html=True)

# Specialization title
st.markdown('<h1 class="specialization-title">Healthcare Organization Operations</h1>', unsafe_allow_html=True)

# Main layout with proper positioning
st.markdown('<div class="main-layout">', unsafe_allow_html=True)

# Left content
st.markdown('<div class="left-content">', unsafe_allow_html=True)

# Completion banner
st.markdown(f"""
<div class="completion-banner">
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
""", unsafe_allow_html=True)

# Specialization info card
st.markdown(f"""
<div class="specialization-card">
    <div class="university-header">
        <div class="university-logo">R</div>
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

st.markdown('</div>', unsafe_allow_html=True)  # Close left content

# Right content - Certificate (positioned correctly)
st.markdown('<div class="right-content">', unsafe_allow_html=True)
st.markdown('<div class="certificate-container">', unsafe_allow_html=True)

# Certificate display logic
certificate_to_display = None
display_message = ""

if certificate_option == "Use Default Certificate":
    certificate_to_display = load_default_certificate()
    if certificate_to_display:
        display_message = "✅ Default Certificate Loaded"
    else:
        display_message = "⚠️ Default certificate not found"
elif uploaded_certificate is not None:
    try:
        certificate_to_display = Image.open(uploaded_certificate)
        display_message = "✅ Custom Certificate Uploaded"
    except Exception as e:
        display_message = f"❌ Error loading uploaded certificate: {e}"

# Show certificate status
if display_message:
    st.markdown(f'<div class="certificate-status">{display_message}</div>', unsafe_allow_html=True)

st.markdown('<div class="certificate-preview">', unsafe_allow_html=True)

# Display certificate or placeholder
if certificate_to_display is not None:
    st.image(certificate_to_display, use_container_width=True, caption=f"{YOUR_NAME}'s Healthcare Organization Operations Certificate")
else:
    # Show placeholder when no certificate is available
    placeholder_text = "Upload Your Certificate" if certificate_option == "Upload New Certificate" else "Default Certificate Not Found"
    placeholder_subtext = "Use the sidebar to upload your certificate PNG file" if certificate_option == "Upload New Certificate" else f"Please check if {DEFAULT_CERTIFICATE_PATH} exists in the app folder"
    
    st.markdown(f"""
    <div class="upload-placeholder">
        <div class="upload-icon">📜</div>
        <div class="upload-text">{placeholder_text}</div>
        <div class="upload-subtext">{placeholder_subtext}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close certificate preview
st.markdown('</div>', unsafe_allow_html=True)  # Close certificate container
st.markdown('</div>', unsafe_allow_html=True)  # Close right content

st.markdown('</div>', unsafe_allow_html=True)  # Close main layout
st.markdown('</div>', unsafe_allow_html=True)  # Close main content

# Footer
st.markdown("""
<div style="margin-top: 80px; padding: 40px 0; text-align: center; color: #999; font-size: 12px; border-top: 1px solid #e1e1e1; background: #f8f9fa;">
    <div style="max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; padding: 0 24px;">
        <div>© 2025 Coursera Inc. All rights reserved.</div>
        <div style="display: flex; gap: 20px;">
            <span>🌐 Facebook</span>
            <span>💼 LinkedIn</span>
            <span>🐦 Twitter</span>
            <span>📺 YouTube</span>
            <span>📸 Instagram</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
