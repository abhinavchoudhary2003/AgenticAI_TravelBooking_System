# import os
# import streamlit as st
# from datetime import datetime
# from langchain_core.messages import HumanMessage
# from main import app

# st.set_page_config(
#     page_title="AI Travel Booking System",
#     page_icon="✈️",
#     layout="wide"
# )

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

# html, body, .stApp {
#     font-family: 'Inter', sans-serif;
#     background-color: #080d14;
# }

# /* ── Hero ── */
# .hero-wrapper {
#     position: relative;
#     border-radius: 20px;
#     overflow: hidden;
#     margin-bottom: 2rem;
#     height: 280px;
# }
# .hero-bg {
#     width: 100%;
#     height: 100%;
#     object-fit: cover;
#     display: block;
#     filter: brightness(0.35);
#     position: absolute;
#     top: 0; left: 0;
# }
# .hero-content {
#     position: relative;
#     z-index: 2;
#     height: 100%;
#     display: flex;
#     flex-direction: column;
#     align-items: center;
#     justify-content: center;
#     text-align: center;
#     padding: 2rem;
# }
# .hero-badge {
#     background: rgba(58,123,213,0.25);
#     border: 1px solid rgba(58,123,213,0.5);
#     color: #7ab8f5 !important;
#     font-size: 0.75rem;
#     font-weight: 600;
#     letter-spacing: 0.12em;
#     text-transform: uppercase;
#     padding: 0.3rem 0.9rem;
#     border-radius: 20px;
#     margin-bottom: 0.9rem;
#     display: inline-block;
# }
# .hero-title {
#     font-size: 2.6rem;
#     font-weight: 700;
#     color: #ffffff;
#     margin: 0 0 0.6rem;
#     line-height: 1.2;
# }
# .hero-sub {
#     color: #94adc8;
#     font-size: 1rem;
#     max-width: 560px;
# }

# /* ── Input card ── */
# .input-card {
#     background: #0e1623;
#     border: 1px solid #1e2e44;
#     border-radius: 16px;
#     padding: 1.6rem 1.8rem;
#     margin-bottom: 1.5rem;
# }
# .input-label {
#     color: #7ab8f5;
#     font-size: 0.8rem;
#     font-weight: 600;
#     letter-spacing: 0.1em;
#     text-transform: uppercase;
#     margin-bottom: 0.5rem;
# }

# /* ── Quick destinations ── */
# .dest-row {
#     display: flex;
#     gap: 0.5rem;
#     flex-wrap: wrap;
#     margin: 0.8rem 0 1.2rem;
# }
# .dest-chip {
#     background: #111b2b;
#     border: 1px solid #1e3050;
#     color: #f7fdf4;
#     padding: 0.35rem 0.85rem;
#     border-radius: 20px;
#     font-size: 0.82rem;
#     cursor: pointer;
#     transition: all 0.2s;
# }
# .dest-chip:hover { background: #1a2e47; border-color: #3a7bd5; color: #fff; }

# /* ── Generate button ── */
# div[data-testid="stButton"] > button {
#     background: linear-gradient(135deg, #1a6bbf 0%, #0d4a8a 50%, #0a3d75 100%) !important;
#     color: #ffffff !important;
#     border: none !important;
#     border-radius: 12px !important;
#     padding: 0.85rem 2.5rem !important;
#     font-size: 1.05rem !important;
#     font-weight: 700 !important;
#     letter-spacing: 0.03em !important;
#     width: 100% !important;
#     box-shadow: 0 0 24px rgba(26,107,191,0.35), 0 4px 15px rgba(0,0,0,0.4) !important;
#     transition: all 0.3s ease !important;
# }
# div[data-testid="stButton"] > button:hover {
#     box-shadow: 0 0 40px rgba(26,107,191,0.6), 0 6px 20px rgba(0,0,0,0.5) !important;
#     transform: translateY(-2px) !important;
#     background: linear-gradient(135deg, #2278d4 0%, #1057a0 50%, #0d4a8a 100%) !important;
# }
# div[data-testid="stButton"] > button:active {
#     transform: translateY(0px) !important;
# }

# /* ── Agent status cards ── */
# [data-testid="stStatusWidget"] {
#     background: #0e1a2e !important;
#     border: 1px solid #1e3050 !important;
#     border-radius: 12px !important;
# }
# [data-testid="stStatusWidget"] > div:first-child {
#     background: #0e1a2e !important;
#     border-radius: 12px 12px 0 0 !important;
# }
# [data-testid="stStatusWidget"] details,
# [data-testid="stStatusWidget"] details > div,
# [data-testid="stStatusWidget"] [data-testid="stVerticalBlock"] {
#     background: #0a1520 !important;
#     color: #ffffff !important;
#     padding: 0.25rem 0.5rem !important;
# }
# [data-testid="stStatusWidget"] * { color: #ffffff !important; }
# [data-testid="stStatusWidget"] a { color: #4ea8f0 !important; }
# [data-testid="stStatusWidget"] hr { border-color: #1e3050 !important; }

