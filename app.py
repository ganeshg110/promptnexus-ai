# import streamlit as st
# import streamlit.components.v1 as components
# import html
# import random
# from datetime import datetime

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
# # SESSION STATE DEFAULTS
# # -------------------------------
# defaults = {
#     "generated_prompt": "",
#     "history": [],
#     "favorites": [],
#     "last_generation_payload": None,
#     "topic_value": "",
#     "audience_value": "",
#     "extra_value": "",
#     "use_case_select": "Content Writing",
#     "style_select": "Professional",
# }
# for key, value in defaults.items():
#     if key not in st.session_state:
#         st.session_state[key] = value

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
# label, .stSelectbox label, .stTextInput label, .stTextArea label, .stSlider label {
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
# .prompt-chip {
#     display: inline-block;
#     padding: 6px 10px;
#     margin: 4px 6px 4px 0;
#     border-radius: 999px;
#     font-size: 12px;
#     color: #e2e8f0;
#     background: rgba(255,255,255,0.05);
#     border: 1px solid rgba(255,255,255,0.08);
# }
# .history-card {
#     background: rgba(17,24,39,0.82);
#     border: 1px solid rgba(255,255,255,0.07);
#     border-radius: 18px;
#     padding: 14px;
#     margin-bottom: 12px;
# }
# .history-meta {
#     color: #94A3B8;
#     font-size: 12px;
#     margin-bottom: 8px;
# }
# .history-title {
#     color: #F8FAFC;
#     font-weight: 700;
#     font-size: 14px;
#     margin-bottom: 6px;
# }
# .history-text {
#     color: #CBD5E1;
#     font-size: 13px;
#     line-height: 1.6;
# }
# .stDownloadButton > button {
#     width: 100%;
#     border-radius: 16px;
#     border: none;
#     padding: 0.75rem 1rem;
#     font-weight: 700;
#     font-size: 15px;
#     color: white;
#     background: linear-gradient(90deg, #111827, #1F2937);
#     border: 1px solid rgba(255,255,255,0.10);
# }
# div[data-testid="stExpander"] {
#     border-radius: 16px !important;
#     border: 1px solid rgba(255,255,255,0.08) !important;
#     overflow: hidden;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # DATA
# # -------------------------------
# USE_CASE_CONFIG = {
#     "Content Writing": {
#         "topic_placeholder": "e.g. Write a blog post on AI tools for productivity",
#         "audience_placeholder": "e.g. content creators, bloggers, marketers",
#         "extra_placeholder": "Add tone, length, SEO keywords, platform, CTA, and output format.",
#         "examples": [
#             "Instagram caption for a fitness brand launch",
#             "SEO blog post on beginner MLOps roadmap",
#             "LinkedIn post about GenAI career transition"
#         ],
#         "random_topics": [
#             "LinkedIn post about AI productivity tools",
#             "Blog article on beginner MLOps roadmap",
#             "Instagram caption for a new tech gadget launch"
#         ]
#     },
#     "Coding": {
#         "topic_placeholder": "e.g. Build a Python script for file organizer automation",
#         "audience_placeholder": "e.g. Python developers, beginners, backend engineers",
#         "extra_placeholder": "Mention language, framework, edge cases, output style, and constraints.",
#         "examples": [
#             "Streamlit app for AI prompt generator",
#             "FastAPI REST API with authentication",
#             "Python function to parse logs and summarize errors"
#         ],
#         "random_topics": [
#             "Python script to organize files by extension",
#             "FastAPI endpoint with JWT authentication",
#             "Streamlit dashboard for sales analytics"
#         ]
#     },
#     "Business": {
#         "topic_placeholder": "e.g. Create a startup idea for AI resume review tool",
#         "audience_placeholder": "e.g. startup founders, consultants, entrepreneurs",
#         "extra_placeholder": "Mention industry, users, pricing, business goal, and market angle.",
#         "examples": [
#             "Business plan for a faceless YouTube automation agency",
#             "Pricing strategy for AI SaaS tool",
#             "Go-to-market plan for student productivity app"
#         ],
#         "random_topics": [
#             "Pricing strategy for AI SaaS product",
#             "Business model for freelancer marketplace",
#             "Go-to-market plan for student productivity app"
#         ]
#     },
#     "Students": {
#         "topic_placeholder": "e.g. Explain neural networks in simple terms",
#         "audience_placeholder": "e.g. school students, college students, exam aspirants",
#         "extra_placeholder": "Mention subject, difficulty, answer style, format, and examples needed.",
#         "examples": [
#             "Study notes for DBMS interview preparation",
#             "Simple explanation of cloud computing",
#             "5-mark answer for machine learning basics"
#         ],
#         "random_topics": [
#             "Simple explanation of cloud computing",
#             "DBMS notes for interview preparation",
#             "Machine learning basics for beginners"
#         ]
#     },
#     "General Use": {
#         "topic_placeholder": "e.g. Write a professional email requesting project access",
#         "audience_placeholder": "e.g. professionals, freelancers, general users",
#         "extra_placeholder": "Mention context, tone, recipient, and desired structure.",
#         "examples": [
#             "Professional apology email to manager",
#             "Daily planner for a productive workday",
#             "Checklist for moving to a new city"
#         ],
#         "random_topics": [
#             "Professional apology email to manager",
#             "Daily productivity planner",
#             "Checklist for moving to a new city"
#         ]
#     },
#     "Marketing": {
#         "topic_placeholder": "e.g. Create ad copy for eco-friendly water bottle",
#         "audience_placeholder": "e.g. customers, marketers, D2C brands",
#         "extra_placeholder": "Mention product, platform, brand tone, CTA, and campaign goal.",
#         "examples": [
#             "Facebook ad copy for skincare product",
#             "Email campaign for Black Friday sale",
#             "Brand tagline ideas for AI startup"
#         ],
#         "random_topics": [
#             "Facebook ad copy for skincare brand",
#             "Email campaign for festive sale",
#             "Tagline ideas for AI startup"
#         ]
#     },
#     "Resume / Career": {
#         "topic_placeholder": "e.g. Rewrite my resume summary for MLOps engineer role",
#         "audience_placeholder": "e.g. recruiters, hiring managers, job seekers",
#         "extra_placeholder": "Mention target role, experience level, key skills, and tone.",
#         "examples": [
#             "Resume bullet points for Python developer",
#             "Cover letter for GenAI engineer role",
#             "LinkedIn About section for fresher in MLOps"
#         ],
#         "random_topics": [
#             "LinkedIn About section for fresher in MLOps",
#             "Resume summary for Python developer",
#             "Cover letter for GenAI engineer role"
#         ]
#     },
#     "Startup Ideas": {
#         "topic_placeholder": "e.g. Generate startup ideas using GenAI in education",
#         "audience_placeholder": "e.g. founders, investors, builders",
#         "extra_placeholder": "Mention niche, user pain point, monetization, and business type.",
#         "examples": [
#             "Low-cost AI SaaS ideas for India",
#             "B2B startup idea for internal documentation",
#             "One-person startup ideas in automation"
#         ],
#         "random_topics": [
#             "AI startup ideas for education",
#             "One-person startup ideas in automation",
#             "B2B AI tool for internal documentation"
#         ]
#     },
#     "Social Media": {
#         "topic_placeholder": "e.g. Create 10 reel ideas for AI productivity content",
#         "audience_placeholder": "e.g. Instagram audience, creators, YouTube viewers",
#         "extra_placeholder": "Mention platform, tone, hook style, audience, and niche.",
#         "examples": [
#             "YouTube Shorts script on AI tools",
#             "Twitter thread on beginner coding mistakes",
#             "Instagram carousel post on career growth"
#         ],
#         "random_topics": [
#             "10 Instagram reel ideas for AI productivity",
#             "Twitter thread on common coding mistakes",
#             "Carousel post on career growth tips"
#         ]
#     },
#     "Email Writing": {
#         "topic_placeholder": "e.g. Draft an email asking for project status update",
#         "audience_placeholder": "e.g. manager, HR, client, colleague",
#         "extra_placeholder": "Mention sender goal, urgency, context, and tone.",
#         "examples": [
#             "Leave request email",
#             "Follow-up email after interview",
#             "Formal escalation email for blocked task"
#         ],
#         "random_topics": [
#             "Leave request email",
#             "Interview follow-up email",
#             "Formal escalation email for blocked task"
#         ]
#     },
#     "Image Generation": {
#         "topic_placeholder": "e.g. Marvel-style superhero poster in pastel space",
#         "audience_placeholder": "e.g. creators, designers, Midjourney users",
#         "extra_placeholder": "Mention must-have details, pose, objects, setting, color direction, or restrictions.",
#         "examples": [
#             "Anime warrior in neon city at night",
#             "Luxury product ad shot with soft lighting",
#             "Marvel-style superhero poster in pastel space"
#         ],
#         "random_topics": [
#             "Marvel-style superhero poster in pastel space",
#             "Anime warrior in neon city at night",
#             "Cyberpunk female assassin in rainy alley"
#         ]
#     },
#     "YouTube Scripts": {
#         "topic_placeholder": "e.g. Write a 60-second YouTube script on top AI tools",
#         "audience_placeholder": "e.g. YouTube viewers, beginners, tech audience",
#         "extra_placeholder": "Mention duration, tone, niche, hook style, CTA, and pacing.",
#         "examples": [
#             "60-second script for motivation reel",
#             "Faceless finance video script",
#             "Tech explainer script on ChatGPT vs OpenAI"
#         ],
#         "random_topics": [
#             "60-second YouTube script on top AI tools",
#             "Faceless finance video script",
#             "Tech explainer on ChatGPT vs OpenAI"
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

# SHOT_OPTIONS = [
#     "low-angle hero shot", "close-up portrait", "wide cinematic shot", "mid-shot composition",
#     "full-body character shot", "over-the-shoulder shot", "bird's-eye view", "dynamic action frame"
# ]
# LIGHTING_OPTIONS = [
#     "dramatic rim lighting", "soft diffused lighting", "golden hour glow", "neon glow",
#     "volumetric god rays", "studio lighting", "moonlit ambience", "high contrast cinematic lighting"
# ]
# MOOD_OPTIONS = ["epic", "dreamy", "mysterious", "dark fantasy", "heroic", "ethereal", "intense", "calm"]
# PALETTE_OPTIONS = [
#     "pastel lavender, baby blue, mint green, peach",
#     "deep blue, violet, silver",
#     "neon cyan, magenta, purple",
#     "gold, crimson, black",
#     "warm beige, ivory, bronze",
#     "emerald, teal, obsidian"
# ]
# CAMERA_OPTIONS = [
#     "cinematic lens feel", "85mm portrait feel", "ultra-wide lens perspective",
#     "movie poster framing", "editorial fashion framing", "DSLR realism", "anamorphic cinematic framing"
# ]
# TEXTURE_OPTIONS = [
#     "ultra-detailed metallic textures", "soft fabric detail", "crystalline surfaces",
#     "photoreal skin detail", "glossy reflective surfaces", "matte cinematic textures"
# ]
# RENDER_OPTIONS = [
#     "professional 8k render", "ultra-detailed digital art", "high-end concept art",
#     "AAA game art quality", "cinematic movie poster quality", "photorealistic studio render"
# ]
# NEGATIVE_DEFAULT = "blurry, low quality, distorted anatomy, extra fingers, cropped, duplicate, watermark, text, logo, oversaturated, noisy background"

# # -------------------------------
# # HELPERS
# # -------------------------------
# def clean_text(value: str) -> str:
#     return value.strip() if value else ""

# def compact_join(parts):
#     return ", ".join([p for p in parts if clean_text(p)])

# def add_to_history(use_case: str, topic: str, prompt: str) -> None:
#     entry = {
#         "use_case": use_case,
#         "topic": topic,
#         "prompt": prompt,
#         "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
#     }
#     st.session_state.history.insert(0, entry)
#     st.session_state.history = st.session_state.history[:10]

# def add_to_favorites(use_case: str, topic: str, prompt: str) -> None:
#     already_exists = any(fav["prompt"] == prompt for fav in st.session_state.favorites)
#     if not already_exists:
#         st.session_state.favorites.insert(0, {
#             "use_case": use_case,
#             "topic": topic,
#             "prompt": prompt,
#             "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
#         })
#         st.session_state.favorites = st.session_state.favorites[:20]

# def set_random_topic():
#     current_use_case = st.session_state.get("use_case_select", "Content Writing")
#     current_config = USE_CASE_CONFIG[current_use_case]
#     st.session_state["topic_value"] = random.choice(current_config["random_topics"])

# def clear_all():
#     st.session_state.generated_prompt = ""
#     st.session_state.topic_value = ""
#     st.session_state.audience_value = ""
#     st.session_state.extra_value = ""

# def build_image_prompt(
#     topic: str,
#     style: str,
#     extra_details: str,
#     shot_type: str,
#     lighting: str,
#     mood: str,
#     palette: str,
#     camera: str,
#     texture: str,
#     render_quality: str,
#     aspect_ratio: str,
#     stylize: int,
#     chaos: int,
#     quality: str,
#     include_negative: bool,
#     negative_prompt: str
# ) -> str:
#     topic = clean_text(topic)
#     extra_details = clean_text(extra_details)

