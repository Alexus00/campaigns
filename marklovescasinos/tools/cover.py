"""cover(src, t, x0, l1, l2, bottom, out, y0=60)  1080x1920, grid-safe (everything inside centre 3:4)"""
import subprocess
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont
W, H = 1080, 1920; F = "fonts/Montserrat.ttf"
def cover(src, t, x0, l1, l2, bottom, out, y0=60, ch=900):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", f"src/{src}.mp4", "-frames:v", "1", "work/_cov.png"], check=True)
    img = Image.open("work/_cov.png").convert("RGB")
    bg = ImageEnhance.Brightness(img.resize((W, H)).filter(ImageFilter.GaussianBlur(30))).enhance(0.3)
    f = img.crop((x0, y0, x0 + 1080, y0 + ch)).resize((W, ch), Image.LANCZOS)
    f = ImageEnhance.Contrast(ImageEnhance.Color(f).enhance(1.15)).enhance(1.08)
    fy = 530; bg.paste(f, (0, fy)); d = ImageDraw.Draw(bg); YEL = (255, 229, 0)
    d.rectangle((0, fy - 8, W, fy), fill=YEL); d.rectangle((0, fy + ch, W, fy + ch + 8), fill=YEL)
    def text(y, s, size, fill, st=11):
        fn = ImageFont.truetype(F, size)
        while d.textlength(s, font=fn) > W - 80: size -= 4; fn = ImageFont.truetype(F, size)
        x = (W - d.textlength(s, font=fn)) / 2
        d.text((x + 6, y + 8), s, font=fn, fill=(0, 0, 0), stroke_width=st, stroke_fill=(0, 0, 0))
        d.text((x, y), s, font=fn, fill=fill, stroke_width=st, stroke_fill=(0, 0, 0))
    text(310, l1, 104, (255, 255, 255)); text(425, l2, 96, YEL)
    text(fy + ch + 35, bottom, 84, (60, 230, 80))
    ov = Image.open("brand/kick_overlay.png"); bg.paste(ov, (0, H - 1080), ov)
    bg.save(out, quality=93); bg.resize((270, 480)).save("work/_cov_s.jpg")
    return out
