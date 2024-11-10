from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai

# For local
# from dotenv import load_dotenv
# load_dotenv()
# genai.configure(api_key=os.getenv("API_KEY"))

# For CLoud
genai.configure(api_key=st.secrets["API_KEY"])

# Set page title and favicon
st.set_page_config(
    page_title="Check ATS Score",
    layout="wide",
    page_icon="💼"  # You can use an emoji for the icon or a path to a custom image file (e.g., 'favicon.ico')
)

ATS_prompt = """
Task: Analyze a LaTeX resume against a specific job description.

Input:

LaTeX Resume: A LaTeX file containing the applicant's resume.
Job Description: A text document outlining the job requirements, including specific keywords, skills, and experiences.
Output:

ATS Score: A numerical score from 0 to 100, indicating the applicant's fit for the job.
Keyword Match: A list of keywords from the job description that were found or missing in the resume.
Section Analysis: A breakdown of how well the resume sections (Work Experience, Skills, Education, Certifications) align with the job requirements.
Formatting Evaluation: A comment on the LaTeX formatting's suitability for ATS parsing.
Scoring Criteria:

Exact Keyword Match (50%):
Award points for each exact keyword match from the job description found in the resume.
Deduct points for each missing keyword, especially if it's a core requirement.
Relevance of Experience and Sections (20%):
Award points for the presence of essential sections (Work Experience, Skills, Education, Certifications).
Deduct points for missing sections or irrelevant experience.
Formatting and ATS Compatibility (10%):
Award points for clear, simple formatting with headings, bullet points, and minimal complexity.
Deduct points for complex formatting that might hinder parsing.
Alignment with Job Requirements (20%):
Award points for direct matches between the applicant's experience and skills and the specific job requirements.
Example Input:

LaTeX Resume: A LaTeX file containing the applicant's CV with sections for Experience, Skills, Education, and Certifications.
Job Description: A text document specifying requirements for a Python developer, including keywords like "Python," "Pandas," "Machine Learning," and "SQL."
Example Output:

ATS Score: 75

Keyword Match:

Found: Python, Pandas
Missing: Machine Learning, SQL
Section Analysis:

Work Experience: Relevant experience in data analysis.
Skills: Python, Pandas, and some relevant soft skills.
Education: Relevant degree in Computer Science.
Certifications: No relevant certifications.
Formatting Evaluation:

Clear and simple formatting, suitable for ATS parsing.
Explanation:
The applicant's resume has a strong match for the core skills of Python and Pandas. However, the lack of Machine Learning and SQL experience, which are crucial for the job, significantly impacts the score. The formatting is clear and ATS-friendly, contributing positively to the overall score.
"""

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

def get_ats_score(input,job_desc,prompt):
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content([input,job_desc,prompt])
    # print(response.text.split('```'))
    return response.text


# Streamlit Interface
def main():
    st.title("Check ATS Score")

    # Step 1: Upload LaTeX Resume
    latex_file = st.file_uploader("Upload LaTeX Resume (.tex)", type="tex")

    # Step 2: Input job description
    job_description = st.text_area("Enter Job Description")

    # When both resume and job description are provided
    if st.button('Get ATS Score') and latex_file and job_description:

        latex_text = latex_file.getvalue().decode("utf-8")


        ats_score = get_ats_score(latex_text, job_description, ATS_prompt)
        st.subheader("ATS SCORE")
        st.text(ats_score.replace('*', ''))


if __name__ == "__main__":
    main()