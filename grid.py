from PIL import Image, ImageDraw, ImageFont

def overlay_grid(image_path, grid_size, grid_color=(255, 255, 255), grid_width=1, font_size=20):
    # Open the image
    image = Image.open(image_path)
    
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    
    # Use a default font (you can adjust the size by providing a different font file)
    font = ImageFont.load_default(size=5)  # This will use a basic default font
    
    # Get image dimensions
    width, height = image.size
    
    # Draw vertical lines and add unique numbers
    for x in range(0, width, grid_size):
        draw.line((x, 0, x, height), fill=grid_color, width=grid_width)
        # for y in range(0, height, grid_size):
        #     cell_number = int(x / grid_size) + int(y / grid_size) * int(width / grid_size)
        #     draw.text((x + 5, y + 5), str(cell_number), fill=(255, 0, 0), font=font)
    
    # Draw horizontal lines
    for y in range(0, height, grid_size):
        draw.line((0, y, width, y), fill=grid_color, width=grid_width)
    
    # Save or show the image
    image.show()

# Example usage
image_path = "/Users/vatsaljoshi/Desktop/mhacks2024/gridtest.png"  # Path to your image
grid_size = 100  # Size of grid squares in pixels
overlay_grid(image_path, grid_size)
