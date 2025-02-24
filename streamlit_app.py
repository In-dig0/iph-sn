import streamlit as st
from browser_detection import browser_detection_engine
from language_detection import detect_browser_language

def main():
    # st.title("Current user session:")
    # st.subheader("Cookies:")
    # st.context.cookies
    
    # st.title("Current context headers:")    
    # st.context.headers
    
    # st.title("Browser detection engine:") 
    # value = browser_detection_engine()
    # st.write(value)

    # st.title("Browser language:") 
    # browser_language = detect_browser_language()
    # # Display the detected language for debugging
    # st.write(f"Detected browser language: {browser_language}")


    # st.title("Query parameters in app's URL")
    # st.query_params

    # Example:
    # https://your_app.streamlit.app/?first_key=1&second_key=two
    
    # https://iph-sn-ep33nvbuic6zbq7uqvbxbm.streamlit.app/?sn=25007677&pn=5C1440154403AN

    st.info(f"Product number: {st.query_params["pn"]}", icon="ℹ️")
    st.info(f"Serial number: {st.query_params["sn"]}", icon="ℹ️")

    pn_dict = {"pn_code": ["5F1370116301AN", "5C1440154403AN"]}
    sn_dict = {"sn_code": ["25007676", "25007677"]}
    desc_dict = {"desc_art": ["5F-03450-116-3-M1460-0000N", "5C-04870-154-4-M0343-0000N"]}

    st.selectbox(
        label="Product number:",
        options=pn_dict.items(),
        index=pn_dict.index(st.query_params["pn"]),
        disabled=False
    )

if __name__ == "__main__":
    main()
