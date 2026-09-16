
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="LPDG Innovation Hub",
    page_icon="🔌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Styling
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background: #06111f;
        color: #f4f7fb;
    }

    [data-testid="stSidebar"] {
        background: #07182b;
        border-right: 1px solid #18314d;
    }

    [data-testid="stSidebar"] * {
        color: #dce9f7;
    }

    .brand {
        font-size: 22px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 4px;
    }

    .brand span {
        color: #19b7ff;
    }

    .subtitle {
        color: #8ea6bf;
        font-size: 13px;
        margin-bottom: 20px;
    }

    .hero {
        padding: 34px 36px;
        border: 1px solid #173653;
        border-radius: 18px;
        background: linear-gradient(135deg, #0b2138 0%, #071525 65%, #08243a 100%);
        margin-bottom: 22px;
    }

    .hero h1 {
        font-size: 42px;
        margin: 0;
        color: white;
    }

    .hero h1 span {
        color: #19b7ff;
    }

    .hero p {
        color: #a8bdd2;
        max-width: 760px;
        font-size: 16px;
        line-height: 1.6;
    }

    .card {
        background: #0b1d31;
        border: 1px solid #183653;
        border-radius: 14px;
        padding: 18px;
        min-height: 105px;
    }

    .card-title {
        color: #89a4be;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.7px;
    }

    .card-value {
        color: white;
        font-size: 28px;
        font-weight: 800;
        margin-top: 8px;
    }

    .card-accent {
        color: #18c7b0;
    }

    .section-title {
        color: white;
        font-size: 20px;
        font-weight: 750;
        margin: 20px 0 10px 0;
    }

    .small-note {
        color: #7892ac;
        font-size: 12px;
    }

    .status {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        background: #0d493f;
        color: #48e6cc;
    }

    .footer {
        text-align: center;
        color: #607991;
        padding: 30px 0 10px 0;
        font-size: 12px;
    }

    div[data-testid="stMetric"] {
        background: #0b1d31;
        border: 1px solid #183653;
        border-radius: 14px;
        padding: 16px;
    }

    div[data-testid="stMetricLabel"] {
        color: #8ea6bf !important;
    }

    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
    }

    .stButton > button {
        background: #119eea;
        color: white;
        border: 0;
        border-radius: 8px;
        font-weight: 700;
    }

    .stButton > button:hover {
        background: #18b5ff;
        color: white;
    }

    .stTextInput input, .stSelectbox div {
        background: #0b1d31 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Data
# -----------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("predictions.csv")
        return df, True
    except Exception:
        # Demo data so the UI still works before predictions.csv exists.
        rng = np.random.default_rng(42)
        n = 120
        weeks = np.repeat(
            pd.date_range("2026-07-06", periods=8, freq="7D").strftime("%Y-%m-%d"),
            15
        )
        gateways = [f"GW-{i:04d}" for i in range(1, n + 1)]
        offline = rng.integers(20, 520, n)
        disconnect = rng.integers(0, 15, n)
        reboot = rng.integers(0, 9, n)
        risk = np.clip(
            0.35 * offline / 520
            + 0.35 * disconnect / 15
            + 0.30 * reboot / 9
            + rng.normal(0, 0.04, n),
            0, 1
        )
        df = pd.DataFrame({
            "week": weeks,
            "gateway_id": gateways,
            "offline_duration_sec": offline,
            "disconnection_cnt": disconnect,
            "reboot_cnt": reboot,
            "risk_score": risk,
        })
        df["priority"] = pd.cut(
            df["risk_score"],
            bins=[-0.01, 0.45, 0.70, 1.0],
            labels=["LOW", "MEDIUM", "HIGH"]
        )
        return df, False


df, real_data = load_data()

# Normalize likely column names from challenge output
rename_map = {}
for c in df.columns:
    lc = c.lower().strip()
    if lc in ["gateway", "gatewayid", "gateway_id", "gateway id"]:
        rename_map[c] = "gateway_id"
    elif lc in ["risk", "risk_score", "risk score", "score"]:
        rename_map[c] = "risk_score"
    elif lc in ["week", "week_start", "week_start_date"]:
        rename_map[c] = "week"
    elif lc in ["offline_duration_sec", "offline_duration", "offline duration"]:
        rename_map[c] = "offline_duration_sec"
    elif lc in ["disconnection_cnt", "disconnect_cnt", "disconnections"]:
        rename_map[c] = "disconnection_cnt"
    elif lc in ["reboot_cnt", "reboots", "reboot_count"]:
        rename_map[c] = "reboot_cnt"

df = df.rename(columns=rename_map)

required = [
    "gateway_id",
    "risk_score",
    "offline_duration_sec",
    "disconnection_cnt",
    "reboot_cnt",
]

for col in required:
    if col not in df.columns:
        if col == "gateway_id":
            df[col] = [f"GW-{i:04d}" for i in range(len(df))]
        else:
            df[col] = 0

if "week" not in df.columns:
    df["week"] = "Evaluation Week"

df["risk_score"] = pd.to_numeric(df["risk_score"], errors="coerce").fillna(0)
df["offline_duration_sec"] = pd.to_numeric(df["offline_duration_sec"], errors="coerce").fillna(0)
df["disconnection_cnt"] = pd.to_numeric(df["disconnection_cnt"], errors="coerce").fillna(0)
df["reboot_cnt"] = pd.to_numeric(df["reboot_cnt"], errors="coerce").fillna(0)

if "priority" not in df.columns:
    df["priority"] = pd.cut(
        df["risk_score"],
        bins=[-0.01, 0.45, 0.70, 1.0],
        labels=["LOW", "MEDIUM", "HIGH"]
    )

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown('<div class="brand">🔌 LPDG <span>Innovation Hub</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Gateway Visit Prioritization 2026</div>', unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Gateway Prioritization",
            "Gateway Explorer",
            "Analytics",
            "Cost & Impact",
            "Methodology",
        ],
        label_visibility="collapsed",
    )

    st.divider()
    if real_data:
        st.markdown("🟢 **Live Dataset Loaded**")
    else:
        st.markdown("🟡 **Demo Data Mode**")
        st.caption("Run ml_model.py to generate predictions.csv.")

