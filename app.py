import streamlit as st
from datetime import datetime
import base64
from PIL import Image
import io
import os

# Page configuration
st.set_page_config(
    page_title="Healthcare Organizations and the Health System - Course Certificate",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 🎯 CUSTOMIZE YOUR DETAILS HERE ONLY
# ==========================================
# Replace with your details:

YOUR_NAME = "Ranjana Jha"
YOUR_COMPLETION_DATE = "June 15, 2025"
DEFAULT_CERTIFICATE_PATH = "ranjanaHealthCare.png"  # Your certificate file

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

# ==========================================
# Rest everything stays exactly the same as original
# ==========================================

# Custom CSS to replicate exact Coursera styling
st.markdown("""
<style>
    .main > div {
        padding-top: 0rem;
    }
    
    .main-header {
        background: #0056D3;
        padding: 12px 0;
        margin: -1rem -1rem 0rem -1rem;
        position: relative;
    }
    
    .coursera-logo {
        color: white;
        font-size: 24px;
        font-weight: bold;
        text-align: left;
        font-family: 'Source Sans Pro', sans-serif;
        padding-left: 50px;
    }
    
    .nav-menu {
        background: white;
        padding: 8px 0;
        border-bottom: 1px solid #e1e1e1;
        margin: 0rem -1rem 1rem -1rem;
    }
    
    .nav-items {
        display: flex;
        justify-content: flex-start;
        padding-left: 50px;
        gap: 30px;
        font-size: 14px;
        color: #666;
        font-weight: 500;
    }
    
    .nav-item {
        padding: 5px 0;
        border-bottom: 2px solid transparent;
    }
    
    .nav-item.active {
        border-bottom: 2px solid #0056D3;
        color: #0056D3;
    }
    
    .main-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 50px;
    }
    
    .breadcrumb {
        font-size: 12px;
        color: #666;
        margin-bottom: 10px;
    }
    
    .course-title {
        font-size: 36px;
        font-weight: 400;
        color: #1f1f1f;
        margin-bottom: 30px;
        font-family: 'Source Sans Pro', sans-serif;
        line-height: 1.2;
    }
    
    .completion-card {
        background: linear-gradient(135deg, #e8f4fd 0%, #d1e7f8 100%);
        border-radius: 8px;
        padding: 30px;
        margin-bottom: 30px;
        position: relative;
    }
    
    .completion-header {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }
    
    .checkmark {
        background: #00C851;
        border-radius: 50%;
        width: 28px;
        height: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        margin-right: 12px;
        font-size: 16px;
    }
    
    .completion-text {
        font-size: 20px;
        font-weight: 600;
        color: #1f1f1f;
    }
    
    .completion-date {
        font-size: 16px;
        color: #1f1f1f;
        margin: 8px 0;
        font-weight: 500;
    }
    
    .completion-hours {
        font-size: 14px;
        color: #666;
        margin-bottom: 15px;
    }
    
    .verification-text {
        font-size: 14px;
        color: #666;
        line-height: 1.4;
    }
    
    .course-info-card {
        background: white;
        border: 1px solid #e1e1e1;
        border-radius: 4px;
        padding: 0;
        margin-bottom: 30px;
        overflow: hidden;
    }
    
    .university-header {
        display: flex;
        align-items: center;
        padding: 20px;
        border-bottom: 1px solid #e1e1e1;
    }
    
    .university-logo {
        width: 48px;
        height: 48px;
        background: #CC0033;
        color: white;
        border-radius: 2px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 20px;
        margin-right: 12px;
        font-family: 'Arial', sans-serif;
    }
    
    .course-details h3 {
        color: #0056D3;
        font-size: 16px;
        font-weight: 600;
        margin: 0 0 4px 0;
        text-decoration: underline;
        cursor: pointer;
    }
    
    .university-name {
        color: #666;
        font-size: 13px;
        margin: 0;
        font-weight: 400;
    }
    
    .rating-section {
        padding: 0 20px 15px 20px;
    }
    
    .stars {
        color: #FF9800;
        font-size: 14px;
        margin-right: 8px;
    }
    
    .rating-text {
        color: #666;
        font-size: 13px;
    }
    
    .enroll-btn {
        background: #0056D3;
        color: white;
        padding: 12px 24px;
        border: none;
        border-radius: 4px;
        font-weight: 600;
        cursor: pointer;
        width: calc(100% - 40px);
        margin: 0 20px 20px 20px;
        font-size: 14px;
    }
    
    .skills-section {
        padding: 20px;
        border-top: 1px solid #e1e1e1;
        background: #fafafa;
    }
    
    .skills-title {
        font-size: 12px;
        font-weight: 700;
        color: #666;
        margin-bottom: 15px;
        letter-spacing: 0.5px;
    }
    
    .skills-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }
    
    .skill-tag {
        background: white;
        border: 1px solid #d1d1d1;
        padding: 6px 12px;
        border-radius: 12px;
        font-size: 12px;
        color: #666;
        font-weight: 400;
    }
    
    .certificate-preview {
        border: 1px solid #d1d1d1;
        border-radius: 4px;
        overflow: hidden;
        background: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .certificate-image {
        width: 100%;
        height: auto;
        display: block;
        border-radius: 4px;
    }
    
    .upload-placeholder {
        padding: 60px 20px;
        text-align: center;
        background: #f8f9fa;
        border: 2px dashed #dee2e6;
        border-radius: 8px;
        color: #6c757d;
    }
    
    .upload-icon {
        font-size: 48px;
        margin-bottom: 16px;
        color: #dee2e6;
    }
    
    .upload-text {
        font-size: 16px;
        margin-bottom: 8px;
        font-weight: 500;
    }
    
    .upload-subtext {
        font-size: 14px;
        color: #6c757d;
    }
    
    .two-column {
        display: flex;
        gap: 40px;
        align-items: flex-start;
    }
    
    .left-column {
        flex: 1;
    }
    
    .right-column {
        flex: 1;
    }
    
    .certificate-status {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 10px 15px;
        border-radius: 4px;
        margin-bottom: 15px;
        font-size: 14px;
        text-align: center;
    }
    
    @media (max-width: 768px) {
        .two-column {
            flex-direction: column;
            gap: 20px;
        }
        
        .main-content {
            padding: 0 20px;
        }
        
        .coursera-logo, .nav-items {
            padding-left: 20px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <div class="coursera-logo">coursera</div>
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
st.markdown('<div class="breadcrumb">Course Certificate</div>', unsafe_allow_html=True)

# Two column layout
st.markdown('<div class="two-column">', unsafe_allow_html=True)

# Left column
st.markdown('<div class="left-column">', unsafe_allow_html=True)

st.markdown('<h1 class="course-title">Healthcare Organizations and the Health System</h1>', unsafe_allow_html=True)

# Completion card
st.markdown(f"""
<div class="completion-card">
    <div class="completion-header">
        <div class="checkmark">✓</div>
        <div class="completion-text">Completed by {YOUR_NAME}</div>
    </div>
    <div class="completion-date">{YOUR_COMPLETION_DATE}</div>
    <div class="completion-hours">17 hours (approximately)</div>
    <div class="verification-text">
        {YOUR_NAME}'s account is verified. Coursera certifies their successful completion of <strong>Healthcare Organizations and the Health System</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# Course info card
st.markdown(f"""
<div class="course-info-card">
    <div class="university-header">
        <div class="university-logo">R</div>
        <div class="course-details">
            <h3>Healthcare Organizations and the Health System</h3>
            <p class="university-name">Rutgers The State University of New Jersey</p>
        </div>
    </div>
    
    <div class="rating-section">
        <span class="stars">★★★★★</span>
        <span class="rating-text">4.6 (346 ratings) | 28K Students Enrolled</span>
    </div>
    
    <button class="enroll-btn">Enroll for Free</button>
    
    <div class="skills-section">
        <div class="skills-title">SKILLS YOU WILL GAIN</div>
        <div class="skills-grid">
            <div class="skill-tag">Healthcare Industry Knowledge</div>
            <div class="skill-tag">Health Systems</div>
            <div class="skill-tag">Health Administration</div>
            <div class="skill-tag">Organizational Structure</div>
            <div class="skill-tag">Organizational Strategy</div>
            <div class="skill-tag">Presentations</div>
            <div class="skill-tag">Health Care Administration</div>
            <div class="skill-tag">Microsoft PowerPoint</div>
            <div class="skill-tag">Health Care</div>
            <div class="skill-tag">Governance</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close left column

# Right column - Certificate
st.markdown('<div class="right-column">', unsafe_allow_html=True)

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
    st.image(certificate_to_display, use_column_width=True, caption=f"{YOUR_NAME}'s Certificate")
else:
    # Show placeholder when no certificate is available
    placeholder_text = "Upload Your Certificate" if certificate_option == "Upload New Certificate" else "Default Certificate Not Found"
    placeholder_subtext = "Use the sidebar to upload your certificate PNG file" if certificate_option == "Upload New Certificate" else "Please check if healthcarecertificateCare.png exists in the app folder"
    
    st.markdown(f"""
    <div class="upload-placeholder">
        <div class="upload-icon">📜</div>
        <div class="upload-text">{placeholder_text}</div>
        <div class="upload-subtext">{placeholder_subtext}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close certificate preview

st.markdown('</div>', unsafe_allow_html=True)  # Close right column
st.markdown('</div>', unsafe_allow_html=True)  # Close two-column
st.markdown('</div>', unsafe_allow_html=True)  # Close main content

# Footer
st.markdown("""
<div style="margin-top: 50px; padding: 20px 0; text-align: center; color: #999; font-size: 11px; border-top: 1px solid #e1e1e1;">
    © 2025 Coursera Inc. All rights reserved.
</div>
""", unsafe_allow_html=True)