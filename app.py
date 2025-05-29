import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page settings
st.set_page_config(page_title="Purple Group QB Analytics", layout="centered")

# Title and subtitle
st.title("Purple Group QB Analytics")
st.markdown("### Human Equation Evaluation: Bo Nix")

# Input sliders
prs = st.slider("Pressure Response Score (PRS)", 0, 100, 88)
confidence = st.slider("Confidence Curve Peak", 0, 100, 84)
radiance = st.slider("Radiance Index", 0, 100, 83)
legacy_fit = st.slider("Legacy Fit %", 0, 100, 89)
focus_inverse = st.slider("Focus Drift Index (Inverse)", 0, 100, 88)

# Store values in a dictionary
metrics = {
    "PRS": prs,
    "Confidence": confidence,
    "Radiance": radiance,
    "Legacy Fit": legacy_fit,
    "Focus (Inverse)": focus_inverse
}

# Display metric table
st.subheader("Player Metric Summary")
st.dataframe(pd.DataFrame.from_dict(metrics, orient='index', columns=['Score']))

# Radar chart setup
st.subheader("Graphical Evaluation")
categories = list(metrics.keys())
values = list(metrics.values())
values += values[:1]  # Loop back to first value

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Plot data
ax.plot(angles, values, linewidth=2, linestyle='solid')
ax.fill(angles, values, 'purple', alpha=0.25)
ax.set_thetagrids(np.degrees(angles[:-1]), categories)
ax.set_title("Bo Nix Human Equation Radar Chart")

# Display chart
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("**Developed by Purple Group Co** — Rooted in Soul. Built with Vision.")
