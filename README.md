
# SecureVote

SecureVote is a private cloud-based voting web application that demonstrates the use of Fully Homomorphic Encryption (FHE) concepts. This application allows users to securely vote for candidates with simulated encryption, view encrypted submissions, and display real-time results through a modern web interface.

## Team Members

- **Name**: Raditya Maheswara  
  **NIM**: 23/516252/PA/22075  
  **University**: Universitas Gadjah Mada (UGM)  
  **GitHub Link**: https://github.com/mash1rou

- **Name**: Muhammad Fariz  
  **NIM**: 23/518174/PA/22237  
  **University**: Universitas Gadjah Mada (UGM)  
  **GitHub Link**: https://github.com/RujakBuah

- **Name**: Girindra Daafi Mada  
  **NIM**: 23/511637/PA/21835  
  **University**: Universitas Gadjah Mada (UGM)  
  **GitHub Link**: https://github.com/girindradmada

- **Name**: Teuku Achmad Ra'di Syah  
  **NIM**: 23/511627/PA/21833  
  **University**: Universitas Gadjah Mada (UGM)  
  **GitHub Link**: https://github.com/yarin-sys


## Technology Stack

- **Backend**: Flask (Python)
- **Encryption**: TenSEAL (Fully Homomorphic Encryption)
- **Frontend**: HTML, CSS, JavaScript
- **Template Engine**: Jinja2
- **System**: WSL Debian (Python 3.10+)
- **Cloud**: AWS and tmux to make the application keep running in the background

## Disclaimer
To run this project, you must use Python 3.10, as TenSEAL is only compatible with that version.  

Python 3.11 or above is not supported by TenSEAL, and attempting to install or run TenSEAL with newer Python versions will result in compatibility errors.  

Additionally, do not run this project using PowerShell — it is recommended to use WSL (Windows Subsystem for Linux), preferably Debian. Some dependencies (e.g., NumPy for Linux) may not function correctly in PowerShell or Command Prompt environments.

## Environment Setup

This project was developed and tested using **WSL (Windows Subsystem for Linux)** with the **Debian Linux** distribution. Please follow the steps below to set up your environment:

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yarin-sys/CC-Kematian
   ```

2. **Launch WSL (Debian)**  
   ```bash
   wsl -d Debian
   cd CC-Kematian/backend
   ```

3. **Ensure Python 3.10 is installed**  
   TenSEAL only supports Python 3.10.  
   Check your version with:
   ```bash
   python3.10 --version
   ```

4. **Create and activate a virtual environment**  
   ```bash
   python3.10 -m venv myenv
   source myenv/bin/activate
   ```

5. **Install project dependencies (within the virtual environment)**  
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the application (still inside the virtual environment)**  
   ```bash
   python app.py
   ```

7. **Access the app**  
   After running, open the provided link (e.g., `http://127.0.0.1:5000/`) in your browser.

## Context

This project was developed for the course *Komputasi Awan* at Universitas Gadjah Mada.

## License

This project is intended for academic use only and is not licensed for commercial use.
