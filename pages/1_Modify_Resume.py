import streamlit as st
import google.generativeai as genai

# For local
# from dotenv import load_dotenv
# load_dotenv()

# import os
# genai.configure(api_key=os.getenv("API_KEY"))

# For CLoud
genai.configure(api_key=st.secrets["API_KEY"])



# Set page title and favicon
st.set_page_config(
    page_title="AI Resume Modifier",
    layout="wide",
    page_icon="💼"  # You can use an emoji for the icon or a path to a custom image file (e.g., 'favicon.ico')
)

prompt = """
Given a LaTeX-formatted resume and a job description, analyze both documents to identify missing keywords and skills that align with the job requirements. Adapt the resume by seamlessly integrating these missing elements into relevant sections while preserving the original structure and formatting.

Specific Instructions:

Keyword Extraction:

Extract keywords and skills from the job description, prioritizing those most relevant to the target position.
Identify potential keywords and phrases within the resume that could be expanded or rephrased to better match the job description.
Resume Adaptation:

Work Experience:
Review each work experience entry and identify opportunities to incorporate keywords and quantifiable achievements.
Rephrase job responsibilities and accomplishments to highlight skills and experiences relevant to the job description.
Add bullet points or paragraphs to emphasize specific projects or responsibilities that align with the target position.
Skills and Technologies:
Add or modify skills sections to include any missing keywords or technologies identified in the job description.
Organize skills into logical categories (e.g., programming languages, data analysis tools, soft skills) for better readability.
Education and Certifications:
Highlight relevant coursework, projects, or certifications that demonstrate proficiency in the required skills.
Add any missing certifications or licenses that could enhance the applicant's profile.
ATS Optimization:

Formatting and Structure:
Maintain the original LaTeX structure and formatting to ensure consistency.
Avoid using unconventional LaTeX commands or symbols that may interfere with ATS parsing.
Clean up any unnecessary or non-standard characters.
Keyword Placement:
Strategically place keywords throughout the resume, including the header, summary, work experience, skills, and education sections.
Use natural language and avoid keyword stuffing.
Output:
A LaTeX-formatted resume with the following improvements:

Enhanced keyword density: Increased the frequency of relevant keywords and phrases.
Improved skill alignment: Added or emphasized skills that match the job requirements.
Quantifiable achievements: Included specific examples of accomplishments to demonstrate impact.
Optimized ATS compatibility: Ensured the resume is easily parsed by applicant tracking systems.

A LaTeX-formatted resume with original spacing and updated content, seamlessly integrated keywords, and optimized for ATS.# Include explanations or notes within the LaTeX document. structure should be resume ''' explanations.
"""


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

def get_gemini_response(input,job_desc,prompt):
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content([input,job_desc,prompt])
    # print(response.text.split('```'))
    return (response.text.split('```')[1], response.text.split('```')[2])

def get_ats_score(input,job_desc,prompt):
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content([input,job_desc,prompt])
    # print(response.text.split('```'))
    return response.text

# # Function to extract text from the uploaded PDF resume
# def extract_text_from_pdf(pdf_file):
#     with pdfplumber.open(pdf_file) as pdf:
#         text = ''
#         for page in pdf.pages:
#             text += page.extract_text()
#     return text

# # Function to extract text from the uploaded PDF resume
# def extract_text_from_tex(latex_file):
#     with open(latex_file, 'r') as file:
#         latex_content = file.read()
#     return latex_content



# Streamlit Interface
def main():
    st.title("AI Resume Modifier")

    # # Step 1: Upload resume
    # resume_file = st.file_uploader("Upload Resume PDF", type="pdf")

    # Step 1: Upload LaTeX Resume
    latex_file = st.file_uploader("Upload LaTeX Resume (.tex)", type="tex")

    # Step 2: Input job description
    job_description = st.text_area("Enter Job Description")

    # When both resume and job description are provided
    if st.button('Modify Resume') and latex_file and job_description:
        try:
            # latex_text = extract_text_from_tex(latex_file)
            latex_text = latex_file.getvalue().decode("utf-8")

            # if st.button('Run'):
            # Modify the resume using Google Gemini
            (modified_resume, changes) = get_gemini_response(latex_text, job_description, prompt)
            # Display the ATS score for resume
            # st.subheader("ATS SCORE")
            # st.text(score)

            ats_score = get_ats_score(modified_resume, job_description, ATS_prompt)
            st.subheader("ATS SCORE")
            st.text(ats_score.replace('*', ''))

            st.download_button(
                label="Download Modified Resume",
                data=modified_resume,
                file_name="modified_resume.tex",
                mime="text/plain"
            )

            # Display the modified resume
            st.subheader("Changes Made")
            st.text(changes.replace('*', ''))

        except:
            # Display the modified resume
            st.subheader("Error: Try after sometime Or Check your inputs and try again")




if __name__ == "__main__":
    main()

