# 📋 Facebook Group List Extractor (Keyboard & Mouse Automation)

This project automates the process of **extracting Facebook group URLs** from a Facebook page (such as search results or a profile's groups list) using Python and `PyAutoGUI`. It simulates keyboard and mouse actions to get the list of your group links without using the Facebook API.

## 📦 Requirements

- Python 3.6 or higher
- PyAutoGUI

Install required packages:

```bash
pip install pyautogui
```

## 🚀 How It Works

1. You open the Facebook page (e.g., "Groups joined", or search results).
2. The script simulates:
   - Scrolling down
   - Right-clicking on each group link
   - Selecting **"Copy link"**
3. It copies links to the clipboard one by one (you can optionally log them to a file).

⚠️ This approach relies on the **UI structure not changing** and works best on **desktop view** in a browser like Chrome or Edge.

## 🧪 Sample Code

```python

def enter_grab_exit():

    pyautogui.hotkey('shift', 'f10', 'o') # Copy link of focused section 
    append_to_file()
    time.sleep(1)
    pyautogui.press('tab') # Navigate divs

```

## 🧠 Use Cases

- Creating a dataset of group URLs for research or analysis
- Saving personal joined group links
- Automating repetitive Facebook browsing tasks

## 📝 Notes

- Works best with English browser UI.
- Make sure you’re **logged in to Facebook** and on the correct section.
- The script relies on **mouse position** — consider using `pyautogui.position()` to calibrate.

## 🖼️ Screenshot

## 🔐 Disclaimer

This project **does not hack or bypass** Facebook’s policies. It simply mimics human interaction using keyboard/mouse automation. Use responsibly and ethically.

 
---

**Built with 🐍 Python + 🖱️ PyAutoGUI**
 

---
 
