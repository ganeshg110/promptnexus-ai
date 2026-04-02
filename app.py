import streamlit as st
from openai import OpenAI
import os

# -------------------------------
# 🔑 OPENAI CLIENT
# -------------------------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
# 🎨 CUSTOM STYLING
# -------------------------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
h1, h2, h3 {
    color: #ffffff;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 📌 SIDEBAR
# -------------------------------
st.sidebar.title("⚡ PromptForge AI")

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "📜 History", "ℹ️ About"]
)

# -------------------------------
# 🧠 FUNCTION: DYNAMIC QUESTIONS
# -------------------------------
def generate_questions(intent):

    if "resume" in intent or "cv" in intent:
        return [
            ("1. Basic Info", "Are you a student, fresher, or experienced professional?", "e.g. Fresher"),
            ("2. Industry", "What is your field/industry?", "e.g. IT, Mechanical"),
            ("3. Target Role", "What role are you targeting?", "e.g. Software Engineer"),
            ("4. Background", "Education / projects / experience?", "e.g. B.Tech + ML project"),
            ("4. Skills", "Key skills?", "e.g. Python, SQL, Communication"),
            ("6. Style", "Resume style?", "ATS-friendly or creative"),
            ("7. Output", "1-page or 2-page?", "e.g. 1-page concise"),
            ("8. Tone", "Tone?", "Formal / Professional")
        ]

    elif "image" in intent:
        return [
            ("1. Image Type", "What type of image?", "e.g. realistic, cartoon, 3D"),
            ("2. Subject", "Main subject?", "e.g. person, product, landscape"),
            ("3. Style", "Art style?", "e.g. cinematic, anime, photorealistic"),
            ("4. Colors", "Color theme?", "e.g. dark, vibrant, pastel"),
            ("5. Usage", "Where will it be used?", "e.g. Instagram, thumbnail"),
            ("6. Details", "Extra details?", "e.g. lighting, background elements"),
            ("7. Quality", "Resolution?", "HD, 4K, ultra realistic")
        ]

    elif "youtube" in intent:
        return [
            ("1. Topic", "Video topic?", "e.g. AI tools that save time"),
            ("2. Audience", "Target audience?", "e.g. students, beginners"),
            ("3. Duration", "Video length?", "Short or long"),
            ("4. Style", "Video style?", "Storytelling, educational"),
            ("5. Goal", "Purpose?", "Views, engagement"),
            ("6. Platform", "Platform?", "YouTube Shorts / Long"),
            ("7. Tone", "Tone?", "Energetic, fun")
        ]

    else:
        return [
            ("1. Goal", "What do you want to achieve?", "e.g. Build a startup idea"),
            ("2. Context", "Topic or domain?", "e.g. fintech, AI"),
            ("3. Audience", "Target users?", "e.g. developers"),
            ("4. Format", "Output format?", "e.g. steps, list"),
            ("5. Tone", "Tone?", "Professional, casual"),
            ("6. Constraints", "Any limits?", "e.g. 60 sec, simple language")
        ]

# =========================================================
# 🏠 HOME PAGE
# =========================================================
if page == "🏠 Home":

    st.markdown("## ⚡ ganEEEE Prompt Magic")
    st.caption("Generate powerful AI prompts with smart guided questions.")

    st.success("🚀 AI-Powered Prompt Generator | Built by Ganesh")

    st.markdown("""
### ✨ Features
- 🧠 Smart question-based input
- 🤖 AI-generated prompts
- 📜 Prompt history tracking
- 🌍 Works for multiple use cases
""")

    user_input = st.text_input(
        "What do you want to create?",
        placeholder="e.g. resume, image, youtube script..."
    )

    intent = user_input.strip().lower() if user_input else ""

    if intent != "":

        st.info(f"🧠 Smart Mode Activated for: {user_input}")

        questions = generate_questions(intent)
        answers = {}

        st.markdown(f"""
### 👋 Let's build your prompt step-by-step

You said: **{user_input}**

Answer a few questions to generate a powerful prompt 👇
""")

        for title, question, example in questions:
            st.markdown(f"### {title}")
            answers[title] = st.text_input(question, placeholder=example, key=title)
            st.caption(f"👉 Example: {example}")

        if st.button("🚀 Generate Prompts", use_container_width=True):

            with st.spinner("Generating AI-powered prompts..."):

                prompt_input = f"User wants: {user_input}\n\nDetails:\n"

                for key, value in answers.items():
                    prompt_input += f"{key}: {value}\n"

                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {
                                "role": "system",
                                "content": "You are PromptForge AI. Generate 4 high-quality prompts in Creative, Analytical, Minimal, and Expert styles."
                            },
                            {
                                "role": "user",
                                "content": prompt_input
                            }
                        ],
                        temperature=0.7
                    )

                    output = response.choices[0].message.content

                except Exception as e:
                    output = "⚠️ Error: API limit reached or issue occurred. Please try again later."

            st.markdown("### 🔥 Generated Prompts")
            st.code(output)

            st.session_state.history.append(output)

            col1, col2 = st.columns(2)

            with col1:
                st.download_button("📥 Download", output, file_name="prompts.txt")

            with col2:
                if st.button("🔄 Regenerate"):
                    st.rerun()

# =========================================================
# 📜 HISTORY PAGE
# =========================================================
elif page == "📜 History":

    st.title("📜 Prompt History")

    if st.session_state.history:
        for item in st.session_state.history[::-1]:
            st.code(item)
    else:
        st.info("No prompts generated yet.")

# =========================================================
# ℹ️ ABOUT PAGE
# =========================================================
elif page == "ℹ️ About":

    st.title("ℹ️ About PromptForge AI")

    st.markdown("""
PromptForge AI is an intelligent prompt generator that helps users create high-quality AI prompts.

### 🚀 Use Cases
- Resume Building  
- YouTube Scripts  
- Image Generation  
- Coding & Business Ideas  

### 🛠 Tech Stack
- Streamlit  
- OpenAI API  

Built with ❤️ by Ganesh Goddilla
""")