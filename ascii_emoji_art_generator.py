import random
from PIL import Image, ImageDraw, ImageFont

__author__ = "Prachi Shah"
__copyright__ = "Copyright 2025"

# Extract background color from an emoji image to ensure consistency
def extract_background_color(emoji_path):
    sample_emoji = Image.open(emoji_path).convert("RGB")
    return sample_emoji.getpixel((5, 5))  # Sample from a clean background area

# Image parameters
img_size = 800  # Square image size
grid_size = 10  # Grid layout (10x10)
emoji_size = img_size // grid_size  # Size of each emoji
bg_color = extract_background_color("assets/pointing_up_light.png")  # Extracted background

# Load emoji assets
emoji_files = {
    "up": "assets/pointing_up_light.png",
    "right": "assets/pointing_right_light.png",
    "left": "assets/pointing_left_light.png",
    "down": "assets/pointing_down_light.png",
    "middle": "assets/middle_finger_light.png",
    "goat": "assets/goat.png"
}

# Skin tone variations for all emoji types
skin_tone_files = {
    "up": ["assets/pointing_up_dark.png", "assets/pointing_up_medium.png", "assets/pointing_up_light.png"],
    "right": ["assets/pointing_right_dark.png", "assets/pointing_right_medium.png", "assets/pointing_right_light.png"],
    "left": ["assets/pointing_left_dark.png", "assets/pointing_left_medium.png", "assets/pointing_left_light.png"],
    "down": ["assets/pointing_down_dark.png", "assets/pointing_down_medium.png", "assets/pointing_down_light.png"],
    "middle": ["assets/middle_finger_light.png", "assets/middle_finger_light.png", "assets/middle_finger_light.png"],  # Middle finger remains light
}

# Create a blank image with the extracted background color
image = Image.new("RGBA", (img_size, img_size), bg_color)

# Function to randomly pick a skin tone for each emoji
def get_random_skin_tone(emoji_type):
    return random.choice(skin_tone_files[emoji_type])

# Place emojis in grid with randomized skin tones
for row in range(grid_size):
    for col in range(grid_size):
        # Define emoji orientation based on position
        if row == grid_size // 2 and col == grid_size // 2 + 2:
            emoji_path = emoji_files["goat"]  # Goat emoji in center-right
        elif row < grid_size // 2 and abs(col - grid_size // 2) <= row:
            emoji_path = get_random_skin_tone("down")  # Top pointing down
        elif row > grid_size // 2 and abs(col - grid_size // 2) <= (grid_size - row - 1):
            emoji_path = get_random_skin_tone("middle")  # Bottom middle finger
        elif col < grid_size // 2:
            emoji_path = get_random_skin_tone("right")  # Left side pointing right
        else:
            emoji_path = get_random_skin_tone("left")  # Right side pointing left

        # Ensure no emoji is placed where the text will be
        if row == grid_size // 2 and col in [grid_size // 2 - 1, grid_size // 2]:
            continue  # Skip these positions for text placement

        # Load and resize emoji image
        emoji_img = Image.open(emoji_path).convert("RGBA")
        emoji_img = emoji_img.resize((emoji_size, emoji_size), Image.Resampling.LANCZOS)

        # Calculate position
        x = col * emoji_size
        y = row * emoji_size

        # Paste emoji onto image
        image.paste(emoji_img, (x, y), emoji_img)

# Add text "Prachi IS" next to the goat
text = "Prachi is " # Extra spaces for better alignment
draw = ImageDraw.Draw(image)

# Load font
try:
    font = ImageFont.truetype("Arial.ttf", 45)  # Adjusted for better proportion
except:
    font = ImageFont.load_default()

# Calculate text size and position (ensuring it's correctly aligned next to the goat)
text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]
text_x = (grid_size // 2 - 1) * emoji_size + (emoji_size // 2)  # Shift text slightly to the right
text_y = (grid_size // 2) * emoji_size + (emoji_size // 4)  # Keep it centered properly

# Clear only the area behind the text using the exact background color
clear_rect = (text_x - 11, text_y - 11, text_x + text_width + 11, text_y + text_height + 11)
draw.rectangle(clear_rect, fill=bg_color)  # Use extracted emoji background

# Draw text correctly aligned closer to the goat
draw.text((text_x, text_y), text, font=font, fill=(110, 80, 60))  # Black text

# Save and show final improved image
final_image_path = "output/prachi_is_goat.png"
image.save(final_image_path)
image.show()

print(f"✅ Image created and saved here: {final_image_path}")

# Output: ✅ Image created and saved here: output/prachi_is_goat.png