import webbrowser
import os
import sys
import threading
import time
import subprocess

def start_server():
    """Start the Django development server."""
    # Use sys.executable to ensure we use the same python interpreter
    subprocess.run([sys.executable, "manage.py", "runserver"], check=True)

def open_browser():
    """Wait for the server to start and then open the browser."""
    time.sleep(2)  # Wait for server to initialize
    url = "http://127.0.0.1:8000/"
    print(f"Opening chatbot at {url}...")
    webbrowser.open(url)

if __name__ == "__main__":
    print("Starting Chatbot Launcher...")
    
    # Start the browser opening in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    try:
        # Start the Django server (this is blocking)
        start_server()
    except KeyboardInterrupt:
        print("\nStopping server...")
    except Exception as e:
        print(f"Error starting server: {e}")
