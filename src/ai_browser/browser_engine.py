from selenium import webdriver
import pyautogui
import requests
import config.api_keys as keys

class BrowserEngine:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Requires ChromeDriver
        self.api_key = keys.openrouter_api_key

    def analyze_page(self, url):
        self.driver.get(url)
        content = self.driver.page_source
        # Summarize using Perplexity via OpenRouter
        payload = {
            "model": "perplexity/pplx-7b-online",
            "messages": [{"role": "user", "content": f"Summarize: {content[:500]}"}]
        }
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
        return response.json()['choices'][0]['message']['content']

    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        return "Screenshot saved"
