import streamlit as st
from browser_detection import browser_detection_engine

def main():
    st.title("Current user session:")
    st.subheader("Cookies:")
    st.context.cookies
<<<<<<< HEAD
    
    st.title("Current context headers:")    
=======
    st.subheader("Contest header:")
>>>>>>> 9853473c31538d5743aadc2a8ef00fd997f96ecd
    st.context.headers
    
    st.title("Browser detection engine:") 
    value = browser_detection_engine()
    st.write(value)

    st.title("Query parameters in app's URL")
    st.query_params

    # Example:
    # https://your_app.streamlit.app/?first_key=1&second_key=two
    
    # https://iph-sn-ep33nvbuic6zbq7uqvbxbm.streamlit.app/?sn=25007677&pn=5C1440154403AN

if __name__ == "__main__":
    main()