# /* ── Section headers ── */
# .sec-head {
#     display: flex;
#     align-items: center;
#     gap: 0.6rem;
#     margin: 2rem 0 0.75rem;
#     padding-bottom: 0.5rem;
#     border-bottom: 1px solid #1e2e44;
# }
# .sec-head span { font-size: 1.15rem; font-weight: 600; color: #e0edf8; }

# /* ── Metric bar ── */
# .metric-row {
#     display: flex;
#     gap: 1rem;
#     margin: 1.5rem 0;
# }
# .metric-box {
#     flex: 1;
#     background: #0e1623;
#     border: 1px solid #1e2e44;
#     border-radius: 12px;
#     padding: 1rem 1.2rem;
#     text-align: center;
# }
# .metric-val { font-size: 1.8rem; font-weight: 700; color: #4ea8f0; }
# .metric-lbl { font-size: 0.78rem; color: #5a7a96; margin-top: 0.2rem; text-transform: uppercase; letter-spacing: 0.08em; }

# /* ── Final plan ── */
# .final-card {
#     background: linear-gradient(160deg, #0c1a2e 0%, #0a1520 100%);
#     border: 1px solid #1e3a5c;
#     border-left: 4px solid #3a7bd5;
#     border-radius: 14px;
#     padding: 1.8rem;
#     line-height: 1.8;
#     color: #cce0f5;
#     font-size: 0.95rem;
# }

# /* ── Save bar ── */
# .save-bar {
#     background: #0e1623;
#     border: 1px solid #1e2e44;
#     border-radius: 10px;
#     padding: 0.85rem 1.2rem;
#     color: #5a8ab0;
#     font-size: 0.88rem;
#     margin-top: 0.5rem;
# }

# /* ── Sidebar ── */
# section[data-testid="stSidebar"] {
#     background: #090e18 !important;
#     border-right: 1px solid #141f30 !important;
# }
# .sidebar-chip {
#     background: #0e1a2b;
#     border: 1px solid #1a2e44;
#     border-radius: 8px;
#     padding: 0.45rem 0.75rem;
#     margin-bottom: 0.4rem;
#     font-size: 0.83rem;
#     color: #7aa8cc;
# }
# .sidebar-title { color: #e0edf8; font-size: 1rem; font-weight: 600; margin: 1rem 0 0.5rem; }

# /* Hide branding */
# #MainMenu, footer, header { visibility: hidden; }

# /* Textarea */
# .stTextArea textarea {
#     background: #0a1520 !important;
#     border: 1px solid #1e2e44 !important;
#     border-radius: 10px !important;
#     color: #e8f4ff !important;
#     font-size: 0.95rem !important;
#     resize: none !important;
# }
# .stTextArea textarea:focus {
#     border-color: #3a7bd5 !important;
#     box-shadow: 0 0 0 2px rgba(58,123,213,0.2) !important;
# }
# .stTextArea textarea::placeholder { color: #4a6a85 !important; }

# /* Text input (sidebar User ID field) */
# input[type="text"], .stTextInput input {
#     background: #0e1a2b !important;
#     border: 1px solid #1a2e44 !important;
#     border-radius: 8px !important;
#     color: #e0edf8 !important;
# }
# input[type="text"]:focus, .stTextInput input:focus {
#     border-color: #3a7bd5 !important;
#     box-shadow: 0 0 0 2px rgba(58,123,213,0.2) !important;
# }
# input[type="text"]::placeholder { color: #3a5570 !important; }

# /* All Streamlit labels — dark bg → light text */
# .stTextInput label, .stTextArea label,
# .stSelectbox label, .stNumberInput label {
#     color: #7ab8f5 !important;
#     font-size: 0.82rem !important;
#     font-weight: 600 !important;
#     letter-spacing: 0.08em !important;
# }

# /* General markdown / paragraph text */
# .stMarkdown p, .stMarkdown li, .stMarkdown td, .stMarkdown th {
#     color: #cce0f5 !important;
# }
# .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { color: #e8f4ff !important; }
# .stMarkdown code {
#     background: #0e1a2b !important;
#     color: #7ab8f5 !important;
#     padding: 0.15em 0.4em;
#     border-radius: 4px;
# }

