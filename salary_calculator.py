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
    "Wireless Network Engineer": {
        "London": (45000, 65000),
        "Manchester": (35000, 50000),
        "Birmingham": (38000, 52000),
        "Remote": (40000, 60000),
    },
    "Network Manager": {
        "London": (65000, 85000),
        "Manchester": (55000, 70000),
        "Birmingham": (55000, 70000),
        "Remote": (60000, 80000),
    },
    "Network Operations Center Engineer": {
        "London": (35000, 45000),
        "Manchester": (28000, 38000),
        "Birmingham": (30000, 40000),
        "Remote": (32000, 45000),
    },
    "Telecoms Network Engineer": {
        "London": (45000, 65000),
        "Manchester": (35000, 50000),
        "Birmingham": (38000, 52000),
        "Remote": (40000, 60000),
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
st.title("Find out your estimated salary range in the UK Network Engineering scene!")
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

import streamlit as st
import base64
import os

# --- Helper function to convert local image to base64 ---
def get_base64_image(image_file):
    file_path = os.path.join(os.path.dirname(__file__), image_file)
    with open(file_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f"data:image/png;base64,{data}"

# --- Carousel section (streamlit-friendly) ---
def image_carousel():
    st.markdown(
        """
        <style>
        .carousel-container {
            display: flex;
            overflow-x: auto;
            gap: 25px;
            padding: 30px 10px;
            justify-content: center;
            scrollbar-width: none;
        }
        .carousel-container::-webkit-scrollbar {
            display: none;
        }
        .carousel-item {
            flex: 0 0 auto;
            text-align: center;
            transition: transform 0.2s ease-in-out;
        }
        .carousel-item:hover {
            transform: scale(1.05);
        }
        .carousel-item img {
            width: 150px;
            height: auto;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(255, 255, 255, 0.15);
        }
        .carousel-label {
            margin-top: 8px;
            font-size: 14px;
            color: #ffffff; /* change this if your bg is light */
            font-weight: 500;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 🖼️ images + links
    images = {
        "Home": ("homepage1.png", "https://www.hamilton-barnes.com/"),
        "Explore More Roles": ("roles2.png", "https://www.hamilton-barnes.com/jobs"),
        "Candidates": ("candidates3.png", "https://www.hamilton-barnes.com/candidates"),
        "Clients": ("clients4.png", "https://www.hamilton-barnes.com/clients"),
        "Graduates": ("graduates5.png", "https://www.empowering-future-network-engineers.com/"),
    }

    html = '<div class="carousel-container">'
    for label, (image_file, link) in images.items():
        img_src = get_base64_image(image_file)
        html += f"""
        <div class="carousel-item">
            <a href="{link}" target="_blank">
                <img src="{img_src}" alt="{label}">
            </a>
            <div class="carousel-label">{label}</div>
        </div>
        """
    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

# --- render it ---
image_carousel()
