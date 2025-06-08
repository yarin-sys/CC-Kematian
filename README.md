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
- **Cloud**: AWS

## Disclaimer
To run this project, you must use Python 3.10, as TenSEAL is only compatible with that version.  
Python 3.11 or above is not supported by TenSEAL, and attempting to install or run TenSEAL with newer Python versions will result in compatibility errors.  
Additionally, do not run this project using PowerShell — it is recommended to use WSL (Windows Subsystem for Linux), preferably Debian. Some dependencies (e.g., NumPy for Linux) may not function correctly in PowerShell or Command Prompt environments.

## Environment Setup

This project was executed within WSL using the Debian Linux distribution

1. Clone the repository:
   ```bash
   https://github.com/yarin-sys/CC-Kematian
   ```
   
2. Activate WSL (Debian)
    ```bash
    wsl -d Debian
    cd backend
    ```
3. Make sure u have Python 3.10 installed
    ```bash
    python3.10 --version
    ```
  
4. Activate Python Virtual Environment
    ```bash
    python3.10 -m venv myenv
    source myenv/bin/activate
    ```

5. Install Project Dependencies (It must be inside the virtual enviroment)
    ```bash
    pip install -r requirements.txt
    ```
7. Run (It must be inside the virtual enviroment)
    ```bash
    python app.py
    ```
Copy the link from the terminal (e.g. `http://127.0.0.1:5000/`) and open it in your browser.

## Context

This project was developed for the course *Komputasi Awan* at Universitas Gadjah Mada.

## License

This project is intended for academic use only and is not licensed for commercial use.

