from PIL import Image, ImageDraw, ImageFont, ImageOps
from tkinter import filedialog


class Watermark():
    def __init__(self, watermark_text):
        self.watermark_text = watermark_text

    def add_watermark(self):
        # Open image file
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            image = Image.open(file_path).convert("RGBA")

            # Add text watermark
            watermark_text = self.watermark_text
            font = ImageFont.truetype("ARIAL.TTF", 50)
            draw = ImageDraw.Draw(image)

            # Get dimensions of the watermark text
            text_width, text_height = draw.textsize(watermark_text, font)

            # Create a pattern of the watermark text
            pattern = Image.new("RGBA", (text_width, text_height))
            pattern_draw = ImageDraw.Draw(pattern)
            pattern_draw.text((0, 0), watermark_text, fill=(255, 255, 255, 128), font=font)

            # Tile the pattern across the entire image
            for x in range(0, image.width, text_width):
                for y in range(0, image.height, text_height):
                    image.alpha_composite(pattern, (x, y))

            # Save watermarked image
            save_path = filedialog.asksaveasfilename(defaultextension=".png")
            if save_path:
                image.convert("RGB").save(save_path)
                print("Watermarked image saved successfully.")

