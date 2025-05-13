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

    # Link funzionante: https://iph-sn-ep33nvbuic6zbq7uqvbxbm.streamlit.app/?pn=5F1370116301AN
    
    st.sidebar.image("https://iph.it/wp-content/uploads/2020/02/logo-scritta.png", width=140)

    st.title(f":blue[IPH Specification Sheet Portal]")

    sn_list = ["25007676", "25007677"]
    pn_list = ["5C1440154403AN", "5F1370116301AN"]
    desc1_list = ["5C-04870-154-4-M0343-0000N", "5F-03450-116-3-M1460-0000N"]
    desc2_list = ["Alternative_descrption_pn1", "Alternative_descrption_pn2"]
    
    #sn = st.query_params.get('sn', None)
    # if sn is None:
    #     st.error("**ERROR: URL doesn't containt serial number. Add '?sn=SERIAL_NUMBER' to the URL.", icon='🚨')
    #     st.stop()
    # if sn not in sn_list:
    #     st.error(f"**ERROR: Serial number {sn} does not exists!", icon='🚨')
    #     st.stop()
    pn = st.query_params.get('pn', None)
    if pn is None:
        st.error("**ERROR: URL doesn't containt product number. Add '?pn=PRODUCT_NUMBER' to the URL.", icon='🚨')
        st.stop()
    if pn not in pn_list:
        st.error(f"**ERROR: Product number {pn} does not exists!", icon='🚨')
        st.stop()

    with st.expander("Device browser info"):
        browser_values = browser_detection_engine()
        st.write(f"Browser values:")
        st.write(browser_values)
        browser_detected_language = detect_browser_language()[0:2]
        st.write(f"Browser language:\n{browser_detected_language}")

    st.subheader(f":grey[Product section]")
    
    with st.container(border=True):   
        #obj_idx = sn_list.index(st.query_params['sn'])
        # serial_nr = st.selectbox(
        #     label=":orange[Serial number]",
        #     options=sn_list,
        #     index=sn_list.index(st.query_params['sn']),
        #     disabled=True
        # )
        
        obj_idx = pn_list.index(st.query_params['pn'])
        product_nr = st.text_input(
            label=":orange[Product number]",
            value=pn_list[obj_idx],
            disabled=True
        )

        product_desc1 = st.text_input(
            label=":orange[Product description 1]",
            value=desc1_list[obj_idx],
            disabled=True
        )

        product_desc2 = st.text_input(
            label=":orange[Product description 2]",
            value=desc2_list[obj_idx],
            disabled=True
        )

    st.subheader(f":grey[Attachment section]")  
    
    with st.form("attachment_form"):
        
        browser_language_option = ['it','en']
        if browser_detected_language:
            lang_idx = browser_language_option.index(browser_detected_language)
        else:
            lang_idx = None

        selected_language = st.selectbox(
            label=":orange[Language]",
            options=browser_language_option,
            index=lang_idx,
            #index=None,
            disabled=False
        )

        selected_attachment_type = st.selectbox(
            label=":orange[Attachment type]",
            options=['Specification sheet','Other'],
            index=0,
            disabled=False
        )



        submitted = st.form_submit_button(label="Search", type="primary", icon=":material/search:")

    
    if submitted:
        if selected_language == None or selected_attachment_type == None:       
            st.warning("Please select language and attachment type first!", icon="⚠️")
            st.stop()
        folder_option = {"Specification sheet":"tech_sheet", "Other":"other"}
        attachment_prefix = {"Specification sheet": "FIG", "Other": "OTH"}
        file_folder = f"files/{folder_option[selected_attachment_type]}/{selected_language}/"
        pdf_filename = f"{attachment_prefix[selected_attachment_type]}-{product_nr}.pdf"
        # Percorso relativo alla cartella files
        pdf_path = os.path.join(file_folder, pdf_filename)
        
        try:
            # Verifica se il file esiste
            if os.path.exists(pdf_path):
                st.success(f"File found: {pdf_path}")
                # Utilizza la funzione di download
                get_binary_file_downloader_html(pdf_path, "Download")
            else:
                st.error(f"File not found: {pdf_path}", icon='🚨')
        except Exception as e:
            st.error(f"**ERROR reading the PDF file: {e}", icon='🚨')
        
        
   

if __name__ == "__main__":
    main()
