#!/usr/bin/env python3
"""
Startup script for the Career Coach Agents Streamlit UI.
"""

import subprocess
import sys
import os
import time
import requests
from pathlib import Path


def check_api_server():
    """Check if the API server is running."""
    try:
        response = requests.get("https://suevnzzvti.us-east-1.awsapprunner.com/health", timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def start_api_server():
    """Start the API server if it's not running."""
    if check_api_server():
        print("✅ API server is already running")
        return True
    
    print("🚀 Starting API server...")
    
    # Get the path to the main API file
    api_path = Path(__file__).parent.parent / "philoagents-api" / "src" / "main.py"
    
    if not api_path.exists():
        print(f"❌ API file not found at {api_path}")
        print("Please ensure you're running this from the correct directory")
        return False
    
    try:
        # Start the API server in the background
        subprocess.Popen([
            sys.executable, str(api_path)
        ], cwd=api_path.parent.parent)
        
        # Wait for the server to start
        print("⏳ Waiting for API server to start...")
        for i in range(30):  # Wait up to 30 seconds
            time.sleep(1)
            if check_api_server():
                print("✅ API server started successfully")
                return True
            print(f"   Waiting... ({i+1}/30)")
        
        print("❌ API server failed to start within 30 seconds")
        return False
        
    except Exception as e:
        print(f"❌ Failed to start API server: {e}")
        return False


def install_dependencies():
    """Install required dependencies."""
    print("📦 Installing UI dependencies...")
    
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    if not requirements_file.exists():
        print("❌ requirements.txt not found")
        return False
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
        ])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False


def start_streamlit():
    """Start the Streamlit application."""
    print("🎯 Starting Career Coach Agents UI...")
    
    streamlit_app = Path(__file__).parent / "streamlit_app.py"
    
    if not streamlit_app.exists():
        print(f"❌ Streamlit app not found at {streamlit_app}")
        return False
    
    try:
        # Start Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", str(streamlit_app),
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ], cwd=streamlit_app.parent)
        
    except KeyboardInterrupt:
        print("\n👋 Shutting down Career Coach Agents UI...")
    except Exception as e:
        print(f"❌ Failed to start Streamlit: {e}")
        return False
    
    return True


def main():
    """Main startup function."""
    print("🎯 Career Coach Agents - Streamlit UI Startup")
    print("=" * 50)
    
    if not start_streamlit():
        print("❌ Failed to start Streamlit UI")
        sys.exit(1)


if __name__ == "__main__":
    main()
