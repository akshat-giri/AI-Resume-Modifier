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
    page_title=" Create Cover Letter",
    layout="wide",
    page_icon="💼"  # You can use an emoji for the icon or a path to a custom image file (e.g., 'favicon.ico')
)

st.write('# Create Cover Letter')

prompt = """
Write a compelling cover letter tailored to the following job description, targeting the position of [Job Role] at [Company Name].

Input:

Job Description: [Insert Job Description here]
Job Role: [Insert Job Role here]
Company Name: [Insert Company Name here]
Resume: [Insert LaTeX Resume here]
Output:

A well-structured cover letter that:

Clearly states the job title and company name.
Concisely highlights key qualifications and experiences relevant to the specific job.
Tailors the letter to the unique requirements of the job description.
Quantifies achievements and results whenever possible.
References specific examples from the resume to support claims.
Expresses enthusiasm for the opportunity and the company.
Concludes with a strong call to action, such as requesting an interview.
Adheres to professional formatting and tone.
Additional Tips:

Leverage the power of the LaTeX resume: Extract key skills, experiences, and accomplishments from the LaTeX resume to strengthen the cover letter.
Utilize AI tools: Employ AI-powered writing assistants to refine sentence structure, grammar, and overall clarity.
Customize for each application: Adapt the cover letter to each specific job, emphasizing the most relevant skills and experiences.
Proofread meticulously: Ensure the final draft is free of errors and typos.
Example Prompt:

Write a cover letter for the position of Senior Data Scientist at Meta using the following job description and my attached LaTeX resume.

Job Description:

Lead the development of cutting-edge machine learning models to improve personalized recommendations.
Collaborate with cross-functional teams to identify opportunities for AI-driven solutions.
Stay up-to-date with the latest advancements in machine learning and data science.
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

def find_jobs(input, job_desc,job_role,company_name,prompt):
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content([input, job_desc,job_role,company_name,prompt])
    return response.text

# Streamlit Interface
def main():

    # Step 2: Input job description
    job_description = st.text_area("Enter Job Description")

    # Step 3: Input job description
    job_role = st.text_area("Enter Job Role")

    # Step 2: Input job description
    company_name = st.text_area("Enter Company Name")


    # # Step 1: Upload LaTeX Resume
    latex_file = st.file_uploader("Upload LaTeX Resume (.tex)", type="tex")

    # When both resume and job description are provided
    if st.button('Create Cover Letter') and job_description and job_role and company_name and latex_file:

        latex_text = latex_file.getvalue().decode("utf-8")


        cover_letter = find_jobs(latex_text, job_description,job_role, company_name, prompt)
        st.subheader("Matching Jobs")
        st.text(cover_letter.replace('*', ''))

        st.download_button(
            label="Download Cover Letter",
            data=cover_letter,
            file_name="cover_letter.text",
            mime="text/plain"
        )


if __name__ == "__main__":
    main()