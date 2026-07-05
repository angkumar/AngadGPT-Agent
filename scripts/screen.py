import base64
import io
from mss import mss
from PIL import Image

def capture_screen():
    with mss() as sct:
        monitor = sct.monitors[1]
        img = sct.grab(monitor)

        im = Image.frombytes("RGB", img.size, img.rgb)

        buffer = io.BytesIO()

        im.save(buffer, format="PNG")
        
        return base64.b64encode(buffer.getvalue()).decode()