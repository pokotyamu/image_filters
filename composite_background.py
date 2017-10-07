import io
from PIL import Image

def composite_background(
    image_binary,
    file_type="png",
    min_width=600,
    min_height=600,
    color=(255, 255, 255)
):
    image = Image.open(image_binary)
    org_x, org_y = image.size
    if org_x >= min_width and org_y >= min_height:
        return image_binary
    x = max(org_x, min_width)
    y = max(org_y, min_height)
    top_x = int((x - org_x) / 2)
    top_y = int((y - org_y) / 2)
    canvas = Image.new("RGB", (x, y), color)
    canvas.paste(image, (top_x, top_y))
    bytes_io = io.BytesIO()
    canvas.save(bytes_io, file_type)
    return bytes_io
