# import streamlit as st
# from openai import OpenAI
# import os

# # -------------------------------
# # 🔑 OPENAI CLIENT
# # -------------------------------
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # -------------------------------
# # 💾 SESSION HISTORY
# # -------------------------------
# if "history" not in st.session_state:
#     st.session_state.history = []

# # -------------------------------
# # 🔧 PAGE CONFIG
# # -------------------------------
# st.set_page_config(page_title="PromptForge AI", page_icon="⚡", layout="centered")

# # -------------------------------
# # 🎨 CUSTOM STYLING
# # -------------------------------
# st.markdown("""
# <style>
# .main {
#     background-color: #0e1117;
# }
# h1, h2, h3 {
#     color: #ffffff;
# }
# .stButton>button {
#     background-color: #4CAF50;
#     color: white;
#     border-radius: 10px;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # 📌 SIDEBAR
# # -------------------------------
# st.sidebar.title("⚡ PromptForge AI")

# page = st.sidebar.radio(
#     "Navigate",
#     ["🏠 Home", "📜 History", "ℹ️ About"]
# )

# # -------------------------------
# # 🧠 FUNCTION: DYNAMIC QUESTIONS
# # -------------------------------
# def generate_questions(intent):

#     if "resume" in intent or "cv" in intent:
#         return [
#             ("1. Basic Info", "Are you a student, fresher, or experienced professional?", "e.g. Fresher"),
#             ("2. Industry", "What is your field/industry?", "e.g. IT, Mechanical"),
#             ("3. Target Role", "What role are you targeting?", "e.g. Software Engineer"),
#             ("4. Background", "Education / projects / experience?", "e.g. B.Tech + ML project"),
#             ("4. Skills", "Key skills?", "e.g. Python, SQL, Communication"),
#             ("6. Style", "Resume style?", "ATS-friendly or creative"),
#             ("7. Output", "1-page or 2-page?", "e.g. 1-page concise"),
#             ("8. Tone", "Tone?", "Formal / Professional")
#         ]

#     elif "image" in intent:
#         return [
#             ("1. Image Type", "What type of image?", "e.g. realistic, cartoon, 3D"),
#             ("2. Subject", "Main subject?", "e.g. person, product, landscape"),
#             ("3. Style", "Art style?", "e.g. cinematic, anime, photorealistic"),
#             ("4. Colors", "Color theme?", "e.g. dark, vibrant, pastel"),
#             ("5. Usage", "Where will it be used?", "e.g. Instagram, thumbnail"),
#             ("6. Details", "Extra details?", "e.g. lighting, background elements"),
#             ("7. Quality", "Resolution?", "HD, 4K, ultra realistic")
#         ]

#     elif "youtube" in intent:
#         return [
#             ("1. Topic", "Video topic?", "e.g. AI tools that save time"),
#             ("2. Audience", "Target audience?", "e.g. students, beginners"),
#             ("3. Duration", "Video length?", "Short or long"),
#             ("4. Style", "Video style?", "Storytelling, educational"),
#             ("5. Goal", "Purpose?", "Views, engagement"),
#             ("6. Platform", "Platform?", "YouTube Shorts / Long"),
#             ("7. Tone", "Tone?", "Energetic, fun")
#         ]

#     else:
#         return [
#             ("1. Goal", "What do you want to achieve?", "e.g. Build a startup idea"),
#             ("2. Context", "Topic or domain?", "e.g. fintech, AI"),
#             ("3. Audience", "Target users?", "e.g. developers"),
#             ("4. Format", "Output format?", "e.g. steps, list"),
#             ("5. Tone", "Tone?", "Professional, casual"),
#             ("6. Constraints", "Any limits?", "e.g. 60 sec, simple language")
#         ]

# # =========================================================
# # 🏠 HOME PAGE
# # =========================================================
# if page == "🏠 Home":

#     st.markdown("## ⚡ ganEEEE Prompt Magic")
#     st.caption("Generate powerful AI prompts with smart guided questions.")

#     st.success("🚀 AI-Powered Prompt Generator | Built by Ganesh")

#     st.markdown("""
# ### ✨ Features
# - 🧠 Smart question-based input
# - 🤖 AI-generated prompts
# - 📜 Prompt history tracking
# - 🌍 Works for multiple use cases
# """)

