import streamlit as st
from streamlit_option_menu import option_menu
import os
import base64

# Function to encode image to base64
def get_base64_image(image_path):
    if not os.path.exists(image_path):
        return None
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set page configuration
st.set_page_config(
    page_title="Akhil Songa Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Encode the profile image
profile_image_path = "profile.jpg"  # Ensure the file is named 'profile.jpg' and is in the same directory
encoded_image = get_base64_image(profile_image_path)

# Inline CSS for custom styling and animations
def apply_inline_css(encoded_image):
    if encoded_image:
        profile_image = f"data:image/jpeg;base64,{encoded_image}"
        st.markdown(
            f"""
            <style>
            /* General Styles */
            body {{
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                color: #333333;
                overflow-x: hidden;
                background-color: #f9f9f9;
            }}
            h1, h2, h3, h4 {{
                color: #2e86de;
                opacity: 0;
                transform: translateY(-20px);
                animation: fadeInDown 0.8s forwards;
            }}
            h1 {{
                animation-delay: 0.2s;
            }}
            h2 {{
                animation-delay: 0.4s;
            }}
            h3 {{
                animation-delay: 0.6s;
            }}
            h4 {{
                animation-delay: 0.8s;
            }}
            p, li {{
                opacity: 0;
                transform: translateY(20px);
                animation: fadeInUp 0.8s forwards;
            }}
            p {{
                animation-delay: 0.9s;
            }}
            li {{
                animation-delay: 1.1s;
            }}
            .footer {{
                text-align: center;
                color: gray;
                padding: 20px 0;
            }}
            /* Profile Container Styles */
            .profile-container {{
                display: flex;
                align-items: center;
                margin-bottom: 20px;
                opacity: 0;
                transform: translateY(-20px);
                animation: fadeIn 0.8s forwards;
                animation-delay: 0.2s;
            }}
            .profile-pic {{
                border-radius: 50%;
                width: 100px;
                height: 100px;
                object-fit: cover;
                border: 3px solid #2e86de;
                margin-right: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            .profile-name {{
                font-size: 2em;
                font-weight: bold;
                color: #2e86de;
            }}
            /* Horizontal Timeline */
            .timeline {{
                display: flex;
                overflow-x: auto;
                padding: 20px 0;
                scroll-snap-type: x mandatory;
                gap: 20px;
            }}
            .timeline-item {{
                flex: 0 0 300px;
                padding: 20px;
                background: #ffffff;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                scroll-snap-align: start;
                opacity: 0;
                transform: translateY(50px);
                animation: slideUp 0.8s forwards;
                animation-delay: calc(0.2s * var(--order));
            }}
            .timeline-item h3 {{
                color: #2e86de;
            }}
            .timeline-item p {{
                color: #555555;
            }}
            /* Keyframes for Animations */
            @keyframes fadeInDown {{
                from {{
                    opacity: 0;
                    transform: translateY(-20px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
            @keyframes fadeInUp {{
                from {{
                    opacity: 0;
                    transform: translateY(20px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
            @keyframes fadeIn {{
                from {{
                    opacity: 0;
                    transform: translateY(-20px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
            @keyframes slideUp {{
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
            /* Scrollbar Styling for Timeline */
            .timeline::-webkit-scrollbar {{
                height: 8px;
            }}
            .timeline::-webkit-scrollbar-track {{
                background: #f1f1f1;
                border-radius: 4px;
            }}
            .timeline::-webkit-scrollbar-thumb {{
                background: #2e86de;
                border-radius: 4px;
            }}
            /* Responsive Design */
            @media (max-width: 768px) {{
                .profile-container {{
                    flex-direction: column;
                    text-align: center;
                }}
                .profile-pic {{
                    margin-bottom: 10px;
                }}
                .timeline-item {{
                    flex: 0 0 250px;
                }}
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        # Inject the profile container HTML
        st.markdown(
            f"""
            <div class="profile-container">
                <img src="{profile_image}" class="profile-pic" alt="Profile Picture">
                <div class="profile-name">Akhil Songa</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Profile image not found! Please add 'profile.jpg' to the app directory.")


apply_inline_css(encoded_image)

# Sidebar Navigation Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",  # required
        options=["Home", "Work Experience", "Projects", "Publications", "Skills"],  # required
        icons=["house", "briefcase", "folder", "book", "tools"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
    )

# Main Content with Animations
if selected == "Home":
    st.title("👋 Welcome to My Portfolio")
    st.markdown(
        """
        Hi, I'm **Akhil Songa** — a passionate developer and researcher with expertise in **AI Development, Data Science, and Generative AI**.
        """
    )
    st.markdown(
        """
        📧 Email: [akhilsonga1@gmail.com](mailto:akhilsonga1@gmail.com)  
        🌍 Location: California, USA  
        🔗 [LinkedIn](https://linkedin.com/in/akhilsonga) | [GitHub](https://github.com/akhilsonga)  
        """
    )

elif selected == "Work Experience":
    st.title("💼 Work Experience")
    experiences = [
        {
            "title": "AUTHENTICATE",
            "duration": "Jan 2024 - Oct 2024",
            "details": [
                "📈 **Leadership and Project Management:** Directed a team of 6 engineers to build 'Ethic-AI,' a cutting-edge reporting platform for California Police Departments.",
                "🤖 **AI Development:** Engineered EthicalLLM9B model with SOTA audio and video processing using META’s ImageBind & BLIP-2 Q-Former pipeline.",
                "⚙️ **Technical Implementations:** Fine-tuned the LLM on a 4-A100 GPU cluster with CA Penal Codes data.",
                "🧠 **AI Agents:** Crafted 15 advanced AI Agents for real-time decisions for situation handling.",
            ],
        },
        {
            "title": "MYEDMASTER",
            "duration": "Sep 2023 – Jan 2024",
            "details": [
                "🎓 **Educational AI Enhancement:** Built a multi-modal LLM system with Mistral7B and Llama2 34B models.",
                "📊 **User Behavior Analysis:** Conducted analysis to group learners into profiles, boosting engagement by 65%.",
                "⚡ **Performance Optimization:** Reduced inference time by 50% through efficient resource utilization.",
            ],
        },
    ]

    # Horizontal Timeline Layout
    st.markdown('<div class="timeline">', unsafe_allow_html=True)
    for idx, exp in enumerate(experiences):
        st.markdown(
            f"""
            <div class="timeline-item" style="--order: {idx};">
                <h3>{exp['title']}</h3>
                <p><strong>Duration:</strong> {exp['duration']}</p>
                <ul>
                    {''.join([f"<li>{detail}</li>" for detail in exp['details']])}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Projects":
    st.title("🛠️ Projects")
    projects = [
        {
            "title": "Ethic-AI",
            "description": "A reporting platform for California Police Departments, optimizing workflows via MLOps and LLMs.",
        },
        {
            "title": "Multi-modal LLM for Education",
            "description": "AI-enhanced learning chatbot using Mistral7B and Llama2 models, boosting engagement by 65%.",
        },
    ]

    # Horizontal Timeline Layout
    st.markdown('<div class="timeline">', unsafe_allow_html=True)
    for idx, project in enumerate(projects):
        st.markdown(
            f"""
            <div class="timeline-item" style="--order: {idx};">
                <h3>{project['title']}</h3>
                <p>{project['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Publications":
    st.title("📚 Publications")
    publications = [
        {
            "title": "A Comparative Study of Various Data Visualization Techniques using COVID-19 Data set",
            "journal": "IRJET",
            "date": "August 2021",
        },
        {
            "title": "The Societal and Transformational Impacts of Data Science",
            "journal": "IJERT",
            "date": "September 2021",
        },
    ]

    for pub in publications:
        st.subheader(pub["title"])
        st.markdown(f"**Journal:** {pub['journal']} | **Date:** {pub['date']}")
        st.markdown("---")

elif selected == "Skills":
    st.title("💡 Skills & Technical Knowledge")
    skills = {
        "Programming Languages": ["Python", "C++", "Objective-C", "Java", "HTML", "CSS", "JavaScript", "SQL"],
        "Tools/Frameworks": ["Tableau", "Power BI", "Sci-kit", "TensorFlow", "PySpark", "Flask"],
        "Cloud Platforms": ["AWS", "Google Cloud Platform", "Azure"],
        "Data Science Knowledge": ["Pandas", "Numpy", "Machine Learning", "Deep Learning", "MLOps", "Docker"],
        "Generative AI": ["LLM Fine-Tuning", "LangChain", "Llama Index", "Prompt Engineering"],
    }

    for category, skillset in skills.items():
        st.subheader(category)
        st.markdown("\n".join([f"- {skill}" for skill in skillset]))

# Footer
st.markdown(
    """
    <div class="footer">
        © 2024 Akhil Songa. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True,
)
