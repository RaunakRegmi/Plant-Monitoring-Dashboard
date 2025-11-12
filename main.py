import streamlit as st
import time
from datetime import datetime
import random

# Page configuration with white theme
st.set_page_config(
    page_title="Plant Monitoring Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for white background and compact layout
st.markdown("""
    <style>
    .stApp {
        background-color: white;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'plant1_relay1' not in st.session_state:
    st.session_state.plant1_relay1 = False
if 'plant1_relay2' not in st.session_state:
    st.session_state.plant1_relay2 = False
if 'plant2_relay1' not in st.session_state:
    st.session_state.plant2_relay1 = False
if 'plant2_relay2' not in st.session_state:
    st.session_state.plant2_relay2 = False
if 'captured_image' not in st.session_state:
    st.session_state.captured_image = None

# Title
st.title("🌱 Plant Monitoring Dashboard")

# Camera and Plants in one row
camera_col, plant1_col, plant2_col = st.columns([1, 1, 1])

# ============ CAMERA SECTION ============
with camera_col:
    st.header("📸 Live Camera Viewer")
    camera_image = st.camera_input("Scan Plant", key="camera")

    if camera_image is not None:
        st.session_state.captured_image = camera_image
        st.success("✓ Image captured successfully!")
        st.info(f"Captured at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ============ PLANT 1 SECTION ============
with plant1_col:
    st.header("🪴 Plant 1")

    with st.expander("Plant 1 Controls", expanded=True):

        # Soil Moisture Check
        st.subheader("💧 Soil Moisture")
        if st.button("Check Soil Moisture - Plant 1", key="p1_moisture"):
            with st.spinner("Reading sensor..."):
                time.sleep(1)
                moisture = random.randint(30, 80)
                st.success(f"Soil Moisture: {moisture}%")

                if moisture < 40:
                    st.warning("⚠️ Low moisture - Consider watering")
                elif moisture > 70:
                    st.info("✓ Optimal moisture level")
                else:
                    st.info("✓ Good moisture level")

        st.divider()

        # Waterproof Sensor
        st.subheader("🌊 Waterproof Sensor")
        if st.button("Check Waterproof Status - Plant 1", key="p1_waterproof"):
            with st.spinner("Checking sensor..."):
                time.sleep(1)
                waterproof_status = random.choice([True, False])
                if waterproof_status:
                    st.success("✓ Waterproof sensor: OK")
                else:
                    st.error("✗ Waterproof sensor: Issue detected")

        st.divider()

        # Relay Controls
        st.subheader("🔌 Relay Controls")

        col_r1, col_r2 = st.columns(2)

        with col_r1:
            if st.button("Toggle Relay 1", key="p1_r1_toggle"):
                st.session_state.plant1_relay1 = not st.session_state.plant1_relay1

            if st.session_state.plant1_relay1:
                st.success("Relay 1: ON 🟢")
            else:
                st.error("Relay 1: OFF 🔴")

        with col_r2:
            if st.button("Toggle Relay 2", key="p1_r2_toggle"):
                st.session_state.plant1_relay2 = not st.session_state.plant1_relay2

            if st.session_state.plant1_relay2:
                st.success("Relay 2: ON 🟢")
            else:
                st.error("Relay 2: OFF 🔴")

# ============ PLANT 2 SECTION ============
with plant2_col:
    st.header("🪴 Plant 2")

    with st.expander("Plant 2 Controls", expanded=True):

        # Soil Moisture Check
        st.subheader("💧 Soil Moisture")
        if st.button("Check Soil Moisture - Plant 2", key="p2_moisture"):
            with st.spinner("Reading sensor..."):
                time.sleep(1)
                moisture = random.randint(30, 80)
                st.success(f"Soil Moisture: {moisture}%")

                if moisture < 40:
                    st.warning("⚠️ Low moisture - Consider watering")
                elif moisture > 70:
                    st.info("✓ Optimal moisture level")
                else:
                    st.info("✓ Good moisture level")

        st.divider()

        # Waterproof Sensor
        st.subheader("🌊 Waterproof Sensor")
        if st.button("Check Waterproof Status - Plant 2", key="p2_waterproof"):
            with st.spinner("Checking sensor..."):
                time.sleep(1)
                waterproof_status = random.choice([True, False])
                if waterproof_status:
                    st.success("✓ Waterproof sensor: OK")
                else:
                    st.error("✗ Waterproof sensor: Issue detected")

        st.divider()

        # Relay Controls
        st.subheader("🔌 Relay Controls")

        col_r1, col_r2 = st.columns(2)

        with col_r1:
            if st.button("Toggle Relay 1", key="p2_r1_toggle"):
                st.session_state.plant2_relay1 = not st.session_state.plant2_relay1

            if st.session_state.plant2_relay1:
                st.success("Relay 1: ON 🟢")
            else:
                st.error("Relay 1: OFF 🔴")

        with col_r2:
            if st.button("Toggle Relay 2", key="p2_r2_toggle"):
                st.session_state.plant2_relay2 = not st.session_state.plant2_relay2

            if st.session_state.plant2_relay2:
                st.success("Relay 2: ON 🟢")
            else:
                st.error("Relay 2: OFF 🔴")

# Footer
st.divider()
st.caption(f"Dashboard Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")