#     user_input = st.text_input(
#         "What do you want to create?",
#         placeholder="e.g. resume, image, youtube script..."
#     )

#     intent = user_input.strip().lower() if user_input else ""

#     if intent != "":

#         st.info(f"🧠 Smart Mode Activated for: {user_input}")

#         questions = generate_questions(intent)
#         answers = {}

#         st.markdown(f"""
# ### 👋 Let's build your prompt step-by-step

# You said: **{user_input}**

# Answer a few questions to generate a powerful prompt 👇
# """)

#         for title, question, example in questions:
#             st.markdown(f"### {title}")
#             answers[title] = st.text_input(question, placeholder=example, key=title)
#             st.caption(f"👉 Example: {example}")

#         if st.button("🚀 Generate Prompts", use_container_width=True):

#             with st.spinner("Generating AI-powered prompts..."):

#                 prompt_input = f"User wants: {user_input}\n\nDetails:\n"

#                 for key, value in answers.items():
#                     prompt_input += f"{key}: {value}\n"

#                 try:
#                     response = client.chat.completions.create(
#                         model="gpt-4o-mini",
#                         messages=[
#                             {
#                                 "role": "system",
#                                 "content": "You are PromptForge AI. Generate 4 high-quality prompts in Creative, Analytical, Minimal, and Expert styles."
#                             },
#                             {
#                                 "role": "user",
#                                 "content": prompt_input
#                             }
#                         ],
#                         temperature=0.7
#                     )

#                     output = response.choices[0].message.content

#                 except Exception as e:
#                     output = "⚠️ Error: API limit reached or issue occurred. Please try again later."

#             st.markdown("### 🔥 Generated Prompts")
#             st.code(output)

#             st.session_state.history.append(output)

#             col1, col2 = st.columns(2)

#             with col1:
#                 st.download_button("📥 Download", output, file_name="prompts.txt")

#             with col2:
#                 if st.button("🔄 Regenerate"):
#                     st.rerun()

# # =========================================================
# # 📜 HISTORY PAGE
# # =========================================================
# elif page == "📜 History":

#     st.title("📜 Prompt History")

#     if st.session_state.history:
#         for item in st.session_state.history[::-1]:
#             st.code(item)
#     else:
#         st.info("No prompts generated yet.")

# # =========================================================
# # ℹ️ ABOUT PAGE
# # =========================================================
# elif page == "ℹ️ About":

#     st.title("ℹ️ About PromptForge AI")

#     st.markdown("""
# PromptForge AI is an intelligent prompt generator that helps users create high-quality AI prompts.

# ### 🚀 Use Cases
# - Resume Building  
# - YouTube Scripts  
# - Image Generation  
# - Coding & Business Ideas  

# ### 🛠 Tech Stack
# - Streamlit  
# - OpenAI API  

# Built with ❤️ by Ganesh Goddilla
# """)



import streamlit as st

# -------------------------------
# 💾 SESSION HISTORY
# -------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------------
# 🔧 PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="PromptForge AI", page_icon="⚡", layout="centered")

