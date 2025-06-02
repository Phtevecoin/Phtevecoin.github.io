import os

# Settings
MEME_FOLDER = 'memes'  # Relative folder with your meme files
OUTPUT_FILE = 'memes_snippet.html'  # Output HTML to paste into your site

# Supported file types
image_extensions = ('.jpg', '.jpeg', '.png', '.gif')
video_extensions = ('.mp4', '.webm')

# Start generating HTML
html_snippets = []

for filename in sorted(os.listdir(MEME_FOLDER)):
    if filename.lower().endswith(image_extensions):
        html_snippets.append(f'<img src="{MEME_FOLDER}/{filename}" alt="Meme">')
    elif filename.lower().endswith(video_extensions):
        html_snippets.append(f'''
<video controls width="100%">
  <source src="{MEME_FOLDER}/{filename}" type="video/mp4">
</video>
''')

# Save to file
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(html_snippets))

print(f"✅ Generated HTML with {len(html_snippets)} memes in {OUTPUT_FILE}")
