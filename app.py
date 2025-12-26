import streamlit as st
import json
import base64
from src.llm.analyzer import InvestmentAnalyzer

# Page configuration
st.set_page_config(page_title="Golden Mile - Investment AI", layout="wide")

@st.cache_resource
def get_analyzer():
    # Replace with your actual token or use environment variables
    return InvestmentAnalyzer(hf_api_key="<hugging_face_api_key>")

analyzer = get_analyzer()

st.title("Golden Mile: Property Investment Analyst")
st.markdown("---")

# --- LEFT SIDEBAR: INPUTS ---
st.sidebar.header("Property Details")
location = st.sidebar.text_input("Location", value="Indiranagar")
p_type = st.sidebar.selectbox("Property Type", ["Apartment", "Villa"])
sqft = st.sidebar.number_input("Total Sqft", value=1200, step=30)
bhk = st.sidebar.slider("BHK", 1, 10, 2)
bath = st.sidebar.slider("Bathrooms", 1, 10, 2)
amenities = st.sidebar.slider("Amenities Score (1-10)", 1, 10, 9)

if st.sidebar.button("Analyze Investment", type="primary"):
    with st.spinner("Analyzing market data and generating AI insights..."):
        # Prepare data
        property_data = {
            "location": location,
            "total_sqft": sqft,
            "bhk": bhk,
            "bath": bath,
            "property_type": p_type,
            "amenities_score": amenities
        }
        
        # Run the full pipeline
        result = analyzer.analyze_property(property_data)
        
        if result.get("success"):
            # --- RIGHT SIDE: RESULTS ---
            col1, col2 = st.columns(2)
            
            ml = result["ml_prediction"]
            inv = result["investment_analysis"]
            
            with col1:
                st.subheader("Price Prediction")
                st.metric("Predicted Price", f"₹{ml['predicted_total_price']:,.0f}")
                st.caption(f"Price per sqft: ₹{ml['predicted_price_per_sqft']:,.0f}")

            with col2:
                st.subheader("Rental Insights")
                st.metric("Est. Annual Yield", f"{ml['estimated_annual_yield_pct']}%")
                st.caption(f"Monthly Rent: ₹{ml['estimated_monthly_rent']:,.0f}")

            st.markdown("---")
            st.subheader("AI Investment Analysis")

            # Create three tabs for a cleaner organization
            tab1, tab2, tab3 = st.tabs(["Key Drivers", "Risk Factors", "Verdict"])

            with tab1:
                drivers = inv.get("key_drivers", [])
                if isinstance(drivers, list):
                    for item in drivers:
                        st.markdown(f"**•** {item}")
                else:
                    st.write(drivers)

            with tab2:
                risks = inv.get("risk_factors", [])
                if isinstance(risks, list):
                    for item in risks:
                        st.markdown(f"**•** {item}")
                else:
                    st.write(risks)

            with tab3:
                # Use columns for a "Scorecard" look
                v_col1, v_col2 = st.columns(2)
                
                recommendation = inv.get("recommendation", "N/A")
                confidence = inv.get("confidence", "Low").capitalize()
                
                with v_col1:
                    st.markdown("**Recommendation**")
                    if recommendation.lower() == "buy":
                        st.success(f"{recommendation.upper()}")
                    else:
                        st.warning(f"{recommendation.upper()}")
                        
                with v_col2:
                    st.markdown("**Confidence Level**")
                    st.info(f"{confidence}")
            # --- DOWNLOAD SECTION ---
            st.markdown("### Detailed Report")
            full_report = json.dumps(result, indent=2)
            b64 = base64.b64encode(full_report.encode()).decode()
            href = f'<a href="data:file/json;base64,{b64}" download="GoldenMile_Report_{location}.json">Download Full JSON Report</a>'
            st.markdown(href, unsafe_allow_html=True)
            
        else:
            st.error(f"Analysis Failed: {result.get('error')}")
