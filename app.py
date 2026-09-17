import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="LPDG Gateway Intelligence Hub", page_icon="⚡", layout="wide"
)

# --- MODERN CLEAN LANDING TEMPLATE STYLING ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
    }
    
    /* Hero Header Card */
    .custom-hero {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 45px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    
    /* Info Cards Style */
    .metric-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
        margin-bottom: 20px;
    }
    
    /* Button Customization */
    .stButton button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        padding: 12px 28px;
        font-weight: 600;
        border: none;
        width: 100%;
    }
    .stButton button:hover {
        background-color: #1d4ed8;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- SESSION STATE FOR NAVIGATION ---
if "active_section" not in st.session_state:
  st.session_state.active_section = 1

# --- SECTION 1: OVERVIEW & PROBLEM STATEMENT ---
if st.session_state.active_section == 1:
  st.markdown(
      """
        <div class="custom-hero">
            <h1 style='font-size: 38px; font-weight: 800; margin: 0;'>LPDG Gateway Intelligence Hub</h1>
            <p style='font-size: 16px; color: #94a3b8; margin-top: 10px;'>Smart Telemetry & Field Visit Optimization Platform</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  # Problem Statement Card
  st.markdown(
      """
        <div class="metric-card" style="text-align: left;">
            <h3 style="color: #0f172a; margin-top: 0;">📌 Problem Statement</h3>
            <p style="font-size: 16px; color: #475569; line-height: 1.6;">
                Fixing broken IoT gateways blindly or too late costs a lot of money and wastes technician visits. 
                By using machine learning to look at past device signals, we can figure out which 15 gateways actually need fixing every week—cutting 
                unnecessary costs from €329,400 down to €270,600.
            </p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.write("")
  if st.button("Scroll to Financial Metrics ➔"):
    st.session_state.active_section = 2
    st.rerun()

# --- SECTION 2: FINANCIAL METRICS & SAVINGS ---
elif st.session_state.active_section == 2:
  st.markdown(
      """
        <div class="custom-hero" style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%);">
            <h1 style='font-size: 34px; font-weight: 800;'>📊 Financial Impact & Cost Analysis</h1>
            <p style='font-size: 15px; color: #cbd5e1;'>Evaluating baseline performance versus optimized machine learning strategies.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  # 3 Columns for Metrics
  c1, c2, c3 = st.columns(3)
  with c1:
    st.markdown(
        """
            <div class="metric-card">
                <p style="color: #64748b; font-size: 14px;">Baseline Cost</p>
                <h2 style="color: #0f172a; font-size: 28px; margin: 5px 0;">€329,400</h2>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with c2:
    st.markdown(
        """
            <div class="metric-card">
                <p style="color: #64748b; font-size: 14px;">Optimized ML Cost</p>
                <h2 style="color: #0f172a; font-size: 28px; margin: 5px 0;">€270,600</h2>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with c3:
    st.markdown(
        """
            <div class="metric-card">
                <p style="color: #64748b; font-size: 14px;">Net Financial Savings</p>
                <h2 style="color: #2563eb; font-size: 28px; margin: 5px 0;">€58,800</h2>
            </div>
        """,
        unsafe_allow_html=True,
    )

  st.write("")
  col_a, col_b = st.columns(2)
  with col_a:
    if st.button("⬅️ Back to Overview"):
      st.session_state.active_section = 1
      st.rerun()
  with col_b:
    if st.button("Proceed to Validation Notice ➔"):
      st.session_state.active_section = 3
      st.rerun()

# --- SECTION 3: VALIDATION NOTICE & DASHBOARD ---
elif st.session_state.active_section == 3:
  st.markdown(
      """
        <div class="custom-hero" style="background: linear-gradient(135deg, #0f172a 0%, #0f172a 100%);">
            <h1 style='font-size: 34px; font-weight: 800;'>🔍 Validation Notice & Telemetry View</h1>
            <p style='font-size: 15px; color: #94a3b8;'>Verification summary and operational compliance guidelines.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div class="metric-card" style="text-align: left; border-left: 4px solid #2563eb;">
            <h4 style="color: #0f172a; margin-top: 0;">Validation Notice:</h4>
            <p style="color: #475569; font-size: 15px;">
                These results utilize a retrospective proxy baseline and do not represent official ground-truth performance. 
                The financial metrics reflect simulated optimization under strict weekly constraints (exactly 15 gateways per week).
            </p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.write("")
  if st.button("⬅️ Back to Financial Metrics"):
    st.session_state.active_section = 2
    st.rerun()