# -------------------------------
# 🎨 PREMIUM STYLING
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main {
    background: linear-gradient(180deg, #0e1117 0%, #111827 100%);
}
h1 {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
}
.subtext {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 20px;
}
.card {
    background: #1f2937;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
}
.stButton>button {
    background: linear-gradient(90deg, #4CAF50, #22c55e);
    color: white;
    border-radius: 12px;
    height: 45px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 📌 SIDEBAR
# -------------------------------
st.sidebar.markdown("""
<h2 style='margin-bottom:0;'>⚡ PromptForge AI</h2>
<p style='color:#6b7280; font-size:11px; margin-top:0;'>By Ganesh Goddilla</p>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📜 History", "ℹ️ About"]
)

# -------------------------------
# 🧠 FUNCTION: DYNAMIC QUESTIONS
# -------------------------------
def generate_questions(intent):

    if "resume" in intent:
        return [
            ("Role", "Target job role?", "Software Engineer"),
            ("Experience", "Experience level?", "Fresher"),
            ("Skills", "Key skills?", "Python, SQL"),
            ("Education", "Education?", "B.Tech"),
        ]

    elif "image" in intent:
        return [
            ("Type", "Image type?", "realistic"),
            ("Subject", "Main subject?", "robot"),
            ("Style", "Style?", "cinematic"),
            ("Mood", "Mood?", "dark"),
        ]

    elif "youtube" in intent:
        return [
            ("Topic", "Video topic?", "AI tools"),
            ("Audience", "Audience?", "students"),
            ("Length", "Length?", "short"),
            ("Tone", "Tone?", "fun"),
        ]

    else:
        return [
            ("Goal", "What do you want?", "startup idea"),
            ("Context", "Topic?", "AI"),
            ("Audience", "Target?", "developers"),
            ("Tone", "Tone?", "professional"),
        ]

# -------------------------------
# 🧠 SMART PROMPT ENGINE
# -------------------------------
def generate_prompts(user_input, answers):

    intent = user_input.lower()

    # 🔥 IMAGE LOGIC (SMART)
    if "image" in intent:

        subject = answers.get("Subject", "")
        style = answers.get("Style", "")
        mood = answers.get("Mood", "")
        type_ = answers.get("Type", "")

        base = f"{type_} {style} {mood} {subject}".strip()

        creative = f"""
🔹 Prompt 1 – Creative Style  
Create a highly detailed {type_} image of {subject} in a {style} style with a {mood} mood.  
Include cinematic lighting, rich textures, and dynamic composition.  
Make it visually stunning and unique.
"""

        analytical = f"""
🔹 Prompt 2 – Analytical Style  
Generate an image with the following structured details:
- Subject: {subject}
- Style: {style}
- Mood: {mood}
- Type: {type_}

Ensure clarity, proper composition, and balanced visual elements.
"""

        minimal = f"""
🔹 Prompt 3 – Minimal Style  
{base}, high quality, detailed
"""

        expert = f"""
🔹 Prompt 4 – Expert-Level Style  
Create a {type_} {style} image of {subject} with a {mood} atmosphere.  
Use professional photography techniques, depth of field, realistic lighting, and high-resolution detail (4K/8K).  
Focus on composition, shadows, and cinematic realism.
"""

        return creative + analytical + minimal + expert

    # 🔥 DEFAULT LOGIC (OTHER USE CASES)
    base = f"Task: {user_input}\n"
    for k, v in answers.items():
        base += f"- {k}: {v}\n"

    return f"""
🔹 Prompt 1 – Creative  
Act as a creative expert and generate output for:

{base}

🔹 Prompt 2 – Analytical  
Break this down step-by-step:

{base}

🔹 Prompt 3 – Minimal  
Create a short prompt for: {user_input}

🔹 Prompt 4 – Expert  
Act as an industry expert and generate a high-quality prompt:

{base}
"""

# =========================================================
# 🏠 HOME
# =========================================================
if page == "🏠 Home":

    st.markdown("<h1>⚡ PromptForge AI</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtext">Generate powerful prompts like a pro 🚀</p>', unsafe_allow_html=True)

    st.markdown("""
<div class="card">
✨ Create prompts for Resume, YouTube, Images, Startups & more  
⚡ 100% Free  
🧠 Smart guided system  
</div>
""", unsafe_allow_html=True)

    user_input = st.text_input("What do you want to create?", placeholder="e.g. image, resume, youtube...")

    if user_input:

        questions = generate_questions(user_input.lower())
        answers = {}

        st.markdown("### ⚙️ Customize your prompt")

        for title, question, example in questions:
            answers[title] = st.text_input(question, placeholder=example)

        if st.button("🚀 Generate Prompts"):

            output = generate_prompts(user_input, answers)

            st.markdown("### 🔥 Your Prompts")
            st.code(output)

            st.session_state.history.append(output)

# =========================================================
# 📜 HISTORY
# =========================================================
elif page == "📜 History":

    st.markdown("## 📜 Prompt History")

    if st.session_state.history:
        for item in st.session_state.history[::-1]:
            st.code(item)
    else:
        st.info("No prompts yet.")

# =========================================================
# ℹ️ ABOUT
# =========================================================
else:

    st.markdown("## ℹ️ About")

    st.write("""
PromptForge AI is a smart prompt generator.
Created By GANESH GODDILLA

🚀 Built for creators, developers, and entrepreneurs  
⚡ 100% Free version  
💡 Upgrade to AI-powered version anytime  
""")