# /* Metric labels — was #5a7a96 (too dim on dark bg) */
# .metric-lbl { color: #7aa8cc !important; }

# /* Save bar — was #5a8ab0 (slightly dim) */
# .save-bar { color: #8ab8d8 !important; }
# .save-bar code { color: #7ab8f5 !important; background: #0a1520 !important; }

# /* Streamlit warning / info / success on dark bg */
# .stAlert { background: #0e1a2b !important; border-radius: 10px !important; }
# .stAlert p, .stAlert div { color: #e0edf8 !important; }

# /* Sidebar text & dividers */
# section[data-testid="stSidebar"] p,
# section[data-testid="stSidebar"] span,
# section[data-testid="stSidebar"] label,
# section[data-testid="stSidebar"] .stMarkdown { color: #a0c4e0 !important; }
# section[data-testid="stSidebar"] hr { border-color: #1a2e44 !important; }

# /* Download button — light bg → dark text  */
# div[data-testid="stDownloadButton"] > button {
#     background: #1a3a5c !important;
#     color: #e8f4ff !important;
#     border: 1px solid #2a5080 !important;
#     border-radius: 10px !important;
# }
# </style>
# """, unsafe_allow_html=True)

# # ── Sidebar ───────────────────────────────────────────────────────────────────
# with st.sidebar:
#     st.markdown("<div class='sidebar-title'>🌍 AI Travel Planner</div>", unsafe_allow_html=True)
#     st.markdown("---")

#     thread_id = st.text_input("👤 User ID", value="user",
#                               help="Your session ID — keeps travel history across queries")

#     st.markdown("<div class='sidebar-title'>Powered by</div>", unsafe_allow_html=True)
#     for tech in ["🔗 LangGraph", "🧠 Groq · LLaMA 3.3 70B", "🐘 PostgreSQL", "🔍 Tavily Search", "✈️ AviationStack"]:
#         st.markdown(f"<div class='sidebar-chip'>{tech}</div>", unsafe_allow_html=True)

#     st.markdown("<div class='sidebar-title'>Agent Pipeline</div>", unsafe_allow_html=True)
#     for step in ["① Flight Agent", "② Hotel Agent", "③ Itinerary Agent", "④ Final Agent"]:
#         st.markdown(f"<div class='sidebar-chip'>{step}</div>", unsafe_allow_html=True)

# # ── Hero ──────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="hero-wrapper">
#     <img class="hero-bg"
#          src="https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=1400&q=80"
#          alt="airplane above clouds"/>
#     <div class="hero-content">
#         <div class="hero-badge">✦ Multi-Agent AI System</div>
#         <div class="hero-title">✈️ AI Travel Booking System</div>
#         <div class="hero-sub">Four specialized agents work together — searching flights, hotels, building an itinerary, and delivering your perfect trip plan.</div>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # ── Destination image strip ───────────────────────────────────────────────────
# DESTINATIONS = [
#     ("🇯🇵 Tokyo",     "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=300&q=70"),
#     ("🇫🇷 Paris",     "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=300&q=70"),
#     ("🇹🇭 Bangkok",   "https://images.unsplash.com/photo-1508009603885-50cf7c579365?w=300&q=70"),
#     ("🇮🇹 Rome",      "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=300&q=70"),
#     ("🇦🇪 Dubai",     "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=300&q=70"),
# ]

# cols = st.columns(5)
# for col, (name, img_url) in zip(cols, DESTINATIONS):
#     with col:
#         st.markdown(f"""
#         <div style="border-radius:10px;overflow:hidden;position:relative;height:90px;cursor:pointer;">
#             <img src="{img_url}" style="width:100%;height:100%;object-fit:cover;filter:brightness(0.55);" />
#             <div style="position:absolute;bottom:8px;left:0;right:0;text-align:center;
#                         color:#fff;font-size:0.8rem;font-weight:600;">{name}</div>
#         </div>
#         """, unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)

# # ── Input ─────────────────────────────────────────────────────────────────────
# st.markdown("<div class='input-label'>🗺️ Describe your trip</div>", unsafe_allow_html=True)

# QUICK = ["7-day Japan under ₹2L", "Paris trip for 5 days", "Dubai weekend trip", "Bali backpacking 10 days"]
# qcols = st.columns(len(QUICK))
# quick_fill = ""
# for qc, label in zip(qcols, QUICK):
#     with qc:
#         if st.button(label, key=f"q_{label}"):
#             quick_fill = label

# user_query = st.text_area(
#     "Travel Request",
#     value=quick_fill,
#     placeholder="e.g. Plan a complete 7-day Japan trip including flights, hotels and sightseeing under ₹2 lakhs",
#     height=100,
#     label_visibility="collapsed",
# )