#     style_prefix_map = {
#         "Cinematic": "A powerful, visually striking cinematic scene of",
#         "Anime": "A highly stylized anime illustration of",
#         "Realistic": "A highly realistic, visually polished depiction of",
#         "Creative": "An imaginative, visually rich composition of",
#         "Minimal": "A clean, elegant visual composition of",
#         "Professional": "A premium, polished visual concept of",
#         "Expert": "An ultra-refined, masterfully art-directed visual of"
#     }
#     style_suffix_map = {
#         "Cinematic": "high-octane cinematic movie poster composition",
#         "Anime": "dynamic anime key visual composition",
#         "Realistic": "photorealistic premium composition",
#         "Creative": "artistic high-impact composition",
#         "Minimal": "clean premium composition",
#         "Professional": "refined commercial-grade composition",
#         "Expert": "world-class concept art composition"
#     }

#     base_prefix = style_prefix_map.get(style, "A highly detailed visual of")
#     composition_style = style_suffix_map.get(style, "premium composition")

#     if style == "Anime":
#         tag_block = f"--stylize {stylize} --chaos {chaos} --quality {quality} --ar {aspect_ratio} --niji 6"
#     else:
#         tag_block = f"--stylize {stylize} --chaos {chaos} --quality {quality} --ar {aspect_ratio}"

#     body_parts = [
#         f"{base_prefix} {topic}",
#         shot_type,
#         f"{mood} atmosphere",
#         lighting,
#         camera,
#         f"color palette of {palette}",
#         texture,
#         composition_style,
#         render_quality,
#         "sharp focus",
#         "intricate details",
#         "depth and dimensionality"
#     ]

#     if extra_details:
#         body_parts.append(extra_details)

#     prompt = compact_join(body_parts)

#     if include_negative:
#         neg = clean_text(negative_prompt) or NEGATIVE_DEFAULT
#         prompt = f"{prompt} --no {neg}"

#     return f"{prompt} {tag_block}".strip()

# def build_final_prompt(use_case, topic, style, audience, extra_details, image_settings):
#     topic = clean_text(topic)
#     audience = clean_text(audience) or "the intended audience"
#     extra_details = clean_text(extra_details)
#     style_instruction = STYLE_GUIDE.get(style, "Use clear and high-quality language.")

#     if use_case == "Image Generation":
#         return build_image_prompt(
#             topic=topic,
#             style=style,
#             extra_details=extra_details,
#             shot_type=image_settings["shot_type"],
#             lighting=image_settings["lighting"],
#             mood=image_settings["mood"],
#             palette=image_settings["palette"],
#             camera=image_settings["camera"],
#             texture=image_settings["texture"],
#             render_quality=image_settings["render_quality"],
#             aspect_ratio=image_settings["aspect_ratio"],
#             stylize=image_settings["stylize"],
#             chaos=image_settings["chaos"],
#             quality=image_settings["quality"],
#             include_negative=image_settings["include_negative"],
#             negative_prompt=image_settings["negative_prompt"]
#         )

#     extra_line = f" Also ensure the output follows these requirements: {extra_details}" if extra_details else ""

#     if use_case == "Resume / Career":
#         return (
#             f"Act as an experienced career coach and professional personal branding expert. "
#             f"Write a strong, polished, and recruiter-friendly response about {topic} for {audience}. "
#             f"{style_instruction} Make the output clear, impactful, and tailored for real hiring scenarios. "
#             f"Highlight strengths, value, credibility, and professional positioning. "
#             f"Keep the language natural, confident, and modern while avoiding vague or generic statements."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Content Writing":
#         return (
#             f"Act as an expert content writer and strategist. Create high-quality content about {topic} for {audience}. "
#             f"{style_instruction} Make the response engaging, well-structured, easy to read, and valuable to the target audience. "
#             f"Include a strong opening, smooth flow, relevant details, and a compelling ending. "
#             f"Ensure the writing feels polished, natural, and ready to publish."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Coding":
#         return (
#             f"Act as a senior software engineer and coding assistant. Help with {topic} for {audience}. "
#             f"{style_instruction} Provide clean, correct, production-ready output with clear logic, readable structure, and best practices. "
#             f"Include explanations where useful, handle edge cases when relevant, and keep the solution practical and maintainable."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Business":
#         return (
#             f"Act as a strategic business consultant. Create a clear, practical, and insight-driven response about {topic} for {audience}. "
#             f"{style_instruction} Focus on business value, execution, realistic strategy, and actionable recommendations. "
#             f"Make the output structured, professional, and useful for decision-making."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Students":
#         return (
#             f"Act as an expert tutor and educational mentor. Explain or create content about {topic} for {audience}. "
#             f"{style_instruction} Make the response easy to understand, well-structured, accurate, and educational. "
#             f"Use simple explanations, step-by-step clarity, and examples wherever helpful."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Marketing":
#         return (
#             f"Act as an expert marketing strategist and copywriter. Create marketing content for {topic} aimed at {audience}. "
#             f"{style_instruction} Focus on audience attention, clarity, persuasion, brand relevance, and conversion potential. "
#             f"Make the output compelling, strategic, and ready for practical campaign use."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Startup Ideas":
#         return (
#             f"Act as an innovative startup advisor and product strategist. Generate strong ideas and strategic thinking around {topic} for {audience}. "
#             f"{style_instruction} Focus on real user pain points, market opportunity, differentiation, monetization, and execution potential. "
#             f"Keep the output practical, high-value, and startup-ready."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Social Media":
#         return (
#             f"Act as a social media strategist and content creator. Create content around {topic} for {audience}. "
#             f"{style_instruction} Make the output attention-grabbing, platform-friendly, engaging, and easy to consume. "
#             f"Use strong hooks, clear flow, and content that encourages interaction or retention."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Email Writing":
#         return (
#             f"Act as a professional communication expert. Write an effective email about {topic} for {audience}. "
#             f"{style_instruction} Make the email clear, polished, purposeful, and appropriate for the situation. "
#             f"Ensure the message has natural wording and a professional tone."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "YouTube Scripts":
#         return (
#             f"Act as an expert YouTube scriptwriter. Write a high-retention script about {topic} for {audience}. "
#             f"{style_instruction} Start with a strong hook, maintain clear pacing, keep the content engaging, and end with a strong closing or CTA. "
#             f"Make the script natural, audience-focused, and optimized for watch time and clarity."
#             f"{extra_line}"
#         ).strip()

#     return (
#         f"Act as an expert assistant. Create a high-quality response about {topic} for {audience}. "
#         f"{style_instruction} Make the output clear, useful, polished, and practical. "
#         f"Ensure the final result is easy to understand and directly usable."
#         f"{extra_line}"
#     ).strip()

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
#         height=360,
#         scrolling=False
#     )

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

#     st.markdown("### ✨ Features")
#     st.markdown("""
#     - Prompt history  
#     - Favorites  
#     - Random prompt  
#     - Regenerate  
#     - Download prompt  
#     - One-click copy  
#     - Pro image controls  
#     """)

# # -------------------------------
# # HERO
# # -------------------------------
# st.markdown("""
# <div class="hero-card">
#     <div class="badge">🚀 AI Prompt Workspace</div>
#     <div class="hero-title">PromptNexus AI</div>
#     <div class="hero-desc">
#         Generate final, crystal-clear prompts for content, coding, career, marketing, and ultra-detailed image generation.
#         Includes history, favorites, random ideas, regenerate, download, and one-click copy.
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # -------------------------------
# # MAIN INPUTS
# # -------------------------------
# use_case_options = list(USE_CASE_CONFIG.keys())

# col1, col2 = st.columns(2)
# with col1:
#     use_case = st.selectbox("Select Use Case", use_case_options, key="use_case_select")

# config = USE_CASE_CONFIG[use_case]

# with col2:
#     style = st.selectbox(
#         "Prompt Style",
#         ["Professional", "Creative", "Minimal", "Cinematic", "Anime", "Realistic", "Expert"],
#         key="style_select"
#     )

# col3, col4 = st.columns(2)

# with col3:
#     topic = st.text_input(
#         "Topic / Goal",
#         placeholder=config["topic_placeholder"],
#         key="topic_value"
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
#         placeholder=config["audience_placeholder"],
#         key="audience_value"
#     )
#     st.markdown(
#         '<div class="small-note">Audience suggestions change based on selected use case.</div>',
#         unsafe_allow_html=True
#     )

# extra_details = st.text_area(
#     "Extra Details / Requirements",
#     placeholder=config["extra_placeholder"],
#     height=130,
#     key="extra_value"
# )

# # -------------------------------
# # RANDOM PROMPT BUTTON
# # -------------------------------
# st.button("🎲 Random Prompt Idea", on_click=set_random_topic)

# # -------------------------------
# # IMAGE ADVANCED CONTROLS
# # -------------------------------
# default_image_settings = {
#     "shot_type": "low-angle hero shot",
#     "lighting": "dramatic rim lighting",
#     "mood": "epic",
#     "palette": "pastel lavender, baby blue, mint green, peach",
#     "camera": "movie poster framing",
#     "texture": "ultra-detailed metallic textures",
#     "render_quality": "professional 8k render",
#     "aspect_ratio": "2:3",
#     "stylize": 750,
#     "chaos": 12,
#     "quality": "1",
#     "include_negative": True,
#     "negative_prompt": NEGATIVE_DEFAULT
# }
# image_settings = default_image_settings.copy()

# if use_case == "Image Generation":
#     st.markdown('<div class="section-title">Advanced Image Controls</div>', unsafe_allow_html=True)

#     with st.expander("Open pro image controls", expanded=True):
#         g1, g2, g3 = st.columns(3)
#         with g1:
#             image_settings["shot_type"] = st.selectbox("Shot / Framing", SHOT_OPTIONS, index=0)
#             image_settings["lighting"] = st.selectbox("Lighting", LIGHTING_OPTIONS, index=0)
#             image_settings["mood"] = st.selectbox("Mood", MOOD_OPTIONS, index=0)
#         with g2:
#             image_settings["palette"] = st.selectbox("Color Palette", PALETTE_OPTIONS, index=0)
#             image_settings["camera"] = st.selectbox("Camera Feel", CAMERA_OPTIONS, index=3)
#             image_settings["texture"] = st.selectbox("Texture Detail", TEXTURE_OPTIONS, index=0)
#         with g3:
#             image_settings["render_quality"] = st.selectbox("Render Style", RENDER_OPTIONS, index=0)
#             image_settings["aspect_ratio"] = st.selectbox("Aspect Ratio", ["1:1", "2:3", "3:2", "4:5", "9:16", "16:9", "21:9"], index=1)
#             image_settings["quality"] = st.selectbox("Quality", ["0.5", "1", "2"], index=1)

#         s1, s2 = st.columns(2)
#         with s1:
#             image_settings["stylize"] = st.slider("Stylize", 0, 1000, 750, 25)
#         with s2:
#             image_settings["chaos"] = st.slider("Chaos", 0, 100, 12, 1)

#         image_settings["include_negative"] = st.checkbox("Include negative prompt", value=True)
#         if image_settings["include_negative"]:
#             image_settings["negative_prompt"] = st.text_area(
#                 "Negative Prompt",
#                 value=NEGATIVE_DEFAULT,
#                 height=90
#             )

# # -------------------------------
# # GENERATE
# # -------------------------------
# def generate_current_prompt():
#     current_topic = st.session_state.get("topic_value", "").strip()
#     current_audience = st.session_state.get("audience_value", "").strip()
#     current_extra = st.session_state.get("extra_value", "").strip()

#     if not current_topic:
#         st.warning("Please enter a Topic / Goal first.")
#         return

#     prompt = build_final_prompt(
#         use_case=st.session_state.get("use_case_select", "Content Writing"),
#         topic=current_topic,
#         style=st.session_state.get("style_select", "Professional"),
#         audience=current_audience,
#         extra_details=current_extra,
#         image_settings=image_settings
#     )

#     st.session_state.generated_prompt = prompt
#     st.session_state.last_generation_payload = {
#         "use_case": st.session_state.get("use_case_select", "Content Writing"),
#         "style": st.session_state.get("style_select", "Professional"),
#         "topic": current_topic,
#         "audience": current_audience,
#         "extra_details": current_extra,
#         "image_settings": image_settings.copy()
#     }
#     add_to_history(st.session_state.get("use_case_select", "Content Writing"), current_topic, prompt)

# b1, b2, b3, b4 = st.columns(4)

# with b1:
#     if st.button("✨ Generate Prompt"):
#         generate_current_prompt()

# with b2:
#     if st.button("🔁 Regenerate"):
#         if st.session_state.last_generation_payload:
#             payload = st.session_state.last_generation_payload
#             regenerated = build_final_prompt(
#                 use_case=payload["use_case"],
#                 topic=payload["topic"],
#                 style=payload["style"],
#                 audience=payload["audience"],
#                 extra_details=payload["extra_details"],
#                 image_settings=payload["image_settings"]
#             )
#             st.session_state.generated_prompt = regenerated
#             add_to_history(payload["use_case"], payload["topic"], regenerated)
#         else:
#             st.info("Generate a prompt first.")

# with b3:
#     if st.button("⭐ Save Favorite"):
#         if st.session_state.generated_prompt:
#             current_topic = st.session_state.get("topic_value", "").strip() or "Untitled"
#             add_to_favorites(st.session_state.get("use_case_select", "Content Writing"), current_topic, st.session_state.generated_prompt)
#             st.success("Added to favorites")
#         else:
#             st.info("Generate a prompt first.")

# with b4:
#     st.button("🗑 Clear", on_click=clear_all)

# # -------------------------------
# # OUTPUT
# # -------------------------------
# st.markdown('<div class="section-title">Prompt’s Generation</div>', unsafe_allow_html=True)

