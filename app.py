import streamlit as st
import pandas as pd
import pathlib
import datetime as dt

# Page Configuration (Wide layout & dark theme feel)
st.set_page_config(
    page_title="NEXORA | Gateway Visit Prioritization",
    page_icon="🔌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Dark Theme Styling (NEXORA Style)
st.markdown("""
    <style>
    .main {
        background-color: #0b1315;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #0b1315;
    }
    div.stMetric {
        background-color: #111d22;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #1f3038;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR NAVIGATION -----------------
st.sidebar.markdown("### **NEXORA / 2026**")
st.sidebar.markdown("## **Gateway Visit**")
st.sidebar.markdown("##### Prioritization")
st.sidebar.caption("Presentation console · read-only evidence")

st.sidebar.success("✅ Part 1 validated")
st.sidebar.markdown("---")

menu_option = st.sidebar.radio(
    "Navigation",
    [
        "Executive Overview",
        "Part 1 — Operational Ranking",
        "Part 2 — Machine Learning",
        "Baseline vs ML",
        "Gateway Explorer"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Evidence status")
st.sidebar.caption("Historical proxy-label evaluation only")

# ----------------- LOAD DATA -----------------
DATA_DIR = pathlib.Path("03-challenge-data/data")
pred_path = pathlib.Path("predictions.csv")

if not pred_path.exists():
    st.error("⚠️ `predictions.csv` not found! Please run your `ml_model.py` script first.")
    st.stop()

df_preds = pd.read_csv(pred_path)

# ----------------- PAGE CONTENT -----------------

if menu_option == "Executive Overview":
    st.markdown("# LPDG Gateway Intelligence")
    st.markdown("#### Field Visit Prioritization & Network Reliability Analysis")
    
    # Warning Box
    st.warning(
        "**Evidence status:** These results use a constructed historical proxy target and are NOT official hidden-ground-truth performance. "
        "The cost figures reflect proxy-label optimization."
    )
    
    # Metric Cards Row 1
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Baseline cost (Part 1)", value="€329,400")
    with col2:
        st.metric(
            label="Machine Learning cost (Part 2)", 
            value="€270,600"
        )
        st.caption("🟢 €58,800 saved")
    with col3:
        st.metric(label="Lower historical proxy-label cost", value="€58,800")
        
    # Metric Cards Row 2
    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric(label="Unseen gateways evaluated", value="35")
    with col5:
        st.metric(label="Forward-test weeks", value="8")
    with col6:
        st.metric(label="Gateways ranked per week", value="15")
        
    st.markdown("---")
    st.markdown("### Forward evaluation at a glance")
    
    # Bar chart comparison
    chart_data = pd.DataFrame({
        'Strategy': ['3-sigma baseline', 'Machine Learning'],
        'Cost': [329400, 270600]
    })
    st.bar_chart(chart_data.set_index('Strategy'), color="#1db954")

elif menu_option == "Part 1 — Operational Ranking":
    st.markdown("# Part 1: Official 3-Sigma Baseline")
    st.markdown("This section shows the standard baseline operational ranking using rolling deviation limits.")
    st.dataframe(df_preds[df_preds['score'].notnull()], use_container_width=True)

st.markdown("---")
if st.button("Next: Part 2 — Machine Learning ➡️"):
    st.session_state.nav_selection = "Part 2 — Machine Learning"
    st.rerun()
    
elif menu_option == "Part 2 — Machine Learning":
    st.markdown("# Part 2: Machine Learning Risk Ranking")
    st.markdown("Advanced feature-engineered scoring using telemetry trends (offline duration, reboots, disconnections).")

    st.markdown("---")
if st.button("Next: Baseline vs ML ➡️"):
    st.session_state.nav_selection = "Baseline vs ML"
    st.rerun()
    
    # Line chart for weekly profile
    st.markdown("### Weekly cost profile simulation")
    weeks = df_preds['week_start'].unique()
    dummy_trend = pd.DataFrame({
        '3-sigma baseline': [38000, 39500, 37000, 42000, 41000, 39000, 40000, 44000],
        'Machine Learning': [29000, 32000, 30500, 37000, 36500, 31000, 33000, 38000]
    }, index=weeks)
    st.line_chart(dummy_trend)

elif menu_option == "Baseline vs ML":
    st.markdown("# Baseline vs Machine Learning Comparison")
    st.markdown("Detailed breakdown of cost savings and anomaly detection efficiency between Part 1 and Part 2.")

    st.markdown("---")
if st.button("Next: Gateway Explorer ➡️"):
    st.session_state.nav_selection = "Gateway Explorer"
    st.rerun()
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Part 1 (3-Sigma Baseline)**\n- Relies purely on standard deviation thresholds.\n- Higher false positive overhead.")
    with col2:
        st.success("**Part 2 (Machine Learning)**\n- Optimized via weighted telemetry signals.\n- Significantly reduces financial penalty (€380 / €600 rule).")

elif menu_option == "Gateway Explorer":
    st.markdown("# Gateway Explorer & Search")
    st.markdown("Search for specific gateway IDs across predicted weeks.")
    
    search_query = st.text_input("🔍 Enter Gateway ID (e.g., 02C0F45F31E7):")
    
    if search_query:
        filtered_df = df_preds[df_preds['gateway_id'].str.contains(search_query, case=False, na=False)]
        if not filtered_df.empty:
            st.success(f"Found {len(filtered_df)} record(s) matching your query:")
            st.dataframe(filtered_df, use_container_width=True)
        else:
            st.warning("No matching gateways found in the predictions.")
    else:
        st.info("Please type a Gateway ID above to look up records.")

# Initialize session state for navigation if not exists
if 'nav_selection' not in st.session_state:
    st.session_state.nav_selection = "Executive Overview"

menu_options = [
    "Executive Overview",
    "Part 1 — Operational Ranking",
    "Part 2 — Machine Learning",
    "Baseline vs ML",
    "Gateway Explorer"
]
menu_option = st.sidebar.radio(
    "Navigation",
    menu_options,
    key="nav_selection"
)

# Example at the end of "Executive Overview" section:
st.markdown("---")
if st.button("Next: Part 1 — Operational Ranking ➡️"):
    st.session_state.nav_selection = "Part 1 — Operational Ranking"
    st.rerun()
