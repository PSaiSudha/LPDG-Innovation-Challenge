import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="LPDG Gateway Intelligence Hub", page_icon="⚡", layout="wide"
)

# --- FRESH MODERN UI STYLING ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    
    /* Sleek Banner */
    .banner-box {
        background: linear-gradient(90deg, #1e293b 0%, #334155 100%);
        padding: 30px;
        border-radius: 14px;
        border: 1px solid #475569;
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Content Cards */
    .content-box {
        background: #1e293b;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #334155;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    
    /* Custom Buttons */
    .stButton button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        border: none;
        width: 100%;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- NAVIGATION SESSION STATE ---
if "section_id" not in st.session_state:
  st.session_state.section_id = 1

# --- SECTION 1: PROBLEM STATEMENT & OVERVIEW ---
if st.session_state.section_id == 1:
  st.markdown(
      """
        <div class="banner-box">
            <h1 style='color: #f8fafc; margin: 0; font-size: 32px;'>⚡ LPDG Gateway Intelligence Hub</h1>
            <p style='color: #94a3b8; margin-top: 8px;'>Intelligent Network Telemetry & Optimization</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div class="content-box">
            <h3 style='color: #60a5fa; margin-top: 0;'>📌 Problem Statement</h3>
            <p style='color: #cbd5e1; font-size: 16px; line-height: 1.6;'>
                Fixing broken IoT gateways blindly or too late costs a lot of money and wastes technician visits. 
                By using machine learning to look at past device signals, we can figure out which 15 gateways actually need fixing every week—cutting 
                unnecessary costs from €329,400 down to €270,600.
            </p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.write("")
  if st.button("Next: View Financial Impact ➔"):
    st.session_state.section_id = 2
    st.rerun()

# --- SECTION 2: FINANCIAL METRICS ---
elif st.session_state.section_id == 2:
  st.markdown(
      """
        <div class="banner-box">
            <h1 style='color: #f8fafc; margin: 0; font-size: 32px;'>📊 Financial Impact & Cost Analysis</h1>
            <p style='color: #94a3b8; margin-top: 8px;'>Baseline vs Optimized Machine Learning Strategy</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  c1, c2, c3 = st.columns(3)
  with c1:
    st.markdown(
        """
            <div class="content-box" style="text-align: center;">
                <p style="color: #94a3b8; font-size: 14px; margin: 0;">Baseline Cost</p>
                <h2 style="color: #f8fafc; font-size: 26px; margin: 10px 0;">€329,400</h2>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with c2:
    st.markdown(
        """
            <div class="content-box" style="text-align: center;">
                <p style="color: #94a3b8; font-size: 14px; margin: 0;">Optimized ML Cost</p>
                <h2 style="color: #f8fafc; font-size: 26px; margin: 10px 0;">€270,600</h2>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with c3:
    st.markdown(
        """
            <div class="content-box" style="text-align: center;">
                <p style="color: #94a3b8; font-size: 14px; margin: 0;">Net Financial Savings</p>
                <h2 style="color: #60a5fa; font-size: 26px; margin: 10px 0;">€58,800</h2>
            </div>
        """,
        unsafe_allow_html=True,
    )

  st.write("")
  col_x, col_y = st.columns(2)
  with col_x:
    if st.button("⬅️ Back to Problem Statement"):
      st.session_state.section_id = 1
      st.rerun()
  with col_y:
    if st.button("Next: Validation Notice ➔"):
      st.session_state.section_id = 3
      st.rerun()

# --- SECTION 3: VALIDATION NOTICE & DASHBOARD ---
elif st.session_state.section_id == 3:
  st.markdown(
      """
        <div class="banner-box">
            <h1 style='color: #f8fafc; margin: 0; font-size: 32px;'>🔍 Validation Notice & Telemetry View</h1>
            <p style='color: #94a3b8; margin-top: 8px;'>Compliance summary and operational guidelines</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div class="content-box" style="border-left: 5px solid #3b82f6;">
            <h4 style='color: #60a5fa; margin-top: 0;'>Validation Notice:</h4>
            <p style='color: #cbd5e1; font-size: 15px; line-height: 1.5;'>
                These results utilize a retrospective proxy baseline and do not represent official ground-truth performance. 
                The financial metrics reflect simulated optimization under strict weekly constraints (exactly 15 gateways per week).
            </p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.write("")
  if st.button("⬅️ Back to Financial Impact"):
    st.session_state.section_id = 2
    st.rerun()
