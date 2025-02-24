import streamlit as st


def main():
    st.title("Current user session:")
    st.context.cookies
    st.context.headers

    st.title("Query parameters in app's URL")
    st.query_params

    # Example:
    # https://your_app.streamlit.app/?first_key=1&second_key=two
    
    # https://iph-sn-ep33nvbuic6zbq7uqvbxbm.streamlit.app/?sn=25007677

if __name__ == "__main__":
    main()
