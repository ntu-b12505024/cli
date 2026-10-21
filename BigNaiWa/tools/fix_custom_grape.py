from PIL import Image, ImageFilter
import numpy as np

src_path = 'src/1.jpg'
out_png = 'v1/assets/fruits/01-grape.png'
out_webp = 'v1/assets/fruits/01-grape.webp'

im = Image.open(src_path).convert('RGBA')
arr = np.array(im)
r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]
white = ((r > 220) & (g > 220) & (b > 220))
black_halo = ((r < 20) & (g < 20) & (b < 20))
alpha = np.where(white | black_halo, 0, 255).astype(np.uint8)
arr2 = arr.copy()
arr2[:, :, 3] = alpha
img = Image.fromarray(arr2, 'RGBA')
mask = np.array(img)[:, :, 3] > 10
ys, xs = np.where(mask)
if len(xs) == 0:
    raise RuntimeError('No visible content found')
box = (xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)
subject = img.crop(box)
scale = 1.15
new_size = (max(1, int(subject.width * scale)), max(1, int(subject.height * scale)))
subject = subject.resize(new_size, Image.LANCZOS)
subject = subject.filter(ImageFilter.GaussianBlur(0.25))
canvas = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
canvas.paste(subject, ((512 - subject.width) // 2, (512 - subject.height) // 2), subject)
canvas.save(out_png, format='PNG', optimize=True)
canvas.save(out_webp, format='WEBP', quality=95)
print('saved', out_png, 'size', canvas.size)
print('saved', out_webp)