# if st.session_state.generated_prompt:
#     if st.session_state.get("use_case_select") == "Image Generation":
#         st.markdown("""
#         <div style="margin-bottom:8px;">
#             <span class="prompt-chip">Direct image prompt</span>
#             <span class="prompt-chip">Ready to paste</span>
#             <span class="prompt-chip">Pro visual detail</span>
#         </div>
#         """, unsafe_allow_html=True)

#     render_copyable_prompt(st.session_state.generated_prompt)

#     st.download_button(
#         label="📥 Download Prompt",
#         data=st.session_state.generated_prompt,
#         file_name="promptnexus_prompt.txt",
#         mime="text/plain"
#     )
# else:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">No prompt generated yet</div>
#         <div class="feature-text">
#             Select a use case, enter your topic, choose style and settings, then click <b>Generate Prompt</b>.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# # -------------------------------
# # HISTORY + FAVORITES
# # -------------------------------
# left_panel, right_panel = st.columns(2)

# with left_panel:
#     st.markdown('<div class="section-title">Recent Prompt History</div>', unsafe_allow_html=True)
#     if st.session_state.history:
#         for item in st.session_state.history[:5]:
#             st.markdown(
#                 f"""
#                 <div class="history-card">
#                     <div class="history-meta">{item['timestamp']} • {item['use_case']}</div>
#                     <div class="history-title">{item['topic']}</div>
#                     <div class="history-text">{html.escape(item['prompt'][:220])}{"..." if len(item['prompt']) > 220 else ""}</div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
#     else:
#         st.markdown("""
#         <div class="feature-card">
#             <div class="feature-title">No history yet</div>
#             <div class="feature-text">Your recent prompts will appear here.</div>
#         </div>
#         """, unsafe_allow_html=True)

# with right_panel:
#     st.markdown('<div class="section-title">Favorite Prompts</div>', unsafe_allow_html=True)
#     if st.session_state.favorites:
#         for item in st.session_state.favorites[:5]:
#             st.markdown(
#                 f"""
#                 <div class="history-card">
#                     <div class="history-meta">{item['timestamp']} • {item['use_case']}</div>
#                     <div class="history-title">{item['topic']}</div>
#                     <div class="history-text">{html.escape(item['prompt'][:220])}{"..." if len(item['prompt']) > 220 else ""}</div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
#     else:
#         st.markdown("""
#         <div class="feature-card">
#             <div class="feature-title">No favorites yet</div>
#             <div class="feature-text">Save your best prompts to see them here.</div>
#         </div>
#         """, unsafe_allow_html=True)

# # -------------------------------
# # FEATURES
# # -------------------------------
# st.markdown('<div class="section-title">Why PromptNexus AI?</div>', unsafe_allow_html=True)

# f1, f2, f3 = st.columns(3)

# with f1:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">🧠 Final Prompt Output</div>
#         <div class="feature-text">
#             Generates direct, usable prompts instead of meta instructions or prompt-overview text.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with f2:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">📜 History + Favorites</div>
#         <div class="feature-text">
#             Keep track of your latest prompts and save the best ones for quick reuse.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with f3:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">🎨 Pro Image Controls</div>
#         <div class="feature-text">
#             Build much richer image prompts with framing, lighting, mood, palette, stylize, chaos, and negative prompt controls.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# # -------------------------------
# # FOOTER
# # -------------------------------
# st.markdown("""
# <br>
# <div style="text-align:center; color:#94A3B8; font-size:14px; padding-bottom:10px;">
#     Built with ❤️ By GANESH GODDILLAfor smarter prompting • <b>PromptNexus AI</b>
# </div>
# """, unsafe_allow_html=True)



# import streamlit as st
# import streamlit.components.v1 as components
# import html
# import random
# from datetime import datetime, timezone

# import resend
# from supabase import Client, create_client

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
# # REQUIRED SECRETS
# # -------------------------------
# # Add these to .streamlit/secrets.toml
# #
# # SUPABASE_URL = "https://YOUR_PROJECT.supabase.co"
# # SUPABASE_ANON_KEY = "YOUR_SUPABASE_ANON_KEY"
# # RESEND_API_KEY = "re_xxxxxxxxx"
# # OWNER_EMAIL = "yourmail@example.com"
# # SENDER_EMAIL = "PromptNexus AI <onboarding@resend.dev>"
# #
# # For production, replace onboarding@resend.dev with your verified sender.

# SUPABASE_URL = st.secrets.get("SUPABASE_URL", "")
# SUPABASE_ANON_KEY = st.secrets.get("SUPABASE_ANON_KEY", "")
# RESEND_API_KEY = st.secrets.get("RESEND_API_KEY", "")
# OWNER_EMAIL = st.secrets.get("OWNER_EMAIL", "")
# SENDER_EMAIL = st.secrets.get("SENDER_EMAIL", "PromptNexus AI <onboarding@resend.dev>")

# SECRETS_READY = all([
#     SUPABASE_URL,
#     SUPABASE_ANON_KEY,
#     RESEND_API_KEY,
#     OWNER_EMAIL,
# ])


# @st.cache_resource
# def get_supabase_client() -> Client:
#     return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)


# if SECRETS_READY:
#     supabase = get_supabase_client()
#     resend.api_key = RESEND_API_KEY
# else:
#     supabase = None

# # -------------------------------
# # SESSION STATE DEFAULTS
# # -------------------------------
# defaults = {
#     "generated_prompt": "",
#     "history": [],
#     "favorites": [],
#     "last_generation_payload": None,
#     "topic_value": "",
#     "audience_value": "",
#     "extra_value": "",
#     "use_case_select": "Content Writing",
#     "style_select": "Professional",
#     "auth_email": "",
#     "auth_code": "",
#     "auth_requested": False,
#     "user_logged_in": False,
#     "user_email": "",
#     "user_id": "",
#     "login_notice_sent": False,
# }
# for key, value in defaults.items():
#     if key not in st.session_state:
#         st.session_state[key] = value

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
# label, .stSelectbox label, .stTextInput label, .stTextArea label, .stSlider label {
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
# .prompt-chip {
#     display: inline-block;
#     padding: 6px 10px;
#     margin: 4px 6px 4px 0;
#     border-radius: 999px;
#     font-size: 12px;
#     color: #e2e8f0;
#     background: rgba(255,255,255,0.05);
#     border: 1px solid rgba(255,255,255,0.08);
# }
# .history-card {
#     background: rgba(17,24,39,0.82);
#     border: 1px solid rgba(255,255,255,0.07);
#     border-radius: 18px;
#     padding: 14px;
#     margin-bottom: 12px;
# }
# .history-meta {
#     color: #94A3B8;
#     font-size: 12px;
#     margin-bottom: 8px;
# }
# .history-title {
#     color: #F8FAFC;
#     font-weight: 700;
#     font-size: 14px;
#     margin-bottom: 6px;
# }
# .history-text {
#     color: #CBD5E1;
#     font-size: 13px;
#     line-height: 1.6;
# }
# .stDownloadButton > button {
#     width: 100%;
#     border-radius: 16px;
#     border: none;
#     padding: 0.75rem 1rem;
#     font-weight: 700;
#     font-size: 15px;
#     color: white;
#     background: linear-gradient(90deg, #111827, #1F2937);
#     border: 1px solid rgba(255,255,255,0.10);
# }
# div[data-testid="stExpander"] {
#     border-radius: 16px !important;
#     border: 1px solid rgba(255,255,255,0.08) !important;
#     overflow: hidden;
# }
# .user-pill {
#     background: rgba(0, 212, 255, 0.10);
#     border: 1px solid rgba(0, 212, 255, 0.18);
#     color: #c4f1ff;
#     border-radius: 14px;
#     padding: 10px 12px;
#     margin-bottom: 14px;
#     font-size: 13px;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # DATA
# # -------------------------------
# USE_CASE_CONFIG = {
#     "Content Writing": {
#         "topic_placeholder": "e.g. Write a blog post on AI tools for productivity",
#         "audience_placeholder": "e.g. content creators, bloggers, marketers",
#         "extra_placeholder": "Add tone, length, SEO keywords, platform, CTA, and output format.",
#         "examples": [
#             "Instagram caption for a fitness brand launch",
#             "SEO blog post on beginner MLOps roadmap",
#             "LinkedIn post about GenAI career transition"
#         ],
#         "random_topics": [
#             "LinkedIn post about AI productivity tools",
#             "Blog article on beginner MLOps roadmap",
#             "Instagram caption for a new tech gadget launch"
#         ]
#     },
#     "Coding": {
#         "topic_placeholder": "e.g. Build a Python script for file organizer automation",
#         "audience_placeholder": "e.g. Python developers, beginners, backend engineers",
#         "extra_placeholder": "Mention language, framework, edge cases, output style, and constraints.",
#         "examples": [
#             "Streamlit app for AI prompt generator",
#             "FastAPI REST API with authentication",
#             "Python function to parse logs and summarize errors"
#         ],
#         "random_topics": [
#             "Python script to organize files by extension",
#             "FastAPI endpoint with JWT authentication",
#             "Streamlit dashboard for sales analytics"
#         ]
#     },
#     "Business": {
#         "topic_placeholder": "e.g. Create a startup idea for AI resume review tool",
#         "audience_placeholder": "e.g. startup founders, consultants, entrepreneurs",
#         "extra_placeholder": "Mention industry, users, pricing, business goal, and market angle.",
#         "examples": [
#             "Business plan for a faceless YouTube automation agency",
#             "Pricing strategy for AI SaaS tool",
#             "Go-to-market plan for student productivity app"
#         ],
#         "random_topics": [
#             "Pricing strategy for AI SaaS product",
#             "Business model for freelancer marketplace",
#             "Go-to-market plan for student productivity app"
#         ]
#     },
#     "Students": {
#         "topic_placeholder": "e.g. Explain neural networks in simple terms",
#         "audience_placeholder": "e.g. school students, college students, exam aspirants",
#         "extra_placeholder": "Mention subject, difficulty, answer style, format, and examples needed.",
#         "examples": [
#             "Study notes for DBMS interview preparation",
#             "Simple explanation of cloud computing",
#             "5-mark answer for machine learning basics"
#         ],
#         "random_topics": [
#             "Simple explanation of cloud computing",
#             "DBMS notes for interview preparation",
#             "Machine learning basics for beginners"
#         ]
#     },
#     "General Use": {
#         "topic_placeholder": "e.g. Write a professional email requesting project access",
#         "audience_placeholder": "e.g. professionals, freelancers, general users",
#         "extra_placeholder": "Mention context, tone, recipient, and desired structure.",
#         "examples": [
#             "Professional apology email to manager",
#             "Daily planner for a productive workday",
#             "Checklist for moving to a new city"
#         ],
#         "random_topics": [
#             "Professional apology email to manager",
#             "Daily productivity planner",
#             "Checklist for moving to a new city"
#         ]
#     },
#     "Marketing": {
#         "topic_placeholder": "e.g. Create ad copy for eco-friendly water bottle",
#         "audience_placeholder": "e.g. customers, marketers, D2C brands",
#         "extra_placeholder": "Mention product, platform, brand tone, CTA, and campaign goal.",
#         "examples": [
#             "Facebook ad copy for skincare product",
#             "Email campaign for Black Friday sale",
#             "Brand tagline ideas for AI startup"
#         ],
#         "random_topics": [
#             "Facebook ad copy for skincare brand",
#             "Email campaign for festive sale",
#             "Tagline ideas for AI startup"
#         ]
#     },
#     "Resume / Career": {
#         "topic_placeholder": "e.g. Rewrite my resume summary for MLOps engineer role",
#         "audience_placeholder": "e.g. recruiters, hiring managers, job seekers",
#         "extra_placeholder": "Mention target role, experience level, key skills, and tone.",
#         "examples": [
#             "Resume bullet points for Python developer",
#             "Cover letter for GenAI engineer role",
#             "LinkedIn About section for fresher in MLOps"
#         ],
#         "random_topics": [
#             "LinkedIn About section for fresher in MLOps",
#             "Resume summary for Python developer",
#             "Cover letter for GenAI engineer role"
#         ]
#     },
#     "Startup Ideas": {
#         "topic_placeholder": "e.g. Generate startup ideas using GenAI in education",
#         "audience_placeholder": "e.g. founders, investors, builders",
#         "extra_placeholder": "Mention niche, user pain point, monetization, and business type.",
#         "examples": [
#             "Low-cost AI SaaS ideas for India",
#             "B2B startup idea for internal documentation",
#             "One-person startup ideas in automation"
#         ],
#         "random_topics": [
#             "AI startup ideas for education",
#             "One-person startup ideas in automation",
#             "B2B AI tool for internal documentation"
#         ]
#     },
#     "Social Media": {
#         "topic_placeholder": "e.g. Create 10 reel ideas for AI productivity content",
#         "audience_placeholder": "e.g. Instagram audience, creators, YouTube viewers",
#         "extra_placeholder": "Mention platform, tone, hook style, audience, and niche.",
#         "examples": [
#             "YouTube Shorts script on AI tools",
#             "Twitter thread on beginner coding mistakes",
#             "Instagram carousel post on career growth"
#         ],
#         "random_topics": [
#             "10 Instagram reel ideas for AI productivity",
#             "Twitter thread on common coding mistakes",
#             "Carousel post on career growth tips"
#         ]
#     },
#     "Email Writing": {
#         "topic_placeholder": "e.g. Draft an email asking for project status update",
#         "audience_placeholder": "e.g. manager, HR, client, colleague",
#         "extra_placeholder": "Mention sender goal, urgency, context, and tone.",
#         "examples": [
#             "Leave request email",
#             "Follow-up email after interview",
#             "Formal escalation email for blocked task"
#         ],
#         "random_topics": [
#             "Leave request email",
#             "Interview follow-up email",
#             "Formal escalation email for blocked task"
#         ]
#     },
#     "Image Generation": {
#         "topic_placeholder": "e.g. Marvel-style superhero poster in pastel space",
#         "audience_placeholder": "e.g. creators, designers, Midjourney users",
#         "extra_placeholder": "Mention must-have details, pose, objects, setting, color direction, or restrictions.",
#         "examples": [
#             "Anime warrior in neon city at night",
#             "Luxury product ad shot with soft lighting",
#             "Marvel-style superhero poster in pastel space"
#         ],
#         "random_topics": [
#             "Marvel-style superhero poster in pastel space",
#             "Anime warrior in neon city at night",
#             "Cyberpunk female assassin in rainy alley"
#         ]
#     },
#     "YouTube Scripts": {
#         "topic_placeholder": "e.g. Write a 60-second YouTube script on top AI tools",
#         "audience_placeholder": "e.g. YouTube viewers, beginners, tech audience",
#         "extra_placeholder": "Mention duration, tone, niche, hook style, CTA, and pacing.",
#         "examples": [
#             "60-second script for motivation reel",
#             "Faceless finance video script",
#             "Tech explainer script on ChatGPT vs OpenAI"
#         ],
#         "random_topics": [
#             "60-second YouTube script on top AI tools",
#             "Faceless finance video script",
#             "Tech explainer on ChatGPT vs OpenAI"
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

