import streamlit as st
from browser_detection import browser_detection_engine
from language_detection import detect_browser_language
from streamlit_pdf_viewer import pdf_viewer
import os
import base64

# Funzione per leggere e codificare il file
def get_binary_file_downloader_html(file_path, file_label):
    with open(file_path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    return st.download_button(
        label=file_label,
        data=data,
        file_name=os.path.basename(file_path),
        mime="application/pdf",
        key="download-pdf",
        icon=":material/download:"
    )


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

    #st.info(f"{st.query_params}")

    st.sidebar.image("https://iph.it/wp-content/uploads/2020/02/logo-scritta.png", width=140)

    st.title(f":blue[IPH Specification Sheet Portal]")

    sn_list = ["25007676", "25007677"]
    pn_list = ["5C1440154403AN", "5F1370116301AN"]
    desc_list = ["5C-04870-154-4-M0343-0000N", "5F-03450-116-3-M1460-0000N"]
    
    
    sn = st.query_params.get('sn', None)
    if sn is None:
        st.error("**ERROR: URL doesn't containt serial number. Add '?sn=SERIAL_NUMBER' to the URL.")
        st.stop()
    if sn not in sn_list:
        st.error(f"**ERROR: Serial number {sn} does not exists!")
        st.stop()

    st.subheader(f":grey[Product section]")
    with st.expander("Device browser info"):
        value = browser_detection_engine()
        st.write(value)
    with st.container(border=True):   
        obj_idx = sn_list.index(st.query_params['sn'])
        serial_nr = st.selectbox(
            label=":orange[Serial number]",
            options=sn_list,
            index=sn_list.index(st.query_params['sn']),
            disabled=True
        )

        product_nr = st.text_input(
            label=":orange[Product number]",
            value=pn_list[obj_idx],
            disabled=True
        )

        product_desc = st.text_input(
            label=":orange[Product description]",
            value=desc_list[obj_idx],
            disabled=True
        )
    
    st.subheader(f":grey[Attachment section]")  
    with st.container(border=True):  
        #browser_detected_language = detect_browser_language().strip()
        #st.write(type(browser_detected_language))
        #browser_language_option = 
        language = st.selectbox(
            label=":orange[Language]",
            options=['it','en'],
            index=browser_language_option.index(detect_browser_language()),
            #index=None,
            disabled=False
        )

        attachment_type = st.selectbox(
            label=":orange[Attachment type]",
            options=['Specification sheet','Other'],
            index=0,
            disabled=False
        )

        search_button = st.button(
            label="Search",
            type="primary",
            disabled=False,
            icon=":material/search:"
        )

    if search_button:
        if attachment_type == 'Specification sheet':
            pdf_filename = f"FIG-{product_nr}.pdf"
        # Percorso relativo alla cartella files
            pdf_path = os.path.join("files", pdf_filename)
        
            try:
                # Verifica se il file esiste
                if os.path.exists(pdf_path):
                    st.success(f"File found: {pdf_path}")
                    # Utilizza la funzione di download
                    get_binary_file_downloader_html(pdf_path, "PDF Download")
                else:
                    st.error(f"File not found: {pdf_path}")
            except Exception as e:
                st.error(f"**ERROR reading the PDF file: {e}")
        elif attachment_type == 'Other':
            pdf_filename = f"OTH-{product_nr}.pdf"
        # Percorso relativo alla cartella files
            pdf_path = os.path.join("files", pdf_filename)
        
            try:
                # Verifica se il file esiste
                if os.path.exists(pdf_path):
                    st.success(f"File found: {pdf_path}")
                    # Utilizza la funzione di download
                    get_binary_file_downloader_html(pdf_path, "PDF Download")
                else:
                    st.error(f"File not found: {pdf_path}")
            except Exception as e:
                st.error(f"**ERROR reading the PDF file: {e}")

            
           
   

if __name__ == "__main__":
    main()
