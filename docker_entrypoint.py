#!/usr/bin/env python3
"""
Docker entrypoint script for Streamlit UI that modifies API_BASE_URL based on environment variables.
"""
import os
import sys
import subprocess
import time

def modify_api_url():
    """Modify the API_BASE_URL in streamlit_app.py based on environment variables."""
    api_url = os.environ.get("API_BASE_URL", "https://suevnzzvti.us-east-1.awsapprunner.com")
    print(f"🔄 Setting API_BASE_URL to: {api_url}")
    
    with open("streamlit_app.py", "r") as f:
        content = f.read()
    
    # Replace the API_BASE_URL line
    modified_content = content.replace(
        'API_BASE_URL = "https://suevnzzvti.us-east-1.awsapprunner.com"',
        f'API_BASE_URL = "{api_url}"'
    )
    
    with open("streamlit_app.py", "w") as f:
        f.write(modified_content)
    
    print("✅ API URL updated successfully")

def main():
    """Main entrypoint function."""
    print("🚀 Starting Career Coach Agents UI in Docker")
    
    # Modify the API URL based on environment variables
    modify_api_url()
    
    # Start Streamlit
    cmd = [
        "streamlit", "run", "streamlit_app.py",
        "--server.port=8501",
        "--server.address=0.0.0.0"
    ]
    
    print(f"🎯 Running command: {' '.join(cmd)}")
    subprocess.run(cmd)

if __name__ == "__main__":
    main()
