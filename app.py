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



# import streamlit as st

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
# # 🎨 PREMIUM STYLING
# # -------------------------------
# st.markdown("""
# <style>
# body {
#     background-color: #0e1117;
# }
# .main {
#     background: linear-gradient(180deg, #0e1117 0%, #111827 100%);
# }
# h1 {
#     font-size: 42px;
#     font-weight: 700;
#     text-align: center;
# }
# .subtext {
#     text-align: center;
#     color: #9ca3af;
#     margin-bottom: 20px;
# }
# .card {
#     background: #1f2937;
#     padding: 15px;
#     border-radius: 12px;
#     margin-bottom: 10px;
# }
# .stButton>button {
#     background: linear-gradient(90deg, #4CAF50, #22c55e);
#     color: white;
#     border-radius: 12px;
#     height: 45px;
#     font-size: 16px;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # 📌 SIDEBAR
# # -------------------------------
# st.sidebar.markdown("""
# <h2 style='margin-bottom:0;'>⚡ PromptForge AI</h2>
# <p style='color:#6b7280; font-size:11px; margin-top:0;'>By Ganesh Goddilla</p>
# """, unsafe_allow_html=True)

# page = st.sidebar.radio(
#     "Navigation",
#     ["🏠 Home", "📜 History", "ℹ️ About"]
# )

# # -------------------------------
# # 🧠 FUNCTION: DYNAMIC QUESTIONS
# # -------------------------------
# def generate_questions(intent):

#     if "resume" in intent:
#         return [
#             ("Role", "Target job role?", "Software Engineer"),
#             ("Experience", "Experience level?", "Fresher"),
#             ("Skills", "Key skills?", "Python, SQL"),
#             ("Education", "Education?", "B.Tech"),
#         ]

#     elif "image" in intent:
#         return [
#             ("Type", "Image type?", "realistic"),
#             ("Subject", "Main subject?", "robot"),
#             ("Style", "Style?", "cinematic"),
#             ("Mood", "Mood?", "dark"),
#         ]

#     elif "youtube" in intent:
#         return [
#             ("Topic", "Video topic?", "AI tools"),
#             ("Audience", "Audience?", "students"),
#             ("Length", "Length?", "short"),
#             ("Tone", "Tone?", "fun"),
#         ]

#     else:
#         return [
#             ("Goal", "What do you want?", "startup idea"),
#             ("Context", "Topic?", "AI"),
#             ("Audience", "Target?", "developers"),
#             ("Tone", "Tone?", "professional"),
#         ]

# # -------------------------------
# # 🧠 SMART PROMPT ENGINE
# # -------------------------------
# def generate_prompts(user_input, answers):

#     intent = user_input.lower()

#     # 🔥 IMAGE LOGIC (SMART)
#     if "image" in intent:

#         subject = answers.get("Subject", "")
#         style = answers.get("Style", "")
#         mood = answers.get("Mood", "")
#         type_ = answers.get("Type", "")

#         base = f"{type_} {style} {mood} {subject}".strip()

#         creative = f"""
# 🔹 Prompt 1 – Creative Style  
# Create a highly detailed {type_} image of {subject} in a {style} style with a {mood} mood.  
# Include cinematic lighting, rich textures, and dynamic composition.  
# Make it visually stunning and unique.
# """

#         analytical = f"""
# 🔹 Prompt 2 – Analytical Style  
# Generate an image with the following structured details:
# - Subject: {subject}
# - Style: {style}
# - Mood: {mood}
# - Type: {type_}

# Ensure clarity, proper composition, and balanced visual elements.
# """

#         minimal = f"""
# 🔹 Prompt 3 – Minimal Style  
# {base}, high quality, detailed
# """

#         expert = f"""
# 🔹 Prompt 4 – Expert-Level Style  
# Create a {type_} {style} image of {subject} with a {mood} atmosphere.  
# Use professional photography techniques, depth of field, realistic lighting, and high-resolution detail (4K/8K).  
# Focus on composition, shadows, and cinematic realism.
# """

#         return creative + analytical + minimal + expert

#     # 🔥 DEFAULT LOGIC (OTHER USE CASES)
#     base = f"Task: {user_input}\n"
#     for k, v in answers.items():
#         base += f"- {k}: {v}\n"

#     return f"""
# 🔹 Prompt 1 – Creative  
# Act as a creative expert and generate output for:

# {base}

# 🔹 Prompt 2 – Analytical  
# Break this down step-by-step:

# {base}

# 🔹 Prompt 3 – Minimal  
# Create a short prompt for: {user_input}

# 🔹 Prompt 4 – Expert  
# Act as an industry expert and generate a high-quality prompt:

# {base}
# """

# # =========================================================
# # 🏠 HOME
# # =========================================================
# if page == "🏠 Home":

#     st.markdown("<h1>⚡ PromptForge AI</h1>", unsafe_allow_html=True)
#     st.markdown('<p class="subtext">Generate powerful prompts like a pro 🚀</p>', unsafe_allow_html=True)

#     st.markdown("""
# <div class="card">
# ✨ Create prompts for Resume, YouTube, Images, Startups & more  
# ⚡ 100% Free  
# 🧠 Smart guided system  
# </div>
# """, unsafe_allow_html=True)

#     user_input = st.text_input("What do you want to create?", placeholder="e.g. image, resume, youtube...")

#     if user_input:

#         questions = generate_questions(user_input.lower())
#         answers = {}

#         st.markdown("### ⚙️ Customize your prompt")

#         for title, question, example in questions:
#             answers[title] = st.text_input(question, placeholder=example)

#         if st.button("🚀 Generate Prompts"):

#             output = generate_prompts(user_input, answers)

#             st.markdown("### 🔥 Your Prompts")
#             st.code(output)

#             st.session_state.history.append(output)

# # =========================================================
# # 📜 HISTORY
# # =========================================================
# elif page == "📜 History":

#     st.markdown("## 📜 Prompt History")

#     if st.session_state.history:
#         for item in st.session_state.history[::-1]:
#             st.code(item)
#     else:
#         st.info("No prompts yet.")

# # =========================================================
# # ℹ️ ABOUT
# # =========================================================
# else:

#     st.markdown("## ℹ️ About")

#     st.write("""
# PromptForge AI is a smart prompt generator.
# Created By GANESH GODDILLA

# 🚀 Built for creators, developers, and entrepreneurs  
# ⚡ 100% Free version  
# 💡 Upgrade to AI-powered version anytime  
# """)


# import streamlit as st

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
# # 🎨 STYLING
# # -------------------------------
# st.markdown("""
# <style>
# body {
#     background-color: #0e1117;
# }
# .main {
#     background: linear-gradient(180deg, #0e1117 0%, #111827 100%);
# }
# h1 {
#     font-size: 42px;
#     text-align: center;
# }
# .subtext {
#     text-align: center;
#     color: #9ca3af;
# }
# .stButton>button {
#     background: linear-gradient(90deg, #4CAF50, #22c55e);
#     color: white;
#     border-radius: 10px;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # 📌 SIDEBAR
# # -------------------------------
# st.sidebar.markdown("""
# <h2 style='margin-bottom:0;'>⚡ PromptForge AI</h2>
# <p style='color:#6b7280; font-size:11px; margin-top:0;'>By Ganesh Goddilla</p>
# """, unsafe_allow_html=True)

# page = st.sidebar.radio("Navigation", ["🏠 Home", "📜 History", "ℹ️ About"])

# # -------------------------------
# # 🧠 QUESTIONS
# # -------------------------------
# def generate_questions(intent):

#     if "image" in intent:
#         return [
#             ("Type", "Image type?", "realistic"),
#             ("Subject", "Main subject?", "robot"),
#             ("Style", "Style?", "cinematic"),
#             ("Mood", "Mood?", "dark"),
#         ]

#     elif "youtube" in intent:
#         return [
#             ("Topic", "Video topic?", "AI tools"),
#             ("Audience", "Audience?", "students"),
#             ("Length", "Length?", "short"),
#             ("Tone", "Tone?", "fun"),
#         ]

#     elif "resume" in intent:
#         return [
#             ("Role", "Target role?", "Software Engineer"),
#             ("Experience", "Experience?", "Fresher"),
#             ("Skills", "Skills?", "Python, SQL"),
#         ]

#     else:
#         return [
#             ("Goal", "Goal?", "startup idea"),
#             ("Context", "Context?", "AI"),
#             ("Audience", "Audience?", "developers"),
#             ("Tone", "Tone?", "professional"),
#         ]

# # -------------------------------
# # 🧠 DYNAMIC EXAMPLES
# # -------------------------------
# def get_examples(intent, field):

#     intent = intent.lower()
#     field = field.lower()

#     if "image" in intent:
#         return {
#             "type": ["realistic", "cartoon", "3D", "illustration"],
#             "subject": ["robot", "astronaut", "lion", "product"],
#             "style": ["cinematic", "anime", "photorealistic", "cyberpunk"],
#             "mood": ["dark", "vibrant", "futuristic", "dreamy"],
#         }.get(field, [])

#     elif "youtube" in intent:
#         return {
#             "topic": ["AI tools", "motivation", "finance"],
#             "audience": ["students", "beginners", "developers"],
#             "length": ["short", "long"],
#             "tone": ["fun", "educational", "serious"],
#         }.get(field, [])

#     elif "resume" in intent:
#         return {
#             "role": ["Software Engineer", "Data Analyst", "HR"],
#             "experience": ["Fresher", "1 year", "3+ years"],
#             "skills": ["Python, SQL", "Excel, Power BI"],
#         }.get(field, [])

#     return []

# # -------------------------------
# # 🧠 PROMPT ENGINE
# # -------------------------------
# def generate_prompts(user_input, answers):

#     if "image" in user_input.lower():

#         subject = answers.get("Subject", "")
#         style = answers.get("Style", "")
#         mood = answers.get("Mood", "")
#         type_ = answers.get("Type", "")

#         return f"""
# 🔹 Prompt 1 – Creative  
# Create a highly detailed {type_} image of {subject} in a {style} style with a {mood} mood.

# 🔹 Prompt 2 – Analytical  
# Subject: {subject}, Style: {style}, Mood: {mood}, Type: {type_}

# 🔹 Prompt 3 – Minimal  
# {type_} {style} {mood} {subject}, high quality

# 🔹 Prompt 4 – Expert  
# Professional {type_} {style} image of {subject}, cinematic lighting, ultra realistic.
# """

#     # default
#     return f"Generate prompts for {user_input}"

# # =========================================================
# # 🏠 HOME
# # =========================================================
# if page == "🏠 Home":

#     st.markdown("<h1>⚡ PromptForge AI</h1>", unsafe_allow_html=True)
#     st.markdown('<p class="subtext">Generate prompts like a pro 🚀</p>', unsafe_allow_html=True)

#     user_input = st.text_input("What do you want to create?")

#     if user_input:

#         questions = generate_questions(user_input.lower())
#         answers = {}

#         st.markdown("### ⚙️ Customize your prompt")

#         for title, question, example in questions:

#             key = f"{title}_{user_input}"

#             # input
#             answers[title] = st.text_input(
#                 question,
#                 placeholder=example,
#                 key=key
#             )

#             # examples
#             examples = get_examples(user_input, title)

#             if examples:
#                 cols = st.columns(len(examples))

#                 for i, ex in enumerate(examples):
#                     with cols[i]:
#                         if st.button(ex, key=f"{key}_{ex}"):
#                             st.session_state[key] = ex
#                             st.rerun()

#         # generate
#         if st.button("🚀 Generate Prompts"):

#             output = generate_prompts(user_input, answers)

#             st.markdown("### 🔥 Output")
#             st.code(output)

#             st.session_state.history.append(output)

# # =========================================================
# # 📜 HISTORY
# # =========================================================
# elif page == "📜 History":

#     for item in st.session_state.history[::-1]:
#         st.code(item)

# # =========================================================
# # ℹ️ ABOUT
# # =========================================================
# else:

#     st.write("PromptForge AI - Free prompt generator 🚀")



# import streamlit as st

# # -------------------------------
# # 🔧 PAGE CONFIG
# # -------------------------------
# st.set_page_config(page_title="PromptForge AI", page_icon="⚡", layout="centered")

# # -------------------------------
# # 💾 SESSION STATE
# # -------------------------------
# if "history" not in st.session_state:
#     st.session_state.history = []

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# # -------------------------------
# # 🔐 LOGIN SYSTEM (FREE)
# # -------------------------------
# def login():
#     st.title("🔐 Login to PromptForge AI")

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         # Simple free login (you can change credentials)
#         if username == "admin" and password == "1234":
#             st.session_state.logged_in = True
#             st.success("Login successful 🚀")
#             st.rerun()
#         else:
#             st.error("Invalid credentials")

# # -------------------------------
# # 🎨 STYLING
# # -------------------------------
# st.markdown("""
# <style>
# body {
#     background-color: #0e1117;
# }
# .main {
#     background: linear-gradient(180deg, #0e1117 0%, #111827 100%);
# }
# .card {
#     background: #1f2937;
#     padding: 15px;
#     border-radius: 12px;
#     margin-bottom: 10px;
# }
# .stButton>button {
#     background: linear-gradient(90deg, #4CAF50, #22c55e);
#     color: white;
#     border-radius: 12px;
#     height: 45px;
#     font-size: 16px;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # 🧠 STYLE PROMPT ENGINE
# # -------------------------------
# def get_style_prompt(style):
#     if style == "Cinematic":
#         return "cinematic lighting, dramatic shadows, ultra realistic, 8k, depth of field, movie still, high contrast"
#     elif style == "Anime":
#         return "anime style, vibrant colors, sharp lines, highly detailed, dynamic pose"
#     elif style == "Realistic":
#         return "photorealistic, ultra detailed, 8k resolution, realistic textures, natural lighting"
#     elif style == "Marvel Style":
#         return "Marvel cinematic universe style, superhero aesthetics, epic pose, glowing energy, dramatic lighting"

# # -------------------------------
# # 🧠 PROMPT ENGINE
# # -------------------------------
# def generate_prompts(user_input, answers):

#     intent = user_input.lower()

#     # 🎯 ROLE-BASED PROMPTS (NEW LOGIC)
#     if "youtube" in intent:

#         topic = answers.get("Goal", "")
#         audience = answers.get("Audience", "")

#         return f"""
# 🔹 Prompt 1 – Expert Script Writer  
# Act as an experienced YouTube content creator.  
# Create an engaging script about "{topic}" for {audience}.  
# Include a strong hook, storytelling, and a clear structure (intro, main content, conclusion).  

# 🔹 Prompt 2 – Growth Focused  
# Act as a YouTube growth strategist.  
# Write a viral-ready script on "{topic}" targeting {audience}.  
# Focus on retention, curiosity gaps, and engagement techniques.  

# 🔹 Prompt 3 – Minimal  
# Write a YouTube script about "{topic}" for {audience}.  