# generate = st.button("🚀  Generate My Travel Plan", use_container_width=True)

# # ── Agent pipeline ────────────────────────────────────────────────────────────
# AGENT_META = {
#     "flight_agent":    ("✈️", "Flight Agent"),
#     "hotel_agent":     ("🏨", "Hotel Agent"),
#     "itinerary_agent": ("🗓️", "Itinerary Agent"),
#     "final_agent":     ("🧠", "Final Agent"),
# }

# if generate:
#     if not user_query.strip():
#         st.warning("Please describe your trip first.")
#     else:
#         config = {"configurable": {"thread_id": thread_id}}
#         collected = {"flight_results": "", "hotel_results": "",
#                      "itinerary": "", "final_response": "", "llm_calls": 0}

#         st.markdown("---")
#         st.markdown("<div class='sec-head'><span>🤖 Agent Pipeline — Live</span></div>",
#                     unsafe_allow_html=True)

#         for chunk in app.stream(
#             {
#                 "messages": [HumanMessage(content=user_query)],
#                 "user_query": user_query,
#                 "flight_results": "",
#                 "hotel_results": "",
#                 "itinerary": "",
#                 "llm_calls": 0,
#             },
#             config=config,
#             stream_mode="updates",
#         ):
#             for node_name, state_update in chunk.items():
#                 icon, label = AGENT_META.get(node_name, ("🔧", node_name))

#                 with st.status(f"{icon}  {label}", state="complete", expanded=True):
#                     if node_name == "flight_agent":
#                         text = state_update.get("flight_results", "")
#                         collected["flight_results"] = text
#                         st.markdown(text or "_No flight data returned._")

#                     elif node_name == "hotel_agent":
#                         text = state_update.get("hotel_results", "")
#                         collected["hotel_results"] = text
#                         st.markdown(text or "_No hotel data returned._")

#                     elif node_name == "itinerary_agent":
#                         text = state_update.get("itinerary", "")
#                         collected["itinerary"] = text
#                         st.markdown(text or "_No itinerary generated._")

#                     elif node_name == "final_agent":
#                         msgs = state_update.get("messages", [])
#                         text = msgs[-1].content if msgs else ""
#                         collected["final_response"] = text
#                         st.markdown(text or "_No final response._")

#                     collected["llm_calls"] = state_update.get("llm_calls", collected["llm_calls"])

#         # Metrics
#         st.markdown(f"""
#         <div class="metric-row">
#             <div class="metric-box"><div class="metric-val">4</div><div class="metric-lbl">Agents Run</div></div>
#             <div class="metric-box"><div class="metric-val">{collected['llm_calls']}</div><div class="metric-lbl">LLM Calls</div></div>
#             <div class="metric-box"><div class="metric-val">✅</div><div class="metric-lbl">Status</div></div>
#         </div>
#         """, unsafe_allow_html=True)

#         # Final plan card
#         if collected["final_response"]:
#             st.markdown("<div class='sec-head'><span>🧠 Final Travel Plan</span></div>",
#                         unsafe_allow_html=True)
#             st.markdown(f"<div class='final-card'>{collected['final_response']}</div>",
#                         unsafe_allow_html=True)

#         # Save
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"travel_plan_{timestamp}.md"
#         save_dir = os.path.join(os.path.dirname(__file__), "travel_plans")
#         os.makedirs(save_dir, exist_ok=True)

#         file_content = f"""# Travel Plan
# **Query:** {user_query}
# **Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
# **User ID:** {thread_id}

# ---

# ## ✈️ Flight Information
# {collected['flight_results'] or 'N/A'}

# ---

# ## 🏨 Hotel Information
# {collected['hotel_results'] or 'N/A'}

# ---

# ## 🗓️ Itinerary
# {collected['itinerary'] or 'N/A'}

# ---

# ## 🧠 Final Travel Plan
# {collected['final_response'] or 'N/A'}

# ---
# *LLM Calls: {collected['llm_calls']}*
# """
#         with open(os.path.join(save_dir, filename), "w", encoding="utf-8") as f:
#             f.write(file_content)

#         dl_col, info_col = st.columns([1, 3])
#         with dl_col:
#             st.download_button("⬇️ Download Plan", data=file_content,
#                                file_name=filename, mime="text/markdown",
#                                use_container_width=True)
#         with info_col:
#             st.markdown(f"<div class='save-bar'>📁 Auto-saved → <code>travel_plans/{filename}</code></div>",
#                         unsafe_allow_html=True)


