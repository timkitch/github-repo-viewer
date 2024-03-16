import streamlit as st
from GitHubApiConnector import GitHubApiConnector
from CodeFormatter import CodeFormatter

# UI for user inputs
st.sidebar.title("GitHub Repository Viewer")
username = st.sidebar.text_input("GitHub Username")
repository_name = st.sidebar.text_input("Repository Name")
file_extension = st.sidebar.text_input("File Extension (e.g., .py)")
token = st.sidebar.text_input("Personal Access Token", type="password")
language = st.sidebar.selectbox("Programming Language (for syntax highlighting)", 
                                ["python", "javascript", "html", "css", "java", "bash", "json", "yaml", "markdown"])

if st.sidebar.button("Fetch Files"):
    if not all([username, repository_name, file_extension, token, language]):
        st.sidebar.error("Please fill in all fields.")
    else:
        try:
            connector = GitHubApiConnector(token)
            files = connector.fetch_repository_contents(username, repository_name, file_extension)
            for file in files:
                file_content, encoding = connector.fetch_file_content(file['download_url'])
                decoded_content = CodeFormatter.decode_content(file_content, encoding)
                # For MVP, displaying without syntax highlighting
                st.text(f"Filename: {file['name']}")
                st.code(decoded_content, language.lower())
        except Exception as e:
            st.error(str(e))
