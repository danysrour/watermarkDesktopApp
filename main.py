import tkinter as tk
from watermark import Watermark

# Create Tkinter window
window = tk.Tk()
window.title("Image Watermarking App")

watermark = Watermark(watermark_text="I am a watermark")

# Add button to add watermark
button = tk.Button(window, text="Add Watermark", command=watermark.add_watermark())
button.pack(pady=20)

# Run Tkinter event loop
window.mainloop()
