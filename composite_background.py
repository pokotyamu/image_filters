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


def paste_image(
    back_image_binary,
    pasted_image_binary,
    position
):
    back_image = Image.open(back_image_binary).convert('RGBA')
    pasted_image = Image.open(pasted_image_binary).convert('RGBA')
    back_size = back_image.size
    pasted_image.thumbnail((back_size[0] * 0.2, back_size[1] * 0.2), Image.LANCZOS)
    layer = Image.new('RGBA', back_image.size, (255, 255, 255, 0))
    coordinate = paste_position(position, back_size, pasted_image.size)
    layer.paste(pasted_image, coordinate)
    canvas = Image.alpha_composite(back_image, layer)
    bytes_io = io.BytesIO()
    canvas.save(bytes_io, 'PNG')
    return bytes_io


def paste_position(position, back_size, pasted_size):
    if position['side'] is 'left':
        x = 0
    elif position['side'] is 'right':
        x = back_size[0] - pasted_size[0]

    if position['length'] is 'top':
        y = 0
    elif position['length'] is 'bottom':
        y = back_size[1] - pasted_size[1]

    return (x, y)