# SHOT_OPTIONS = [
#     "low-angle hero shot", "close-up portrait", "wide cinematic shot", "mid-shot composition",
#     "full-body character shot", "over-the-shoulder shot", "bird's-eye view", "dynamic action frame"
# ]
# LIGHTING_OPTIONS = [
#     "dramatic rim lighting", "soft diffused lighting", "golden hour glow", "neon glow",
#     "volumetric god rays", "studio lighting", "moonlit ambience", "high contrast cinematic lighting"
# ]
# MOOD_OPTIONS = ["epic", "dreamy", "mysterious", "dark fantasy", "heroic", "ethereal", "intense", "calm"]
# PALETTE_OPTIONS = [
#     "pastel lavender, baby blue, mint green, peach",
#     "deep blue, violet, silver",
#     "neon cyan, magenta, purple",
#     "gold, crimson, black",
#     "warm beige, ivory, bronze",
#     "emerald, teal, obsidian"
# ]
# CAMERA_OPTIONS = [
#     "cinematic lens feel", "85mm portrait feel", "ultra-wide lens perspective",
#     "movie poster framing", "editorial fashion framing", "DSLR realism", "anamorphic cinematic framing"
# ]
# TEXTURE_OPTIONS = [
#     "ultra-detailed metallic textures", "soft fabric detail", "crystalline surfaces",
#     "photoreal skin detail", "glossy reflective surfaces", "matte cinematic textures"
# ]
# RENDER_OPTIONS = [
#     "professional 8k render", "ultra-detailed digital art", "high-end concept art",
#     "AAA game art quality", "cinematic movie poster quality", "photorealistic studio render"
# ]
# NEGATIVE_DEFAULT = "blurry, low quality, distorted anatomy, extra fingers, cropped, duplicate, watermark, text, logo, oversaturated, noisy background"

# # -------------------------------
# # HELPERS
# # -------------------------------
# def clean_text(value: str) -> str:
#     return value.strip() if value else ""


# def compact_join(parts):
#     return ", ".join([p for p in parts if clean_text(p)])


# def add_to_history(use_case: str, topic: str, prompt: str) -> None:
#     entry = {
#         "use_case": use_case,
#         "topic": topic,
#         "prompt": prompt,
#         "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
#     }
#     st.session_state.history.insert(0, entry)
#     st.session_state.history = st.session_state.history[:10]


# def add_to_favorites(use_case: str, topic: str, prompt: str) -> None:
#     already_exists = any(fav["prompt"] == prompt for fav in st.session_state.favorites)
#     if not already_exists:
#         st.session_state.favorites.insert(0, {
#             "use_case": use_case,
#             "topic": topic,
#             "prompt": prompt,
#             "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
#         })
#         st.session_state.favorites = st.session_state.favorites[:20]


# def set_random_topic():
#     current_use_case = st.session_state.get("use_case_select", "Content Writing")
#     current_config = USE_CASE_CONFIG[current_use_case]
#     st.session_state["topic_value"] = random.choice(current_config["random_topics"])


# def clear_all():
#     st.session_state.generated_prompt = ""
#     st.session_state.topic_value = ""
#     st.session_state.audience_value = ""
#     st.session_state.extra_value = ""


# def logout_user():
#     st.session_state.user_logged_in = False
#     st.session_state.user_email = ""
#     st.session_state.user_id = ""
#     st.session_state.auth_requested = False
#     st.session_state.auth_code = ""
#     st.session_state.login_notice_sent = False
#     st.rerun()


# def send_owner_login_notification(user_email: str, user_id: str):
#     if not RESEND_API_KEY or not OWNER_EMAIL:
#         return

#     try:
#         resend.Emails.send({
#             "from": SENDER_EMAIL,
#             "to": [OWNER_EMAIL],
#             "subject": "New PromptNexus AI login",
#             "html": f"""
#                 <div style=\"font-family:Arial,sans-serif;line-height:1.6\">
#                     <h2>New user login</h2>
#                     <p><strong>Email:</strong> {html.escape(user_email)}</p>
#                     <p><strong>User ID:</strong> {html.escape(user_id)}</p>
#                     <p><strong>Time (UTC):</strong> {datetime.now(timezone.utc).strftime('%d-%m-%Y %H:%M:%S')}</p>
#                 </div>
#             """
#         })
#     except Exception as e:
#         st.warning(f"Owner email notification failed: {e}")


# def store_login_event(user_email: str, user_id: str):
#     if not supabase:
#         return

#     try:
#         supabase.table("login_events").insert({
#             "email": user_email,
#             "user_id": user_id,
#             "logged_at": datetime.now(timezone.utc).isoformat()
#         }).execute()
#     except Exception:
#         pass


# def request_email_otp(email_value: str):
#     if not supabase:
#         st.error("Missing app secrets. Please configure Supabase and Resend first.")
#         return

#     try:
#         supabase.auth.sign_in_with_otp({
#             "email": email_value,
#             "options": {
#                 "should_create_user": True
#             }
#         })
#         st.session_state.auth_requested = True
#         st.success("Login code sent to your email.")
#         st.info("In Supabase, set the email template to show the OTP token if you want users to enter a 6-digit code.")
#     except Exception as e:
#         st.error(f"Could not send login code: {e}")


# def verify_email_otp(email_value: str, otp_code: str):
#     if not supabase:
#         st.error("Missing app secrets. Please configure Supabase and Resend first.")
#         return

#     try:
#         result = supabase.auth.verify_otp({
#             "email": email_value,
#             "token": otp_code,
#             "type": "email"
#         })

#         user = None
#         if hasattr(result, "user") and result.user is not None:
#             user = result.user
#         elif hasattr(result, "session") and result.session is not None and hasattr(result.session, "user"):
#             user = result.session.user
#         elif isinstance(result, dict):
#             user = result.get("user")
#             if user is None and result.get("session"):
#                 session = result.get("session")
#                 if isinstance(session, dict):
#                     user = session.get("user")

#         if not user:
#             st.error("OTP verified, but no user details were returned.")
#             return

#         user_email = getattr(user, "email", None) if not isinstance(user, dict) else user.get("email")
#         user_id = getattr(user, "id", None) if not isinstance(user, dict) else user.get("id")

#         st.session_state.user_logged_in = True
#         st.session_state.user_email = user_email or email_value
#         st.session_state.user_id = user_id or "unknown"
#         st.session_state.auth_requested = False
#         st.session_state.login_notice_sent = False

#         if not st.session_state.login_notice_sent:
#             store_login_event(st.session_state.user_email, st.session_state.user_id)
#             send_owner_login_notification(st.session_state.user_email, st.session_state.user_id)
#             st.session_state.login_notice_sent = True

#         st.success("Login successful.")
#         st.rerun()
#     except Exception as e:
#         st.error(f"Invalid or expired code: {e}")


# def build_image_prompt(
#     topic: str,
#     style: str,
#     extra_details: str,
#     shot_type: str,
#     lighting: str,
#     mood: str,
#     palette: str,
#     camera: str,
#     texture: str,
#     render_quality: str,
#     aspect_ratio: str,
#     stylize: int,
#     chaos: int,
#     quality: str,
#     include_negative: bool,
#     negative_prompt: str
# ) -> str:
#     topic = clean_text(topic)
#     extra_details = clean_text(extra_details)

#     style_prefix_map = {
#         "Cinematic": "A powerful, visually striking cinematic scene of",
#         "Anime": "A highly stylized anime illustration of",
#         "Realistic": "A highly realistic, visually polished depiction of",
#         "Creative": "An imaginative, visually rich composition of",
#         "Minimal": "A clean, elegant visual composition of",
#         "Professional": "A premium, polished visual concept of",
#         "Expert": "An ultra-refined, masterfully art-directed visual of"
#     }
#     style_suffix_map = {
#         "Cinematic": "high-octane cinematic movie poster composition",
#         "Anime": "dynamic anime key visual composition",
#         "Realistic": "photorealistic premium composition",
#         "Creative": "artistic high-impact composition",
#         "Minimal": "clean premium composition",
#         "Professional": "refined commercial-grade composition",
#         "Expert": "world-class concept art composition"
#     }

#     base_prefix = style_prefix_map.get(style, "A highly detailed visual of")
#     composition_style = style_suffix_map.get(style, "premium composition")

#     if style == "Anime":
#         tag_block = f"--stylize {stylize} --chaos {chaos} --quality {quality} --ar {aspect_ratio} --niji 6"
#     else:
#         tag_block = f"--stylize {stylize} --chaos {chaos} --quality {quality} --ar {aspect_ratio}"

#     body_parts = [
#         f"{base_prefix} {topic}",
#         shot_type,
#         f"{mood} atmosphere",
#         lighting,
#         camera,
#         f"color palette of {palette}",
#         texture,
#         composition_style,
#         render_quality,
#         "sharp focus",
#         "intricate details",
#         "depth and dimensionality"
#     ]

#     if extra_details:
#         body_parts.append(extra_details)

#     prompt = compact_join(body_parts)

#     if include_negative:
#         neg = clean_text(negative_prompt) or NEGATIVE_DEFAULT
#         prompt = f"{prompt} --no {neg}"

#     return f"{prompt} {tag_block}".strip()


# def build_final_prompt(use_case, topic, style, audience, extra_details, image_settings):
#     topic = clean_text(topic)
#     audience = clean_text(audience) or "the intended audience"
#     extra_details = clean_text(extra_details)
#     style_instruction = STYLE_GUIDE.get(style, "Use clear and high-quality language.")

#     if use_case == "Image Generation":
#         return build_image_prompt(
#             topic=topic,
#             style=style,
#             extra_details=extra_details,
#             shot_type=image_settings["shot_type"],
#             lighting=image_settings["lighting"],
#             mood=image_settings["mood"],
#             palette=image_settings["palette"],
#             camera=image_settings["camera"],
#             texture=image_settings["texture"],
#             render_quality=image_settings["render_quality"],
#             aspect_ratio=image_settings["aspect_ratio"],
#             stylize=image_settings["stylize"],
#             chaos=image_settings["chaos"],
#             quality=image_settings["quality"],
#             include_negative=image_settings["include_negative"],
#             negative_prompt=image_settings["negative_prompt"]
#         )

#     extra_line = f" Also ensure the output follows these requirements: {extra_details}" if extra_details else ""

#     if use_case == "Resume / Career":
#         return (
#             f"Act as an experienced career coach and professional personal branding expert. "
#             f"Write a strong, polished, and recruiter-friendly response about {topic} for {audience}. "
#             f"{style_instruction} Make the output clear, impactful, and tailored for real hiring scenarios. "
#             f"Highlight strengths, value, credibility, and professional positioning. "
#             f"Keep the language natural, confident, and modern while avoiding vague or generic statements."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Content Writing":
#         return (
#             f"Act as an expert content writer and strategist. Create high-quality content about {topic} for {audience}. "
#             f"{style_instruction} Make the response engaging, well-structured, easy to read, and valuable to the target audience. "
#             f"Include a strong opening, smooth flow, relevant details, and a compelling ending. "
#             f"Ensure the writing feels polished, natural, and ready to publish."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Coding":
#         return (
#             f"Act as a senior software engineer and coding assistant. Help with {topic} for {audience}. "
#             f"{style_instruction} Provide clean, correct, production-ready output with clear logic, readable structure, and best practices. "
#             f"Include explanations where useful, handle edge cases when relevant, and keep the solution practical and maintainable."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Business":
#         return (
#             f"Act as a strategic business consultant. Create a clear, practical, and insight-driven response about {topic} for {audience}. "
#             f"{style_instruction} Focus on business value, execution, realistic strategy, and actionable recommendations. "
#             f"Make the output structured, professional, and useful for decision-making."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Students":
#         return (
#             f"Act as an expert tutor and educational mentor. Explain or create content about {topic} for {audience}. "
#             f"{style_instruction} Make the response easy to understand, well-structured, accurate, and educational. "
#             f"Use simple explanations, step-by-step clarity, and examples wherever helpful."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Marketing":
#         return (
#             f"Act as an expert marketing strategist and copywriter. Create marketing content for {topic} aimed at {audience}. "
#             f"{style_instruction} Focus on audience attention, clarity, persuasion, brand relevance, and conversion potential. "
#             f"Make the output compelling, strategic, and ready for practical campaign use."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Startup Ideas":
#         return (
#             f"Act as an innovative startup advisor and product strategist. Generate strong ideas and strategic thinking around {topic} for {audience}. "
#             f"{style_instruction} Focus on real user pain points, market opportunity, differentiation, monetization, and execution potential. "
#             f"Keep the output practical, high-value, and startup-ready."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Social Media":
#         return (
#             f"Act as a social media strategist and content creator. Create content around {topic} for {audience}. "
#             f"{style_instruction} Make the output attention-grabbing, platform-friendly, engaging, and easy to consume. "
#             f"Use strong hooks, clear flow, and content that encourages interaction or retention."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "Email Writing":
#         return (
#             f"Act as a professional communication expert. Write an effective email about {topic} for {audience}. "
#             f"{style_instruction} Make the email clear, polished, purposeful, and appropriate for the situation. "
#             f"Ensure the message has natural wording and a professional tone."
#             f"{extra_line}"
#         ).strip()

