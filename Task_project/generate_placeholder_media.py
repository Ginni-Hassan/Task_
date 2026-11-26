from PIL import Image, ImageDraw, ImageFont
import os, random

OUT = "tasks/static/tasks/images"
os.makedirs(OUT, exist_ok=True)

def get_font(size):
    for path in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def gradient(size, c1, c2):
    w, h = size
    base = Image.new("RGB", (w, h), c1)
    top = Image.new("RGB", (w, h), c2)
    mask = Image.new("L", (w, h))
    mask_data = []
    for y in range(h):
        mask_data.extend([int(255 * (y / h))] * w)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def make_card(filename, title, c1, c2, size=(700, 450)):
    img = gradient(size, c1, c2)
    draw = ImageDraw.Draw(img)
    # subtle diagonal shapes
    for i in range(6):
        x = random.randint(-100, size[0])
        y = random.randint(-100, size[1])
        r = random.randint(40, 140)
        draw.ellipse([x, y, x+r, y+r], fill=None, outline=(255,255,255,60), width=3)
    font = get_font(46)
    # word-wrap
    words = title.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=font) > size[0] - 80:
            lines.append(cur)
            cur = w
        else:
            cur = test
    lines.append(cur)
    total_h = len(lines) * 56
    y = (size[1] - total_h) // 2
    for line in lines:
        tw = draw.textlength(line, font=font)
        draw.text(((size[0]-tw)//2, y), line, font=font, fill="white")
        y += 56
    img.save(os.path.join(OUT, filename), quality=90)
    print("saved", filename)

# 7 homepage cards
cards = [
    ("card1.jpg", "Plan Your Day", (30,60,114), (56,146,229)),
    ("card2.jpg", "Stay Organized", (17,153,142), (56,239,125)),
    ("card3.jpg", "Track Progress", (255,94,58), (255,149,0)),
    ("card4.jpg", "Never Miss a Task", (131,58,180), (253,29,29)),
    ("card5.jpg", "Boost Productivity", (0,114,206), (0,201,167)),
    ("card6.jpg", "Manage Deadlines", (44,62,80), (52,152,219)),
    ("card7.jpg", "Achieve Your Goals", (237,117,255), (128,90,213)),
]
for fname, title, c1, c2 in cards:
    make_card(fname, title, c1, c2)

# 3 carousel slides (wider)
slides = [
    ("slide1.jpg", "Welcome to TaskMaster", (16,20,40), (76,29,149)),
    ("slide2.jpg", "Organize. Execute. Succeed.", (12,84,96), (56,193,182)),
    ("slide3.jpg", "Your Tasks, Simplified", (120,20,60), (255,94,98)),
]
for fname, title, c1, c2 in slides:
    make_card(fname, title, c1, c2, size=(1400, 500))

# 3 images for contactviewpage
contact_imgs = [
    ("contact1.jpg", "Get In Touch", (0,60,100), (0,180,180)),
    ("contact2.jpg", "We'd Love To Hear From You", (100,20,80), (240,100,60)),
    ("contact3.jpg", "Contact Our Team", (30,30,60), (100,100,220)),
]
for fname, title, c1, c2 in contact_imgs:
    make_card(fname, title, c1, c2, size=(700, 450))

print("Done")