import os
import streamlit as st
from datetime import datetime
from langchain_core.messages import HumanMessage
from main import app

st.set_page_config(
    page_title="AI Travel Booking System",
    page_icon="🎫",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap');

:root {
    --bg: #0F1E2E;
    --card: #16283C;
    --card-2: #122236;
    --line: #24384E;
    --parchment: #F3E9D2;
    --ink: #0F1E2E;
    --gold: #C9A227;
    --teal: #2E8B7C;
    --text: #E7EEF3;
    --muted: #7F97AC;
}

html, body, .stApp { font-family: 'Inter', sans-serif; background-color: var(--bg); color: var(--text); }
h1, h2, h3, .display { font-family: 'Fraunces', serif; }

/* ── Boarding pass hero ── */
.pass-wrapper {
    display: flex;
    background: linear-gradient(160deg, var(--card) 0%, var(--card-2) 100%);
    border: 1px solid var(--line);
    border-radius: 18px;
    overflow: hidden;
    margin-bottom: 1.6rem;
    min-height: 210px;
}
.pass-main {
    flex: 1;
    padding: 2.1rem 2.4rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
}
.pass-route {
    font-size: 0.82rem;
    letter-spacing: 0.06em;
    color: var(--gold);
    font-weight: 600;
    margin-bottom: 0.5rem;
}
.pass-title {
    font-family: 'Fraunces', serif;
    font-size: 2.5rem;
    font-weight: 600;
    color: #FBF6EA;
    margin: 0 0 0.5rem;
    line-height: 1.15;
}
.pass-sub {
    color: var(--muted);
    font-size: 0.98rem;
    max-width: 480px;
    line-height: 1.5;
}
.pass-stub {
    width: 220px;
    background: repeating-linear-gradient(135deg, #10202f, #10202f 10px, #0e1c2a 10px, #0e1c2a 20px);
    border-left: 2px dashed var(--muted);
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 1.5rem 1rem;
    gap: 0.35rem;
    text-align: center;
}
.pass-stub::before, .pass-stub::after {
    content: "";
    position: absolute;
    left: -11px;
    width: 22px; height: 22px;
    background: var(--bg);
    border-radius: 50%;
}
.pass-stub::before { top: -11px; }
.pass-stub::after { bottom: -11px; }
.stub-label { font-size: 0.68rem; letter-spacing: 0.14em; color: var(--muted); }
.stub-value { font-family: 'Fraunces', serif; font-size: 1.3rem; color: var(--parchment); font-weight: 600; }

/* ── Buttons (base reset — Streamlit defaults to white) ── */
.tag-hint { color: var(--muted); font-size: 0.82rem; margin: 0.2rem 0 0.6rem; }
.stButton { width: 100%; }
.stButton > button,
.stButton > button:visited,
.stButton > button p {
    background: var(--card) !important;
    color: var(--text) !important;
    border: 1px solid var(--line) !important;
    border-radius: 8px !important;
    padding: 0.5rem 0.7rem !important;
    font-size: 0.83rem !important;
    font-weight: 500 !important;
    box-shadow: none !important;
}
.stButton > button:hover,
.stButton > button:hover p {
    border-color: var(--gold) !important;
    color: var(--gold) !important;
    background: var(--card) !important;
    transform: none !important;
}
.stButton > button:active,
.stButton > button:focus:not(:active) {
    border-color: var(--gold) !important;
    color: var(--gold) !important;
    box-shadow: 0 0 0 1px var(--gold) !important;
}

/* ── Generate button (overrides the base button style above) ── */
.generate-btn .stButton > button,
.generate-btn .stButton > button p {
    background: var(--gold) !important;
    color: #1a1305 !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.9rem 2.4rem !important;
    font-size: 1.02rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.02em !important;
    box-shadow: 0 4px 18px rgba(201,162,39,0.25) !important;
    transition: all 0.2s ease !important;
}
.generate-btn .stButton > button:hover,
.generate-btn .stButton > button:hover p {
    background: #dbb230 !important;
    color: #1a1305 !important;
    box-shadow: 0 6px 24px rgba(201,162,39,0.4) !important;
    transform: translateY(-1px) !important;
}
.generate-btn .stButton > button:active,
.generate-btn .stButton > button:focus:not(:active) {
    box-shadow: 0 4px 18px rgba(201,162,39,0.25) !important;
}

/* ── Section headers ── */
.sec-head {
    display: flex;
    align-items: baseline;
    gap: 0.6rem;
    margin: 2rem 0 0.9rem;
}
.sec-head .num { font-family: 'Fraunces', serif; color: var(--gold); font-size: 1.1rem; }
.sec-head .label { font-size: 1.05rem; font-weight: 600; color: var(--text); }
.sec-rule { flex: 1; border-bottom: 1px dashed var(--line); }

/* ── Agent status stubs (status widget + underlying expander) ── */
[data-testid="stStatusWidget"],
[data-testid="stStatusWidget"] > div,
[data-testid="stStatusWidgetIcon"],
[data-testid="stExpander"],
[data-testid="stExpander"] > details,
[data-testid="stExpander"] summary,
.streamlit-expanderHeader {
    background: var(--card) !important;
    border-color: var(--line) !important;
}
[data-testid="stStatusWidget"] { border: 1px solid var(--line) !important; border-radius: 10px !important; }
[data-testid="stExpander"] { border: 1px solid var(--line) !important; border-radius: 10px !important; }
[data-testid="stExpander"] summary,
[data-testid="stStatusWidget"] summary {
    border-radius: 10px 10px 0 0 !important;
}
[data-testid="stExpander"] summary p,
[data-testid="stExpander"] summary span,
[data-testid="stStatusWidget"] summary p,
[data-testid="stStatusWidget"] summary span,
.streamlit-expanderHeader p,
.streamlit-expanderHeader span {
    color: var(--text) !important;
}
[data-testid="stExpander"] summary svg,
[data-testid="stStatusWidget"] summary svg {
    fill: var(--gold) !important;
    color: var(--gold) !important;
}
[data-testid="stStatusWidget"] details, [data-testid="stStatusWidget"] details > div,
[data-testid="stStatusWidget"] [data-testid="stVerticalBlock"],
[data-testid="stExpander"] details, [data-testid="stExpander"] details > div,
[data-testid="stExpander"] [data-testid="stVerticalBlock"] { background: var(--card-2) !important; color: var(--text) !important; }
[data-testid="stStatusWidget"] *, [data-testid="stExpander"] * { color: var(--text) !important; }
[data-testid="stStatusWidget"] a, [data-testid="stExpander"] a { color: var(--teal) !important; }
[data-testid="stStatusWidget"] hr, [data-testid="stExpander"] hr { border-color: var(--line) !important; }

/* ── Wax-seal metrics ── */
.metric-row { display: flex; gap: 1rem; margin: 1.6rem 0; }
.metric-box {
    flex: 1;
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 1rem 1.2rem;
    text-align: center;
}
.metric-val { font-family: 'Fraunces', serif; font-size: 1.9rem; font-weight: 600; color: var(--gold); }
.metric-lbl { font-size: 0.74rem; color: var(--muted); margin-top: 0.15rem; letter-spacing: 0.06em; }

/* ── Final ticket card with scalloped edge ── */
.ticket-card {
    position: relative;
    background: var(--parchment);
    color: #241d0f;
    border-radius: 4px;
    padding: 2.2rem 2rem 1.8rem;
    line-height: 1.75;
    font-size: 0.96rem;
    margin-top: 14px;
}
.ticket-card::before {
    content: "";
    position: absolute;
    top: -11px; left: 0; right: 0; height: 22px;
    background-image: radial-gradient(circle at 11px 11px, var(--bg) 11px, transparent 11.5px);
    background-size: 22px 22px;
    background-repeat: repeat-x;
}
div.ticket-card,
div.ticket-card p,
div.ticket-card li,
div.ticket-card span,
div.ticket-card div,
div.ticket-card h1, div.ticket-card h2, div.ticket-card h3, div.ticket-card h4,
div.ticket-card strong, div.ticket-card b, div.ticket-card em {
    color: #241d0f !important;
}
div.ticket-card table { border-collapse: collapse; width: 100%; margin: 0.6rem 0; }
div.ticket-card table, div.ticket-card th, div.ticket-card td {
    border: 1px solid rgba(36,29,15,0.25) !important;
}
div.ticket-card th, div.ticket-card td {
    color: #241d0f !important;
    padding: 0.4rem 0.6rem;
    background: transparent !important;
}
div.ticket-card th { background: rgba(36,29,15,0.08) !important; font-weight: 700; }
div.ticket-card a { color: #0a5c4e !important; text-decoration: underline; }
div.ticket-card code { background: rgba(36,29,15,0.08) !important; color: #6b3f0a !important; }
div.ticket-card hr { border-color: rgba(36,29,15,0.25) !important; }

/* ── Save bar ── */
.save-bar {
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 0.8rem 1.1rem;
    color: var(--muted);
    font-size: 0.86rem;
    margin-top: 0.5rem;
}
.save-bar code { color: var(--teal) !important; background: var(--card-2) !important; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] { background: #0A1420 !important; border-right: 1px solid var(--line) !important; }
.sidebar-title { font-family: 'Fraunces', serif; color: var(--parchment); font-size: 1.05rem; font-weight: 600; margin: 1.1rem 0 0.6rem; }
.sidebar-chip {
    background: var(--card-2);
    border: 1px solid var(--line);
    border-radius: 6px;
    padding: 0.4rem 0.7rem;
    margin-bottom: 0.35rem;
    font-size: 0.82rem;
    color: var(--muted);
}
.pipeline-chip { display: flex; align-items: center; gap: 0.5rem; }
.pipeline-chip .n { color: var(--gold); font-family: 'Fraunces', serif; font-weight: 600; }

/* ── Inputs ── */
#MainMenu, footer, header { visibility: hidden; }
.stTextArea textarea {
    background: var(--card) !important;
    border: 1px solid var(--line) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-size: 0.95rem !important;
    resize: none !important;
}
.stTextArea textarea:focus { border-color: var(--gold) !important; box-shadow: 0 0 0 2px rgba(201,162,39,0.18) !important; }
.stTextArea textarea::placeholder { color: var(--muted) !important; }
input[type="text"], .stTextInput input {
    background: var(--card-2) !important;
    border: 1px solid var(--line) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
}
input[type="text"]:focus, .stTextInput input:focus { border-color: var(--gold) !important; box-shadow: 0 0 0 2px rgba(201,162,39,0.18) !important; }
.stTextInput label, .stTextArea label { color: var(--gold) !important; font-size: 0.8rem !important; font-weight: 600 !important; }
.stMarkdown p, .stMarkdown li, .stMarkdown td, .stMarkdown th { color: var(--text) !important; }
.stMarkdown code { background: var(--card-2) !important; color: var(--teal) !important; padding: 0.15em 0.4em; border-radius: 4px; }
.stAlert { background: var(--card) !important; border-radius: 10px !important; }
.stAlert p, .stAlert div { color: var(--text) !important; }
section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] .stMarkdown { color: var(--muted) !important; }
section[data-testid="stSidebar"] hr { border-color: var(--line) !important; }
div[data-testid="stDownloadButton"] > button {
    background: var(--card-2) !important;
    color: var(--gold) !important;
    border: 1px solid var(--gold) !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("<div class='sidebar-title'>🎫 Travel Dossier</div>", unsafe_allow_html=True)
    st.markdown("---")

    thread_id = st.text_input("Passenger ID", value="user",
                              help="Your session ID — keeps travel history across queries")

    st.markdown("<div class='sidebar-title'>Powered by</div>", unsafe_allow_html=True)
    for tech in ["LangGraph", "Groq · LLaMA 3.3 70B", "PostgreSQL", "Tavily Search", "AviationStack"]:
        st.markdown(f"<div class='sidebar-chip'>{tech}</div>", unsafe_allow_html=True)

    st.markdown("<div class='sidebar-title'>Agent Pipeline</div>", unsafe_allow_html=True)
    for n, step in enumerate(["Flight Agent", "Hotel Agent", "Itinerary Agent", "Final Agent"], start=1):
        st.markdown(f"<div class='sidebar-chip pipeline-chip'><span class='n'>{n:02d}</span> {step}</div>",
                    unsafe_allow_html=True)

# ── Boarding-pass hero ───────────────────────────────────────────────────
today = datetime.now().strftime("%d %b %Y")
st.markdown(f"""
<div class="pass-wrapper">
    <div class="pass-main">
        <div class="pass-route">YOU  ✈  ANYWHERE</div>
        <div class="pass-title">Where to, next?</div>
        <div class="pass-sub">Four agents work in sequence — flights, hotels, itinerary and a
        final plan — assembled into one dossier, ready to download.</div>
    </div>
    <div class="pass-stub">
        <div class="stub-label">ISSUED</div>
        <div class="stub-value" style="font-size:1rem;">{today}</div>
        <div class="stub-label" style="margin-top:0.6rem;">CLASS</div>
        <div class="stub-value">Explorer</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Destination quick-picks ──────────────────────────────────────────────
if "trip_query" not in st.session_state:
    st.session_state.trip_query = ""

st.markdown("<div class='tag-hint'>QUICK PICKS</div>", unsafe_allow_html=True)
QUICK = ["7-day Japan under ₹2L", "Paris trip for 5 days", "Dubai weekend trip", "Bali backpacking 10 days"]
qcols = st.columns(len(QUICK))
for qc, label in zip(qcols, QUICK):
    with qc:
        if st.button(label, key=f"q_{label}"):
            st.session_state.trip_query = label

st.markdown("<div class='tag-hint' style='margin-top:1.2rem;'>DESCRIBE YOUR TRIP</div>", unsafe_allow_html=True)
user_query = st.text_area(
    "Travel Request",
    key="trip_query",
    placeholder="e.g. Plan a complete 7-day Japan trip including flights, hotels and sightseeing under ₹2 lakhs",
    height=100,
    label_visibility="collapsed",
)

st.markdown('<div class="generate-btn">', unsafe_allow_html=True)
generate = st.button("Generate My Travel Plan", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Agent pipeline ────────────────────────────────────────────────────────
AGENT_META = {
    "flight_agent":    ("01", "Flight Agent"),
    "hotel_agent":     ("02", "Hotel Agent"),
    "itinerary_agent": ("03", "Itinerary Agent"),
    "final_agent":     ("04", "Final Agent"),
}

if generate:
    if not user_query.strip():
        st.warning("Please describe your trip first.")
    else:
        config = {"configurable": {"thread_id": thread_id}}
        collected = {"flight_results": "", "hotel_results": "",
                     "itinerary": "", "final_response": "", "llm_calls": 0}

        st.markdown(f"""
        <div class="sec-head">
            <span class="num">§</span>
            <span class="label">Agent Pipeline — Live</span>
            <span class="sec-rule"></span>
        </div>
        """, unsafe_allow_html=True)

        for chunk in app.stream(
            {
                "messages": [HumanMessage(content=user_query)],
                "user_query": user_query,
                "flight_results": "",
                "hotel_results": "",
                "itinerary": "",
                "llm_calls": 0,
            },
            config=config,
            stream_mode="updates",
        ):
            for node_name, state_update in chunk.items():
                num, label = AGENT_META.get(node_name, ("•", node_name))

                with st.status(f"{num}  {label}", state="complete", expanded=True):
                    if node_name == "flight_agent":
                        text = state_update.get("flight_results", "")
                        collected["flight_results"] = text
                        st.markdown(text or "_No flight data returned._")

                    elif node_name == "hotel_agent":
                        text = state_update.get("hotel_results", "")
                        collected["hotel_results"] = text
                        st.markdown(text or "_No hotel data returned._")

                    elif node_name == "itinerary_agent":
                        text = state_update.get("itinerary", "")
                        collected["itinerary"] = text
                        st.markdown(text or "_No itinerary generated._")

                    elif node_name == "final_agent":
                        msgs = state_update.get("messages", [])
                        text = msgs[-1].content if msgs else ""
                        collected["final_response"] = text
                        st.markdown(text or "_No final response._")

                    collected["llm_calls"] = state_update.get("llm_calls", collected["llm_calls"])

        # Metrics
        st.markdown(f"""
        <div class="metric-row">
            <div class="metric-box"><div class="metric-val">4</div><div class="metric-lbl">AGENTS RUN</div></div>
            <div class="metric-box"><div class="metric-val">{collected['llm_calls']}</div><div class="metric-lbl">LLM CALLS</div></div>
            <div class="metric-box"><div class="metric-val">✓</div><div class="metric-lbl">STATUS</div></div>
        </div>
        """, unsafe_allow_html=True)

        # Final plan — torn ticket card
        if collected["final_response"]:
            st.markdown(f"""
            <div class="sec-head">
                <span class="num">§</span>
                <span class="label">Final Travel Plan</span>
                <span class="sec-rule"></span>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(f"<div class='ticket-card'>{collected['final_response']}</div>",
                        unsafe_allow_html=True)

        # Save
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"travel_plan_{timestamp}.md"
        save_dir = os.path.join(os.path.dirname(__file__), "travel_plans")
        os.makedirs(save_dir, exist_ok=True)

        file_content = f"""# Travel Plan
**Query:** {user_query}
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**User ID:** {thread_id}

---

## Flight Information
{collected['flight_results'] or 'N/A'}

---

## Hotel Information
{collected['hotel_results'] or 'N/A'}

---

## Itinerary
{collected['itinerary'] or 'N/A'}

---

## Final Travel Plan
{collected['final_response'] or 'N/A'}

---
*LLM Calls: {collected['llm_calls']}*
"""
        with open(os.path.join(save_dir, filename), "w", encoding="utf-8") as f:
            f.write(file_content)

        dl_col, info_col = st.columns([1, 3])
        with dl_col:
            st.download_button("⬇ Download Plan", data=file_content,
                               file_name=filename, mime="text/markdown",
                               use_container_width=True)
        with info_col:
            st.markdown(f"<div class='save-bar'>Auto-saved → <code>travel_plans/{filename}</code></div>",
                        unsafe_allow_html=True)