#     if use_case == "YouTube Scripts":
#         return (
#             f"Act as an expert YouTube scriptwriter. Write a high-retention script about {topic} for {audience}. "
#             f"{style_instruction} Start with a strong hook, maintain clear pacing, keep the content engaging, and end with a strong closing or CTA. "
#             f"Make the script natural, audience-focused, and optimized for watch time and clarity."
#             f"{extra_line}"
#         ).strip()

#     return (
#         f"Act as an expert assistant. Create a high-quality response about {topic} for {audience}. "
#         f"{style_instruction} Make the output clear, useful, polished, and practical. "
#         f"Ensure the final result is easy to understand and directly usable."
#         f"{extra_line}"
#     ).strip()


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
#         height=360,
#         scrolling=False
#     )

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

#     if st.session_state.user_logged_in:
#         st.markdown(
#             f"""
#             <div class="user-pill">
#                 <b>Logged in as</b><br>{html.escape(st.session_state.user_email)}
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
#         if st.button("🚪 Logout"):
#             logout_user()

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

#     st.markdown("### ✨ Features")
#     st.markdown("""
#     - Email OTP login  
#     - Prompt history  
#     - Favorites  
#     - Random prompt  
#     - Regenerate  
#     - Download prompt  
#     - One-click copy  
#     - Pro image controls  
#     """)

# # -------------------------------
# # LOGIN GATE
# # -------------------------------
# if not SECRETS_READY:
#     st.markdown("""
#     <div class="hero-card">
#         <div class="badge">⚠️ Setup Required</div>
#         <div class="hero-title">Configure auth first</div>
#         <div class="hero-desc">
#             Add SUPABASE_URL, SUPABASE_ANON_KEY, RESEND_API_KEY, OWNER_EMAIL, and SENDER_EMAIL to your Streamlit secrets.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
#     st.stop()

# if not st.session_state.user_logged_in:
#     st.markdown("""
#     <div class="hero-card">
#         <div class="badge">🔐 Email Login</div>
#         <div class="hero-title">Login to PromptNexus AI</div>
#         <div class="hero-desc">
#             Enter your email, receive a login code, and access the app without a password.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     with st.form("login_form"):
#         login_col1, login_col2 = st.columns(2)
#         with login_col1:
#             st.text_input(
#                 "Email address",
#                 placeholder="you@example.com",
#                 key="auth_email"
#             )
#         with login_col2:
#             st.text_input(
#                 "6-digit code",
#                 placeholder="Enter code from email",
#                 key="auth_code"
#             )

#         a1, a2 = st.columns(2)
#         send_clicked = a1.form_submit_button("📩 Send Login Code")
#         verify_clicked = a2.form_submit_button("✅ Verify & Login")

#     if send_clicked:
#         email_value = clean_text(st.session_state.auth_email).lower()
#         if not email_value:
#             st.warning("Please enter your email first.")
#         else:
#             request_email_otp(email_value)

#     if verify_clicked:
#         email_value = clean_text(st.session_state.auth_email).lower()
#         otp_code = clean_text(st.session_state.auth_code)
#         if not email_value:
#             st.warning("Please enter your email.")
#         elif not otp_code:
#             st.warning("Please enter the 6-digit code.")
#         else:
#             verify_email_otp(email_value, otp_code)

#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">How it works</div>
#         <div class="feature-text">
#             1) Enter your email<br>
#             2) Click Send Login Code<br>
#             3) Check your inbox<br>
#             4) Enter the code<br>
#             5) Use PromptNexus AI
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.stop()

# # -------------------------------
# # HERO
# # -------------------------------
# st.markdown("""
# <div class="hero-card">
#     <div class="badge">🚀 AI Prompt Workspace</div>
#     <div class="hero-title">PromptNexus AI</div>
#     <div class="hero-desc">
#         Generate final, crystal-clear prompts for content, coding, career, marketing, and ultra-detailed image generation.
#         Includes history, favorites, random ideas, regenerate, download, and one-click copy.
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # -------------------------------
# # MAIN INPUTS
# # -------------------------------
# use_case_options = list(USE_CASE_CONFIG.keys())

# col1, col2 = st.columns(2)
# with col1:
#     use_case = st.selectbox("Select Use Case", use_case_options, key="use_case_select")

# config = USE_CASE_CONFIG[use_case]

# with col2:
#     style = st.selectbox(
#         "Prompt Style",
#         ["Professional", "Creative", "Minimal", "Cinematic", "Anime", "Realistic", "Expert"],
#         key="style_select"
#     )

# col3, col4 = st.columns(2)

# with col3:
#     topic = st.text_input(
#         "Topic / Goal",
#         placeholder=config["topic_placeholder"],
#         key="topic_value"
#     )
#     st.markdown(
#         f"""
#         <div class="example-box">
#             <b>Examples for {use_case}:</b><br>
#             • {config['examples'][0]}<br>
#             • {config['examples'][1]}<br>
#             • {config['examples'][2]}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# with col4:
#     audience = st.text_input(
#         "Target Audience",
#         placeholder=config["audience_placeholder"],
#         key="audience_value"
#     )
#     st.markdown(
#         '<div class="small-note">Audience suggestions change based on selected use case.</div>',
#         unsafe_allow_html=True
#     )

# extra_details = st.text_area(
#     "Extra Details / Requirements",
#     placeholder=config["extra_placeholder"],
#     height=130,
#     key="extra_value"
# )

# # -------------------------------
# # RANDOM PROMPT BUTTON
# # -------------------------------
# st.button("🎲 Random Prompt Idea", on_click=set_random_topic)

# # -------------------------------
# # IMAGE ADVANCED CONTROLS
# # -------------------------------
# default_image_settings = {
#     "shot_type": "low-angle hero shot",
#     "lighting": "dramatic rim lighting",
#     "mood": "epic",
#     "palette": "pastel lavender, baby blue, mint green, peach",
#     "camera": "movie poster framing",
#     "texture": "ultra-detailed metallic textures",
#     "render_quality": "professional 8k render",
#     "aspect_ratio": "2:3",
#     "stylize": 750,
#     "chaos": 12,
#     "quality": "1",
#     "include_negative": True,
#     "negative_prompt": NEGATIVE_DEFAULT
# }
# image_settings = default_image_settings.copy()

# if use_case == "Image Generation":
#     st.markdown('<div class="section-title">Advanced Image Controls</div>', unsafe_allow_html=True)

#     with st.expander("Open pro image controls", expanded=True):
#         g1, g2, g3 = st.columns(3)
#         with g1:
#             image_settings["shot_type"] = st.selectbox("Shot / Framing", SHOT_OPTIONS, index=0)
#             image_settings["lighting"] = st.selectbox("Lighting", LIGHTING_OPTIONS, index=0)
#             image_settings["mood"] = st.selectbox("Mood", MOOD_OPTIONS, index=0)
#         with g2:
#             image_settings["palette"] = st.selectbox("Color Palette", PALETTE_OPTIONS, index=0)
#             image_settings["camera"] = st.selectbox("Camera Feel", CAMERA_OPTIONS, index=3)
#             image_settings["texture"] = st.selectbox("Texture Detail", TEXTURE_OPTIONS, index=0)
#         with g3:
#             image_settings["render_quality"] = st.selectbox("Render Style", RENDER_OPTIONS, index=0)
#             image_settings["aspect_ratio"] = st.selectbox("Aspect Ratio", ["1:1", "2:3", "3:2", "4:5", "9:16", "16:9", "21:9"], index=1)
#             image_settings["quality"] = st.selectbox("Quality", ["0.5", "1", "2"], index=1)

#         s1, s2 = st.columns(2)
#         with s1:
#             image_settings["stylize"] = st.slider("Stylize", 0, 1000, 750, 25)
#         with s2:
#             image_settings["chaos"] = st.slider("Chaos", 0, 100, 12, 1)

#         image_settings["include_negative"] = st.checkbox("Include negative prompt", value=True)
#         if image_settings["include_negative"]:
#             image_settings["negative_prompt"] = st.text_area(
#                 "Negative Prompt",
#                 value=NEGATIVE_DEFAULT,
#                 height=90
#             )

# # -------------------------------
# # GENERATE
# # -------------------------------
# def generate_current_prompt():
#     current_topic = st.session_state.get("topic_value", "").strip()
#     current_audience = st.session_state.get("audience_value", "").strip()
#     current_extra = st.session_state.get("extra_value", "").strip()

#     if not current_topic:
#         st.warning("Please enter a Topic / Goal first.")
#         return

#     prompt = build_final_prompt(
#         use_case=st.session_state.get("use_case_select", "Content Writing"),
#         topic=current_topic,
#         style=st.session_state.get("style_select", "Professional"),
#         audience=current_audience,
#         extra_details=current_extra,
#         image_settings=image_settings
#     )

#     st.session_state.generated_prompt = prompt
#     st.session_state.last_generation_payload = {
#         "use_case": st.session_state.get("use_case_select", "Content Writing"),
#         "style": st.session_state.get("style_select", "Professional"),
#         "topic": current_topic,
#         "audience": current_audience,
#         "extra_details": current_extra,
#         "image_settings": image_settings.copy()
#     }
#     add_to_history(st.session_state.get("use_case_select", "Content Writing"), current_topic, prompt)

# b1, b2, b3, b4 = st.columns(4)

# with b1:
#     if st.button("✨ Generate Prompt"):
#         generate_current_prompt()

# with b2:
#     if st.button("🔁 Regenerate"):
#         if st.session_state.last_generation_payload:
#             payload = st.session_state.last_generation_payload
#             regenerated = build_final_prompt(
#                 use_case=payload["use_case"],
#                 topic=payload["topic"],
#                 style=payload["style"],
#                 audience=payload["audience"],
#                 extra_details=payload["extra_details"],
#                 image_settings=payload["image_settings"]
#             )
#             st.session_state.generated_prompt = regenerated
#             add_to_history(payload["use_case"], payload["topic"], regenerated)
#         else:
#             st.info("Generate a prompt first.")

# with b3:
#     if st.button("⭐ Save Favorite"):
#         if st.session_state.generated_prompt:
#             current_topic = st.session_state.get("topic_value", "").strip() or "Untitled"
#             add_to_favorites(st.session_state.get("use_case_select", "Content Writing"), current_topic, st.session_state.generated_prompt)
#             st.success("Added to favorites")
#         else:
#             st.info("Generate a prompt first.")

# with b4:
#     st.button("🗑 Clear", on_click=clear_all)

# # -------------------------------
# # OUTPUT
# # -------------------------------
# st.markdown('<div class="section-title">Prompt’s Generation</div>', unsafe_allow_html=True)

# if st.session_state.generated_prompt:
#     if st.session_state.get("use_case_select") == "Image Generation":
#         st.markdown("""
#         <div style="margin-bottom:8px;">
#             <span class="prompt-chip">Direct image prompt</span>
#             <span class="prompt-chip">Ready to paste</span>
#             <span class="prompt-chip">Pro visual detail</span>
#         </div>
#         """, unsafe_allow_html=True)

#     render_copyable_prompt(st.session_state.generated_prompt)

#     st.download_button(
#         label="📥 Download Prompt",
#         data=st.session_state.generated_prompt,
#         file_name="promptnexus_prompt.txt",
#         mime="text/plain"
#     )
# else:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">No prompt generated yet</div>
#         <div class="feature-text">
#             Select a use case, enter your topic, choose style and settings, then click <b>Generate Prompt</b>.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# # -------------------------------
# # HISTORY + FAVORITES
# # -------------------------------
# left_panel, right_panel = st.columns(2)

# with left_panel:
#     st.markdown('<div class="section-title">Recent Prompt History</div>', unsafe_allow_html=True)
#     if st.session_state.history:
#         for item in st.session_state.history[:5]:
#             st.markdown(
#                 f"""
#                 <div class="history-card">
#                     <div class="history-meta">{item['timestamp']} • {item['use_case']}</div>
#                     <div class="history-title">{item['topic']}</div>
#                     <div class="history-text">{html.escape(item['prompt'][:220])}{'...' if len(item['prompt']) > 220 else ''}</div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
#     else:
#         st.markdown("""
#         <div class="feature-card">
#             <div class="feature-title">No history yet</div>
#             <div class="feature-text">Your recent prompts will appear here.</div>
#         </div>
#         """, unsafe_allow_html=True)

