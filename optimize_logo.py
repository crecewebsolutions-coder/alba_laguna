from PIL import Image
import numpy as np

im = Image.open('new_logo_transparent.png')
print("Image size:", im.size)
# Resize to a crisp 600x600 for web display (which displays at 180-220px max width on mobile/desktop, so 600px is 3x retina ready!)
im_resized = im.resize((600, 600), Image.Resampling.LANCZOS)
im_resized.save('logo_optimized.png', optimize=True)

import os
print("logo_optimized.png size:", os.path.getsize('logo_optimized.png'))