# 🔹 Prompt 4 – Professional  
# Act as a professional scriptwriter.  
# Create a high-quality, well-structured YouTube script on "{topic}" tailored for {audience}.  
# Ensure clarity, engagement, and audience retention.
# """

#     elif "resume" in intent:

#         role = answers.get("Role", "job role")
#         skills = answers.get("Skills", "")

#         return f"""
# 🔹 Prompt 1 – Career Coach  
# You are an experienced career coach.  
# Review my resume for a "{role}" position and suggest improvements.  
# Focus on clarity, impact, and ATS optimization.  

# 🔹 Prompt 2 – Recruiter Perspective  
# Act as a recruiter hiring for "{role}".  
# Evaluate my resume and suggest what to improve to stand out.  

# 🔹 Prompt 3 – Minimal  
# Review my resume for {role}.  

# 🔹 Prompt 4 – Expert  
# Act as a senior hiring manager.  
# Provide detailed feedback on my resume for a "{role}" role, focusing on achievements, structure, and keywords.
# """

#     elif "image" in intent:

#         character = answers.get("Character", "")
#         pose = answers.get("Pose", "")
#         background = answers.get("Background", "")
#         colors = answers.get("Colors", "")
#         style = answers.get("Style", "")

#         style_prompt = get_style_prompt(style)

#         return f"""
# 🔹 Prompt 1 – Professional AI Artist  
# Act as a professional AI artist.  
# Create a highly detailed image of a {character}, {pose}, in a {background}.  
# Use {colors} color palette and {style} style.  
# Apply cinematic lighting, depth of field, and ultra-high resolution (8K).

# 🔹 Prompt 2 – Creative Direction  
# Act as a creative director.  
# Design a visually stunning {character} performing {pose} in {background},  
# with {colors} tones and {style} aesthetics.  

# 🔹 Prompt 3 – Minimal  
# {character}, {pose}, {background}, {colors}, {style}, high quality  

# 🔹 Prompt 4 – Expert-Level Prompt  
# Act as an expert prompt engineer.  
# Generate a production-quality AI image prompt for a {character} in {background},  
# with {pose}, {colors}, and {style}.  
# Include lighting, composition, textures, and realism enhancements.
# """

#     # 🔥 DEFAULT (SMART GENERIC)
#     return f"""
# 🔹 Prompt 1 – Expert  
# Act as an expert in the field.  
# Help me with: "{user_input}".  
# Provide clear, structured, and actionable output.

# 🔹 Prompt 2 – Creative  
# Act as a creative professional.  
# Generate innovative ideas for: "{user_input}".

# 🔹 Prompt 3 – Minimal  
# {user_input}

# 🔹 Prompt 4 – Professional  
# Act as an industry expert.  
# Deliver high-quality output for: "{user_input}" with clarity and depth.
# """

#     # DEFAULT
#     base = f"Task: {user_input}\n"
#     for k, v in answers.items():
#         base += f"- {k}: {v}\n"

#     return f"""
# 🔹 Prompt 1 – Creative  
# {base}

# 🔹 Prompt 2 – Analytical  
# Break step-by-step:
# {base}

# 🔹 Prompt 3 – Minimal  
# {user_input}

# 🔹 Prompt 4 – Expert  
# {base}
# """

# # -------------------------------
# # 🔐 LOGIN CHECK
# # -------------------------------
# if not st.session_state.logged_in:
#     login()
#     st.stop()

# # -------------------------------
# # 📌 SIDEBAR
# # -------------------------------
# st.sidebar.title("⚡ PromptForge AI")

# page = st.sidebar.radio(
#     "Navigation",
#     ["🏠 Home", "📜 History", "ℹ️ About"]
# )

# # =========================================================
# # 🏠 HOME
# # =========================================================
# if page == "🏠 Home":

#     st.title("⚡ PromptForge AI")
#     st.markdown("Generate powerful prompts like a pro 🚀")

#     user_input = st.text_input(
#         "What do you want to create?",
#         placeholder="e.g. image, resume, youtube..."
#     )

#     if user_input:

#         answers = {}

#         # 🔥 IMAGE UI (NEW)
#         if "image" in user_input.lower():

#             st.markdown("### 🎨 Image Settings")

#             answers["Character"] = st.text_input("Character Type", "male superhero")
#             answers["Pose"] = st.text_input("Pose", "standing confidently")
#             answers["Background"] = st.text_input("Background", "space")
#             answers["Colors"] = st.text_input("Color Theme", "pastel colors")

#             answers["Style"] = st.selectbox(
#                 "Style",
#                 ["Cinematic", "Anime", "Realistic", "Marvel Style"]
#             )

#         else:
#             answers["Goal"] = st.text_input("Goal", "startup idea")
#             answers["Audience"] = st.text_input("Audience", "developers")

#         if st.button("🚀 Generate Prompts"):

#             output = generate_prompts(user_input, answers)

#             st.markdown("### 🔥 Your Prompts")
#             st.code(output)

#             st.session_state.history.append(output)

# # =========================================================
# # 📜 HISTORY
# # =========================================================
# elif page == "📜 History":

#     st.markdown("## 📜 Prompt History")

#     if st.session_state.history:
#         for item in st.session_state.history[::-1]:
#             st.code(item)
#     else:
#         st.info("No prompts yet.")

# # =========================================================
# # ℹ️ ABOUT
# # =========================================================
# else:

#     st.markdown("## ℹ️ About")

#     st.write("""
# PromptForge AI is a smart prompt generator.

# 🚀 Built by Ganesh Goddilla
# ⚡ Free version  
# 💡 Supports image, resume, YouTube prompts  
# """)





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
# st.set_page_config(
#     page_title="PromptForge AI",
#     page_icon="⚡",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # -------------------------------
# # 🎨 PREMIUM CHATGPT-LIKE UI
# # -------------------------------
# st.markdown("""
# <style>
# /* Global */
# html, body, [class*="css"] {
#     font-family: "Inter", sans-serif;
# }

# .stApp {
#     background: linear-gradient(180deg, #0b1020 0%, #111827 100%);
#     color: #ffffff;
# }

# /* Main container */
# .block-container {
#     padding-top: 2rem;
#     padding-bottom: 2rem;
#     max-width: 1200px;
# }

# /* Sidebar */
# section[data-testid="stSidebar"] {
#     background: #0b1220;
#     border-right: 1px solid rgba(255,255,255,0.08);
# }

# /* Headings */
# h1, h2, h3, h4 {
#     color: #ffffff !important;
# }

# /* Hero Card */
# .hero-card {
#     background: linear-gradient(135deg, rgba(99,102,241,0.18), rgba(16,185,129,0.12));
#     border: 1px solid rgba(255,255,255,0.08);
#     border-radius: 24px;
#     padding: 26px;
#     margin-bottom: 22px;
#     box-shadow: 0 10px 30px rgba(0,0,0,0.25);
# }

# .hero-title {
#     font-size: 2.1rem;
#     font-weight: 800;
#     margin-bottom: 8px;
# }

# .hero-sub {
#     color: #cbd5e1;
#     font-size: 1rem;
#     line-height: 1.7;
# }

# /* Section Cards */
# .glass-card {
#     background: rgba(17, 24, 39, 0.78);
#     border: 1px solid rgba(255,255,255,0.08);
#     backdrop-filter: blur(10px);
#     border-radius: 22px;
#     padding: 22px;
#     margin-bottom: 18px;
#     box-shadow: 0 10px 24px rgba(0,0,0,0.22);
# }

# /* Feature grid */
# .feature-item {
#     background: rgba(255,255,255,0.03);
#     border: 1px solid rgba(255,255,255,0.06);
#     border-radius: 16px;
#     padding: 14px 16px;
#     margin-bottom: 10px;
#     color: #e5e7eb;
#     line-height: 1.6;
# }

# /* Prompt Output */
# .chat-shell {
#     background: #0f172a;
#     border: 1px solid rgba(255,255,255,0.08);
#     border-radius: 22px;
#     padding: 18px;
#     margin-top: 14px;
#     box-shadow: 0 10px 24px rgba(0,0,0,0.22);
# }

# .user-bubble {
#     background: #1e293b;
#     border-left: 4px solid #60a5fa;
#     padding: 16px 18px;
#     border-radius: 16px;
#     margin-bottom: 14px;
#     color: #e2e8f0;
#     line-height: 1.7;
# }

# .assistant-bubble {
#     background: #111827;
#     border-left: 4px solid #34d399;
#     padding: 18px 20px;
#     border-radius: 16px;
#     color: #f9fafb;
#     line-height: 1.9;
#     white-space: pre-wrap;
#     font-size: 15px;
# }

# /* Labels */
# .tag {
#     display: inline-block;
#     padding: 6px 10px;
#     margin-right: 8px;
#     margin-bottom: 8px;
#     border-radius: 999px;
#     background: rgba(255,255,255,0.06);
#     color: #dbeafe;
#     font-size: 13px;
#     border: 1px solid rgba(255,255,255,0.08);
# }

# /* Buttons */
# .stButton > button {
#     width: 100%;
#     background: linear-gradient(90deg, #2563eb, #7c3aed);
#     color: white;
#     border: none;
#     border-radius: 14px;
#     padding: 0.85rem 1rem;
#     font-weight: 700;
#     font-size: 15px;
#     box-shadow: 0 8px 18px rgba(37,99,235,0.25);
# }

# .stDownloadButton > button {
#     width: 100%;
#     border-radius: 14px;
#     padding: 0.85rem 1rem;
#     font-weight: 700;
#     border: 1px solid rgba(255,255,255,0.08);
#     background: #0f172a;
#     color: white;
# }

# /* Inputs */
# .stTextInput > div > div > input {
#     border-radius: 14px !important;
#     background: #0f172a !important;
#     color: white !important;
#     border: 1px solid rgba(255,255,255,0.09) !important;
#     padding: 0.8rem 1rem !important;
# }

# .small-note {
#     color: #94a3b8;
#     font-size: 13px;
#     line-height: 1.6;
# }

# hr {
#     border: none;
#     border-top: 1px solid rgba(255,255,255,0.07);
#     margin: 18px 0;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # 📌 SIDEBAR
# # -------------------------------
# st.sidebar.markdown("## ⚡ PromptForge AI")
# st.sidebar.caption("Premium prompt generation workspace")

# page = st.sidebar.radio(
#     "Navigate",
#     ["🏠 Home", "📜 History", "ℹ️ About"]
# )

# st.sidebar.markdown("---")
# st.sidebar.markdown("### Quick Use Cases")
# st.sidebar.markdown("""
# - Resume prompts  
# - Image prompts  
# - Midjourney prompts  
# - YouTube scripts  
# - Marketing copy  
# - Coding prompts  
# - Startup ideas  
# - LinkedIn content  
# """)

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
#             ("5. Skills", "Key skills?", "e.g. Python, SQL, Communication"),
#             ("6. Style", "Resume style?", "ATS-friendly or creative"),
#             ("7. Output", "1-page or 2-page?", "e.g. 1-page concise"),
#             ("8. Tone", "Tone?", "Formal / Professional")
#         ]

#     elif "image" in intent or "midjourney" in intent or "art" in intent:
#         return [
#             ("1. Image Type", "What type of image?", "e.g. realistic, cartoon, 3D"),
#             ("2. Subject", "Main subject?", "e.g. person, product, landscape"),
#             ("3. Style", "Art style?", "e.g. cinematic, anime, photorealistic"),
#             ("4. Colors", "Color theme?", "e.g. dark, vibrant, pastel"),
#             ("5. Usage", "Where will it be used?", "e.g. Instagram, thumbnail"),
#             ("6. Details", "Extra details?", "e.g. lighting, background elements"),
#             ("7. Quality", "Resolution?", "HD, 4K, ultra realistic")
#         ]

#     elif "youtube" in intent or "video" in intent or "reel" in intent:
#         return [
#             ("1. Topic", "Video topic?", "e.g. AI tools that save time"),
#             ("2. Audience", "Target audience?", "e.g. students, beginners"),
#             ("3. Duration", "Video length?", "Short or long"),
#             ("4. Style", "Video style?", "Storytelling, educational"),
#             ("5. Goal", "Purpose?", "Views, engagement"),
#             ("6. Platform", "Platform?", "YouTube Shorts / Long"),
#             ("7. Tone", "Tone?", "Energetic, fun")
#         ]

#     elif "business" in intent or "startup" in intent:
#         return [
#             ("1. Business Type", "What type of business idea do you want?", "e.g. SaaS, local business"),
#             ("2. Industry", "Which industry?", "e.g. AI, fintech, e-commerce"),
#             ("3. Target Audience", "Who is it for?", "e.g. students, founders"),
#             ("4. Goal", "What outcome do you want?", "e.g. startup idea, pitch"),
#             ("5. Format", "Output format?", "e.g. roadmap, strategy, pitch deck"),
#             ("6. Tone", "Tone?", "Professional, persuasive")
#         ]

#     elif "coding" in intent or "code" in intent or "app" in intent or "streamlit" in intent:
#         return [
#             ("1. Project Type", "What do you want to build?", "e.g. Streamlit app, website, API"),
#             ("2. Language", "Preferred language/stack?", "e.g. Python, React"),
#             ("3. Purpose", "What should it do?", "e.g. generate prompts"),
#             ("4. Users", "Who will use it?", "e.g. developers, general users"),
#             ("5. Features", "Important features?", "e.g. login, export, history"),
#             ("6. Style", "Code style?", "Beginner-friendly / production-ready")
#         ]

#     elif "marketing" in intent or "copy" in intent or "linkedin" in intent:
#         return [
#             ("1. Content Type", "What do you want to create?", "e.g. ad copy, email, landing page"),
#             ("2. Product/Service", "What are you promoting?", "e.g. AI tool"),
#             ("3. Audience", "Who is the target audience?", "e.g. founders, students"),
#             ("4. Goal", "Main objective?", "e.g. sales, clicks, signups"),
#             ("5. Tone", "Brand tone?", "e.g. bold, premium, friendly"),
#             ("6. Platform", "Where will it be used?", "e.g. Instagram, website")
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


# def build_prompt_input(user_input, answers):
#     prompt_input = f"User wants: {user_input}\n\nDetails:\n"
#     for key, value in answers.items():
#         prompt_input += f"{key}: {value}\n"
#     return prompt_input


# def format_prompt_output(raw_text):
#     if not raw_text:
#         return ""
#     return raw_text.strip().replace("```", "")


# # =========================================================
# # 🏠 HOME PAGE
# # =========================================================
# if page == "🏠 Home":

#     st.markdown("""
#     <div class="hero-card">
#         <div class="hero-title">⚡ ganEEEE Prompt Magic</div>
#         <div class="hero-sub">
#             Create premium AI prompts with smart guided questions, polished output,
#             and a modern interface that feels closer to real AI conversation tools.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     colA, colB = st.columns([1.4, 1])