# with right_panel:
#     st.markdown('<div class="section-title">Favorite Prompts</div>', unsafe_allow_html=True)
#     if st.session_state.favorites:
#         for item in st.session_state.favorites[:5]:
#             st.markdown(
#                 f"""
#                 <div class="history-card">
#                     <div class="history-meta">{item['timestamp']} • {item['use_case']}</div>
#                     <div class="history-title">{item['topic']}</div>
#                     <div class="history-text">{html.escape(item['prompt'][:220])}{'...' if len(item['prompt']) > 220 else ''}</div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
#     else:
#         st.markdown("""
#         <div class="feature-card">
#             <div class="feature-title">No favorites yet</div>
#             <div class="feature-text">Save your best prompts to see them here.</div>
#         </div>
#         """, unsafe_allow_html=True)

# # -------------------------------
# # FEATURES
# # -------------------------------
# st.markdown('<div class="section-title">Why PromptNexus AI?</div>', unsafe_allow_html=True)

# f1, f2, f3 = st.columns(3)

# with f1:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">🧠 Final Prompt Output</div>
#         <div class="feature-text">
#             Generates direct, usable prompts instead of meta instructions or prompt-overview text.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with f2:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">📜 History + Favorites</div>
#         <div class="feature-text">
#             Keep track of your latest prompts and save the best ones for quick reuse.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with f3:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-title">🔐 Email OTP Login</div>
#         <div class="feature-text">
#             Public-friendly access control with passwordless email login and owner login notifications.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# # -------------------------------
# # FOOTER
# # -------------------------------
# st.markdown("""
# <br>
# <div style="text-align:center; color:#94A3B8; font-size:14px; padding-bottom:10px;">
#     Built with ❤️ By GANESH GODDILLA for smarter prompting • <b>PromptNexus AI</b>
# </div>
# """, unsafe_allow_html=True)


import streamlit as st
import streamlit.components.v1 as components
import html
import random
from datetime import datetime, timezone

import resend
from supabase import Client, create_client

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
# REQUIRED SECRETS
# -------------------------------
# Add these to .streamlit/secrets.toml
#
# SUPABASE_URL = "https://YOUR_PROJECT.supabase.co"
# SUPABASE_ANON_KEY = "YOUR_SUPABASE_ANON_KEY"
# RESEND_API_KEY = "re_xxxxxxxxx"
# OWNER_EMAIL = "yourmail@example.com"
# SENDER_EMAIL = "PromptNexus AI <onboarding@resend.dev>"
#
# For production, replace onboarding@resend.dev with your verified sender.

SUPABASE_URL = st.secrets.get("SUPABASE_URL", "")
SUPABASE_ANON_KEY = st.secrets.get("SUPABASE_ANON_KEY", "")
RESEND_API_KEY = st.secrets.get("RESEND_API_KEY", "")
OWNER_EMAIL = st.secrets.get("OWNER_EMAIL", "")
SENDER_EMAIL = st.secrets.get("SENDER_EMAIL", "PromptNexus AI <onboarding@resend.dev>")

SECRETS_READY = all([
    SUPABASE_URL,
    SUPABASE_ANON_KEY,
    RESEND_API_KEY,
    OWNER_EMAIL,
])


@st.cache_resource
def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)


if SECRETS_READY:
    supabase = get_supabase_client()
    resend.api_key = RESEND_API_KEY
else:
    supabase = None

