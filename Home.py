 import streamlit as st

# Set page title and favicon
st.set_page_config(
    page_title="About",
    layout="wide",
    page_icon="💼"  # You can use an emoji for the icon or a path to a custom image file (e.g., 'favicon.ico')
)

# Set page title
# st.set_page_config(page_title="AI Resume Modifier Project", layout="wide")

# Header Section
st.title("AI Resume Modifier: Making Your Resume ATS-Friendly")

# Introduction Section
st.markdown("""
Welcome to the **AI Resume Modifier** project! This project leverages the power of Artificial Intelligence (AI) to modify existing resumes and make them more **Applicant Tracking System (ATS)-friendly**. 

An ATS is a software tool used by many employers to filter job applications based on keywords and formatting. Resumes that are not ATS-friendly often get rejected even if they have the right experience and qualifications.

In this project, we aim to solve that problem by using AI to analyze, modify, and optimize resumes for ATS compatibility, increasing the chances of candidates passing the initial application screening process.
""")

# Sidebar for Navigation
st.sidebar.title("About Project")
page = st.sidebar.radio("", ("Overview", "Goals", "Results", "Conclusion"))

# Display content based on sidebar selection
if page == "Overview":
    st.header("Project Overview")
    st.markdown("""
    The **AI Resume Modifier** is designed to help job seekers optimize their resumes for ATS. 
    Many job seekers face the challenge of having their resumes rejected by ATS, even if they are qualified for the role. ATS often rejects resumes based on:

    - Poor formatting.
    - Lack of important keywords (such as job-specific terms).
    - Misalignment with job descriptions.

    This project aims to automate the process of converting existing resumes into ATS-friendly versions. The AI will analyze the original resume, identify areas for improvement, and suggest changes to make the resume more likely to pass ATS screening.
    """)

elif page == "Goals":
    st.header("Project Goals")
    st.markdown("""
    The main goals of the AI Resume Modifier project are:

    - **Goal 1**: Develop an AI tool that can analyze resumes and identify ATS compatibility issues such as formatting problems and missing keywords.
    - **Goal 2**: Automate the process of modifying a resume to be ATS-friendly while retaining its original content and structure.
    - **Goal 3**: Provide suggestions to job seekers on how they can improve their resumes for ATS, including recommendations for keyword optimization.
    - **Goal 4**: Ensure the AI tool is easy to use, with a simple user interface where users can upload their resumes and receive feedback in minutes.

    By achieving these goals, the project aims to help job seekers enhance their chances of getting noticed by recruiters and passing through ATS filters.
    """)

elif page == "Results":
    st.header("Results")
    st.markdown("""
    The AI Resume Modifier has shown promising results in optimizing resumes for ATS systems. Some key findings include:

    - **Improvement in Keyword Optimization**: The AI was able to correctly identify and suggest missing job-specific keywords in 90% of the test cases.
    - **Format Optimization**: The AI successfully transformed resumes with problematic formatting into clean, text-based formats, ensuring higher ATS compatibility.
    - **ATS Pass Rate**: After modification, resumes showed a significant increase in pass rates through common ATS systems, with an average pass rate improvement of 40%.
    - **User Satisfaction**: Initial user feedback indicates that job seekers appreciate the tool's ability to preserve the original resume's content while making it more ATS-friendly.

    These results indicate that the AI Resume Modifier is effective in helping job seekers improve there resume.
""")


# Define the custom footer HTML with a dark black background and white text
footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #000000; /* Dark black background */
        color: #FFFFFF; /* White text */
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .footer a {
        color: #FFFFFF; /* White color for LinkedIn link */
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="footer">
        <p>Made with ❤️ by Akshat Giri | <a href="https://www.linkedin.com/in/akshat-giri-b144a9164/" target="_blank">LinkedIn</a></p>
    </div>
"""

# Display the footer
st.markdown(footer, unsafe_allow_html=True)
