import streamlit as st


def main():
    st.title("Current user session:")
    st.subheader("Cookies:")
    st.context.cookies
    st.subheader("Contest header:")
    st.context.headers

    st.title("Query parameters in app's URL")
    st.query_params

    # Example:
    # https://your_app.streamlit.app/?first_key=1&second_key=two
    
    # https://iph-sn-ep33nvbuic6zbq7uqvbxbm.streamlit.app/?sn=25007677&pn=5C1440154403AN

if __name__ == "__main__":
    main()
