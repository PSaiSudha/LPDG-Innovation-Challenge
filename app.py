import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="LPDG Gateway Intelligence", page_icon="⚡", layout="wide"
)

# --- MODERN FULL-PAGE LANDING DESIGN (No Sidebar) ---
st.markdown(
    """
    <style>
    /* Main App Background - Clean Light Mode */
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
    }
    
    /* Hero Banner Style */
    .hero-container {
        background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid #cbd5e1;
        margin-bottom: 30px;
        text-align: center;
    }
    
    /* Content Cards Style */
    .content-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Button Styling */
    .stButton button {
        background-color: #0f172a;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        border: none;
        width: 100%;
    }
    .stButton button:hover {
        background-color: #3b82f6;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- SESSION STATE FOR SECTION NAVIGATION ---
if "section" not in st.session_state:
  st.session_state.section = 1

# --- SECTION 1: EXECUTIVE OVERVIEW ---
if st.session_state.section == 1:
  st.markdown(
      """
        <div class="hero-container">
            <h1 style='color: #0f172a; font-size: 36px; font-weight: 800; margin: 0;'>LPDG Gateway Intelligence</h1>
            <p style='color: #64748b; font-size: 16px; margin-top: 10px;'>Field Visit Prioritization & Network Reliability Analysis</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  # Metric Cards Layout
  col1, col2, col3 = st.columns(3)
  with col1:
    st.markdown(
        """
            <div class="content-card">
                <p style="color: #64748b; font-size: 14px;">Baseline cost</p>
                <h2 style="color: #0f172a; font-size: 26px; margin: 5px 0;">€329,400</h2>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with col2:
    st.markdown(
        """
            <div class="content-card">
                <p style="color: #64748b; font-size: 14px;">Logistic Regression cost</p>
                <h2 style="color: #0f172a; font-size: 26px; margin: 5px 0;">€270,600</h2>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with col3:
    st.markdown(
        """
            <div class="content-card">
                <p style="color: #64748b; font-size: 14px;">Lower historical proxy-label cost</p>
                <h2 style="color: #2563eb; font-size: 26px; margin: 5px 0;">€58,800</h2>
            </div>
        """,
        unsafe_allow_html=True,
    )

  st.write("")
  if st.button("Scroll to Operational Ranking Section ➔"):
    st.session_state.section = 2
    st.rerun()

# --- SECTION 2: OPERATIONAL RANKING ---
elif st.session_state.section == 2:
  st.markdown(
      """
        <div class="hero-container">
            <h1 style='color: #0f172a; font-size: 32px; font-weight: 800;'>📊 Part 1 – Operational Ranking</h1>
            <p style='color: #64748b; font-size: 15px;'>Evaluating baseline costs and weekly visit priority constraints.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div class="content-card" style="text-align: left;">
            <h3>Key Ranking Metrics</h3>
            <p><b>Weekly Visit Constraint:</b> Exactly 15 gateways per week across evaluation periods.</p>
            <p><b>Financial Impact:</b> Optimization brings down baseline cost from €329,400 to €270,600.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.write("")
  col_b1, col_b2 = st.columns(2)
  with col_b1:
    if st.button("⬅️ Back to Executive Overview"):
      st.session_state.section = 1
      st.rerun()
  with col_b2:
    if st.button("Proceed to Machine Learning Section ➔"):
      st.session_state.section = 3
      st.rerun()

# --- SECTION 3: MACHINE LEARNING & EXPLORER ---
elif st.session_state.section == 3:
  st.markdown(
      """
        <div class="hero-container">
            <h1 style='color: #0f172a; font-size: 32px; font-weight: 800;'>🤖 Part 2 – Machine Learning</h1>
            <p style='color: #64748b; font-size: 15px;'>Telemetry-driven predictive maintenance and risk scoring pipeline.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div class="content-card" style="text-align: left;">
            <h3>Model Intelligence & Gateway Explorer</h3>
            <p><b>Features Used:</b> offline_duration_sec, disconnection_cnt, reboot_cnt.</p>
            <p><b>Outcome:</b> Successfully saves €58,800 through proactive field interventions.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.write("")
  if st.button("⬅️ Back to Operational Ranking"):
    st.session_state.section = 2
    st.rerun()
