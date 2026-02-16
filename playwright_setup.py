import subprocess
import os
import sys

def ensure_playwright_installed():
    """Ensure Playwright browsers are installed."""
    try:
        from playwright.async_api import async_playwright
        # Try to access the browser to see if it's installed
        chromium_path = os.path.expanduser("~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome")
        if not any(os.path.exists(p) for p in [os.path.expanduser("~/.cache/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell"), os.path.expanduser("~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome")]):
            print("Installing Playwright browsers...")
            subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    except Exception as e:
        print(f"Warning: Could not install Playwright: {e}")

ensure_playwright_installed()