#     with colA:
#         st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#         st.markdown("### ✨ Features")
#         st.markdown("""
#         <div class="feature-item">🧠 Smart question-based input flow</div>
#         <div class="feature-item">🤖 Multi-style prompt generation</div>
#         <div class="feature-item">💬 ChatGPT-style conversation layout</div>
#         <div class="feature-item">🎨 Midjourney-style image prompt writing</div>
#         <div class="feature-item">📹 YouTube, Reels, and Shorts prompt creation</div>
#         <div class="feature-item">💻 Coding, app-building, and debugging prompts</div>
#         <div class="feature-item">📈 Business, startup, and marketing prompts</div>
#         <div class="feature-item">🧾 Copywriting and brand messaging prompts</div>
#         <div class="feature-item">📜 Prompt history with cleaner display</div>
#         <div class="feature-item">📥 Export generated prompts instantly</div>
#         """, unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)

#     with colB:
#         st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#         st.markdown("### 🚀 Popular Categories")
#         st.markdown("""
#         <span class="tag">Resume</span>
#         <span class="tag">Image</span>
#         <span class="tag">Midjourney</span>
#         <span class="tag">YouTube</span>
#         <span class="tag">Coding</span>
#         <span class="tag">Marketing</span>
#         <span class="tag">Business</span>
#         <span class="tag">LinkedIn</span>
#         """, unsafe_allow_html=True)
#         st.markdown("<p class='small-note'>Tip: type something like <b>resume</b>, <b>image</b>, <b>youtube script</b>, <b>business idea</b>, or <b>coding app</b>.</p>", unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)

#     st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#     user_input = st.text_input(
#         "What do you want to create?",
#         placeholder="e.g. resume, image, youtube script, startup idea, coding prompt..."
#     )

#     intent = user_input.strip().lower() if user_input else ""

#     if intent:
#         st.success(f"🧠 Smart Mode Activated for: {user_input}")

#         questions = generate_questions(intent)
#         answers = {}

#         st.markdown("### 👋 Let’s build your prompt step-by-step")
#         st.markdown(f"<p class='small-note'>You selected: <b>{user_input}</b></p>", unsafe_allow_html=True)

#         qcol1, qcol2 = st.columns(2)
#         for i, (title, question, example) in enumerate(questions):
#             with qcol1 if i % 2 == 0 else qcol2:
#                 st.markdown(f"**{title}**")
#                 answers[title] = st.text_input(question, placeholder=example, key=title)
#                 st.caption(f"Example: {example}")

#         if st.button("🚀 Generate Prompts"):
#             with st.spinner("Generating premium prompts..."):
#                 prompt_input = build_prompt_input(user_input, answers)

#                 try:
#                     response = client.chat.completions.create(
#                         model="gpt-4o-mini",
#                         messages=[
#                             {
#                                 "role": "system",
#                                 "content": """
# You are PromptForge AI, a world-class prompt engineer.

# Generate exactly 4 prompt versions:
# 1. Creative Prompt
# 2. Analytical Prompt
# 3. Minimal Prompt
# 4. Expert Prompt

# Rules:
# - Write each version as a polished professional paragraph.
# - Make the output feel premium, natural, and ready to copy-paste.
# - Use role assignment, context, goal, constraints, tone, and output instructions.
# - Keep each version distinct in quality and style.
# - For image prompts, make them highly visual and cinematic like Midjourney-quality prompts.
# - For writing, coding, business, or resume prompts, make them structured like elite ChatGPT prompts.
# - Do not return JSON.
# - Do not wrap the answer in code fences.
# - Use clean headings for each version.
# """
#                             },
#                             {
#                                 "role": "user",
#                                 "content": prompt_input
#                             }
#                         ],
#                         temperature=0.8
#                     )

#                     output = format_prompt_output(response.choices[0].message.content)

#                 except Exception:
#                     output = "⚠️ Error: API limit reached or an unexpected issue occurred. Please try again later."

#             st.markdown("## 🔥 Prompt's Generation")

#             st.markdown(f"""
#             <div class="chat-shell">
#                 <div class="user-bubble">
#                     <b>You:</b><br>
#                     Create a premium prompt for: <b>{user_input}</b>
#                 </div>
#                 <div class="assistant-bubble">
#                     <b>PromptForge AI:</b><br><br>
#                     {output}
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)

#             st.session_state.history.append({
#                 "topic": user_input,
#                 "output": output
#             })

