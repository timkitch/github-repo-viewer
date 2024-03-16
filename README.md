# GitHub Repository Viewer

## Project Summary
This project is a web application that allows users to view the contents of a GitHub repository. Users can input the GitHub username, repository name, file extension of interest, and their personal access token. The application fetches the files from the specified repository and displays their contents. The application also supports syntax highlighting for various programming languages.

## Technologies Used
- Python
- Streamlit
- GitHub API

## How to Run the App
1. Clone the repository to your local machine.
2. Install the required Python packages by running `pip install streamlit requests` in your terminal.
3. Run the app by typing `streamlit run app.py --server.port <port>` in your terminal.
4. Launch a browser and enter URL: http://localhost:<port>

## How to Use the Web App
1. Input your GitHub username in the "GitHub Username" field.
2. Input the name of the repository you want to view in the "Repository Name" field.
3. Input the file extension of the files you want to view in the "File Extension" field.
4. Input your personal access token in the "Personal Access Token" field.
5. Select the programming language for syntax highlighting from the "Programming Language" dropdown.
6. Click the "Fetch Files" button to fetch and display the files.

Please note that all fields are required. If any field is left empty, an error message will be displayed.