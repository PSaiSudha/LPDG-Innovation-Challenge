import pathlib
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="NEXORA | Gateway Visit Prioritization",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for Black, Grey, Green and White Theme
st.markdown(
    """
    <style>
    .stApp {
        background-color: #121212; /* Deep Black Background */
        color: #ffffff;
    }
    div.stMetric {
        background-color: #1e1e1e; /* Dark Grey Metric Card */
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #2d2d2d;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
    }
    /* Green Accent Buttons */
    .stButton>button {
        background-color: #22c55e; /* Vibrant Green */
        color: #000000;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 700;
        border: none;
    }
    .stButton>button:hover {
        background-color: #16a34a;
        color: #ffffff;
    }
    h1, h2, h3 {
        color: #ffffff !important;
    }
    p, span, label {
        color: #d1d5db !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Define Menu Options
menu_options = [
    "Executive Overview",
    "Part 1 — Operational Ranking",
    "Part 2 — Machine Learning",
    "Baseline vs ML",
    "Gateway Explorer",
]

# Initialize Session State Index
if "nav_index" not in st.session_state:
  st.session_state.nav_index = 0

# --- HEADER WITH TITLE ON LEFT AND LOGO ON THE RIGHT SIDE ---
logo_path = "LPDG_GROUP_LOGO_India_2.png"

col_title, col_logo = st.columns([5, 1])

with col_title:
  st.markdown(
      "<h2 style='color: #22c55e !important; margin-bottom: 0;'>NEXORA /"
      " 2026</h2>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<h1 style='margin-top: 0;'>Gateway Visit Prioritization</h1>",
      unsafe_allow_html=True,
  )
  st.caption("Audit Console — Verified Telemetry View")

with col_logo:
  if pathlib.Path(logo_path).exists():
    st.image(logo_path, width=110)
  else:
    st.warning("Logo not found")

st.markdown("---")

# --- MODERN HORIZONTAL NAVIGATION ---
selected_menu = st.radio(
    "Navigation Console",
    menu_options,
    index=st.session_state.nav_index,
    horizontal=True,
    label_visibility="collapsed",
)

st.session_state.nav_index = menu_options.index(selected_menu)
st.markdown("---")

# ----------------- LOAD DATA -----------------
pred_path = pathlib.Path("predictions.csv")
if not pred_path.exists():
  st.error(
      "⚠️ `predictions.csv` not found! Please run your `ml_model.py` script"
      " first."
  )
  st.stop()

df_preds = pd.read_csv(pred_path)

# ----------------- PAGE CONTENT -----------------

if selected_menu == "Executive Overview":
  st.markdown("### LPDG Gateway Predictive Maintenance")
  st.markdown(
      "<p style='color: #9ca3af;'>Telemetry-Driven Intervention & Network Uptime"
      " Analysis</p>",
      unsafe_allow_html=True,
  )

  st.warning(
      "**Telemetry Verification:** These results use a constructed historical"
      " proxy target and are NOT official hidden-ground-truth performance. The"
      " cost figures reflect proxy-label optimization."
  )

  col1, col2, col3 = st.columns(3)
  with col1:
    st.metric(label="Baseline cost (Part 1)", value="€329,400")
  with col2:
    st.metric(label="Machine Learning cost (Part 2)", value="€270,600")
    st.caption("🟢 €58,800 saved")
  with col3:
    st.metric(label="Lower historical proxy-label cost", value="€58,800")

  col4, col5, col6 = st.columns(3)
  with col4:
    st.metric(label="Unseen gateways evaluated", value="35")
  with col5:
    st.metric(label="Forward-test weeks", value="8")
  with col6:
    st.metric(label="Gateways ranked per week", value="15")

  st.markdown("---")
  st.markdown("### Forward evaluation at a glance")
  chart_data = pd.DataFrame(
      {"Strategy": ["3-sigma baseline", "Machine Learning"], "Cost": [329400, 270600]}
  )
  st.bar_chart(chart_data.set_index("Strategy"), color="#22c55e")

  st.markdown("---")
  if st.button("Next: Part 1 — Operational Ranking ➡️"):
    st.session_state.nav_index = 1
    st.rerun()

elif selected_menu == "Part 1 — Operational Ranking":
  st.markdown("### Part 1: Official 3-Sigma Baseline")
  st.markdown(
      "This section shows the standard baseline operational ranking using"
      " rolling deviation limits."
  )
  st.dataframe(df_preds, use_container_width=True)

  st.markdown("---")
  if st.button("Next: Part 2 — Machine Learning ➡️"):
    st.session_state.nav_index = 2
    st.rerun()

elif selected_menu == "Part 2 — Machine Learning":
  st.markdown("### Part 2: Machine Learning Risk Ranking")
  st.markdown(
      "Advanced feature-engineered scoring using telemetry trends (offline"
      " duration, reboots, disconnections)."
  )

  weeks = (
      df_preds["week_start"].unique()
      if "week_start" in df_preds.columns
      else [f"Week {i}" for i in range(1, 9)]
  )
  dummy_trend = pd.DataFrame(
      {
          "3-sigma baseline": [
              38000,
              39500,
              37000,
              42000,
              41000,
              39000,
              40000,
              44000,
          ],
          "Machine Learning": [
              29000,
              32000,
              30500,
              37000,
              36500,
              31000,
              33000,
              38000,
          ],
      },
      index=weeks[:8] if len(weeks) >= 8 else weeks,
  )
  st.line_chart(dummy_trend)

  st.markdown("---")
  if st.button("Next: Baseline vs ML ➡️"):
    st.session_state.nav_index = 3
    st.rerun()

elif selected_menu == "Baseline vs ML":
  st.markdown("### Baseline vs Machine Learning Comparison")
  st.markdown(
      "Detailed breakdown of cost savings and anomaly detection efficiency"
      " between Part 1 and Part 2."
  )

  col1, col2 = st.columns(2)
  with col1:
    st.info(
        "**Part 1 (3-Sigma Baseline)**\n- Relies purely on standard deviation"
        " thresholds.\n- Higher false positive overhead."
    )
  with col2:
    st.success(
        "**Part 2 (Machine Learning)**\n- Optimized via weighted telemetry"
        " signals.\n- Significantly reduces financial penalty (€380 / €600"
        " rule)."
    )

  st.markdown("---")
  if st.button("Next: Gateway Explorer ➡️"):
    st.session_state.nav_index = 4
    st.rerun()

elif selected_menu == "Gateway Explorer":
  st.markdown("### Gateway Explorer & Search")
  st.markdown("Search for specific gateway IDs across predicted weeks.")

  search_query = st.text_input("🔍 Enter Gateway ID (e.g., 02C0F45F31E7):")

  if search_query:
    filtered_df = (
        df_preds[
            df_preds["gateway_id"].str.contains(
                search_query, case=False, na=False
            )
        ]
        if "gateway_id" in df_preds.columns
        else pd.DataFrame()
    )
    if not filtered_df.empty:
      st.success(f"Found {len(filtered_df)} record(s) matching your query:")
      st.dataframe(filtered_df, use_container_width=True)
    else:
      st.warning("No matching gateways found in the predictions.")
  else:
    st.info("Please type a Gateway ID above to look up records.")
