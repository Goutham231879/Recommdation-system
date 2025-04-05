import streamlit as st

st.sidebar.title("Hey hi this is a Recommended Assessment Test System")
st.sidebar.title("Know your tests")

st.title("Enter your Details")


if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

if "name" not in st.session_state:
    st.session_state.name = ""
    st.session_state.pno = ""
    st.session_state.pa = ""
    st.session_state.we = ""
    st.session_state.ed = ""
    st.session_state.skills = ["", "", "", ""]

# Form only shows if not submitted
if not st.session_state.form_submitted:
    with st.form(key="user_info_form"):
        name = st.text_input("Enter your Name", st.session_state.name)
        pno = st.text_input("Enter your Phone Number", st.session_state.pno)
        pa = st.text_input("Position Applied", st.session_state.pa)
        we = st.text_input("Work Experience", st.session_state.we)
        ed = st.text_input("Education", st.session_state.ed)
        sk1 = st.text_input("Skill-1", st.session_state.skills[0])
        sk2 = st.text_input("Skill-2", st.session_state.skills[1])
        sk3 = st.text_input("Skill-3", st.session_state.skills[2])
        sk4 = st.text_input("Skill-4", st.session_state.skills[3])
        bt = st.form_submit_button("Submit")

    if bt:
       
        st.session_state.name = name
        st.session_state.pno = pno
        st.session_state.pa = pa
        st.session_state.we = we
        st.session_state.ed = ed
        st.session_state.skills = [sk1, sk2, sk3, sk4]
        st.session_state.form_submitted = True

def recommand(job, exp, skills, shl_catalogue):
    rec = []

    if "manager" in job.lower() or "lead" in job.lower() or "director" in job.lower() or "senior" in job.lower():
        rec.append("Assessment & Development Centers")
        rec.append("Personality Assessment")

    if "sales" in job.lower() or "customer" in job.lower() or "account" in job.lower() or "retail" in job.lower():
        rec.append("Behavioral Assessments")
        rec.append("Job-Focused Assessments")

    if "engineer" in job.lower() or "data" in job.lower() or "scientist" in job.lower() or "analyst" in job.lower() or "mlops" in job.lower() or "nlp" in job.lower():
        rec.append("Cognitive Assessments")
        rec.append("Skills & Simulations")

    for skill in skills:
        for assessment, keywords in shl_catalogue.items():
            if any(keyword.lower() in skill.lower() for keyword in keywords):
                rec.append(assessment)

    return rec

shl_catalogue = {
    "Assessment & Development Centers": ["Leadership roles", "Succession planning", "Senior management"],
    "Personality Assessment": ["Culture fit", "Leadership potential", "Workplace preferences"],
    "Behavioral Assessments": ["Teamwork", "Customer service", "Communication"],
    "Job-Focused Assessments": ["Sales roles", "Customer service roles", "Role-specific skills"],
    "Cognitive Assessments": ["Problem solving", "Analytical thinking", "Logical reasoning"],
    "Skills & Simulations": ["Practical skills", "Technical roles", "Task simulations"]
}


if st.session_state.form_submitted:
    job = st.session_state.pa
    experience = st.session_state.we
    skills = st.session_state.skills

    rs = list(set(recommand(job, experience, skills, shl_catalogue)))
    bt2 = st.button("Show")
    if bt2:
        st.success(f"Thank you {st.session_state.name}! Based on your input, here are your recommended assessments:")

        for assessment in rs:
            st.write(f"- {assessment}")

 
    if st.button("Submit another response"):
        st.session_state.form_submitted = False
