# salary_calculator.py
import streamlit as st
import os
st.set_page_config(page_title="Network Engineer Salary Calculator", layout="centered")

from PIL import Image
import base64

# --- background part ---
def add_bg_from_local(image_file):
    file_path = os.path.join(os.path.dirname(__file__), image_file)
    with open(file_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("bg4.png")

# --- helper function for images ---
def get_base64_image(image_file):
    import base64, os
    file_path = os.path.join(os.path.dirname(__file__), image_file)
    with open(file_path, "rb") as f:
        data = f.read()
    return "data:image/png;base64," + base64.b64encode(data).decode()

st.image("hb_logo.png", width=250)

# --- Salary data (role -> location -> (min, max)) ---
salary_data = {
    "--- Network Engineer ---": {},
    "Network Engineer": {
        "London": (55000, 70000),
        "Manchester": (40000, 55000),
        "Birmingham": (45000, 60000),
        "Remote": (50000, 70000),
    },
    "Network Administrator": {
        "London": (35000, 45000),
        "Manchester": (28000, 38000),
        "Birmingham": (30000, 40000),
        "Remote": (32000, 45000),
    },
    "Network Analyst": {
        "London": (40000, 55000),
        "Manchester": (32000, 45000),
        "Birmingham": (35000, 48000),
        "Remote": (38000, 55000),
    },
    "Network Architect": {
        "London": (70000, 95000),
        "Manchester": (60000, 75000),
        "Birmingham": (60000, 75000),
        "Remote": (60000, 85000),
    },
    "Network Security Engineer": {
        "London": (60000, 80000),
        "Manchester": (50000, 65000),
        "Birmingham": (50000, 65000),
        "Remote": (55000, 75000),
    },
    "Network Support Engineer": {
        "London": (30000, 40000),
        "Manchester": (25000, 35000),
        "Birmingham": (26000, 36000),
        "Remote": (28000, 40000),
    },
    
    "--- Radio Frequency ---": {},
    "Wireless Network Engineer": {
        "London": (45000, 65000),
        "Manchester": (35000, 50000),
        "Birmingham": (38000, 52000),
        "Remote": (40000, 60000),
    },
    "Radio Frequency (RF) Engineer": {
        "London": (45000, 70000),
        "Manchester": (38000, 55000),
        "Birmingham": (36000, 53000),
        "Remote": (40000, 65000),
    },
    "Radio Frequency (RF) Design Engineer": {
        "London": (48000, 75000),
        "Manchester": (40000, 60000),
        "Birmingham": (38000, 58000),
        "Remote": (43000, 70000),
    },
    "Radio Frequency (RF) Test Engineer": {
        "London": (40000, 60000),
        "Manchester": (34000, 50000),
        "Birmingham": (32000, 48000),
        "Remote": (35000, 55000),
    },
    "RAN Engineer": {
        "London": (45000, 72000),
        "Manchester": (38000, 56000),
        "Birmingham": (36000, 53000),
        "Remote": (40000, 68000),
    },
    "DMR / PMR Engineer": {
        "London": (45000, 60000),
        "Manchester": (40000, 55000),
        "Birmingham": (40000, 55000),
        "Remote": (35000, 50000),
    },
    "Military Leaver (Signals / EWSI)": {
        "London": (40000, 50000),
        "Manchester": (35000, 45000),
        "Birmingham": (30000, 40000),
        "Remote": (30000, 40000),
    },
    
    "--- IP and Transmission ---": {},
    "Senior IP Network Engineer": {
        "London": (65000, 85000),
        "Manchester": (55000, 80000),
        "Birmingham": (55000, 80000),
        "Remote": (55000, 85000),
    },
    "IP Operations / NetOps Engineer": {
        "London": (45000, 70000),
        "Manchester": (37000, 55000),
        "Birmingham": (34000, 52000),
        "Remote": (40000, 65000),
    },
    "IP Engineer / Test / Dev Engineer": {
        "London": (45000, 78000),
        "Manchester": (38000, 62000),
        "Birmingham": (35000, 60000),
        "Remote": (40000, 72000),
    },
    "Backbone / Core Engineer": {
        "London": (55000, 85000),
        "Manchester": (45000, 68000),
        "Birmingham": (42000, 65000),
        "Remote": (48000, 80000),
    },
    "Transmission / Ethernet / DWDM Engineer": {
        "London": (45000, 80000),
        "Manchester": (40000, 62000),
        "Birmingham": (38000, 58000),
        "Remote": (44000, 75000),
    },
    "SIP & Voice Engineer": {
        "London": (42000, 68000),
        "Manchester": (35000, 54000),
        "Birmingham": (33000, 50000),
        "Remote": (38000, 62000),
    },
    "IP Network Design Engineer": {
        "London": (60000, 85000),
        "Manchester": (55000, 80000),
        "Birmingham": (55000, 75000),
        "Remote": (50000, 75000),
    },
    "Transmission Architect": {
        "London": (60000, 100000),
        "Manchester": (55000, 90000),
        "Birmingham": (50000, 85000),
        "Remote": (50000, 90000),
    },
    
    "--- Satellite ---": {},
    "Satellite Architect": {
        "London": (70000, 100000),
        "Manchester": (58000, 82000),
        "Birmingham": (55000, 78000),
        "Remote": (62000, 95000),
    },
    "Satcom Engineer": {
        "London": (48000, 78000),
        "Manchester": (40000, 62000),
        "Birmingham": (38000, 60000),
        "Remote": (42000, 70000),
    },
    "Satellite Systems Engineer": {
        "London": (45000, 70000),
        "Manchester": (38000, 55000),
        "Birmingham": (35000, 50000),
        "Remote": (40000, 65000),
    },
    "Satellite Operations Engineer": {
        "London": (42000, 70000),
        "Manchester": (35000, 55000),
        "Birmingham": (33000, 52000),
        "Remote": (38000, 62000),
    },
    "Ground Systems Engineer": {
        "London": (42000, 70000),
        "Manchester": (35000, 55000),
        "Birmingham": (33000, 52000),
        "Remote": (38000, 62000),
    },
    "Satcom Integration Engineer": {
        "London": (50000, 90000),
        "Manchester": (42000, 70000),
        "Birmingham": (40000, 65000),
        "Remote": (45000, 80000),
    },
    "SATCOM Field Service Engineer": {
        "London": (45000, 75000),
        "Manchester": (38000, 60000),
        "Birmingham": (35000, 55000),
        "Remote": (40000, 70000),
    },
    "SATCOM Business Development Manager": {
        "London": (60000, 95000),
        "Manchester": (48000, 75000),
        "Birmingham": (45000, 70000),
        "Remote": (50000, 90000),
    },
    "SATCOM Pre-Sales Engineer": {
        "London": (50000, 90000),
        "Manchester": (42000, 70000),
        "Birmingham": (40000, 65000),
        "Remote": (45000, 80000),
    },
    
    "--- Data Centres ---": {},
    "Data Centre Technician": {
        "London": (31000, 49000),
        "Manchester": (26000, 40000),
        "Birmingham": (25000, 38000),
        "Remote": (28000, 45000),
    },
    "Data Centre Engineer": {
        "London": (42000, 70000),
        "Manchester": (35000, 56000),
        "Birmingham": (33000, 52000),
        "Remote": (38000, 65000),
    },
    "Network Engineer (Data Centre)": {
        "London": (50000, 78000),
        "Manchester": (42000, 62000),
        "Birmingham": (40000, 60000),
        "Remote": (45000, 75000),
    },
    "Data Centre Operations Manager": {
        "London": (60000, 95000),
        "Manchester": (48000, 75000),
        "Birmingham": (45000, 70000),
        "Remote": (50000, 85000),
    },
    "Infrastructure Engineer (Data Centre)": {
        "London": (40000, 90000),
        "Manchester": (34000, 70000),
        "Birmingham": (32000, 65000),
        "Remote": (38000, 80000),
    },
    "Facilities Engineer (Data Centre)": {
        "London": (45000, 65000),
        "Manchester": (40000, 55000),
        "Birmingham": (40000, 55000),
        "Remote": (30000, 60000),
    },
    "Data Centre Security Analyst": {
        "London": (45000, 75000),
        "Manchester": (38000, 60000),
        "Birmingham": (35000, 55000),
        "Remote": (40000, 70000),
    },
    "DevOps Engineer (Data Centre Operations)": {
        "London": (50000, 85000),
        "Manchester": (42000, 65000),
        "Birmingham": (40000, 60000),
        "Remote": (45000, 80000),
    },
    
    "--- Broadcasting ---": {},
    "Broadcast Systems Engineer": {
        "London": (40000, 75000),
        "Manchester": (32000, 56000),
        "Birmingham": (30000, 52000),
        "Remote": (35000, 65000),
    },
    "Network Broadcast Engineer": {
        "London": (42000, 78000),
        "Manchester": (34000, 60000),
        "Birmingham": (32000, 58000),
        "Remote": (38000, 68000),
    },
    "Cloud Broadcast Engineer": {
        "London": (45000, 80000),
        "Manchester": (38000, 60000),
        "Birmingham": (35000, 58000),
        "Remote": (40000, 72000),
    },
    "Streaming Media Engineer": {
        "London": (45000, 80000),
        "Manchester": (38000, 60000),
        "Birmingham": (35000, 58000),
        "Remote": (40000, 72000),
    },
    "CDN (Content Delivery Network) Engineer": {
        "London": (45000, 80000),
        "Manchester": (38000, 60000),
        "Birmingham": (35000, 58000),
        "Remote": (40000, 72000),
    },
    "Video over IP Specialist": {
        "London": (44000, 78000),
        "Manchester": (36000, 58000),
        "Birmingham": (34000, 55000),
        "Remote": (38000, 70000),
    },
    "Systems Integration Specialist": {
        "London": (40000, 70000),
        "Manchester": (34000, 55000),
        "Birmingham": (30000, 50000),
        "Remote": (36000, 65000),
    },
    "Digital Content Delivery Specialist": {
        "London": (40000, 70000),
        "Manchester": (34000, 55000),
        "Birmingham": (30000, 50000),
        "Remote": (36000, 65000),
    },
    "Distribution Engineer": {
        "London": (45000, 65000),
        "Manchester": (40000, 58000),
        "Birmingham": (40000, 55000),
        "Remote": (38000, 70000),
    },
    "Event Engineer": {
        "London": (45000, 60000),
        "Manchester": (45000, 55000),
        "Birmingham": (40000, 50000),
        "Remote": (40000, 65000),
    },
    
    "--- Support (Telecoms) ---": {},
    "1st Line Support Engineer": {
        "London": (25000, 32000),
        "Manchester": (25000, 28000),
        "Birmingham": (25000, 27000),
        "Remote": (23000, 30000),
    },
    "2nd Line Support Engineer": {
        "London": (30000, 40000),
        "Manchester": (26000, 34000),
        "Birmingham": (26000, 33000),
        "Remote": (27000, 36000),
    },
    "3rd Line Support Engineer": {
        "London": (40000, 55000),
        "Manchester": (34000, 45000),
        "Birmingham": (33000, 44000),
        "Remote": (35000, 48000),
    },
    
    "--- Design ---": {},
    "Network Designer": {
        "London": (60000, 95000),
        "Manchester": (55000, 85000),
        "Birmingham": (55000, 75000),
        "Remote": (55000, 90000),
    },
    
    "--- Pre-Sales (IT Telecoms) ---": {},
    "Sales Engineer": {
        "London": (45000, 90000),
        "Manchester": (36000, 72000),
        "Birmingham": (34000, 65000),
        "Remote": (40000, 80000),
    },
    
    "--- Cybersecurity ---": {},
    "Cyber Security Engineer": {
        "London": (65000, 90000),
        "Manchester": (55000, 75000),
        "Birmingham": (50000, 70000),
        "Remote": (60000, 85000),
    },
    "Application Security Engineer": {
        "London": (70000, 100000),
        "Manchester": (60000, 80000),
        "Birmingham": (55000, 75000),
        "Remote": (65000, 90000),
    },
    "Cloud Security Engineer": {
        "London": (55000, 75000),
        "Manchester": (50000, 65000),
        "Birmingham": (48000, 65000),
        "Remote": (55000, 80000),
    },
    "Cyber Security Analyst": {
        "London": (50000, 65000),
        "Manchester": (40000, 55000),
        "Birmingham": (38000, 55000),
        "Remote": (45000, 65000),
    },
    "Digital Forensics": {
        "London": (55000, 80000),
        "Manchester": (45000, 65000),
        "Birmingham": (42000, 60000),
        "Remote": (50000, 70000),
    },
    "GRC Analyst (Governance, Risk & Compliance)": {
        "London": (60000, 80000),
        "Manchester": (50000, 65000),
        "Birmingham": (45000, 60000),
        "Remote": (55000, 75000),
    },
    "Incident Response Specialist": {
        "London": (65000, 85000),
        "Manchester": (55000, 70000),
        "Birmingham": (50000, 65000),
        "Remote": (60000, 80000),
    },
    "Information Security": {
        "London": (60000, 80000),
        "Manchester": (50000, 65000),
        "Birmingham": (48000, 62000),
        "Remote": (55000, 75000),
    },
    "OT Security": {
        "London": (60000, 85000),
        "Manchester": (50000, 65000),
        "Birmingham": (48000, 65000),
        "Remote": (60000, 85000),
    },
    "Red Team Engineer": {
        "London": (70000, 100000),
        "Manchester": (60000, 80000),
        "Birmingham": (55000, 75000),
        "Remote": (65000, 90000),
    },
    "SOC Analyst (Security Operations Centre)": {
        "London": (45000, 65000),
        "Manchester": (35000, 50000),
        "Birmingham": (33000, 50000),
        "Remote": (40000, 60000),
    },
    "Threat Intelligence Analyst": {
        "London": (60000, 80000),
        "Manchester": (50000, 65000),
        "Birmingham": (48000, 65000),
        "Remote": (55000, 75000),
    },
}


# seniority percentiles: the percentile inside the range to show as an estimated salary
seniority_percentiles = {
    "Junior": 0.25,
    "Intermediate": 0.50,
    "Senior": 0.75,
    "Managerial": 0.90
}

# --- Dropdown data ---
roles = list(salary_data.keys())
locations = ["London", "Manchester", "Birmingham", "Remote"]
levels = ["Junior", "Intermediate", "Senior", "Managerial"]

# --- UI ---
st.title("Discover salary benchmarks across the UK tech industry")
st.write("---")
st.write("Select role, location and experience level to see an estimated salary range. This is for guidance only.")

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    role = st.selectbox("Role", roles)
with col2:
    location = st.selectbox("Location", locations)
with col3:
    level = st.selectbox("Experience", levels)

# button below dropdowns
st.write("")
show = st.button("Show Estimate", use_container_width=True)

# defining the number formatter
def fmt(n):
    return f"£{n:,.0f}"

st.write("---")

if show:
    min_sal, max_sal = salary_data[role][location]
    suggested = int(min_sal + (max_sal - min_sal) * seniority_percentiles[level])

    st.subheader(f"{level} {role} Salary in {location}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**Estimated salary range:** {fmt(min_sal)} – {fmt(max_sal)}")
    with col2:
        st.markdown(f"**Estimated salary for this experience level:** {fmt(suggested)}")
    
    st.info("This is an estimate based on market ranges. Actual offers vary by skills, certifications and company.")

st.caption("Data source: internal market ranges. Use for guidance only.")

# --- Simple Button Section ---
st.markdown("---")

st.markdown("""
<style>
.explore-btn {
    display: inline-block;
    border: 1px solid rgba(255, 255, 255, 0.8); /* thinner + softer */
    color: white;
    background-color: transparent;
    padding: 10px 20px;
    border-radius: 10px;
    margin: 8px;
    text-decoration: none; /* removes underline */
    font-weight: 500;
    font-size: 15px;
    letter-spacing: 0.5px;
    transition: all 0.25s ease;
}
.explore-btn:hover {
    background-color: rgba(255, 255, 255, 0.9);
    color: black;
}
</style>
""", unsafe_allow_html=True)

buttons = [
    ("Home", "https://www.hamilton-barnes.com/"),
    ("Explore Roles", "https://www.hamilton-barnes.com/jobs"),
    ("Candidates", "https://www.hamilton-barnes.com/candidates"),
    ("Clients", "https://www.hamilton-barnes.com/clients"),
    ("Graduates", "https://www.empowering-future-network-engineers.com/")
]

btn_html = '<div style="text-align:center;">'
for label, link in buttons:
    btn_html += f'<a href="{link}" target="_blank" class="explore-btn">{label}</a>'
btn_html += '</div>'

st.markdown(btn_html, unsafe_allow_html=True)