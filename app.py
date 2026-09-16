import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="LPDG Gateway Intelligence", page_icon="⚡", layout="wide"
)

# --- MODERN CLEAN UI DESIGN (No Sidebar, Full Sections & Buttons) ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0c0a1d;
        color: #e2e8f0;
    }
    .hero-container {
        background: linear-gradient(135deg, #1a1630 0%, #0f0c1b 100%);
        padding: 35px;
        border-radius: 16px;
        border: 1px solid #2d2456;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }
    .content-card {
        background: rgba(26, 22, 48, 0.7);
        border: 1px solid #2d2456;
        padding: 25px;
        border-radius: 14px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 20px;
    }
    .stButton button {
        background-color: #7c3aed;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        border: none;
        width: 100%;
    }
    .stButton button:hover {
        background-color: #6d28d9;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- SESSION STATE FOR NAVIGATION ---
if "page" not in st.session_state:
  st.session_state.page = "Overview"

# --- PAGE 1: EXECUTIVE OVERVIEW ---
if st.session_state.page == "Overview":
  st.markdown(
      """
        <div class="hero-container">
            <h1 style='color: #f3e8ff; font-size: 34px; font-weight: 800; margin: 0;'>LPDG Gateway Intelligence</h1>
            <p style='color: #94a3b8; font-size: 16px; margin-top: 8px;'>Field Visit Prioritization & Network Reliability Analysis</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  col1, col2, col3 = st.columns(3)
  with col1:
    st.markdown(
        """
            <div class="content-card" style="text-align: center;">
                <p style="color: #94a3b8; font-size: 14px;">Baseline cost</p>
                <h2 style="color: #f8fafc; font-size: 26px; margin: 5px 0;">€329,400</h2>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with col2:
    st.markdown(
        """
            <div class="content-card" style="text-align: center;">
                <p style="color: #94a3b8; font-size: 14px;">Logistic Regression cost</p>
                <h2 style="color: #f8fafc; font-size: 26px; margin: 5px 0;">€270,600</h2>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with col3:
    st.markdown(
        """
            <div class="content-card" style="text-align: center;">
                <p style="color: #94a3b8; font-size: 14px;">Lower historical proxy-label cost</p>
                <h2 style="color: #a78bfa; font-size: 26px; margin: 5px 0;">€58,800</h2>
            </div>
        """,
        unsafe_allow_html=True,
    )

  st.write("")
  if st.button("Proceed to Part 1 – Operational Ranking ➔"):
    st.session_state.page = "Part1"
    st.rerun()

# --- PAGE 2: PART 1 - OPERATIONAL RANKING ---
elif st.session_state.page == "Part1":
  st.markdown(
      """
        <div class="hero-container">
            <h1 style='color: #f3e8ff; font-size: 30px; font-weight: 800;'>📊 Part 1 – Operational Ranking</h1>
            <p style='color: #94a3b8; font-size: 15px;'>Analyzing baseline rankings and historical proxy targets.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div class="content-card">
            <h3>Operational Details</h3>
            <p><b>Constraint:</b> Weekly Visit Constraint of 15 gateways.</p>
            <p><b>Status:</b> Read-only evidence loaded successfully.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.write("")
  col_p1, col_p2 = st.columns(2)
  with col_p1:
    if st.button("⬅️ Back to Overview"):
      st.session_state.page = "Overview"
      st.rerun()
  with col_p2:
    if st.button("Proceed to Part 2 – Machine Learning ➔"):
      st.session_state.page = "Part2"
      st.rerun()

# --- PAGE 3: PART 2 - MACHINE LEARNING ---
elif st.session_state.page == "Part2":
  st.markdown(
      """
        <div class="hero-container">
            <h1 style='color: #f3e8ff; font-size: 30px; font-weight: 800;'>🤖 Part 2 – Machine Learning</h1>
            <p style='color: #94a3b8; font-size: 15px;'>Predictive maintenance models and telemetry optimization.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div class="content-card">
            <h3>Model Intelligence & Gateway Explorer</h3>
            <p><b>Telemetry Features:</b> offline_duration_sec, disconnection_cnt, reboot_cnt.</p>
            <p><b>Financial Impact:</b> €58,800 total estimated reduction in proxy operational cost.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.write("")
  if st.button("⬅️ Back to Operational Ranking"):
    st.session_state.page = "Part1"
    st.rerun()