#             st.markdown("<br>", unsafe_allow_html=True)
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.download_button(
#                     "📥 Download Prompt",
#                     output,
#                     file_name="prompts.txt",
#                     use_container_width=True
#                 )

#             with col2:
#                 if st.button("🔄 Regenerate", use_container_width=True):
#                     st.rerun()

#     st.markdown("</div>", unsafe_allow_html=True)

# # =========================================================
# # 📜 HISTORY PAGE
# # =========================================================
# elif page == "📜 History":

#     st.markdown("""
#     <div class="hero-card">
#         <div class="hero-title">📜 Prompt History</div>
#         <div class="hero-sub">
#             Review your previously generated prompts in a cleaner conversation-style layout.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     if st.session_state.history:
#         for item in reversed(st.session_state.history):
#             topic = item["topic"] if isinstance(item, dict) else "Prompt"
#             output = item["output"] if isinstance(item, dict) else str(item)

#             st.markdown(f"""
#             <div class="chat-shell">
#                 <div class="user-bubble">
#                     <b>You:</b><br>
#                     {topic}
#                 </div>
#                 <div class="assistant-bubble">
#                     <b>PromptForge AI:</b><br><br>
#                     {output}
#                 </div>
#             </div>
#             <br>
#             """, unsafe_allow_html=True)
#     else:
#         st.info("No prompts generated yet.")

# # =========================================================
# # ℹ️ ABOUT PAGE
# # =========================================================
# elif page == "ℹ️ About":

#     st.markdown("""
#     <div class="hero-card">
#         <div class="hero-title">ℹ️ About prompts for free</div>
#         <div class="hero-sub">
#             PromptForge AI helps users generate high-quality prompts for content, images,
#             coding, business, and more through an elegant guided experience.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#     st.markdown("""
# ### 🚀 Use Cases
# - Resume Building  
# - YouTube Scripts  
# - Image Generation  
# - Midjourney Prompt Writing  
# - Coding & App Building  
# - Business Ideas  
# - Startup Validation  
# - Marketing & Copywriting  
# - LinkedIn Content  
# - Product Descriptions  
# - Social Media Captions  
# - Email Writing Prompts  

# ### 🛠 Tech Stack
# - Streamlit  
# - OpenAI API  
# - Custom CSS UI  

# Built with ❤️ by Ganesh Goddilla
# """)
#     st.markdown("</div>", unsafe_allow_html=True)







# import streamlit as st
# import textwrap

# # -------------------------------
# # PAGE CONFIG
# # -------------------------------
# st.set_page_config(
#     page_title="PromptNexus AI",
#     page_icon="🧠",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # -------------------------------
# # SESSION STATE
# # -------------------------------
# if "generated_prompt" not in st.session_state:
#     st.session_state.generated_prompt = ""

# # -------------------------------
# # CUSTOM CSS
# # -------------------------------
# st.markdown("""
# <style>
# /* Global */
# html, body, [class*="css"] {
#     font-family: 'Inter', sans-serif;
# }

# .stApp {
#     background: linear-gradient(135deg, #0B0F19 0%, #111827 40%, #0F172A 100%);
#     color: white;
# }

# /* Sidebar */
# section[data-testid="stSidebar"] {
#     background: linear-gradient(180deg, #0F172A 0%, #111827 100%);
#     border-right: 1px solid rgba(255,255,255,0.08);
# }

# .sidebar-logo {
#     padding: 14px 10px 18px 10px;
#     border-radius: 18px;
#     background: linear-gradient(135deg, rgba(108,99,255,0.15), rgba(0,212,255,0.10));
#     border: 1px solid rgba(255,255,255,0.08);
#     box-shadow: 0 0 18px rgba(108,99,255,0.18);
#     margin-bottom: 18px;
# }

# .logo-title {
#     font-size: 28px;
#     font-weight: 800;
#     line-height: 1.1;
#     background: linear-gradient(90deg, #6C63FF, #00D4FF, #A855F7);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
# }

# .logo-subtitle {
#     color: #9CA3AF;
#     font-size: 13px;
#     margin-top: 6px;
# }

# /* Main title */
# .hero-card {
#     padding: 28px;
#     border-radius: 24px;
#     background: linear-gradient(135deg, rgba(17,24,39,0.92), rgba(15,23,42,0.92));
#     border: 1px solid rgba(255,255,255,0.08);
#     box-shadow: 0 0 30px rgba(0,212,255,0.08), 0 0 50px rgba(108,99,255,0.08);
#     margin-bottom: 22px;
# }

# .hero-title {
#     font-size: 42px;
#     font-weight: 800;
#     margin-bottom: 10px;
#     background: linear-gradient(90deg, #FFFFFF, #00D4FF, #A855F7);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
# }

# .hero-desc {
#     color: #cbd5e1;
#     font-size: 16px;
#     line-height: 1.6;
# }

# /* Cards */
# .feature-card {
#     background: rgba(17,24,39,0.85);
#     border: 1px solid rgba(255,255,255,0.07);
#     border-radius: 20px;
#     padding: 18px;
#     margin-bottom: 16px;
#     box-shadow: 0 0 20px rgba(0,0,0,0.18);
# }

# .feature-title {
#     font-size: 20px;
#     font-weight: 700;
#     margin-bottom: 10px;
#     color: #E5E7EB;
# }

# .feature-text {
#     color: #9CA3AF;
#     line-height: 1.7;
#     font-size: 15px;
# }

# /* Prompt output box */
# .prompt-box {
#     background: linear-gradient(135deg, rgba(17,24,39,0.98), rgba(30,41,59,0.98));
#     border: 1px solid rgba(0,212,255,0.22);
#     border-radius: 22px;
#     padding: 24px;
#     box-shadow: 0 0 25px rgba(0,212,255,0.10), 0 0 35px rgba(168,85,247,0.10);
#     margin-top: 18px;
#     white-space: pre-wrap;
#     line-height: 1.75;
#     font-size: 16px;
#     color: #F8FAFC;
# }

# .prompt-heading {
#     font-size: 24px;
#     font-weight: 800;
#     margin-bottom: 14px;
#     color: #FFFFFF;
# }

# /* Input labels */
# label, .stSelectbox label, .stTextInput label, .stTextArea label {
#     color: #E5E7EB !important;
#     font-weight: 600 !important;
# }

# /* Buttons */
# .stButton > button {
#     width: 100%;
#     border-radius: 16px;
#     border: none;
#     padding: 0.75rem 1rem;
#     font-weight: 700;
#     font-size: 15px;
#     color: white;
#     background: linear-gradient(90deg, #6C63FF, #00D4FF);
#     box-shadow: 0 0 18px rgba(0,212,255,0.25);
#     transition: all 0.25s ease-in-out;
# }

# .stButton > button:hover {
#     transform: translateY(-2px);
#     box-shadow: 0 0 24px rgba(108,99,255,0.35);
# }

# /* Text area / inputs */
# .stTextArea textarea,
# .stTextInput input {
#     background: rgba(17,24,39,0.95) !important;
#     color: white !important;
#     border-radius: 14px !important;
#     border: 1px solid rgba(255,255,255,0.08) !important;
# }

# /* Selectbox */
# .stSelectbox div[data-baseweb="select"] > div {
#     background: rgba(17,24,39,0.95) !important;
#     border-radius: 14px !important;
#     border: 1px solid rgba(255,255,255,0.08) !important;
# }

# /* Divider heading */
# .section-title {
#     font-size: 26px;
#     font-weight: 800;
#     margin-top: 12px;
#     margin-bottom: 14px;
#     color: #F8FAFC;
# }

# /* Small badge */
# .badge {
#     display: inline-block;
#     padding: 6px 12px;
#     border-radius: 999px;
#     background: rgba(108,99,255,0.16);
#     color: #dbeafe;
#     border: 1px solid rgba(255,255,255,0.08);
#     font-size: 13px;
#     margin-bottom: 10px;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # PROMPT GENERATOR LOGIC
# # -------------------------------
# def build_prompt(use_case, topic, style, audience, extra_details):
#     style_map = {
#         "Professional": "Write in a polished, structured, professional tone with clarity and strong intent.",
#         "Creative": "Write in an imaginative, engaging, high-impact style with expressive language and originality.",
#         "Minimal": "Write in a concise, sharp, clean style with no fluff and maximum clarity.",
#         "Cinematic": "Write in a vivid, dramatic, immersive cinematic style with rich visual detail and emotional depth.",
#         "Anime": "Write in a visually expressive anime-inspired style with strong mood, dynamic imagery, and stylized details.",
#         "Realistic": "Write in a grounded, highly realistic style with precise details and practical clarity.",
#         "Expert": "Write in an advanced expert-level style with authority, precision, structure, and strategic detail."
#     }

#     base_templates = {
#         "Content Writing": f"""
# Act as an expert content strategist and professional writer. Create a high-quality prompt for {use_case.lower()} focused on "{topic}".

# The prompt should be written for {audience.lower()} and should guide the AI to produce output that is clear, engaging, useful, and well-structured. {style_map[style]}

# Make sure the final generated content includes:
# - a strong objective
# - the right tone for the target audience
# - clear structure with logical flow
# - practical, high-value output
# - polished, natural language that feels professional

# Additional context to include:
# {extra_details if extra_details else "No extra constraints provided."}

# Return the final prompt as one professional paragraph, ready to paste into ChatGPT or any advanced AI tool.
# """,

#         "Coding": f"""
# Act as a senior software engineer and AI coding assistant. Create a high-quality prompt for {use_case.lower()} focused on "{topic}".

# The prompt should help generate accurate, production-quality, well-explained output for {audience.lower()}. {style_map[style]}

# Make sure the final generated result asks for:
# - clean and correct code
# - best practices
# - clear explanations
# - modular structure
# - error handling where relevant
# - readable formatting and maintainability

# Additional context to include:
# {extra_details if extra_details else "No extra constraints provided."}

# Return the final prompt as one polished professional paragraph.
# """,

#         "Business": f"""
# Act as a strategic business consultant and prompt engineer. Create a premium-quality prompt for {use_case.lower()} focused on "{topic}".

# The prompt should be suitable for {audience.lower()} and should drive AI to produce useful, practical, and decision-oriented output. {style_map[style]}

# Ensure the prompt asks for:
# - strategic thinking
# - clarity and business relevance
# - actionable insights
# - professional tone
# - organized response structure
# - realistic recommendations

# Additional context to include:
# {extra_details if extra_details else "No extra constraints provided."}

# Return the final prompt as one refined paragraph that sounds premium and professional.
# """,

#         "Students": f"""
# Act as an educational mentor and smart AI tutor. Create a high-quality prompt for {use_case.lower()} focused on "{topic}".

# The prompt should be designed for {audience.lower()} and should help the AI deliver clear, accurate, easy-to-understand, and valuable educational support. {style_map[style]}

# Ensure the prompt requests:
# - step-by-step clarity
# - simple but intelligent explanations
# - structured output
# - practical examples where useful
# - beginner-friendly understanding without losing quality

# Additional context to include:
# {extra_details if extra_details else "No extra constraints provided."}

# Return the final prompt as one polished and user-friendly paragraph.
# """,

#         "General Use": f"""
# Act as a world-class AI assistant and prompt engineer. Create a premium-quality prompt for {use_case.lower()} focused on "{topic}".

# The prompt should be useful for {audience.lower()} and should produce a clear, intelligent, high-quality result. {style_map[style]}

# Ensure the prompt asks for:
# - accurate output
# - strong clarity
# - professional structure
# - relevant detail
# - polished natural language
# - a result that feels thoughtful and high-value

# Additional context to include:
# {extra_details if extra_details else "No extra constraints provided."}

# Return the final prompt as one strong, professional paragraph ready for direct use.
# """
#     }

#     prompt = base_templates.get(use_case, base_templates["General Use"])
#     return " ".join(prompt.split())


# # -------------------------------
# # SIDEBAR
# # -------------------------------
# with st.sidebar:
#     st.markdown("""
#     <div class="sidebar-logo">
#         <div class="logo-title">PromptNexus AI</div>
#         <div class="logo-subtitle">Where prompts become intelligence.</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("### ⚡ Use Cases")
#     st.markdown("""
#     - Content Writing  
#     - Coding  
#     - Business Ideas  
#     - Resume Building  
#     - Marketing  
#     - Startup Planning  
#     - Study Help  
#     - Social Media  
#     - Product Descriptions  
#     - Email Writing  
#     - YouTube Scripts  
#     - Image Generation Prompts  
#     """)

#     st.markdown("### 🎨 Prompt Styles")
#     st.markdown("""
#     - Professional  
#     - Creative  
#     - Minimal  
#     - Cinematic  
#     - Anime  
#     - Realistic  
#     - Expert  
#     """)

# # -------------------------------
# # HERO SECTION
# # -------------------------------
# st.markdown("""
# <div class="hero-card">
#     <div class="badge">🚀 AI Prompt Workspace</div>
#     <div class="hero-title">PromptNexus AI</div>
#     <div class="hero-desc">
#         Generate premium, professional, and ready-to-use prompts for content, coding, business, student needs, and more.
#         Designed with a futuristic SaaS-style interface for a cleaner and smarter prompting experience.
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # -------------------------------
# # INPUT SECTION
# # -------------------------------
# col1, col2 = st.columns(2)

# with col1:
#     use_case = st.selectbox(
#         "Select Use Case",
#         ["Content Writing", "Coding", "Business", "Students", "General Use"]
#     )

#     topic = st.text_input("Topic / Goal", placeholder="e.g. YouTube script for AI tools, portfolio website, resume rewrite")

# with col2:
#     style = st.selectbox(
#         "Prompt Style",
#         ["Professional", "Creative", "Minimal", "Cinematic", "Anime", "Realistic", "Expert"]
#     )

#     audience = st.text_input("Target Audience", placeholder="e.g. beginners, developers, recruiters, startup founders")

# extra_details = st.text_area(
#     "Extra Details / Requirements",
#     placeholder="Add constraints, tone, platform, format, keywords, output expectations, etc.",
#     height=140
# )

# # -------------------------------
# # BUTTONS
# # -------------------------------
# btn1, btn2 = st.columns([2, 1])

# with btn1:
#     if st.button("✨ Generate Prompt"):
#         if topic.strip():
#             st.session_state.generated_prompt = build_prompt(
#                 use_case=use_case,
#                 topic=topic,
#                 style=style,
#                 audience=audience if audience.strip() else "general users",
#                 extra_details=extra_details
#             )
#         else:
#             st.warning("Please enter a topic or goal first.")

# with btn2:
#     if st.button("🗑 Clear"):
#         st.session_state.generated_prompt = ""

# # -------------------------------
# # OUTPUT SECTION
# # -------------------------------
# st.markdown('<div class="section-title">Prompt’s Generation</div>', unsafe_allow_html=True)

# if st.session_state.generated_prompt:
#     st.markdown(
#         f"""
#         <div class="prompt-box">
#             <div class="prompt-heading">🎯 Prompt</div>
#             {st.session_state.generated_prompt}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

#     st.text_area(
#         "Copy Prompt",
#         value=st.session_state.generated_prompt,
#         height=220
#     )
# else:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">No prompt generated yet</div>
#         <div class="feature-text">
#             Fill in your topic, choose a style, and click <b>Generate Prompt</b> to create a polished AI-ready prompt.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# # -------------------------------
# # FEATURES SECTION
# # -------------------------------
# st.markdown('<div class="section-title">Why PromptNexus AI?</div>', unsafe_allow_html=True)

# f1, f2, f3 = st.columns(3)

# with f1:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">🧠 Smart Prompt Structuring</div>
#         <div class="feature-text">
#             Generates prompts that feel refined, goal-oriented, and professional instead of random one-line instructions.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with f2:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">🎨 Multi-Style Output</div>
#         <div class="feature-text">
#             Switch between professional, creative, cinematic, anime, realistic, and expert styles based on your exact use case.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with f3:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">⚡ Ready for Real Work</div>
#         <div class="feature-text">
#             Useful for content creators, developers, students, marketers, founders, freelancers, and AI enthusiasts.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# # -------------------------------
# # FOOTER
# # -------------------------------
# st.markdown("""
# <br>
# <div style="text-align:center; color:#94A3B8; font-size:14px; padding-bottom:10px;">
#     Built with ❤️ By Ganesh Goddilla for smarter prompting • <b>PromptNexus AI</b>
# </div>
# """, unsafe_allow_html=True)




# import streamlit as st

# # -------------------------------
# # PAGE CONFIG
# # -------------------------------
# st.set_page_config(
#     page_title="PromptNexus AI",
#     page_icon="🧠",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # -------------------------------
# # SESSION STATE
# # -------------------------------
# if "generated_prompt" not in st.session_state:
#     st.session_state.generated_prompt = ""

# # -------------------------------
# # CUSTOM CSS
# # -------------------------------
# st.markdown("""
# <style>
# html, body, [class*="css"] {
#     font-family: 'Inter', sans-serif;
# }

# .stApp {
#     background: linear-gradient(135deg, #0B0F19 0%, #111827 40%, #0F172A 100%);
#     color: white;
# }

# section[data-testid="stSidebar"] {
#     background: linear-gradient(180deg, #0F172A 0%, #111827 100%);
#     border-right: 1px solid rgba(255,255,255,0.08);
# }

# .sidebar-logo {
#     padding: 14px 10px 18px 10px;
#     border-radius: 18px;
#     background: linear-gradient(135deg, rgba(108,99,255,0.15), rgba(0,212,255,0.10));
#     border: 1px solid rgba(255,255,255,0.08);
#     box-shadow: 0 0 18px rgba(108,99,255,0.18);
#     margin-bottom: 18px;
# }

# .logo-title {
#     font-size: 28px;
#     font-weight: 800;
#     line-height: 1.1;
#     background: linear-gradient(90deg, #6C63FF, #00D4FF, #A855F7);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
# }

# .logo-subtitle {
#     color: #9CA3AF;
#     font-size: 13px;
#     margin-top: 6px;
# }

# .hero-card {
#     padding: 28px;
#     border-radius: 24px;
#     background: linear-gradient(135deg, rgba(17,24,39,0.92), rgba(15,23,42,0.92));
#     border: 1px solid rgba(255,255,255,0.08);
#     box-shadow: 0 0 30px rgba(0,212,255,0.08), 0 0 50px rgba(108,99,255,0.08);
#     margin-bottom: 22px;
# }

# .hero-title {
#     font-size: 42px;
#     font-weight: 800;
#     margin-bottom: 10px;
#     background: linear-gradient(90deg, #FFFFFF, #00D4FF, #A855F7);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
# }

# .hero-desc {
#     color: #cbd5e1;
#     font-size: 16px;
#     line-height: 1.6;
# }

# .feature-card {
#     background: rgba(17,24,39,0.85);
#     border: 1px solid rgba(255,255,255,0.07);
#     border-radius: 20px;
#     padding: 18px;
#     margin-bottom: 16px;
#     box-shadow: 0 0 20px rgba(0,0,0,0.18);
# }

# .feature-title {
#     font-size: 20px;
#     font-weight: 700;
#     margin-bottom: 10px;
#     color: #E5E7EB;
# }

# .feature-text {
#     color: #9CA3AF;
#     line-height: 1.7;
#     font-size: 15px;
# }

# .prompt-box {
#     background: linear-gradient(135deg, rgba(17,24,39,0.98), rgba(30,41,59,0.98));
#     border: 1px solid rgba(0,212,255,0.22);
#     border-radius: 22px;
#     padding: 24px;
#     box-shadow: 0 0 25px rgba(0,212,255,0.10), 0 0 35px rgba(168,85,247,0.10);
#     margin-top: 18px;
#     white-space: pre-wrap;
#     line-height: 1.75;
#     font-size: 16px;
#     color: #F8FAFC;
# }

# .prompt-heading {
#     font-size: 24px;
#     font-weight: 800;
#     margin-bottom: 14px;
#     color: #FFFFFF;
# }

# label, .stSelectbox label, .stTextInput label, .stTextArea label {
#     color: #E5E7EB !important;
#     font-weight: 600 !important;
# }

# .stButton > button {
#     width: 100%;
#     border-radius: 16px;
#     border: none;
#     padding: 0.75rem 1rem;
#     font-weight: 700;
#     font-size: 15px;
#     color: white;
#     background: linear-gradient(90deg, #6C63FF, #00D4FF);
#     box-shadow: 0 0 18px rgba(0,212,255,0.25);
#     transition: all 0.25s ease-in-out;
# }

# .stButton > button:hover {
#     transform: translateY(-2px);
#     box-shadow: 0 0 24px rgba(108,99,255,0.35);
# }

# .stTextArea textarea,
# .stTextInput input {
#     background: rgba(17,24,39,0.95) !important;
#     color: white !important;
#     border-radius: 14px !important;
#     border: 1px solid rgba(255,255,255,0.08) !important;
# }

# .stSelectbox div[data-baseweb="select"] > div {
#     background: rgba(17,24,39,0.95) !important;
#     border-radius: 14px !important;
#     border: 1px solid rgba(255,255,255,0.08) !important;
# }

# .section-title {
#     font-size: 26px;
#     font-weight: 800;
#     margin-top: 12px;
#     margin-bottom: 14px;
#     color: #F8FAFC;
# }

# .badge {
#     display: inline-block;
#     padding: 6px 12px;
#     border-radius: 999px;
#     background: rgba(108,99,255,0.16);
#     color: #dbeafe;
#     border: 1px solid rgba(255,255,255,0.08);
#     font-size: 13px;
#     margin-bottom: 10px;
# }

# .example-box {
#     background: rgba(17,24,39,0.72);
#     border: 1px solid rgba(255,255,255,0.06);
#     border-radius: 16px;
#     padding: 14px 16px;
#     margin-top: 8px;
#     margin-bottom: 10px;
#     color: #cbd5e1;
#     font-size: 14px;
#     line-height: 1.7;
# }

# .small-note {
#     color: #94A3B8;
#     font-size: 13px;
#     margin-top: -5px;
#     margin-bottom: 12px;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # USE CASE DATA
# # -------------------------------
# USE_CASE_CONFIG = {
#     "Content Writing": {
#         "topic_placeholder": "e.g. Write a blog post on AI tools for productivity",
#         "audience_placeholder": "e.g. content creators, bloggers, marketers",
#         "extra_placeholder": "Add tone, content length, SEO keywords, platform, CTA, and format needs.",
#         "examples": [
#             "Instagram caption for a fitness brand launch",
#             "SEO blog post on beginner MLOps roadmap",
#             "LinkedIn post about GenAI career transition"
#         ]
#     },
#     "Coding": {
#         "topic_placeholder": "e.g. Build a Python script for file organizer automation",
#         "audience_placeholder": "e.g. Python developers, beginners, backend engineers",
#         "extra_placeholder": "Mention language, framework, output format, best practices, edge cases, and constraints.",
#         "examples": [
#             "Streamlit app for AI prompt generator",
#             "FastAPI REST API with authentication",
#             "Python function to parse logs and summarize errors"
#         ]
#     },
#     "Business": {
#         "topic_placeholder": "e.g. Create a startup idea for AI resume review tool",
#         "audience_placeholder": "e.g. startup founders, consultants, entrepreneurs",
#         "extra_placeholder": "Mention industry, target market, budget, revenue model, and strategic goals.",
#         "examples": [
#             "Business plan for a faceless YouTube automation agency",
#             "Pricing strategy for AI SaaS tool",
#             "Go-to-market plan for student productivity app"
#         ]
#     },
#     "Students": {
#         "topic_placeholder": "e.g. Explain neural networks in simple terms",
#         "audience_placeholder": "e.g. school students, college students, exam aspirants",
#         "extra_placeholder": "Mention difficulty level, subject, exam type, explanation style, and examples needed.",
#         "examples": [
#             "Study notes for DBMS interview preparation",
#             "Simple explanation of cloud computing",
#             "5-mark answer for machine learning basics"
#         ]
#     },
#     "General Use": {
#         "topic_placeholder": "e.g. Write a professional email requesting project access",
#         "audience_placeholder": "e.g. professionals, general users, freelancers",
#         "extra_placeholder": "Mention tone, context, recipient, expected format, and any important details.",
#         "examples": [
#             "Professional apology email to manager",
#             "Daily planner for a productive workday",
#             "Checklist for moving to a new city"
#         ]
#     },
#     "Marketing": {
#         "topic_placeholder": "e.g. Create ad copy for eco-friendly water bottle",
#         "audience_placeholder": "e.g. customers, marketers, D2C brands",
#         "extra_placeholder": "Mention platform, product, brand voice, CTA, target market, and campaign goal.",
#         "examples": [
#             "Facebook ad copy for skincare product",
#             "Email campaign for Black Friday sale",
#             "Brand tagline ideas for AI startup"
#         ]
#     },
#     "Resume / Career": {
#         "topic_placeholder": "e.g. Rewrite my resume summary for MLOps engineer role",
#         "audience_placeholder": "e.g. recruiters, hiring managers, job seekers",
#         "extra_placeholder": "Mention target role, years of experience, industry, skills, and desired tone.",
#         "examples": [
#             "Resume bullet points for Python developer",
#             "Cover letter for GenAI engineer role",
#             "LinkedIn About section for fresher in MLOps"
#         ]
#     },
#     "Startup Ideas": {
#         "topic_placeholder": "e.g. Generate startup ideas using GenAI in education",
#         "audience_placeholder": "e.g. founders, investors, builders",
#         "extra_placeholder": "Mention niche, monetization preference, user pain points, and level of innovation.",
#         "examples": [
#             "Low-cost AI SaaS ideas for India",
#             "B2B startup idea for internal documentation",
#             "One-person startup ideas in automation"
#         ]
#     },
#     "Social Media": {
#         "topic_placeholder": "e.g. Create 10 reel ideas for AI productivity content",
#         "audience_placeholder": "e.g. Instagram audience, creators, YouTube viewers",
#         "extra_placeholder": "Mention platform, tone, niche, content length, hook style, and target audience.",
#         "examples": [
#             "YouTube Shorts script on AI tools",
#             "Twitter thread on beginner coding mistakes",
#             "Instagram carousel post on career growth"
#         ]
#     },
#     "Email Writing": {
#         "topic_placeholder": "e.g. Draft an email asking for project status update",
#         "audience_placeholder": "e.g. manager, HR, client, colleague",
#         "extra_placeholder": "Mention sender intent, recipient, tone, urgency, and required action.",
#         "examples": [
#             "Leave request email",
#             "Follow-up email after interview",
#             "Formal escalation email for blocked task"
#         ]
#     },
#     "Image Generation": {
#         "topic_placeholder": "e.g. Create a cinematic superhero portrait in space",
#         "audience_placeholder": "e.g. Midjourney users, designers, creators",
#         "extra_placeholder": "Mention art style, camera angle, lighting, composition, mood, colors, and quality.",
#         "examples": [
#             "Anime warrior in neon city at night",
#             "Luxury product ad shot with soft lighting",
#             "Marvel-style superhero poster in pastel space"
#         ]
#     },
#     "YouTube Scripts": {
#         "topic_placeholder": "e.g. Write a 60-second YouTube script on top AI tools",
#         "audience_placeholder": "e.g. YouTube viewers, beginners, tech audience",
#         "extra_placeholder": "Mention niche, duration, hook style, CTA, tone, and retention style.",
#         "examples": [
#             "60-second script for motivation reel",
#             "Faceless finance video script",
#             "Tech explainer script on ChatGPT vs OpenAI"
#         ]
#     }
# }

# # -------------------------------
# # PROMPT GENERATOR LOGIC
# # -------------------------------
# def build_prompt(use_case, topic, style, audience, extra_details):
#     style_map = {
#         "Professional": "Write in a polished, structured, professional tone with clarity and strong intent.",
#         "Creative": "Write in an imaginative, engaging, high-impact style with expressive language and originality.",
#         "Minimal": "Write in a concise, sharp, clean style with no fluff and maximum clarity.",
#         "Cinematic": "Write in a vivid, dramatic, immersive cinematic style with rich visual detail and emotional depth.",
#         "Anime": "Write in a visually expressive anime-inspired style with strong mood, dynamic imagery, and stylized details.",
#         "Realistic": "Write in a grounded, highly realistic style with precise details and practical clarity.",
#         "Expert": "Write in an advanced expert-level style with authority, precision, structure, and strategic detail."
#     }

#     base_instruction = f"""
# Act as an expert AI prompt engineer. Create a premium, highly effective prompt for the use case "{use_case}" focused on "{topic}".

# The prompt should be designed for {audience.lower()} and should generate output that is useful, clear, professional, and context-aware. {style_map[style]}

# The final prompt must:
# - clearly define the AI's role
# - describe the task with strong intent
# - include the right tone and structure
# - request detailed, high-quality output
# - feel polished and ready for direct use in ChatGPT or any advanced AI tool

# Additional requirements and context:
# {extra_details if extra_details.strip() else "No extra constraints provided."}

# Return only one strong, refined, professional paragraph prompt.
# """

#     use_case_addons = {
#         "Content Writing": "Make the prompt optimized for strong writing quality, readability, audience engagement, and content structure.",
#         "Coding": "Make the prompt optimized for clean code, correct logic, maintainability, explanations, and best practices.",
#         "Business": "Make the prompt optimized for strategic thinking, actionable insights, market relevance, and practical recommendations.",
#         "Students": "Make the prompt optimized for clear explanation, step-by-step teaching, easy understanding, and educational value.",
#         "General Use": "Make the prompt optimized for flexibility, clarity, and practical usefulness.",
#         "Marketing": "Make the prompt optimized for conversion, audience targeting, brand tone, persuasion, and campaign effectiveness.",
#         "Resume / Career": "Make the prompt optimized for hiring impact, clarity, ATS-friendly quality, and professional career positioning.",
#         "Startup Ideas": "Make the prompt optimized for innovation, business viability, target user pain points, and monetization potential.",
#         "Social Media": "Make the prompt optimized for attention-grabbing hooks, engagement, clarity, and platform-specific performance.",
#         "Email Writing": "Make the prompt optimized for professionalism, tone control, clarity, and actionable communication.",
#         "Image Generation": "Make the prompt optimized for visual richness, style clarity, composition, mood, camera details, and generation quality.",
#         "YouTube Scripts": "Make the prompt optimized for retention, hook strength, clear script flow, audience engagement, and strong CTA."
#     }

#     full_prompt = f"{base_instruction} {use_case_addons.get(use_case, '')}"
#     return " ".join(full_prompt.split())

# # -------------------------------
# # SIDEBAR
# # -------------------------------
# with st.sidebar:
#     st.markdown("""
#     <div class="sidebar-logo">
#         <div class="logo-title">PromptNexus AI</div>
#         <div class="logo-subtitle">Where prompts become intelligence.</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("### ⚡ Use Cases")
#     st.markdown("""
#     - Content Writing  
#     - Coding  
#     - Business  
#     - Students  
#     - Marketing  
#     - Resume / Career  
#     - Startup Ideas  
#     - Social Media  
#     - Email Writing  
#     - Image Generation  
#     - YouTube Scripts  
#     - General Use  
#     """)

#     st.markdown("### 🎨 Prompt Styles")
#     st.markdown("""
#     - Professional  
#     - Creative  
#     - Minimal  
#     - Cinematic  
#     - Anime  
#     - Realistic  
#     - Expert  
#     """)

# # -------------------------------
# # HERO
# # -------------------------------
# st.markdown("""
# <div class="hero-card">
#     <div class="badge">🚀 AI Prompt Workspace</div>
#     <div class="hero-title">PromptNexus AI</div>
#     <div class="hero-desc">
#         Generate premium, professional, and ready-to-use prompts for content, coding, marketing, career growth,
#         startup ideas, image generation, YouTube scripts, and more — all inside a futuristic SaaS-style interface.
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # -------------------------------
# # INPUTS
# # -------------------------------
# use_case_options = list(USE_CASE_CONFIG.keys())

# col1, col2 = st.columns(2)

# with col1:
#     use_case = st.selectbox("Select Use Case", use_case_options)

# config = USE_CASE_CONFIG[use_case]

# with col2:
#     style = st.selectbox(
#         "Prompt Style",
#         ["Professional", "Creative", "Minimal", "Cinematic", "Anime", "Realistic", "Expert"]
#     )

# col3, col4 = st.columns(2)

# with col3:
#     topic = st.text_input(
#         "Topic / Goal",
#         placeholder=config["topic_placeholder"]
#     )
#     st.markdown(
#         f"""
#         <div class="example-box">
#             <b>Examples for {use_case}:</b><br>
#             • {config["examples"][0]}<br>
#             • {config["examples"][1]}<br>
#             • {config["examples"][2]}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# with col4:
#     audience = st.text_input(
#         "Target Audience",
#         placeholder=config["audience_placeholder"]
#     )
#     st.markdown(
#         '<div class="small-note">Audience can also change based on use case selection.</div>',
#         unsafe_allow_html=True
#     )

# extra_details = st.text_area(
#     "Extra Details / Requirements",
#     placeholder=config["extra_placeholder"],
#     height=150
# )

# # -------------------------------
# # BUTTONS
# # -------------------------------
# btn1, btn2 = st.columns([2, 1])

# with btn1:
#     if st.button("✨ Generate Prompt"):
#         if topic.strip():
#             st.session_state.generated_prompt = build_prompt(
#                 use_case=use_case,
#                 topic=topic,
#                 style=style,
#                 audience=audience.strip() if audience.strip() else "general users",
#                 extra_details=extra_details
#             )
#         else:
#             st.warning("Please enter a Topic / Goal first.")

# with btn2:
#     if st.button("🗑 Clear"):
#         st.session_state.generated_prompt = ""

# # -------------------------------
# # OUTPUT
# # -------------------------------
# st.markdown('<div class="section-title">Prompt’s Generation</div>', unsafe_allow_html=True)

# if st.session_state.generated_prompt:
#     st.markdown(
#         f"""
#         <div class="prompt-box">
#             <div class="prompt-heading">🎯 Prompt</div>
#             {st.session_state.generated_prompt}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

#     st.text_area(
#         "Copy Prompt",
#         value=st.session_state.generated_prompt,
#         height=220
#     )
# else:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">No prompt generated yet</div>
#         <div class="feature-text">
#             Select a use case, review the dynamic examples, enter your topic, and click <b>Generate Prompt</b>.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# # -------------------------------
# # FEATURES
# # -------------------------------
# st.markdown('<div class="section-title">Why PromptNexus AI?</div>', unsafe_allow_html=True)

# f1, f2, f3 = st.columns(3)

# with f1:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">🧠 Dynamic Smart Guidance</div>
#         <div class="feature-text">
#             Topic examples and placeholders change automatically based on the selected use case, making prompt creation faster and smarter.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with f2:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">🎨 More Use Cases</div>
#         <div class="feature-text">
#             Covers writing, coding, marketing, social media, resumes, startup ideas, image prompts, YouTube scripts, and more.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with f3:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">⚡ Professional Prompt Quality</div>
#         <div class="feature-text">
#             Generates refined paragraph-style prompts that feel closer to premium AI workflow tools instead of basic prompt templates.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# # -------------------------------
# # FOOTER
# # -------------------------------
# st.markdown("""
# <br>
# <div style="text-align:center; color:#94A3B8; font-size:14px; padding-bottom:10px;">
#     Built with ❤️ By Ganesh Goddilla for smarter prompting • <b>PromptNexus AI</b>
# </div>
# """, unsafe_allow_html=True)




# import streamlit as st
# import streamlit.components.v1 as components
# import html

# # -------------------------------
# # PAGE CONFIG
# # -------------------------------
# st.set_page_config(
#     page_title="PromptNexus AI",
#     page_icon="🧠",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # -------------------------------
# # SESSION STATE
# # -------------------------------
# if "generated_prompt" not in st.session_state:
#     st.session_state.generated_prompt = ""

# # -------------------------------
# # CUSTOM CSS
# # -------------------------------
# st.markdown("""
# <style>
# html, body, [class*="css"] {
#     font-family: 'Inter', sans-serif;
# }

# .stApp {
#     background: linear-gradient(135deg, #0B0F19 0%, #111827 40%, #0F172A 100%);
#     color: white;
# }

# section[data-testid="stSidebar"] {
#     background: linear-gradient(180deg, #0F172A 0%, #111827 100%);
#     border-right: 1px solid rgba(255,255,255,0.08);
# }

# .sidebar-logo {
#     padding: 14px 10px 18px 10px;
#     border-radius: 18px;
#     background: linear-gradient(135deg, rgba(108,99,255,0.15), rgba(0,212,255,0.10));
#     border: 1px solid rgba(255,255,255,0.08);
#     box-shadow: 0 0 18px rgba(108,99,255,0.18);
#     margin-bottom: 18px;
# }

# .logo-title {
#     font-size: 28px;
#     font-weight: 800;
#     line-height: 1.1;
#     background: linear-gradient(90deg, #6C63FF, #00D4FF, #A855F7);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
# }

# .logo-subtitle {
#     color: #9CA3AF;
#     font-size: 13px;
#     margin-top: 6px;
# }

# .hero-card {
#     padding: 28px;
#     border-radius: 24px;
#     background: linear-gradient(135deg, rgba(17,24,39,0.92), rgba(15,23,42,0.92));
#     border: 1px solid rgba(255,255,255,0.08);
#     box-shadow: 0 0 30px rgba(0,212,255,0.08), 0 0 50px rgba(108,99,255,0.08);
#     margin-bottom: 22px;
# }

# .hero-title {
#     font-size: 42px;
#     font-weight: 800;
#     margin-bottom: 10px;
#     background: linear-gradient(90deg, #FFFFFF, #00D4FF, #A855F7);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
# }

# .hero-desc {
#     color: #cbd5e1;
#     font-size: 16px;
#     line-height: 1.6;
# }

# .feature-card {
#     background: rgba(17,24,39,0.85);
#     border: 1px solid rgba(255,255,255,0.07);
#     border-radius: 20px;
#     padding: 18px;
#     margin-bottom: 16px;
#     box-shadow: 0 0 20px rgba(0,0,0,0.18);
# }

# .feature-title {
#     font-size: 20px;
#     font-weight: 700;
#     margin-bottom: 10px;
#     color: #E5E7EB;
# }

# .feature-text {
#     color: #9CA3AF;
#     line-height: 1.7;
#     font-size: 15px;
# }

# label, .stSelectbox label, .stTextInput label, .stTextArea label {
#     color: #E5E7EB !important;
#     font-weight: 600 !important;
# }

# .stButton > button {
#     width: 100%;
#     border-radius: 16px;
#     border: none;
#     padding: 0.75rem 1rem;
#     font-weight: 700;
#     font-size: 15px;
#     color: white;
#     background: linear-gradient(90deg, #6C63FF, #00D4FF);
#     box-shadow: 0 0 18px rgba(0,212,255,0.25);
#     transition: all 0.25s ease-in-out;
# }

# .stButton > button:hover {
#     transform: translateY(-2px);
#     box-shadow: 0 0 24px rgba(108,99,255,0.35);
# }

# .stTextArea textarea,
# .stTextInput input {
#     background: rgba(17,24,39,0.95) !important;
#     color: white !important;
#     border-radius: 14px !important;
#     border: 1px solid rgba(255,255,255,0.08) !important;
# }

# .stSelectbox div[data-baseweb="select"] > div {
#     background: rgba(17,24,39,0.95) !important;
#     border-radius: 14px !important;
#     border: 1px solid rgba(255,255,255,0.08) !important;
# }

# .section-title {
#     font-size: 26px;
#     font-weight: 800;
#     margin-top: 12px;
#     margin-bottom: 14px;
#     color: #F8FAFC;
# }

# .badge {
#     display: inline-block;
#     padding: 6px 12px;
#     border-radius: 999px;
#     background: rgba(108,99,255,0.16);
#     color: #dbeafe;
#     border: 1px solid rgba(255,255,255,0.08);
#     font-size: 13px;
#     margin-bottom: 10px;
# }

# .example-box {
#     background: rgba(17,24,39,0.72);
#     border: 1px solid rgba(255,255,255,0.06);
#     border-radius: 16px;
#     padding: 14px 16px;
#     margin-top: 8px;
#     margin-bottom: 10px;
#     color: #cbd5e1;
#     font-size: 14px;
#     line-height: 1.7;
# }

# .small-note {
#     color: #94A3B8;
#     font-size: 13px;
#     margin-top: -5px;
#     margin-bottom: 12px;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # USE CASE DATA
# # -------------------------------
# USE_CASE_CONFIG = {
#     "Content Writing": {
#         "topic_placeholder": "e.g. Write a blog post on AI tools for productivity",
#         "audience_placeholder": "e.g. content creators, bloggers, marketers",
#         "extra_placeholder": "Add tone, content length, SEO keywords, platform, CTA, and format needs.",
#         "examples": [
#             "Instagram caption for a fitness brand launch",
#             "SEO blog post on beginner MLOps roadmap",
#             "LinkedIn post about GenAI career transition"
#         ]
#     },
#     "Coding": {
#         "topic_placeholder": "e.g. Build a Python script for file organizer automation",
#         "audience_placeholder": "e.g. Python developers, beginners, backend engineers",
#         "extra_placeholder": "Mention language, framework, output format, best practices, edge cases, and constraints.",
#         "examples": [
#             "Streamlit app for AI prompt generator",
#             "FastAPI REST API with authentication",
#             "Python function to parse logs and summarize errors"
#         ]
#     },
#     "Business": {
#         "topic_placeholder": "e.g. Create a startup idea for AI resume review tool",
#         "audience_placeholder": "e.g. startup founders, consultants, entrepreneurs",
#         "extra_placeholder": "Mention industry, target market, budget, revenue model, and strategic goals.",
#         "examples": [
#             "Business plan for a faceless YouTube automation agency",
#             "Pricing strategy for AI SaaS tool",
#             "Go-to-market plan for student productivity app"
#         ]
#     },
#     "Students": {
#         "topic_placeholder": "e.g. Explain neural networks in simple terms",
#         "audience_placeholder": "e.g. school students, college students, exam aspirants",
#         "extra_placeholder": "Mention difficulty level, subject, exam type, explanation style, and examples needed.",
#         "examples": [
#             "Study notes for DBMS interview preparation",
#             "Simple explanation of cloud computing",
#             "5-mark answer for machine learning basics"
#         ]
#     },
#     "General Use": {
#         "topic_placeholder": "e.g. Write a professional email requesting project access",
#         "audience_placeholder": "e.g. professionals, general users, freelancers",
#         "extra_placeholder": "Mention tone, context, recipient, expected format, and any important details.",
#         "examples": [
#             "Professional apology email to manager",
#             "Daily planner for a productive workday",
#             "Checklist for moving to a new city"
#         ]
#     },
#     "Marketing": {
#         "topic_placeholder": "e.g. Create ad copy for eco-friendly water bottle",
#         "audience_placeholder": "e.g. customers, marketers, D2C brands",
#         "extra_placeholder": "Mention platform, product, brand voice, CTA, target market, and campaign goal.",
#         "examples": [
#             "Facebook ad copy for skincare product",
#             "Email campaign for Black Friday sale",
#             "Brand tagline ideas for AI startup"
#         ]
#     },
#     "Resume / Career": {
#         "topic_placeholder": "e.g. Rewrite my resume summary for MLOps engineer role",
#         "audience_placeholder": "e.g. recruiters, hiring managers, job seekers",
#         "extra_placeholder": "Mention target role, years of experience, industry, skills, and desired tone.",
#         "examples": [
#             "Resume bullet points for Python developer",
#             "Cover letter for GenAI engineer role",
#             "LinkedIn About section for fresher in MLOps"
#         ]
#     },
#     "Startup Ideas": {
#         "topic_placeholder": "e.g. Generate startup ideas using GenAI in education",
#         "audience_placeholder": "e.g. founders, investors, builders",
#         "extra_placeholder": "Mention niche, monetization preference, user pain points, and level of innovation.",
#         "examples": [
#             "Low-cost AI SaaS ideas for India",
#             "B2B startup idea for internal documentation",
#             "One-person startup ideas in automation"
#         ]
#     },
#     "Social Media": {
#         "topic_placeholder": "e.g. Create 10 reel ideas for AI productivity content",
#         "audience_placeholder": "e.g. Instagram audience, creators, YouTube viewers",
#         "extra_placeholder": "Mention platform, tone, niche, content length, hook style, and target audience.",
#         "examples": [
#             "YouTube Shorts script on AI tools",
#             "Twitter thread on beginner coding mistakes",
#             "Instagram carousel post on career growth"
#         ]
#     },
#     "Email Writing": {
#         "topic_placeholder": "e.g. Draft an email asking for project status update",
#         "audience_placeholder": "e.g. manager, HR, client, colleague",
#         "extra_placeholder": "Mention sender intent, recipient, tone, urgency, and required action.",
#         "examples": [
#             "Leave request email",
#             "Follow-up email after interview",
#             "Formal escalation email for blocked task"
#         ]
#     },
#     "Image Generation": {
#         "topic_placeholder": "e.g. Create a cinematic superhero portrait in space",
#         "audience_placeholder": "e.g. Midjourney users, designers, creators",
#         "extra_placeholder": "Mention art style, camera angle, lighting, composition, mood, colors, and quality.",
#         "examples": [
#             "Anime warrior in neon city at night",
#             "Luxury product ad shot with soft lighting",
#             "Marvel-style superhero poster in pastel space"
#         ]
#     },
#     "YouTube Scripts": {
#         "topic_placeholder": "e.g. Write a 60-second YouTube script on top AI tools",
#         "audience_placeholder": "e.g. YouTube viewers, beginners, tech audience",
#         "extra_placeholder": "Mention niche, duration, hook style, CTA, tone, and retention style.",
#         "examples": [
#             "60-second script for motivation reel",
#             "Faceless finance video script",
#             "Tech explainer script on ChatGPT vs OpenAI"
#         ]
#     }
# }

# STYLE_GUIDE = {
#     "Professional": "Use a polished, structured, confident, and professional tone.",
#     "Creative": "Use engaging, imaginative, vivid, and fresh language.",
#     "Minimal": "Keep the wording concise, sharp, and direct with no fluff.",
#     "Cinematic": "Use immersive, visually rich, dramatic, and emotionally engaging language.",
#     "Anime": "Use expressive, stylized, vibrant, and visually dynamic language.",
#     "Realistic": "Use grounded, practical, precise, and believable details.",
#     "Expert": "Use advanced, strategic, highly refined, and authoritative language."
# }

# def clean_text(value: str) -> str:
#     return value.strip() if value else ""

# def join_requirements(extra_details: str) -> str:
#     extra_details = clean_text(extra_details)
#     if not extra_details:
#         return ""
#     return f" Also ensure the output follows these requirements: {extra_details}."

# def build_final_prompt(use_case, topic, style, audience, extra_details):
#     topic = clean_text(topic)
#     audience = clean_text(audience) or "the intended audience"
#     extra = join_requirements(extra_details)
#     style_instruction = STYLE_GUIDE.get(style, "Use clear and high-quality language.")

#     if use_case == "Resume / Career":
#         return (
#             f"Act as an experienced career coach and professional personal branding expert. "
#             f"Write a strong, polished, and recruiter-friendly response about {topic} for {audience}. "
#             f"{style_instruction} Make the output clear, impactful, and tailored for real hiring scenarios. "
#             f"Highlight strengths, value, credibility, and professional positioning. "
#             f"Keep the language natural, confident, and modern while avoiding vague or generic statements."
#             f"{extra}"
#         )
#     elif use_case == "Content Writing":
#         return (
#             f"Act as an expert content writer and strategist. Create high-quality content about {topic} for {audience}. "
#             f"{style_instruction} Make the response engaging, well-structured, easy to read, and valuable to the target audience. "
#             f"Include a strong opening, smooth flow, relevant details, and a compelling ending. "
#             f"Ensure the writing feels polished, natural, and ready to publish."
#             f"{extra}"
#         )
#     elif use_case == "Coding":
#         return (
#             f"Act as a senior software engineer and coding assistant. Help with {topic} for {audience}. "
#             f"{style_instruction} Provide clean, correct, production-quality output with clear logic, readable structure, and best practices. "
#             f"Include explanations where useful, handle edge cases when relevant, and keep the solution practical and maintainable."
#             f"{extra}"
#         )
#     elif use_case == "Business":
#         return (
#             f"Act as a strategic business consultant. Create a clear, practical, and insight-driven response about {topic} for {audience}. "
#             f"{style_instruction} Focus on business value, execution, realistic strategy, and actionable recommendations. "
#             f"Make the output structured, professional, and useful for decision-making."
#             f"{extra}"
#         )
#     elif use_case == "Students":
#         return (
#             f"Act as an expert tutor and educational mentor. Explain or create content about {topic} for {audience}. "
#             f"{style_instruction} Make the response easy to understand, well-structured, accurate, and educational. "
#             f"Use simple explanations, step-by-step clarity, and examples wherever helpful."
#             f"{extra}"
#         )
#     elif use_case == "Marketing":
#         return (
#             f"Act as an expert marketing strategist and copywriter. Create marketing content for {topic} aimed at {audience}. "
#             f"{style_instruction} Focus on audience attention, clarity, persuasion, brand relevance, and conversion potential. "
#             f"Make the output compelling, strategic, and ready for practical campaign use."
#             f"{extra}"
#         )
#     elif use_case == "Startup Ideas":
#         return (
#             f"Act as an innovative startup advisor and product strategist. Generate strong ideas and strategic thinking around {topic} for {audience}. "
#             f"{style_instruction} Focus on real user pain points, market opportunity, differentiation, monetization, and execution potential. "
#             f"Keep the output practical, high-value, and startup-ready."
#             f"{extra}"
#         )
#     elif use_case == "Social Media":
#         return (
#             f"Act as a social media strategist and content creator. Create content around {topic} for {audience}. "
#             f"{style_instruction} Make the output attention-grabbing, platform-friendly, engaging, and easy to consume. "
#             f"Use strong hooks, clear flow, and content that encourages interaction or retention."
#             f"{extra}"
#         )
#     elif use_case == "Email Writing":
#         return (
#             f"Act as a professional communication expert. Write an effective email about {topic} for {audience}. "
#             f"{style_instruction} Make the email clear, polished, purposeful, and appropriate for the situation. "
#             f"Ensure the message has a strong subject line if relevant, natural wording, and a professional tone."
#             f"{extra}"
#         )
#     elif use_case == "Image Generation":
#         return (
#             f"Create an ultra-clear, highly descriptive image generation prompt for {topic}, designed for {audience}. "
#             f"{style_instruction} Include subject details, environment, composition, lighting, mood, camera feel, colors, textures, and quality cues. "
#             f"Make the final prompt visually rich, precise, and directly usable in image generation tools like Midjourney or similar platforms."
#             f"{extra}"
#         )
#     elif use_case == "YouTube Scripts":
#         return (
#             f"Act as an expert YouTube scriptwriter. Write a high-retention script about {topic} for {audience}. "
#             f"{style_instruction} Start with a strong hook, maintain clear pacing, keep the content engaging, and end with a strong closing or CTA. "
#             f"Make the script natural, audience-focused, and optimized for watch time and clarity."
#             f"{extra}"
#         )
#     else:
#         return (
#             f"Act as an expert assistant. Create a high-quality response about {topic} for {audience}. "
#             f"{style_instruction} Make the output clear, useful, polished, and practical. "
#             f"Ensure the final result is easy to understand and directly usable."
#             f"{extra}"
#         )

# def render_copyable_prompt(prompt_text: str):
#     escaped_prompt = html.escape(prompt_text).replace("\n", "<br>")
#     js_safe_prompt = (
#         prompt_text
#         .replace("\\", "\\\\")
#         .replace("`", "\\`")
#         .replace("${", "\\${")
#     )

#     components.html(
#         f"""
#         <html>
#         <head>
#         <style>
#             body {{
#                 margin: 0;
#                 padding: 0;
#                 background: transparent;
#                 font-family: Inter, Arial, sans-serif;
#                 color: white;
#             }}

#             .prompt-card {{
#                 width: 100%;
#                 box-sizing: border-box;
#                 background: linear-gradient(135deg, rgba(17,24,39,0.98), rgba(30,41,59,0.98));
#                 border: 1px solid rgba(0,212,255,0.22);
#                 border-radius: 22px;
#                 padding: 24px;
#                 box-shadow: 0 0 25px rgba(0,212,255,0.10), 0 0 35px rgba(168,85,247,0.10);
#             }}

#             .prompt-title {{
#                 font-size: 22px;
#                 font-weight: 800;
#                 color: #ffffff;
#                 margin-bottom: 16px;
#             }}

#             .prompt-body {{
#                 font-size: 16px;
#                 line-height: 1.9;
#                 color: #F8FAFC;
#                 word-wrap: break-word;
#                 overflow-wrap: break-word;
#                 white-space: normal;
#                 margin-bottom: 22px;
#             }}

#             .prompt-footer {{
#                 display: flex;
#                 justify-content: flex-end;
#                 align-items: center;
#                 gap: 12px;
#             }}

#             .copy-btn {{
#                 display: inline-flex;
#                 align-items: center;
#                 justify-content: center;
#                 width: 44px;
#                 height: 44px;
#                 border-radius: 14px;
#                 border: 1px solid rgba(255,255,255,0.10);
#                 background: rgba(255,255,255,0.05);
#                 color: white;
#                 cursor: pointer;
#                 transition: all 0.25s ease;
#                 box-shadow: 0 0 12px rgba(0,212,255,0.10);
#             }}

#             .copy-btn:hover {{
#                 transform: translateY(-1px);
#                 background: rgba(255,255,255,0.08);
#                 box-shadow: 0 0 18px rgba(0,212,255,0.22);
#             }}

#             .copy-status {{
#                 font-size: 13px;
#                 color: #7dd3fc;
#                 min-width: 110px;
#                 text-align: right;
#             }}
#         </style>
#         </head>
#         <body>
#             <div class="prompt-card">
#                 <div class="prompt-title">🎯 Prompt</div>
#                 <div class="prompt-body">{escaped_prompt}</div>

#                 <div class="prompt-footer">
#                     <div id="copy-status" class="copy-status"></div>
#                     <button class="copy-btn" onclick="copyPrompt()" title="Copy prompt">
#                         <svg xmlns="http://www.w3.org/2000/svg" width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
#                             <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
#                             <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
#                         </svg>
#                     </button>
#                 </div>
#             </div>

#             <script>
#             async function copyPrompt() {{
#                 const text = `{js_safe_prompt}`;
#                 const status = document.getElementById("copy-status");
#                 try {{
#                     await navigator.clipboard.writeText(text);
#                     status.innerText = "Copied";
#                     setTimeout(() => {{
#                         status.innerText = "";
#                     }}, 1500);
#                 }} catch (err) {{
#                     status.innerText = "Copy failed";
#                 }}
#             }}
#             </script>
#         </body>
#         </html>
#         """,
#         height=320,
#         scrolling=False
#     )

# with st.sidebar:
#     st.markdown("""
#     <div class="sidebar-logo">
#         <div class="logo-title">PromptNexus AI</div>
#         <div class="logo-subtitle">Where prompts become intelligence.</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("### ⚡ Use Cases")
#     st.markdown("""
#     - Content Writing  
#     - Coding  
#     - Business  
#     - Students  
#     - Marketing  
#     - Resume / Career  
#     - Startup Ideas  
#     - Social Media  
#     - Email Writing  
#     - Image Generation  
#     - YouTube Scripts  
#     - General Use  
#     """)

#     st.markdown("### 🎨 Prompt Styles")
#     st.markdown("""
#     - Professional  
#     - Creative  
#     - Minimal  
#     - Cinematic  
#     - Anime  
#     - Realistic  
#     - Expert  
#     """)

# st.markdown("""
# <div class="hero-card">
#     <div class="badge">🚀 AI Prompt Workspace</div>
#     <div class="hero-title">PromptNexus AI</div>
#     <div class="hero-desc">
#         Generate final, ready-to-use, crystal-clear prompts for content, coding, marketing, resume building,
#         image generation, YouTube scripts, and more.
#     </div>
# </div>
# """, unsafe_allow_html=True)

# use_case_options = list(USE_CASE_CONFIG.keys())

# col1, col2 = st.columns(2)

# with col1:
#     use_case = st.selectbox("Select Use Case", use_case_options)

# config = USE_CASE_CONFIG[use_case]

# with col2:
#     style = st.selectbox(
#         "Prompt Style",
#         ["Professional", "Creative", "Minimal", "Cinematic", "Anime", "Realistic", "Expert"]
#     )

# col3, col4 = st.columns(2)

# with col3:
#     topic = st.text_input("Topic / Goal", placeholder=config["topic_placeholder"])
#     st.markdown(
#         f"""
#         <div class="example-box">
#             <b>Examples for {use_case}:</b><br>
#             • {config["examples"][0]}<br>
#             • {config["examples"][1]}<br>
#             • {config["examples"][2]}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# with col4:
#     audience = st.text_input("Target Audience", placeholder=config["audience_placeholder"])
#     st.markdown(
#         '<div class="small-note">Audience suggestions change based on selected use case.</div>',
#         unsafe_allow_html=True
#     )

# extra_details = st.text_area(
#     "Extra Details / Requirements",
#     placeholder=config["extra_placeholder"],
#     height=150
# )

# btn1, btn2 = st.columns([2, 1])

# with btn1:
#     if st.button("✨ Generate Prompt"):
#         if topic.strip():
#             st.session_state.generated_prompt = build_final_prompt(
#                 use_case=use_case,
#                 topic=topic,
#                 style=style,
#                 audience=audience,
#                 extra_details=extra_details
#             )
#         else:
#             st.warning("Please enter a Topic / Goal first.")

# with btn2:
#     if st.button("🗑 Clear"):
#         st.session_state.generated_prompt = ""

# st.markdown('<div class="section-title">Prompt’s Generation</div>', unsafe_allow_html=True)

# if st.session_state.generated_prompt:
#     render_copyable_prompt(st.session_state.generated_prompt)
# else:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">No prompt generated yet</div>
#         <div class="feature-text">
#             Select a use case, review the examples, enter your topic, and click <b>Generate Prompt</b> to get a final ready-to-use prompt.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# st.markdown('<div class="section-title">Why PromptNexus AI?</div>', unsafe_allow_html=True)

# f1, f2, f3 = st.columns(3)

# with f1:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">🧠 Final Prompt Output</div>
#         <div class="feature-text">
#             Generates direct, usable prompts instead of prompt-overview text or prompt-to-generate-prompt structure.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with f2:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">📋 One-Click Copy</div>
#         <div class="feature-text">
#             Copy the final prompt instantly from the icon placed neatly at the end of the prompt card.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with f3:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">⚡ Dynamic by Use Case</div>
#         <div class="feature-text">
#             Placeholders and examples update according to the selected use case, making the app smarter and easier to use.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# st.markdown("""
# <br>
# <div style="text-align:center; color:#94A3B8; font-size:14px; padding-bottom:10px;">
#     Built with ❤️ By Ganesh Goddilla for smarter prompting • <b>PromptNexus AI</b>
# </div>
# """, unsafe_allow_html=True)





import streamlit as st
import streamlit.components.v1 as components
import html

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="PromptNexus AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# SESSION STATE
# -------------------------------
if "generated_prompt" not in st.session_state:
    st.session_state.generated_prompt = ""

# -------------------------------
# CUSTOM CSS
# -------------------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0B0F19 0%, #111827 40%, #0F172A 100%);
    color: white;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0F172A 0%, #111827 100%);
    border-right: 1px solid rgba(255,255,255,0.08);
}

