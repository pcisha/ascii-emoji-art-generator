# Ascii Emoji Art Generator 🎨🐐

This Python project generates **emoji-based ASCII art**.

## 📂 Features

- Creates **emoji art** with different text variations.
- Randomized skin tones for all emojis.
- Accurate positioning for emojis and text.
- Properly centered text `"Prachi is"` next to the goat emoji.
- Extracted background color from emoji images for seamless blending.
- Ensures no emoji is behind the text.
- Supports **custom emoji images** stored in the `assets/` folder.
- Outputs **high-quality PNG images**.

## 📂 Project Structure
<img width="811" alt="Screenshot 2025-03-16 at 6 10 18 AM" src="https://github.com/user-attachments/assets/600ea259-04ed-4d7b-abc9-01e5a67e651b" />

## Tech stack
- Python 3.12.8
- Pillow (Python Imaging Library)

## Run the script

```$ python ascii_emoji_art_generator.py```

## Customize text

```text = "Prachi is"  # Add your own name here```

## Emoji selection
Function to randomly pick a skin tone for each emoji: Modify the random skin tone assignment in ascii_emoji_art_generator.py to change how emojis are distributed:
```
def get_random_skin_tone(emoji_type):
    return random.choice(skin_tone_files[emoji_type])
```

## Different emoji's supported:
- Pointing up ☝🏻
- Pointing down 👇🏼
- Pointing right 👉🏻
- Pointing left 👈🏼
- Middle middle 🖕🏽
- Goat 🐐

## Different emoji skin tones supported:
- Light 🤝🏻
- Medium 🙌🏼
- Dark 👏🏽

### Reference
- Emoji pictures from https://emojipedia.org/
- Original Tweet by Kanye West: https://x.com/EastKanyeYE/status/1900484763963752528
<img width="302" alt="og" src="https://github.com/user-attachments/assets/f8d124e3-fbf5-4654-843c-141439a2d0c2" />

#
Date: March 16, 2025

Author: Prachi Shah @ https://pcisha.my.canva.site/

P.S. The default copyright laws apply.