# -----------------------------
# Helpers
# -----------------------------
def metric_card(title, value, accent=""):
    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">{title}</div>
            <div class="card-value {accent}">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def dark_chart(fig, height=330):
    fig.update_layout(
        template="plotly_dark",
        height=height,
        margin=dict(l=10, r=10, t=45, b=10),
        paper_bgcolor="#0b1d31",
        plot_bgcolor="#0b1d31",
        font=dict(color="#cfe0ef"),
        legend=dict(bgcolor="rgba(0,0,0,0)"),
    )
    return fig


# -----------------------------
# Dashboard
# -----------------------------
if page == "Dashboard":
    st.markdown("""
    <div class="hero">
        <h1>LPDG <span>Innovation Hub</span></h1>
        <h3 style="color:#dce9f7;">Gateway Visit Prioritization 2026</h3>
        <p>
        Machine learning and telemetry-driven analytics for prioritizing
        IoT gateway field visits, reducing operational cost, and improving
        network reliability.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Total Gateways", f"{df['gateway_id'].nunique():,}")
    with c2:
        metric_card("Weekly Visits", "15")
    with c3:
        metric_card("Optimized Cost", "€270,600", "card-accent")
    with c4:
        metric_card("Estimated Savings", "€58,800", "card-accent")

    st.markdown('<div class="section-title">Operational Overview</div>', unsafe_allow_html=True)

    left, right = st.columns([1.4, 1])

    with left:
        if len(df) > 0:
            weekly = df.groupby("week", dropna=False).size().reset_index(name="visits")
            weekly["baseline_cost"] = 329400 / max(len(weekly), 1)
            weekly["optimized_cost"] = 270600 / max(len(weekly), 1)

            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=weekly["week"],
                y=weekly["baseline_cost"],
                name="Baseline",
            ))
            fig.add_trace(go.Bar(
                x=weekly["week"],
                y=weekly["optimized_cost"],
                name="Optimized",
            ))
            fig.update_layout(
                title="Weekly Cost Comparison",
                barmode="group",
                yaxis_title="Cost (€)",
            )
            st.plotly_chart(dark_chart(fig), use_container_width=True)

    with right:
        priority_counts = df["priority"].astype(str).value_counts()
        fig = px.pie(
            values=priority_counts.values,
            names=priority_counts.index,
            hole=0.62,
            title="Gateway Risk Distribution",
        )
        st.plotly_chart(dark_chart(fig), use_container_width=True)

    st.markdown('<div class="section-title">Top Priority Gateways</div>', unsafe_allow_html=True)

    top = df.sort_values("risk_score", ascending=False).head(15).copy()
    top.insert(0, "Rank", range(1, len(top) + 1))
    top["Risk Score"] = top["risk_score"].round(3)
    top["Offline Duration"] = top["offline_duration_sec"].round(0).astype(int)
    top["Disconnections"] = top["disconnection_cnt"].round(0).astype(int)
    top["Reboots"] = top["reboot_cnt"].round(0).astype(int)

    st.dataframe(
        top[[
            "Rank", "gateway_id", "Risk Score",
            "Offline Duration", "Disconnections", "Reboots", "priority"
        ]].rename(columns={
            "gateway_id": "Gateway ID",
            "priority": "Priority"
        }),
        use_container_width=True,
        hide_index=True,
    )

# -----------------------------
# Gateway Prioritization
# -----------------------------
elif page == "Gateway Prioritization":
    st.title("Gateway Prioritization")
    st.caption("Weekly gateway ranking based on telemetry-derived risk.")

    weeks = sorted(df["week"].astype(str).unique().tolist())
    selected_week = st.selectbox("Select Evaluation Week", weeks)

    week_df = df[df["week"].astype(str) == selected_week].copy()
    week_df = week_df.sort_values("risk_score", ascending=False).head(15)
    week_df.insert(0, "Rank", range(1, len(week_df) + 1))

    st.info(f"Showing the top {len(week_df)} gateways for week: {selected_week}")

    display_df = week_df[[
        "Rank", "gateway_id", "risk_score",
        "offline_duration_sec", "disconnection_cnt",
        "reboot_cnt", "priority"
    ]].copy()

    display_df.columns = [
        "Rank", "Gateway ID", "Risk Score",
        "Offline Duration (sec)", "Disconnections",
        "Reboots", "Priority"
    ]

    st.dataframe(display_df, use_container_width=True, hide_index=True)

    fig = px.bar(
        week_df.sort_values("risk_score"),
        x="risk_score",
        y="gateway_id",
        orientation="h",
        title="Top 15 Gateway Risk Scores",
        labels={"risk_score": "Risk Score", "gateway_id": "Gateway ID"},
    )
    st.plotly_chart(dark_chart(fig), use_container_width=True)

# -----------------------------
# Gateway Explorer
# -----------------------------
elif page == "Gateway Explorer":
    st.title("Gateway Explorer")
    st.caption("Search and inspect an individual IoT gateway.")

    gateway_ids = df["gateway_id"].astype(str).unique().tolist()
    search = st.text_input("Search Gateway ID", placeholder="Example: GW-0001")

    if search:
        matches = [x for x in gateway_ids if search.lower() in x.lower()]
    else:
        matches = gateway_ids[:1]

    if matches:
        gateway = st.selectbox("Select Gateway", matches)
        g = df[df["gateway_id"].astype(str) == gateway].sort_values("week")

        latest = g.iloc[-1]

        a, b, c, d = st.columns(4)
        with a:
            metric_card("Risk Score", f"{latest['risk_score']:.3f}")
        with b:
            metric_card("Offline Duration", f"{latest['offline_duration_sec']:.0f}s")
        with c:
            metric_card("Disconnections", f"{latest['disconnection_cnt']:.0f}")
        with d:
            metric_card("Reboots", f"{latest['reboot_cnt']:.0f}")

        telemetry = g[[
            "week", "offline_duration_sec",
            "disconnection_cnt", "reboot_cnt"
        ]].copy()

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=telemetry["week"],
            y=telemetry["offline_duration_sec"],
            mode="lines+markers",
            name="Offline Duration",
        ))
        fig.add_trace(go.Scatter(
            x=telemetry["week"],
            y=telemetry["disconnection_cnt"],
            mode="lines+markers",
            name="Disconnections",
        ))
        fig.add_trace(go.Scatter(
            x=telemetry["week"],
            y=telemetry["reboot_cnt"],
            mode="lines+markers",
            name="Reboots",
        ))
        fig.update_layout(title=f"Telemetry Trend — {gateway}")
        st.plotly_chart(dark_chart(fig, 380), use_container_width=True)

        st.subheader("Gateway Records")
        st.dataframe(g, use_container_width=True, hide_index=True)
    else:
        st.warning("No matching gateway found.")

# -----------------------------
# Analytics
# -----------------------------
elif page == "Analytics":
    st.title("Analytics")
    st.caption("Telemetry trends and risk distribution.")

    c1, c2 = st.columns(2)

    with c1:
        trend = df.groupby("week", dropna=False)["offline_duration_sec"].mean().reset_index()
        fig = px.line(
            trend,
            x="week",
            y="offline_duration_sec",
            markers=True,
            title="Average Offline Duration",
        )
        st.plotly_chart(dark_chart(fig), use_container_width=True)

    with c2:
        trend = df.groupby("week", dropna=False)["disconnection_cnt"].mean().reset_index()
        fig = px.line(
            trend,
            x="week",
            y="disconnection_cnt",
            markers=True,
            title="Average Disconnection Count",
        )
        st.plotly_chart(dark_chart(fig), use_container_width=True)

    c3, c4 = st.columns(2)

    with c3:
        trend = df.groupby("week", dropna=False)["reboot_cnt"].mean().reset_index()
        fig = px.line(
            trend,
            x="week",
            y="reboot_cnt",
            markers=True,
            title="Average Reboot Count",
        )
        st.plotly_chart(dark_chart(fig), use_container_width=True)

    with c4:
        fig = px.histogram(
            df,
            x="risk_score",
            nbins=15,
            title="Risk Score Distribution",
        )
        st.plotly_chart(dark_chart(fig), use_container_width=True)

# -----------------------------
# Cost & Impact
# -----------------------------
elif page == "Cost & Impact":
    st.title("Cost & Impact")
    st.caption("Operational cost comparison under the challenge cost framework.")

    c1, c2, c3 = st.columns(3)
    with c1:
        metric_card("Baseline Cost", "€329,400")
    with c2:
        metric_card("Optimized ML Cost", "€270,600", "card-accent")
    with c3:
        metric_card("Estimated Savings", "€58,800", "card-accent")

    st.markdown('<div class="section-title">Cost Comparison</div>', unsafe_allow_html=True)

    cost_df = pd.DataFrame({
        "Scenario": ["Baseline", "Optimized ML"],
        "Cost": [329400, 270600],
    })

    fig = px.bar(
        cost_df,
        x="Scenario",
        y="Cost",
        text="Cost",
        title="Baseline vs Optimized Operational Cost",
    )
    fig.update_traces(texttemplate="€%{text:,}", textposition="outside")
    st.plotly_chart(dark_chart(fig, 400), use_container_width=True)

    left, right = st.columns(2)

    with left:
        st.markdown("""
        <div class="card">
            <div class="card-title">Challenge Cost Framework</div>
            <div style="font-size:18px;font-weight:700;margin-top:12px;">
                False Alarm: €380
            </div>
            <div style="font-size:18px;font-weight:700;margin-top:10px;">
                Missed Fault: €600
            </div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class="card">
            <div class="card-title">Weekly Constraint</div>
            <div class="card-value">15 Gateways / Week</div>
            <div class="small-note">Field intervention selection constraint</div>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------
# Methodology
# -----------------------------
elif page == "Methodology":
    st.title("About / Methodology")
    st.caption("How the LPDG Innovation Hub pipeline works.")

    cols = st.columns(4)

    steps = [
        ("01", "Telemetry Data", "Historical gateway telemetry is collected and prepared for analysis."),
        ("02", "Feature Engineering", "28-day rolling telemetry features capture recent gateway behavior."),
        ("03", "Risk Scoring", "Gateways are assigned a risk score using telemetry-derived indicators."),
        ("04", "Prioritization", "The highest-risk gateways are ranked and selected for weekly visits."),
    ]

    for col, (num, title, text) in zip(cols, steps):
        with col:
            st.markdown(
                f"""
                <div class="card" style="min-height:190px;">
                    <div style="color:#19b7ff;font-size:13px;font-weight:800;">{num}</div>
                    <div style="font-size:19px;font-weight:750;margin-top:12px;">{title}</div>
                    <div class="small-note" style="margin-top:12px;line-height:1.6;">{text}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown('<div class="section-title">Telemetry Features</div>', unsafe_allow_html=True)

    feature_df = pd.DataFrame({
        "Feature": [
            "offline_duration_sec",
            "disconnection_cnt",
            "reboot_cnt",
        ],
        "Meaning": [
            "Gateway offline duration",
            "Number of disconnection events",
            "Number of reboot events",
        ],
    })
    st.dataframe(feature_df, use_container_width=True, hide_index=True)

    st.markdown('<div class="section-title">Pipeline</div>', unsafe_allow_html=True)
    st.code(
        """Historical Telemetry
        ↓
Data Processing
        ↓
28-Day Rolling Features
        ↓
Risk Scoring
        ↓
Gateway Ranking
        ↓
Top 15 Gateways / Week
        ↓
predictions.csv
        ↓
Validation + Dashboard""",
        language="text",
    )

st.markdown(
    '<div class="footer">LPDG Innovation Hub • Gateway Visit Prioritization 2026 • ML + IoT Telemetry Analytics</div>',
    unsafe_allow_html=True,
)
