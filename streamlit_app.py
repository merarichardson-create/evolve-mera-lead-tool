import streamlit as st
import asyncio
from lead_scanner import scan_leads

st.set_page_config(page_title="Lead Scanner", layout="wide")
st.title("🎯 Lead Generation Scanner")
st.write("Scan Airbnb host profiles to identify potential leads with property information.")

st.divider()

# Input section
st.subheader("📝 Input Host URLs")
col1, col2 = st.columns([3, 1])
with col1:
    urls_input = st.text_area(
        "Enter Airbnb host profile URLs (one per line):",
        height=150,
        placeholder="https://www.airbnb.com/users/show/123456789\nhttps://www.airbnb.com/users/show/987654321"
    )
with col2:
    st.write("")
    st.write("")
    scan_button = st.button("🚀 Scan Leads", use_container_width=True)

st.divider()

# Process URLs
if scan_button:
    if not urls_input.strip():
        st.error("Please enter at least one URL to scan.")
    else:
        urls = [url.strip() for url in urls_input.split('\n') if url.strip()]
        st.info(f"Scanning {len(urls)} host profile(s)... This may take a few minutes.")
        
        try:
            with st.spinner("🔍 Scanning profiles..."):
                results_df = asyncio.run(scan_leads(urls))
            
            if len(results_df) > 0:
                st.success(f"✅ Found {len(results_df)} leads!")
                
                # Display results
                st.subheader("📊 Results")
                st.dataframe(results_df, use_container_width=True)
                
                # Export options
                col1, col2 = st.columns(2)
                with col1:
                    csv = results_df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download CSV",
                        data=csv,
                        file_name="leads.csv",
                        mime="text/csv"
                    )
                with col2:
                    xlsx = results_df.to_excel(index=False, engine='openpyxl')
                    st.download_button(
                        label="📥 Download Excel",
                        data=xlsx,
                        file_name="leads.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
            else:
                st.warning("⚠️ No leads found. The profiles may not match the target criteria.")
                
        except Exception as e:
            st.error(f"❌ Error during scanning: {str(e)}")
            st.write("Please check your URLs and try again.")