# -------------------------------
# SESSION STATE DEFAULTS
# -------------------------------
defaults = {
    "generated_prompt": "",
    "history": [],
    "favorites": [],
    "last_generation_payload": None,
    "topic_value": "",
    "audience_value": "",
    "extra_value": "",
    "use_case_select": "Content Writing",
    "style_select": "Professional",
    "auth_email": "",
    "auth_code": "",
    "auth_requested": False,
    "user_logged_in": False,
    "user_email": "",
    "user_id": "",
    "login_notice_sent": False,
    "otp_last_sent_at": None,
    "otp_cooldown_seconds": 60,
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

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
label, .stSelectbox label, .stTextInput label, .stTextArea label, .stSlider label {
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
.prompt-chip {
    display: inline-block;
    padding: 6px 10px;
    margin: 4px 6px 4px 0;
    border-radius: 999px;
    font-size: 12px;
    color: #e2e8f0;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
}
.history-card {
    background: rgba(17,24,39,0.82);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 18px;
    padding: 14px;
    margin-bottom: 12px;
}
.history-meta {
    color: #94A3B8;
    font-size: 12px;
    margin-bottom: 8px;
}
.history-title {
    color: #F8FAFC;
    font-weight: 700;
    font-size: 14px;
    margin-bottom: 6px;
}
.history-text {
    color: #CBD5E1;
    font-size: 13px;
    line-height: 1.6;
}
.stDownloadButton > button {
    width: 100%;
    border-radius: 16px;
    border: none;
    padding: 0.75rem 1rem;
    font-weight: 700;
    font-size: 15px;
    color: white;
    background: linear-gradient(90deg, #111827, #1F2937);
    border: 1px solid rgba(255,255,255,0.10);
}
div[data-testid="stExpander"] {
    border-radius: 16px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    overflow: hidden;
}
.user-pill {
    background: rgba(0, 212, 255, 0.10);
    border: 1px solid rgba(0, 212, 255, 0.18);
    color: #c4f1ff;
    border-radius: 14px;
    padding: 10px 12px;
    margin-bottom: 14px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# DATA
# -------------------------------
USE_CASE_CONFIG = {
    "Content Writing": {
        "topic_placeholder": "e.g. Write a blog post on AI tools for productivity",
        "audience_placeholder": "e.g. content creators, bloggers, marketers",
        "extra_placeholder": "Add tone, length, SEO keywords, platform, CTA, and output format.",
        "examples": [
            "Instagram caption for a fitness brand launch",
            "SEO blog post on beginner MLOps roadmap",
            "LinkedIn post about GenAI career transition"
        ],
        "random_topics": [
            "LinkedIn post about AI productivity tools",
            "Blog article on beginner MLOps roadmap",
            "Instagram caption for a new tech gadget launch"
        ]
    },
    "Coding": {
        "topic_placeholder": "e.g. Build a Python script for file organizer automation",
        "audience_placeholder": "e.g. Python developers, beginners, backend engineers",
        "extra_placeholder": "Mention language, framework, edge cases, output style, and constraints.",
        "examples": [
            "Streamlit app for AI prompt generator",
            "FastAPI REST API with authentication",
            "Python function to parse logs and summarize errors"
        ],
        "random_topics": [
            "Python script to organize files by extension",
            "FastAPI endpoint with JWT authentication",
            "Streamlit dashboard for sales analytics"
        ]
    },
    "Business": {
        "topic_placeholder": "e.g. Create a startup idea for AI resume review tool",
        "audience_placeholder": "e.g. startup founders, consultants, entrepreneurs",
        "extra_placeholder": "Mention industry, users, pricing, business goal, and market angle.",
        "examples": [
            "Business plan for a faceless YouTube automation agency",
            "Pricing strategy for AI SaaS tool",
            "Go-to-market plan for student productivity app"
        ],
        "random_topics": [
            "Pricing strategy for AI SaaS product",
            "Business model for freelancer marketplace",
            "Go-to-market plan for student productivity app"
        ]
    },
    "Students": {
        "topic_placeholder": "e.g. Explain neural networks in simple terms",
        "audience_placeholder": "e.g. school students, college students, exam aspirants",
        "extra_placeholder": "Mention subject, difficulty, answer style, format, and examples needed.",
        "examples": [
            "Study notes for DBMS interview preparation",
            "Simple explanation of cloud computing",
            "5-mark answer for machine learning basics"
        ],
        "random_topics": [
            "Simple explanation of cloud computing",
            "DBMS notes for interview preparation",
            "Machine learning basics for beginners"
        ]
    },
    "General Use": {
        "topic_placeholder": "e.g. Write a professional email requesting project access",
        "audience_placeholder": "e.g. professionals, freelancers, general users",
        "extra_placeholder": "Mention context, tone, recipient, and desired structure.",
        "examples": [
            "Professional apology email to manager",
            "Daily planner for a productive workday",
            "Checklist for moving to a new city"
        ],
        "random_topics": [
            "Professional apology email to manager",
            "Daily productivity planner",
            "Checklist for moving to a new city"
        ]
    },
    "Marketing": {
        "topic_placeholder": "e.g. Create ad copy for eco-friendly water bottle",
        "audience_placeholder": "e.g. customers, marketers, D2C brands",
        "extra_placeholder": "Mention product, platform, brand tone, CTA, and campaign goal.",
        "examples": [
            "Facebook ad copy for skincare product",
            "Email campaign for Black Friday sale",
            "Brand tagline ideas for AI startup"
        ],
        "random_topics": [
            "Facebook ad copy for skincare brand",
            "Email campaign for festive sale",
            "Tagline ideas for AI startup"
        ]
    },
    "Resume / Career": {
        "topic_placeholder": "e.g. Rewrite my resume summary for MLOps engineer role",
        "audience_placeholder": "e.g. recruiters, hiring managers, job seekers",
        "extra_placeholder": "Mention target role, experience level, key skills, and tone.",
        "examples": [
            "Resume bullet points for Python developer",
            "Cover letter for GenAI engineer role",
            "LinkedIn About section for fresher in MLOps"
        ],
        "random_topics": [
            "LinkedIn About section for fresher in MLOps",
            "Resume summary for Python developer",
            "Cover letter for GenAI engineer role"
        ]
    },
    "Startup Ideas": {
        "topic_placeholder": "e.g. Generate startup ideas using GenAI in education",
        "audience_placeholder": "e.g. founders, investors, builders",
        "extra_placeholder": "Mention niche, user pain point, monetization, and business type.",
        "examples": [
            "Low-cost AI SaaS ideas for India",
            "B2B startup idea for internal documentation",
            "One-person startup ideas in automation"
        ],
        "random_topics": [
            "AI startup ideas for education",
            "One-person startup ideas in automation",
            "B2B AI tool for internal documentation"
        ]
    },
    "Social Media": {
        "topic_placeholder": "e.g. Create 10 reel ideas for AI productivity content",
        "audience_placeholder": "e.g. Instagram audience, creators, YouTube viewers",
        "extra_placeholder": "Mention platform, tone, hook style, audience, and niche.",
        "examples": [
            "YouTube Shorts script on AI tools",
            "Twitter thread on beginner coding mistakes",
            "Instagram carousel post on career growth"
        ],
        "random_topics": [
            "10 Instagram reel ideas for AI productivity",
            "Twitter thread on common coding mistakes",
            "Carousel post on career growth tips"
        ]
    },
    "Email Writing": {
        "topic_placeholder": "e.g. Draft an email asking for project status update",
        "audience_placeholder": "e.g. manager, HR, client, colleague",
        "extra_placeholder": "Mention sender goal, urgency, context, and tone.",
        "examples": [
            "Leave request email",
            "Follow-up email after interview",
            "Formal escalation email for blocked task"
        ],
        "random_topics": [
            "Leave request email",
            "Interview follow-up email",
            "Formal escalation email for blocked task"
        ]
    },
    "Image Generation": {
        "topic_placeholder": "e.g. Marvel-style superhero poster in pastel space",
        "audience_placeholder": "e.g. creators, designers, Midjourney users",
        "extra_placeholder": "Mention must-have details, pose, objects, setting, color direction, or restrictions.",
        "examples": [
            "Anime warrior in neon city at night",
            "Luxury product ad shot with soft lighting",
            "Marvel-style superhero poster in pastel space"
        ],
        "random_topics": [
            "Marvel-style superhero poster in pastel space",
            "Anime warrior in neon city at night",
            "Cyberpunk female assassin in rainy alley"
        ]
    },
    "YouTube Scripts": {
        "topic_placeholder": "e.g. Write a 60-second YouTube script on top AI tools",
        "audience_placeholder": "e.g. YouTube viewers, beginners, tech audience",
        "extra_placeholder": "Mention duration, tone, niche, hook style, CTA, and pacing.",
        "examples": [
            "60-second script for motivation reel",
            "Faceless finance video script",
            "Tech explainer script on ChatGPT vs OpenAI"
        ],
        "random_topics": [
            "60-second YouTube script on top AI tools",
            "Faceless finance video script",
            "Tech explainer on ChatGPT vs OpenAI"
        ]
    }
}

STYLE_GUIDE = {
    "Professional": "Use a polished, structured, confident, and professional tone.",
    "Creative": "Use engaging, imaginative, vivid, and fresh language.",
    "Minimal": "Keep the wording concise, sharp, and direct with no fluff.",
    "Cinematic": "Use immersive, visually rich, dramatic, and emotionally engaging language.",
    "Anime": "Use expressive, stylized, vibrant, and visually dynamic language.",
    "Realistic": "Use grounded, practical, precise, and believable details.",
    "Expert": "Use advanced, strategic, highly refined, and authoritative language."
}

SHOT_OPTIONS = [
    "low-angle hero shot", "close-up portrait", "wide cinematic shot", "mid-shot composition",
    "full-body character shot", "over-the-shoulder shot", "bird's-eye view", "dynamic action frame"
]
LIGHTING_OPTIONS = [
    "dramatic rim lighting", "soft diffused lighting", "golden hour glow", "neon glow",
    "volumetric god rays", "studio lighting", "moonlit ambience", "high contrast cinematic lighting"
]
MOOD_OPTIONS = ["epic", "dreamy", "mysterious", "dark fantasy", "heroic", "ethereal", "intense", "calm"]
PALETTE_OPTIONS = [
    "pastel lavender, baby blue, mint green, peach",
    "deep blue, violet, silver",
    "neon cyan, magenta, purple",
    "gold, crimson, black",
    "warm beige, ivory, bronze",
    "emerald, teal, obsidian"
]
CAMERA_OPTIONS = [
    "cinematic lens feel", "85mm portrait feel", "ultra-wide lens perspective",
    "movie poster framing", "editorial fashion framing", "DSLR realism", "anamorphic cinematic framing"
]
TEXTURE_OPTIONS = [
    "ultra-detailed metallic textures", "soft fabric detail", "crystalline surfaces",
    "photoreal skin detail", "glossy reflective surfaces", "matte cinematic textures"
]
RENDER_OPTIONS = [
    "professional 8k render", "ultra-detailed digital art", "high-end concept art",
    "AAA game art quality", "cinematic movie poster quality", "photorealistic studio render"
]
NEGATIVE_DEFAULT = "blurry, low quality, distorted anatomy, extra fingers, cropped, duplicate, watermark, text, logo, oversaturated, noisy background"

# -------------------------------
# HELPERS
# -------------------------------
def clean_text(value: str) -> str:
    return value.strip() if value else ""


def compact_join(parts):
    return ", ".join([p for p in parts if clean_text(p)])


def add_to_history(use_case: str, topic: str, prompt: str) -> None:
    entry = {
        "use_case": use_case,
        "topic": topic,
        "prompt": prompt,
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
    st.session_state.history.insert(0, entry)
    st.session_state.history = st.session_state.history[:10]


def add_to_favorites(use_case: str, topic: str, prompt: str) -> None:
    already_exists = any(fav["prompt"] == prompt for fav in st.session_state.favorites)
    if not already_exists:
        st.session_state.favorites.insert(0, {
            "use_case": use_case,
            "topic": topic,
            "prompt": prompt,
            "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })
        st.session_state.favorites = st.session_state.favorites[:20]


def set_random_topic():
    current_use_case = st.session_state.get("use_case_select", "Content Writing")
    current_config = USE_CASE_CONFIG[current_use_case]
    st.session_state["topic_value"] = random.choice(current_config["random_topics"])


def clear_all():
    st.session_state.generated_prompt = ""
    st.session_state.topic_value = ""
    st.session_state.audience_value = ""
    st.session_state.extra_value = ""


def get_otp_cooldown_remaining() -> int:
    last_sent = st.session_state.get("otp_last_sent_at")
    cooldown = st.session_state.get("otp_cooldown_seconds", 60)

    if last_sent is None:
        return 0

    elapsed = (datetime.now(timezone.utc) - last_sent).total_seconds()
    remaining = int(cooldown - elapsed)
    return max(0, remaining)


def logout_user():
    st.session_state.user_logged_in = False
    st.session_state.user_email = ""
    st.session_state.user_id = ""
    st.session_state.auth_requested = False
    if "auth_code" in st.session_state:
        del st.session_state["auth_code"]
    st.session_state.login_notice_sent = False
    st.rerun()


def send_owner_login_notification(user_email: str, user_id: str):
    if not RESEND_API_KEY or not OWNER_EMAIL:
        return

    try:
        resend.Emails.send({
            "from": SENDER_EMAIL,
            "to": [OWNER_EMAIL],
            "subject": "New PromptNexus AI login",
            "html": f"""
                <div style=\"font-family:Arial,sans-serif;line-height:1.6\">
                    <h2>New user login</h2>
                    <p><strong>Email:</strong> {html.escape(user_email)}</p>
                    <p><strong>User ID:</strong> {html.escape(user_id)}</p>
                    <p><strong>Time (UTC):</strong> {datetime.now(timezone.utc).strftime('%d-%m-%Y %H:%M:%S')}</p>
                </div>
            """
        })
    except Exception as e:
        st.warning(f"Owner email notification failed: {e}")


def store_login_event(user_email: str, user_id: str):
    if not supabase:
        return

    try:
        supabase.table("login_events").insert({
            "email": user_email,
            "user_id": user_id,
            "logged_at": datetime.now(timezone.utc).isoformat()
        }).execute()
    except Exception:
        pass


def request_email_otp(email_value: str):
    if not supabase:
        st.error("Missing app secrets. Please configure Supabase and Resend first.")
        return

    remaining = get_otp_cooldown_remaining()
    if remaining > 0:
        st.warning(f"Please wait {remaining} seconds before requesting a new login code.")
        return

    try:
        supabase.auth.sign_in_with_otp({
            "email": email_value,
            "options": {
                "should_create_user": True
            }
        })
        st.session_state.auth_requested = True
        st.session_state.otp_last_sent_at = datetime.now(timezone.utc)
        st.success("Login code sent to your email.")
        st.info("In Supabase, set the email template to show the OTP token if you want users to enter a 6-digit code.")
    except Exception as e:
        error_text = str(e).lower()
        if "rate limit" in error_text or "email rate limit exceeded" in error_text:
            st.error("Too many login code requests. Please wait a minute and try again.")
        else:
            st.error(f"Could not send login code: {e}")


def verify_email_otp(email_value: str, otp_code: str):
    if not supabase:
        st.error("Missing app secrets. Please configure Supabase and Resend first.")
        return

    try:
        result = supabase.auth.verify_otp({
            "email": email_value,
            "token": otp_code,
            "type": "email"
        })

        user = None
        if hasattr(result, "user") and result.user is not None:
            user = result.user
        elif hasattr(result, "session") and result.session is not None and hasattr(result.session, "user"):
            user = result.session.user
        elif isinstance(result, dict):
            user = result.get("user")
            if user is None and result.get("session"):
                session = result.get("session")
                if isinstance(session, dict):
                    user = session.get("user")

        if not user:
            st.error("OTP verified, but no user details were returned.")
            return

        user_email = getattr(user, "email", None) if not isinstance(user, dict) else user.get("email")
        user_id = getattr(user, "id", None) if not isinstance(user, dict) else user.get("id")

        st.session_state.user_logged_in = True
        st.session_state.user_email = user_email or email_value
        st.session_state.user_id = user_id or "unknown"
        st.session_state.auth_requested = False
        st.session_state.login_notice_sent = False

        if not st.session_state.login_notice_sent:
            store_login_event(st.session_state.user_email, st.session_state.user_id)
            send_owner_login_notification(st.session_state.user_email, st.session_state.user_id)
            st.session_state.login_notice_sent = True

        st.success("Login successful.")
        st.rerun()
    except Exception as e:
        st.error(f"Invalid or expired code: {e}")


def build_image_prompt(
    topic: str,
    style: str,
    extra_details: str,
    shot_type: str,
    lighting: str,
    mood: str,
    palette: str,
    camera: str,
    texture: str,
    render_quality: str,
    aspect_ratio: str,
    stylize: int,
    chaos: int,
    quality: str,
    include_negative: bool,
    negative_prompt: str
) -> str:
    topic = clean_text(topic)
    extra_details = clean_text(extra_details)

    style_prefix_map = {
        "Cinematic": "A powerful, visually striking cinematic scene of",
        "Anime": "A highly stylized anime illustration of",
        "Realistic": "A highly realistic, visually polished depiction of",
        "Creative": "An imaginative, visually rich composition of",
        "Minimal": "A clean, elegant visual composition of",
        "Professional": "A premium, polished visual concept of",
        "Expert": "An ultra-refined, masterfully art-directed visual of"
    }
    style_suffix_map = {
        "Cinematic": "high-octane cinematic movie poster composition",
        "Anime": "dynamic anime key visual composition",
        "Realistic": "photorealistic premium composition",
        "Creative": "artistic high-impact composition",
        "Minimal": "clean premium composition",
        "Professional": "refined commercial-grade composition",
        "Expert": "world-class concept art composition"
    }

    base_prefix = style_prefix_map.get(style, "A highly detailed visual of")
    composition_style = style_suffix_map.get(style, "premium composition")

    if style == "Anime":
        tag_block = f"--stylize {stylize} --chaos {chaos} --quality {quality} --ar {aspect_ratio} --niji 6"
    else:
        tag_block = f"--stylize {stylize} --chaos {chaos} --quality {quality} --ar {aspect_ratio}"

    body_parts = [
        f"{base_prefix} {topic}",
        shot_type,
        f"{mood} atmosphere",
        lighting,
        camera,
        f"color palette of {palette}",
        texture,
        composition_style,
        render_quality,
        "sharp focus",
        "intricate details",
        "depth and dimensionality"
    ]

    if extra_details:
        body_parts.append(extra_details)

    prompt = compact_join(body_parts)

    if include_negative:
        neg = clean_text(negative_prompt) or NEGATIVE_DEFAULT
        prompt = f"{prompt} --no {neg}"

    return f"{prompt} {tag_block}".strip()


def build_final_prompt(use_case, topic, style, audience, extra_details, image_settings):
    topic = clean_text(topic)
    audience = clean_text(audience) or "the intended audience"
    extra_details = clean_text(extra_details)
    style_instruction = STYLE_GUIDE.get(style, "Use clear and high-quality language.")

    if use_case == "Image Generation":
        return build_image_prompt(
            topic=topic,
            style=style,
            extra_details=extra_details,
            shot_type=image_settings["shot_type"],
            lighting=image_settings["lighting"],
            mood=image_settings["mood"],
            palette=image_settings["palette"],
            camera=image_settings["camera"],
            texture=image_settings["texture"],
            render_quality=image_settings["render_quality"],
            aspect_ratio=image_settings["aspect_ratio"],
            stylize=image_settings["stylize"],
            chaos=image_settings["chaos"],
            quality=image_settings["quality"],
            include_negative=image_settings["include_negative"],
            negative_prompt=image_settings["negative_prompt"]
        )

    extra_line = f" Also ensure the output follows these requirements: {extra_details}" if extra_details else ""

    if use_case == "Resume / Career":
        return (
            f"Act as an experienced career coach and professional personal branding expert. "
            f"Write a strong, polished, and recruiter-friendly response about {topic} for {audience}. "
            f"{style_instruction} Make the output clear, impactful, and tailored for real hiring scenarios. "
            f"Highlight strengths, value, credibility, and professional positioning. "
            f"Keep the language natural, confident, and modern while avoiding vague or generic statements."
            f"{extra_line}"
        ).strip()

    if use_case == "Content Writing":
        return (
            f"Act as an expert content writer and strategist. Create high-quality content about {topic} for {audience}. "
            f"{style_instruction} Make the response engaging, well-structured, easy to read, and valuable to the target audience. "
            f"Include a strong opening, smooth flow, relevant details, and a compelling ending. "
            f"Ensure the writing feels polished, natural, and ready to publish."
            f"{extra_line}"
        ).strip()

    if use_case == "Coding":
        return (
            f"Act as a senior software engineer and coding assistant. Help with {topic} for {audience}. "
            f"{style_instruction} Provide clean, correct, production-ready output with clear logic, readable structure, and best practices. "
            f"Include explanations where useful, handle edge cases when relevant, and keep the solution practical and maintainable."
            f"{extra_line}"
        ).strip()

    if use_case == "Business":
        return (
            f"Act as a strategic business consultant. Create a clear, practical, and insight-driven response about {topic} for {audience}. "
            f"{style_instruction} Focus on business value, execution, realistic strategy, and actionable recommendations. "
            f"Make the output structured, professional, and useful for decision-making."
            f"{extra_line}"
        ).strip()

    if use_case == "Students":
        return (
            f"Act as an expert tutor and educational mentor. Explain or create content about {topic} for {audience}. "
            f"{style_instruction} Make the response easy to understand, well-structured, accurate, and educational. "
            f"Use simple explanations, step-by-step clarity, and examples wherever helpful."
            f"{extra_line}"
        ).strip()

    if use_case == "Marketing":
        return (
            f"Act as an expert marketing strategist and copywriter. Create marketing content for {topic} aimed at {audience}. "
            f"{style_instruction} Focus on audience attention, clarity, persuasion, brand relevance, and conversion potential. "
            f"Make the output compelling, strategic, and ready for practical campaign use."
            f"{extra_line}"
        ).strip()

    if use_case == "Startup Ideas":
        return (
            f"Act as an innovative startup advisor and product strategist. Generate strong ideas and strategic thinking around {topic} for {audience}. "
            f"{style_instruction} Focus on real user pain points, market opportunity, differentiation, monetization, and execution potential. "
            f"Keep the output practical, high-value, and startup-ready."
            f"{extra_line}"
        ).strip()

    if use_case == "Social Media":
        return (
            f"Act as a social media strategist and content creator. Create content around {topic} for {audience}. "
            f"{style_instruction} Make the output attention-grabbing, platform-friendly, engaging, and easy to consume. "
            f"Use strong hooks, clear flow, and content that encourages interaction or retention."
            f"{extra_line}"
        ).strip()

    if use_case == "Email Writing":
        return (
            f"Act as a professional communication expert. Write an effective email about {topic} for {audience}. "
            f"{style_instruction} Make the email clear, polished, purposeful, and appropriate for the situation. "
            f"Ensure the message has natural wording and a professional tone."
            f"{extra_line}"
        ).strip()

    if use_case == "YouTube Scripts":
        return (
            f"Act as an expert YouTube scriptwriter. Write a high-retention script about {topic} for {audience}. "
            f"{style_instruction} Start with a strong hook, maintain clear pacing, keep the content engaging, and end with a strong closing or CTA. "
            f"Make the script natural, audience-focused, and optimized for watch time and clarity."
            f"{extra_line}"
        ).strip()

    return (
        f"Act as an expert assistant. Create a high-quality response about {topic} for {audience}. "
        f"{style_instruction} Make the output clear, useful, polished, and practical. "
        f"Ensure the final result is easy to understand and directly usable."
        f"{extra_line}"
    ).strip()


def render_copyable_prompt(prompt_text: str):
    escaped_prompt = html.escape(prompt_text).replace("\n", "<br>")
    js_safe_prompt = (
        prompt_text
        .replace("\\", "\\\\")
        .replace("`", "\\`")
        .replace("${", "\\${")
    )

    components.html(
        f"""
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
            .prompt-body {{
                font-size: 16px;
                line-height: 1.9;
                color: #F8FAFC;
                word-wrap: break-word;
                overflow-wrap: break-word;
                white-space: normal;
                margin-bottom: 22px;
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
        </style>
        </head>
        <body>
            <div class="prompt-card">
                <div class="prompt-title">🎯 Prompt</div>
                <div class="prompt-body">{escaped_prompt}</div>
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
        """,
        height=360,
        scrolling=False
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

    if st.session_state.user_logged_in:
        st.markdown(
            f"""
            <div class="user-pill">
                <b>Logged in as</b><br>{html.escape(st.session_state.user_email)}
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("🚪 Logout"):
            logout_user()

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

    st.markdown("### ✨ Features")
    st.markdown("""
    - Email OTP login  
    - Prompt history  
    - Favorites  
    - Random prompt  
    - Regenerate  
    - Download prompt  
    - One-click copy  
    - Pro image controls  
    """)

    st.markdown("### 📩 Support")
    st.markdown("""
    Contact if you face any issue:  
    **ganeshgoddilla110@gmail.com**
    """)

# -------------------------------
# LOGIN GATE
# -------------------------------
if not SECRETS_READY:
    st.markdown("""
    <div class="hero-card">
        <div class="badge">⚠️ Setup Required</div>
        <div class="hero-title">Configure auth first</div>
        <div class="hero-desc">
            Add SUPABASE_URL, SUPABASE_ANON_KEY, RESEND_API_KEY, OWNER_EMAIL, and SENDER_EMAIL to your Streamlit secrets.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

if not st.session_state.user_logged_in:
    st.markdown("""
    <div class="hero-card">
        <div class="badge">🔐 Email Login</div>
        <div class="hero-title">Login to PromptNexus AI</div>
        <div class="hero-desc">
            Enter your email, receive a login code, and access the app without a password.
        </div>
    </div>
    """, unsafe_allow_html=True)

    remaining = get_otp_cooldown_remaining()

    with st.form("login_form"):
        login_col1, login_col2 = st.columns(2)
        with login_col1:
            st.text_input(
                "Email address",
                placeholder="you@example.com",
                key="auth_email"
            )
        with login_col2:
            st.text_input(
                "6-digit code",
                placeholder="Enter code from email",
                key="auth_code"
            )

        a1, a2 = st.columns(2)
        send_label = f"📩 Send Login Code ({remaining}s)" if remaining > 0 else "📩 Send Login Code"
        send_clicked = a1.form_submit_button(send_label, disabled=remaining > 0)
        verify_clicked = a2.form_submit_button("✅ Verify & Login")

    if send_clicked:
        email_value = clean_text(st.session_state.auth_email).lower()
        if not email_value:
            st.warning("Please enter your email first.")
        else:
            request_email_otp(email_value)

    if verify_clicked:
        email_value = clean_text(st.session_state.auth_email).lower()
        otp_code = clean_text(st.session_state.auth_code)
        if not email_value:
            st.warning("Please enter your email.")
        elif not otp_code:
            st.warning("Please enter the 6-digit code.")
        else:
            verify_email_otp(email_value, otp_code)

    remaining = get_otp_cooldown_remaining()
    if remaining > 0:
        st.caption(f"You can request a new login code in {remaining} seconds.")

    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">How it works</div>
        <div class="feature-text">
            1) Enter your email<br>
            2) Click Send Login Code<br>
            3) Check your inbox<br>
            4) Enter the code<br>
            5) Use PromptNexus AI
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.stop()

# -------------------------------
# HERO
# -------------------------------
st.markdown("""
<div class="hero-card">
    <div class="badge">🚀 AI Prompt Workspace</div>
    <div class="hero-title">PromptNexus AI</div>
    <div class="hero-desc">
        Generate final, crystal-clear prompts for content, coding, career, marketing, and ultra-detailed image generation.
        Includes history, favorites, random ideas, regenerate, download, and one-click copy.
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# MAIN INPUTS
# -------------------------------
use_case_options = list(USE_CASE_CONFIG.keys())

col1, col2 = st.columns(2)
with col1:
    use_case = st.selectbox("Select Use Case", use_case_options, key="use_case_select")

config = USE_CASE_CONFIG[use_case]

with col2:
    style = st.selectbox(
        "Prompt Style",
        ["Professional", "Creative", "Minimal", "Cinematic", "Anime", "Realistic", "Expert"],
        key="style_select"
    )

col3, col4 = st.columns(2)

with col3:
    topic = st.text_input(
        "Topic / Goal",
        placeholder=config["topic_placeholder"],
        key="topic_value"
    )
    st.markdown(
        f"""
        <div class="example-box">
            <b>Examples for {use_case}:</b><br>
            • {config['examples'][0]}<br>
            • {config['examples'][1]}<br>
            • {config['examples'][2]}
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    audience = st.text_input(
        "Target Audience",
        placeholder=config["audience_placeholder"],
        key="audience_value"
    )
    st.markdown(
        '<div class="small-note">Audience suggestions change based on selected use case.</div>',
        unsafe_allow_html=True
    )

extra_details = st.text_area(
    "Extra Details / Requirements",
    placeholder=config["extra_placeholder"],
    height=130,
    key="extra_value"
)

# -------------------------------
# RANDOM PROMPT BUTTON
# -------------------------------
st.button("🎲 Random Prompt Idea", on_click=set_random_topic)

# -------------------------------
# IMAGE ADVANCED CONTROLS
# -------------------------------
default_image_settings = {
    "shot_type": "low-angle hero shot",
    "lighting": "dramatic rim lighting",
    "mood": "epic",
    "palette": "pastel lavender, baby blue, mint green, peach",
    "camera": "movie poster framing",
    "texture": "ultra-detailed metallic textures",
    "render_quality": "professional 8k render",
    "aspect_ratio": "2:3",
    "stylize": 750,
    "chaos": 12,
    "quality": "1",
    "include_negative": True,
    "negative_prompt": NEGATIVE_DEFAULT
}
image_settings = default_image_settings.copy()

if use_case == "Image Generation":
    st.markdown('<div class="section-title">Advanced Image Controls</div>', unsafe_allow_html=True)

    with st.expander("Open pro image controls", expanded=True):
        g1, g2, g3 = st.columns(3)
        with g1:
            image_settings["shot_type"] = st.selectbox("Shot / Framing", SHOT_OPTIONS, index=0)
            image_settings["lighting"] = st.selectbox("Lighting", LIGHTING_OPTIONS, index=0)
            image_settings["mood"] = st.selectbox("Mood", MOOD_OPTIONS, index=0)
        with g2:
            image_settings["palette"] = st.selectbox("Color Palette", PALETTE_OPTIONS, index=0)
            image_settings["camera"] = st.selectbox("Camera Feel", CAMERA_OPTIONS, index=3)
            image_settings["texture"] = st.selectbox("Texture Detail", TEXTURE_OPTIONS, index=0)
        with g3:
            image_settings["render_quality"] = st.selectbox("Render Style", RENDER_OPTIONS, index=0)
            image_settings["aspect_ratio"] = st.selectbox("Aspect Ratio", ["1:1", "2:3", "3:2", "4:5", "9:16", "16:9", "21:9"], index=1)
            image_settings["quality"] = st.selectbox("Quality", ["0.5", "1", "2"], index=1)

        s1, s2 = st.columns(2)
        with s1:
            image_settings["stylize"] = st.slider("Stylize", 0, 1000, 750, 25)
        with s2:
            image_settings["chaos"] = st.slider("Chaos", 0, 100, 12, 1)

        image_settings["include_negative"] = st.checkbox("Include negative prompt", value=True)
        if image_settings["include_negative"]:
            image_settings["negative_prompt"] = st.text_area(
                "Negative Prompt",
                value=NEGATIVE_DEFAULT,
                height=90
            )

# -------------------------------
# GENERATE
# -------------------------------
def generate_current_prompt():
    current_topic = st.session_state.get("topic_value", "").strip()
    current_audience = st.session_state.get("audience_value", "").strip()
    current_extra = st.session_state.get("extra_value", "").strip()

    if not current_topic:
        st.warning("Please enter a Topic / Goal first.")
        return

    prompt = build_final_prompt(
        use_case=st.session_state.get("use_case_select", "Content Writing"),
        topic=current_topic,
        style=st.session_state.get("style_select", "Professional"),
        audience=current_audience,
        extra_details=current_extra,
        image_settings=image_settings
    )

    st.session_state.generated_prompt = prompt
    st.session_state.last_generation_payload = {
        "use_case": st.session_state.get("use_case_select", "Content Writing"),
        "style": st.session_state.get("style_select", "Professional"),
        "topic": current_topic,
        "audience": current_audience,
        "extra_details": current_extra,
        "image_settings": image_settings.copy()
    }
    add_to_history(st.session_state.get("use_case_select", "Content Writing"), current_topic, prompt)

b1, b2, b3, b4 = st.columns(4)

with b1:
    if st.button("✨ Generate Prompt"):
        generate_current_prompt()

with b2:
    if st.button("🔁 Regenerate"):
        if st.session_state.last_generation_payload:
            payload = st.session_state.last_generation_payload
            regenerated = build_final_prompt(
                use_case=payload["use_case"],
                topic=payload["topic"],
                style=payload["style"],
                audience=payload["audience"],
                extra_details=payload["extra_details"],
                image_settings=payload["image_settings"]
            )
            st.session_state.generated_prompt = regenerated
            add_to_history(payload["use_case"], payload["topic"], regenerated)
        else:
            st.info("Generate a prompt first.")

with b3:
    if st.button("⭐ Save Favorite"):
        if st.session_state.generated_prompt:
            current_topic = st.session_state.get("topic_value", "").strip() or "Untitled"
            add_to_favorites(st.session_state.get("use_case_select", "Content Writing"), current_topic, st.session_state.generated_prompt)
            st.success("Added to favorites")
        else:
            st.info("Generate a prompt first.")

with b4:
    st.button("🗑 Clear", on_click=clear_all)

# -------------------------------
# OUTPUT
# -------------------------------
st.markdown('<div class="section-title">Prompt’s Generation</div>', unsafe_allow_html=True)

if st.session_state.generated_prompt:
    if st.session_state.get("use_case_select") == "Image Generation":
        st.markdown("""
        <div style="margin-bottom:8px;">
            <span class="prompt-chip">Direct image prompt</span>
            <span class="prompt-chip">Ready to paste</span>
            <span class="prompt-chip">Pro visual detail</span>
        </div>
        """, unsafe_allow_html=True)

    render_copyable_prompt(st.session_state.generated_prompt)

    st.download_button(
        label="📥 Download Prompt",
        data=st.session_state.generated_prompt,
        file_name="promptnexus_prompt.txt",
        mime="text/plain"
    )
else:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">No prompt generated yet</div>
        <div class="feature-text">
            Select a use case, enter your topic, choose style and settings, then click <b>Generate Prompt</b>.
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# HISTORY + FAVORITES
# -------------------------------
left_panel, right_panel = st.columns(2)

with left_panel:
    st.markdown('<div class="section-title">Recent Prompt History</div>', unsafe_allow_html=True)
    if st.session_state.history:
        for item in st.session_state.history[:5]:
            st.markdown(
                f"""
                <div class="history-card">
                    <div class="history-meta">{item['timestamp']} • {item['use_case']}</div>
                    <div class="history-title">{item['topic']}</div>
                    <div class="history-text">{html.escape(item['prompt'][:220])}{'...' if len(item['prompt']) > 220 else ''}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">No history yet</div>
            <div class="feature-text">Your recent prompts will appear here.</div>
        </div>
        """, unsafe_allow_html=True)

with right_panel:
    st.markdown('<div class="section-title">Favorite Prompts</div>', unsafe_allow_html=True)
    if st.session_state.favorites:
        for item in st.session_state.favorites[:5]:
            st.markdown(
                f"""
                <div class="history-card">
                    <div class="history-meta">{item['timestamp']} • {item['use_case']}</div>
                    <div class="history-title">{item['topic']}</div>
                    <div class="history-text">{html.escape(item['prompt'][:220])}{'...' if len(item['prompt']) > 220 else ''}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">No favorites yet</div>
            <div class="feature-text">Save your best prompts to see them here.</div>
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
        <div class="feature-title">🧠 Final Prompt Output</div>
        <div class="feature-text">
            Generates direct, usable prompts instead of meta instructions or prompt-overview text.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📜 History + Favorites</div>
        <div class="feature-text">
            Keep track of your latest prompts and save the best ones for quick reuse.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🔐 Email OTP Login</div>
        <div class="feature-text">
            Public-friendly access control with passwordless email login and owner login notifications.
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