.sidebar-logo {
    padding: 14px 10px 18px 10px;
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(108,99,255,0.15), rgba(0,212,255,0.10));
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 0 18px rgba(108,99,255,0.18);
    margin-bottom: 18px;
}

.logo-title {
    font-size: 28px;
    font-weight: 800;
    line-height: 1.1;
    background: linear-gradient(90deg, #6C63FF, #00D4FF, #A855F7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.logo-subtitle {
    color: #9CA3AF;
    font-size: 13px;
    margin-top: 6px;
}

.hero-card {
    padding: 28px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(17,24,39,0.92), rgba(15,23,42,0.92));
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 0 30px rgba(0,212,255,0.08), 0 0 50px rgba(108,99,255,0.08);
    margin-bottom: 22px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 10px;
    background: linear-gradient(90deg, #FFFFFF, #00D4FF, #A855F7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-desc {
    color: #cbd5e1;
    font-size: 16px;
    line-height: 1.6;
}

.feature-card {
    background: rgba(17,24,39,0.85);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    padding: 18px;
    margin-bottom: 16px;
    box-shadow: 0 0 20px rgba(0,0,0,0.18);
}

.feature-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
    color: #E5E7EB;
}

.feature-text {
    color: #9CA3AF;
    line-height: 1.7;
    font-size: 15px;
}

