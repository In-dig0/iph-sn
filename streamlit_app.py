import streamlit as st
from browser_detection import browser_detection_engine
from language_detection import detect_browser_language
from streamlit_pdf_viewer import pdf_viewer

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
    
    # https://iph-sn-ep33nvbuic6zbq7uqvbxbm.streamlit.app/?sn=25007677

    # st.info(f"Product number: {st.query_params["pn"]}", icon="ℹ️")
    # st.info(f"Serial number: {st.query_params["sn"]}", icon="ℹ️")

    st.info(f"{st.query_params}")

    st.sidebar.image("https://iph.it/wp-content/uploads/2020/02/logo-scritta.png", width=140)
    st.title(f":blue[IPH Specification Sheet Portal]")

    sn_list = ["25007676", "25007677"]
    pn_list = ["5C1440154403AN", "5F1370116301AN"]
    desc_list = ["5C-04870-154-4-M0343-0000N", "5F-03450-116-3-M1460-0000N"]
    
    
    sn = st.query_params.get('sn', None)
    if sn is None:
        st.error("**ERROR:** URL doesn't containt serial number. Add '?sn=SERIAL_NUMBER' to the URL.")
        st.stop()
    if sn not in sn_list:
        st.error(f"**ERROR:** Serial number {sn} does not exists!")
        st.stop()

    with st.container(border=True):   
        obj_idx = sn_list.index(st.query_params['sn'])
        serial_nr = st.selectbox(
            label="Serial number:",
            options=sn_list,
            index=sn_list.index(st.query_params['sn']),
            disabled=True
        )

        product_nr = st.text_input(
            label="Product number:",
            value=pn_list[obj_idx],
            disabled=True
        )

        product_desc = st.text_input(
            label="Product description:",
            value=desc_list[obj_idx],
            disabled=True
        )

        download_button = st.button(
            label="Download Tech Sheet",
            type="primary",
            disabled=False
        )

        if download_button:
            # pdf_filename = f"FIG-{product_nr}.pdf" 
            # pdf_fileobj = f"files/{pdf_filename}"
            # st.write(pdf_fileobj)
            # pdf_viewer(pdf_fileobj)
            # Aggiungi il pulsante di download
            
            pdf_filename = f"FIG-{product_nr}.pdf" 
            #pdf_buffer = modules.servant.create_pdf_buffer(df_out)
            st.download_button(
                label="Download PDF",
                data=f"files/{pdf_filename}"
                file_name=file_name,
                mime="application/pdf",
                key="download-pdf",
                help="Download PDF",
                type="primary",
                icon=":material/download:"
            )            
   

if __name__ == "__main__":
    main()
