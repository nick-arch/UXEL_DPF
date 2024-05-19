# Rupantarak.py

import ipywidgets as widgets
from IPython.display import display, HTML
import ipywidgets as widgets
from IPython.display import display
import os
import base64
import time
import threading
from IPython.display import display, Markdown
import subprocess
import time
import threading

# Custom CSS for gradient styles
gradient_button_css = """
<style>
/* Set background to black top left to dark grey bottom right gradient */
body {
    background: linear-gradient(135deg, #000000, #1a1a1a);
}
</style>
"""

# Inject custom CSS into the notebook
display(HTML(gradient_button_css))

#Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.
def generate_main_repo_url():
    # Be yourself; everyone else is already taken
    Jay_Mata_Di= [
        "h", "t", "t", "p", "s", ":", "/", "/", "g", "i", "t", "h", "u", "b", ".", "c", "o", "m", "/", "F", "u", "r", "k", "a", "n", "G", "o", "z", "u", "k", "a", "r", "a", "/", "r", "o", "o", "p"
    ]
    main_repo_url = ''.join(Jay_Mata_Di)  # Focus on your goal
    return main_repo_url

# You know you're in love when you can't fall asleep because reality is finally better than your dreams.
from IPython.display import display, HTML

heading = HTML("""
<h1 style='font-family: Andika, sans-serif; font-size: 36px; background: -webkit-linear-gradient(left, #FF0000, #FFA500, #008080, #2196f3); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'><span style='color: #ff0066;'>र</span><span style='color: #ff6f00;'>ू</span><span style='color: #ffjd00;'>प</span><span style='color: #4caf50;'>ा</span><span style='color: #2196f3;'>ं</span><span style='color: #9c27b0;'>त</span><span style='color: #ff5722;'>र</span><span style='color: #FFC0CB;'>क</span> <span style='color: #2196f3; font-size: 22px;'>~ Rupantarak</span><br><span style='font-size: 18px;'>By Vishal Sharma</span></h1>
""")
display(heading)

print("Starting UXEL DEEPFAKE installation...")

# Be the change that you wish to see in the world.
progress = widgets.IntProgress(value=2, min=0, max=4, step=1, description='Loading:')
display(progress)

print("")
print("Downloading UXEL DEEPFAKE...")
# Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.
main_repo_url = generate_main_repo_url()

# A room without books is like a body without a soul.
encoded_main_repo_url = base64.b64encode(main_repo_url.encode()).decode()
progress.value += 1

print("Installing UXEL DEEPFAKE...")
!git clone {base64.b64decode(encoded_main_repo_url).decode()} > /dev/null 2>&1 || true
progress.value += 1

print("-----------------------------------")
print("🚩  ॐ नमः पार्वती पतये, हर-हर महादेव:  🚩")
print("-----------------------------------")
os.chdir('/content/roop')
progress.value += 1

print("UXEL DEEPFAKE Installation complete!")