label, .stSelectbox label, .stTextInput label, .stTextArea label {
    color: #E5E7EB !important;
    font-weight: 600 !important;
}

.stButton > button {
    width: 100%;
    border-radius: 16px;
    border: none;
    padding: 0.75rem 1rem;
    font-weight: 700;
    font-size: 15px;
    color: white;
    background: linear-gradient(90deg, #6C63FF, #00D4FF);
    box-shadow: 0 0 18px rgba(0,212,255,0.25);
    transition: all 0.25s ease-in-out;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 24px rgba(108,99,255,0.35);
}

.stTextArea textarea,
.stTextInput input {
    background: rgba(17,24,39,0.95) !important;
    color: white !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: rgba(17,24,39,0.95) !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}

.section-title {
    font-size: 26px;
    font-weight: 800;
    margin-top: 12px;
    margin-bottom: 14px;
    color: #F8FAFC;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(108,99,255,0.16);
    color: #dbeafe;
    border: 1px solid rgba(255,255,255,0.08);
    font-size: 13px;
    margin-bottom: 10px;
}

.example-box {
    background: rgba(17,24,39,0.72);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    padding: 14px 16px;
    margin-top: 8px;
    margin-bottom: 10px;
    color: #cbd5e1;
    font-size: 14px;
    line-height: 1.7;
}

.small-note {
    color: #94A3B8;
    font-size: 13px;
    margin-top: -5px;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# USE CASE DATA
# -------------------------------
USE_CASE_CONFIG = {
    "Content Writing": {
        "topic_placeholder": "e.g. Write a blog post on AI tools for productivity",
        "audience_placeholder": "e.g. content creators, bloggers, marketers",
        "extra_placeholder": "Add tone, length, SEO keywords, platform, CTA, and structure needs.",
        "examples": [
            "Instagram caption for a fitness brand launch",
            "SEO blog post on beginner MLOps roadmap",
            "LinkedIn post about GenAI career transition"
        ]
    },
    "Coding": {
        "topic_placeholder": "e.g. Build a Streamlit app for AI prompt generation",
        "audience_placeholder": "e.g. Python developers, beginners, backend engineers",
        "extra_placeholder": "Mention language, framework, output format, best practices, edge cases, and constraints.",
        "examples": [
            "Streamlit app for AI prompt generator",
            "FastAPI REST API with authentication",
            "Python function to parse logs and summarize errors"
        ]
    },
    "Business": {
        "topic_placeholder": "e.g. Create a startup idea for AI resume review tool",
        "audience_placeholder": "e.g. startup founders, consultants, entrepreneurs",
        "extra_placeholder": "Mention industry, target market, budget, revenue model, and strategic goals.",
        "examples": [
            "Business plan for a faceless YouTube automation agency",
            "Pricing strategy for AI SaaS tool",
            "Go-to-market plan for student productivity app"
        ]
    },
    "Students": {
        "topic_placeholder": "e.g. Explain neural networks in simple terms",
        "audience_placeholder": "e.g. school students, college students, exam aspirants",
        "extra_placeholder": "Mention difficulty level, subject, exam type, explanation style, and examples needed.",
        "examples": [
            "Study notes for DBMS interview preparation",
            "Simple explanation of cloud computing",
            "5-mark answer for machine learning basics"
        ]
    },
    "General Use": {
        "topic_placeholder": "e.g. Write a professional email requesting project access",
        "audience_placeholder": "e.g. professionals, general users, freelancers",
        "extra_placeholder": "Mention tone, context, recipient, expected format, and important details.",
        "examples": [
            "Professional apology email to manager",
            "Daily planner for a productive workday",
            "Checklist for moving to a new city"
        ]
    },
    "Marketing": {
        "topic_placeholder": "e.g. Create ad copy for eco-friendly water bottle",
        "audience_placeholder": "e.g. customers, marketers, D2C brands",
        "extra_placeholder": "Mention platform, product, brand voice, CTA, target market, and campaign goal.",
        "examples": [
            "Facebook ad copy for skincare product",
            "Email campaign for Black Friday sale",
            "Brand tagline ideas for AI startup"
        ]
    },
    "Resume / Career": {
        "topic_placeholder": "e.g. LinkedIn About section for fresher in MLOps",
        "audience_placeholder": "e.g. recruiters, hiring managers, job seekers",
        "extra_placeholder": "Mention target role, years of experience, industry, skills, and desired tone.",
        "examples": [
            "Resume bullet points for Python developer",
            "Cover letter for GenAI engineer role",
            "LinkedIn About section for fresher in MLOps"
        ]
    },
    "Startup Ideas": {
        "topic_placeholder": "e.g. Generate startup ideas using GenAI in education",
        "audience_placeholder": "e.g. founders, investors, builders",
        "extra_placeholder": "Mention niche, monetization preference, user pain points, and innovation level.",
        "examples": [
            "Low-cost AI SaaS ideas for India",
            "B2B startup idea for internal documentation",
            "One-person startup ideas in automation"
        ]
    },
    "Social Media": {
        "topic_placeholder": "e.g. Create 10 reel ideas for AI productivity content",
        "audience_placeholder": "e.g. Instagram audience, creators, YouTube viewers",
        "extra_placeholder": "Mention platform, tone, niche, content length, hook style, and target audience.",
        "examples": [
            "YouTube Shorts script on AI tools",
            "Twitter thread on beginner coding mistakes",
            "Instagram carousel post on career growth"
        ]
    },
    "Email Writing": {
        "topic_placeholder": "e.g. Draft an email asking for project status update",
        "audience_placeholder": "e.g. manager, HR, client, colleague",
        "extra_placeholder": "Mention sender intent, recipient, tone, urgency, and required action.",
        "examples": [
            "Leave request email",
            "Follow-up email after interview",
            "Formal escalation email for blocked task"
        ]
    },
    "Image Generation": {
        "topic_placeholder": "e.g. Marvel-style superhero poster in pastel space",
        "audience_placeholder": "e.g. creators, Midjourney users, designers",
        "extra_placeholder": "Mention subject, art style, colors, lighting, camera angle, mood, textures, quality, aspect ratio, and render style.",
        "examples": [
            "Anime warrior in neon city at night",
            "Luxury product ad shot with soft lighting",
            "Marvel-style superhero poster in pastel space"
        ]
    },
    "YouTube Scripts": {
        "topic_placeholder": "e.g. Write a 60-second YouTube script on top AI tools",
        "audience_placeholder": "e.g. YouTube viewers, beginners, tech audience",
        "extra_placeholder": "Mention niche, duration, hook style, CTA, tone, and retention style.",
        "examples": [
            "60-second script for motivation reel",
            "Faceless finance video script",
            "Tech explainer script on ChatGPT vs OpenAI"
        ]
    }
}

STYLE_GUIDE = {
    "Professional": "polished, structured, confident, and professional",
    "Creative": "imaginative, vivid, engaging, and expressive",
    "Minimal": "concise, sharp, clean, and direct",
    "Cinematic": "dramatic, immersive, visually rich, and emotionally powerful",
    "Anime": "stylized, vibrant, expressive, and dynamic",
    "Realistic": "grounded, precise, believable, and highly detailed",
    "Expert": "advanced, strategic, refined, and authoritative"
}

# -------------------------------
# HELPERS
# -------------------------------
def clean_text(value: str) -> str:
    return value.strip() if value else ""

def titleize_topic(topic: str) -> str:
    small_words = {"in", "of", "for", "and", "to", "with", "on", "at", "by", "the", "a", "an"}
    words = topic.split()
    result = []
    for i, w in enumerate(words):
        if i != 0 and w.lower() in small_words:
            result.append(w.lower())
        else:
            result.append(w.capitalize())
    return " ".join(result)

def extra_sentence(extra_details: str) -> str:
    extra_details = clean_text(extra_details)
    return extra_details if extra_details else "No extra constraints provided."

# -------------------------------
# PROMPT BUILDERS
# -------------------------------
def build_image_master_prompt(topic, style, audience, extra_details):
    style_phrase = STYLE_GUIDE.get(style, "high-quality and detailed")
    title = f"The Master Prompt: {titleize_topic(topic)}"

    return f"""{title}

Core Concept:
A high-impact, {style_phrase} image concept centered on {topic}, designed for {audience}. The final image should feel premium, visually cohesive, and immediately usable in advanced image-generation tools.

Visual Description & Details:

Subject:
The main subject should clearly focus on {topic}. The design must emphasize strong visual identity, memorable silhouette, and rich detail. Make the subject feel intentional, visually striking, and compositionally dominant.

Setting & Environment:
Place the subject in a visually compelling environment that enhances the idea of {topic}. The background should support the story with strong atmosphere, environmental depth, and layered visual interest instead of feeling empty or generic.

Composition:
Use a professional composition with a clear focal point, balanced framing, and strong visual flow. The scene should guide the viewer’s eye naturally and feel cinematic, poster-worthy, and carefully directed.

Lighting & Mood:
Use lighting that enhances the emotional impact of the scene. The mood should match the concept of {topic} while maintaining a premium, polished, visually dramatic finish.

Camera Feel & Style:
Describe the shot like a professional creative direction brief. Include a cinematic camera feel, strong framing, and a sense of scale, depth, and visual storytelling.

Colors & Textures:
Use a cohesive palette that supports the concept. Add texture detail to surfaces, materials, fabrics, skin, armor, reflections, particles, or surrounding elements where relevant. Avoid flat or generic visuals.

Quality Cues:
Ultra-detailed, visually rich, high resolution, sharp focus, strong composition, premium rendering quality, intricate detail, professional-grade finish.

Additional Requirements:
{extra_sentence(extra_details)}

Optimized, Direct-Usable Prompt String:
/imagine prompt: {topic}, {style_phrase} visual treatment, highly descriptive subject, cinematic environment, strong composition, premium lighting, clear focal point, rich textures, cohesive color palette, atmospheric depth, ultra-detailed, sharp focus, high resolution, intricate details, professional quality render --ar 2:3 --stylize 750 --v 6.0
"""

def build_resume_prompt(topic, style, audience, extra_details):
    style_phrase = STYLE_GUIDE.get(style, "polished and professional")
    return f"""Act as an experienced career coach and personal branding expert. Write a {style_phrase} {topic} tailored for {audience}. Make it impactful, natural, recruiter-friendly, and specific rather than generic. Highlight strengths, skills, value, credibility, and career direction clearly. Keep the language modern, confident, and professional. Additional requirements: {extra_sentence(extra_details)}"""

def build_content_prompt(topic, style, audience, extra_details):
    style_phrase = STYLE_GUIDE.get(style, "engaging and polished")
    return f"""Act as an expert content strategist and professional writer. Create high-quality content on {topic} for {audience}. The writing should be {style_phrase}, easy to read, well-structured, and valuable. Include a strong opening, smooth flow, relevant insights, and a compelling ending. Additional requirements: {extra_sentence(extra_details)}"""

def build_coding_prompt(topic, style, audience, extra_details):
    style_phrase = STYLE_GUIDE.get(style, "clear and professional")
    return f"""Act as a senior software engineer and coding assistant. Help with {topic} for {audience}. Use a {style_phrase} approach. Provide clean, correct, production-quality output with readable structure, best practices, practical logic, and useful explanations where needed. Additional requirements: {extra_sentence(extra_details)}"""

def build_business_prompt(topic, style, audience, extra_details):
    style_phrase = STYLE_GUIDE.get(style, "strategic and refined")
    return f"""Act as a strategic business consultant. Create a {style_phrase} response about {topic} for {audience}. Focus on execution, business value, practical ideas, realistic recommendations, and clear decision-making value. Additional requirements: {extra_sentence(extra_details)}"""

def build_students_prompt(topic, style, audience, extra_details):
    style_phrase = STYLE_GUIDE.get(style, "clear and easy to understand")
    return f"""Act as an expert tutor and educational mentor. Explain or create content about {topic} for {audience}. Keep it {style_phrase}, accurate, well-structured, and educational. Use step-by-step clarity and examples where helpful. Additional requirements: {extra_sentence(extra_details)}"""

def build_marketing_prompt(topic, style, audience, extra_details):
    style_phrase = STYLE_GUIDE.get(style, "persuasive and polished")
    return f"""Act as an expert marketing strategist and copywriter. Create marketing content for {topic} aimed at {audience}. Make it {style_phrase}, audience-focused, conversion-aware, and brand-relevant. Use strong messaging, clear positioning, and compelling wording. Additional requirements: {extra_sentence(extra_details)}"""

def build_startup_prompt(topic, style, audience, extra_details):
    style_phrase = STYLE_GUIDE.get(style, "innovative and practical")
    return f"""Act as a startup advisor and product strategist. Generate ideas and strategic thinking around {topic} for {audience}. Keep the output {style_phrase}, market-aware, solution-oriented, and monetization-conscious. Focus on pain points, differentiation, and execution potential. Additional requirements: {extra_sentence(extra_details)}"""

def build_social_prompt(topic, style, audience, extra_details):
    style_phrase = STYLE_GUIDE.get(style, "engaging and platform-friendly")
    return f"""Act as a social media strategist and creator. Create content around {topic} for {audience}. Make it {style_phrase}, attention-grabbing, easy to consume, and optimized for interaction and retention. Use strong hooks, clarity, and audience relevance. Additional requirements: {extra_sentence(extra_details)}"""

def build_email_prompt(topic, style, audience, extra_details):
    style_phrase = STYLE_GUIDE.get(style, "professional and clear")
    return f"""Act as a professional communication expert. Write an email about {topic} for {audience}. The email should be {style_phrase}, purposeful, natural, and appropriate for the situation. Keep the wording polished and action-oriented. Additional requirements: {extra_sentence(extra_details)}"""

def build_youtube_prompt(topic, style, audience, extra_details):
    style_phrase = STYLE_GUIDE.get(style, "engaging and high-retention")
    return f"""Act as an expert YouTube scriptwriter. Write a script about {topic} for {audience}. Make it {style_phrase}, audience-focused, and easy to follow. Start with a strong hook, maintain momentum throughout, and end with a strong CTA or closing. Additional requirements: {extra_sentence(extra_details)}"""

def build_general_prompt(topic, style, audience, extra_details):
    style_phrase = STYLE_GUIDE.get(style, "clear and high-quality")
    return f"""Act as an expert assistant. Create a {style_phrase} response about {topic} for {audience}. Make the output useful, polished, practical, and directly usable. Additional requirements: {extra_sentence(extra_details)}"""

def build_final_prompt(use_case, topic, style, audience, extra_details):
    topic = clean_text(topic)
    audience = clean_text(audience) or "the intended audience"

    if use_case == "Image Generation":
        return build_image_master_prompt(topic, style, audience, extra_details)
    elif use_case == "Resume / Career":
        return build_resume_prompt(topic, style, audience, extra_details)
    elif use_case == "Content Writing":
        return build_content_prompt(topic, style, audience, extra_details)
    elif use_case == "Coding":
        return build_coding_prompt(topic, style, audience, extra_details)
    elif use_case == "Business":
        return build_business_prompt(topic, style, audience, extra_details)
    elif use_case == "Students":
        return build_students_prompt(topic, style, audience, extra_details)
    elif use_case == "Marketing":
        return build_marketing_prompt(topic, style, audience, extra_details)
    elif use_case == "Startup Ideas":
        return build_startup_prompt(topic, style, audience, extra_details)
    elif use_case == "Social Media":
        return build_social_prompt(topic, style, audience, extra_details)
    elif use_case == "Email Writing":
        return build_email_prompt(topic, style, audience, extra_details)
    elif use_case == "YouTube Scripts":
        return build_youtube_prompt(topic, style, audience, extra_details)
    else:
        return build_general_prompt(topic, style, audience, extra_details)

# -------------------------------
# COPYABLE PROMPT CARD
# -------------------------------
def render_copyable_prompt(prompt_text: str):
    escaped_prompt = html.escape(prompt_text).replace("\n", "<br>")
    js_safe_prompt = (
        prompt_text
        .replace("\\", "\\\\")
        .replace("`", "\\`")
        .replace("${", "\\${")
    )

    html_code = f"""
    <html>
    <head>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: transparent;
            font-family: Inter, Arial, sans-serif;
            color: white;
        }}

        .prompt-card {{
            width: 100%;
            box-sizing: border-box;
            background: linear-gradient(135deg, rgba(17,24,39,0.98), rgba(30,41,59,0.98));
            border: 1px solid rgba(0,212,255,0.22);
            border-radius: 22px;
            padding: 24px;
            box-shadow: 0 0 25px rgba(0,212,255,0.10), 0 0 35px rgba(168,85,247,0.10);
        }}

        .prompt-title {{
            font-size: 22px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 16px;
        }}

        .prompt-body-wrap {{
            max-height: 620px;
            overflow-y: auto;
            padding-right: 8px;
            margin-bottom: 22px;
        }}

        .prompt-body {{
            font-size: 15px;
            line-height: 1.9;
            color: #F8FAFC;
            word-wrap: break-word;
            overflow-wrap: break-word;
            white-space: normal;
        }}

        .prompt-footer {{
            display: flex;
            justify-content: flex-end;
            align-items: center;
            gap: 12px;
        }}

        .copy-btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 44px;
            height: 44px;
            border-radius: 14px;
            border: 1px solid rgba(255,255,255,0.10);
            background: rgba(255,255,255,0.05);
            color: white;
            cursor: pointer;
            transition: all 0.25s ease;
            box-shadow: 0 0 12px rgba(0,212,255,0.10);
        }}

        .copy-btn:hover {{
            transform: translateY(-1px);
            background: rgba(255,255,255,0.08);
            box-shadow: 0 0 18px rgba(0,212,255,0.22);
        }}

        .copy-status {{
            font-size: 13px;
            color: #7dd3fc;
            min-width: 110px;
            text-align: right;
        }}

        .prompt-body-wrap::-webkit-scrollbar {{
            width: 8px;
        }}

        .prompt-body-wrap::-webkit-scrollbar-thumb {{
            background: rgba(125, 211, 252, 0.35);
            border-radius: 10px;
        }}

        .prompt-body-wrap::-webkit-scrollbar-track {{
            background: rgba(255,255,255,0.04);
            border-radius: 10px;
        }}
    </style>
    </head>
    <body>
        <div class="prompt-card">
            <div class="prompt-title">🎯 Prompt</div>

            <div class="prompt-body-wrap">
                <div class="prompt-body">{escaped_prompt}</div>
            </div>

            <div class="prompt-footer">
                <div id="copy-status" class="copy-status"></div>
                <button class="copy-btn" onclick="copyPrompt()" title="Copy prompt">
                    <svg xmlns="http://www.w3.org/2000/svg" width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                    </svg>
                </button>
            </div>
        </div>

        <script>
        async function copyPrompt() {{
            const text = `{js_safe_prompt}`;
            const status = document.getElementById("copy-status");
            try {{
                await navigator.clipboard.writeText(text);
                status.innerText = "Copied";
                setTimeout(() => {{
                    status.innerText = "";
                }}, 1500);
            }} catch (err) {{
                status.innerText = "Copy failed";
            }}
        }}
        </script>
    </body>
    </html>
    """

    components.html(
        html_code,
        height=900,
        scrolling=True
    )

# -------------------------------
# SIDEBAR
# -------------------------------
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="logo-title">PromptNexus AI</div>
        <div class="logo-subtitle">Where prompts become intelligence.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⚡ Use Cases")
    st.markdown("""
    - Content Writing  
    - Coding  
    - Business  
    - Students  
    - Marketing  
    - Resume / Career  
    - Startup Ideas  
    - Social Media  
    - Email Writing  
    - Image Generation  
    - YouTube Scripts  
    - General Use  
    """)

    st.markdown("### 🎨 Prompt Styles")
    st.markdown("""
    - Professional  
    - Creative  
    - Minimal  
    - Cinematic  
    - Anime  
    - Realistic  
    - Expert  
    """)

# -------------------------------
# HERO
# -------------------------------
st.markdown("""
<div class="hero-card">
    <div class="badge">🚀 AI Prompt Workspace</div>
    <div class="hero-title">PromptNexus AI</div>
    <div class="hero-desc">
        Generate richer, final, ready-to-use prompts for content, coding, marketing, career growth,
        image generation, and more.
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# INPUTS
# -------------------------------
use_case_options = list(USE_CASE_CONFIG.keys())

col1, col2 = st.columns(2)

with col1:
    use_case = st.selectbox("Select Use Case", use_case_options)

config = USE_CASE_CONFIG[use_case]

with col2:
    style = st.selectbox(
        "Prompt Style",
        ["Professional", "Creative", "Minimal", "Cinematic", "Anime", "Realistic", "Expert"]
    )

col3, col4 = st.columns(2)

with col3:
    topic = st.text_input("Topic / Goal", placeholder=config["topic_placeholder"])
    st.markdown(
        f"""
        <div class="example-box">
            <b>Examples for {use_case}:</b><br>
            • {config["examples"][0]}<br>
            • {config["examples"][1]}<br>
            • {config["examples"][2]}
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    audience = st.text_input("Target Audience", placeholder=config["audience_placeholder"])
    st.markdown(
        '<div class="small-note">Audience suggestions change based on selected use case.</div>',
        unsafe_allow_html=True
    )

extra_details = st.text_area(
    "Extra Details / Requirements",
    placeholder=config["extra_placeholder"],
    height=160
)

# -------------------------------
# BUTTONS
# -------------------------------
btn1, btn2 = st.columns([2, 1])

with btn1:
    if st.button("✨ Generate Prompt"):
        if topic.strip():
            st.session_state.generated_prompt = build_final_prompt(
                use_case=use_case,
                topic=topic,
                style=style,
                audience=audience,
                extra_details=extra_details
            )
        else:
            st.warning("Please enter a Topic / Goal first.")

with btn2:
    if st.button("🗑 Clear"):
        st.session_state.generated_prompt = ""

# -------------------------------
# OUTPUT
# -------------------------------
st.markdown('<div class="section-title">Prompt’s Generation</div>', unsafe_allow_html=True)

if st.session_state.generated_prompt:
    render_copyable_prompt(st.session_state.generated_prompt)
else:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">No prompt generated yet</div>
        <div class="feature-text">
            Select a use case, review the examples, enter your topic, and click <b>Generate Prompt</b> to get a richer final prompt.
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# FEATURES
# -------------------------------
st.markdown('<div class="section-title">Why PromptNexus AI?</div>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🧠 Richer Final Output</div>
        <div class="feature-text">
            Generates detailed, usable prompts instead of generic meta instructions.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📋 One-Click Copy</div>
        <div class="feature-text">
            Copy the final prompt instantly from the icon placed neatly at the end of the prompt card.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">⚡ Better Image Prompting</div>
        <div class="feature-text">
            Image generation prompts now include richer concept, visual breakdown, and optimized final prompt string.
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("""
<br>
<div style="text-align:center; color:#94A3B8; font-size:14px; padding-bottom:10px;">
    Built with ❤️ By GANESH GODDILLA for smarter prompting • <b>PromptNexus AI</b>
</div>
""", unsafe_allow_html=True)