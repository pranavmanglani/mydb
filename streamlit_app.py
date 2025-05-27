mport streamlit as st
import os
import base64

# Replace this with a secure password system in production
PASSWORD = "1234"
FILES_DIR = "uploaded_files"

# Create upload folder if it doesn't exist
if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)

def save_uploaded_file(uploaded_file):
    with open(os.path.join(FILES_DIR, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

def list_files():
    return os.listdir(FILES_DIR)

def file_download_link(file_path, file_label):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:file/octet-stream;base64,{b64}" download="{file_label}">Download {file_label}</a>'
    return href

def main():
    st.title("Secure File Upload & Download")

    # Login
    password = st.text_input("Enter password", type="password")
    if password != PASSWORD:
        st.warning("Enter correct password to access the system.")
        return

    st.success("Logged in successfully!")

    # Upload section
    st.header("Upload File")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file:
        save_uploaded_file(uploaded_file)
        st.success(f"{uploaded_file.name} uploaded successfully!")

    # Download section
    st.header("Download Files")
    files = list_files()
    if files:
        for file in files:
            file_path = os.path.join(FILES_DIR, file)
            st.markdown(file_download_link(file_path, file), unsafe_allow_html=True)
    else:
        st.write("No files available.")

if _name_ == "_main_":
    main()
