"""
Sprite generation / fallback for Breakout game.

The pixel-art assets (ball.png, paddle.png, brick.png) are generated via
PixelLab MCP and checked into the repository.  Run this script only when
you need to regenerate plain white placeholder sprites (e.g. for testing).
"""
from PIL import Image

def generate_placeholders():
    # 球 20x20 — 白色占位
    ball = Image.new('RGBA', (20, 20), (255, 255, 255, 255))
    ball.save('ball_placeholder.png')

    # 挡板 120x20 — 白色占位
    paddle = Image.new('RGBA', (120, 20), (255, 255, 255, 255))
    paddle.save('paddle_placeholder.png')

    # 砖块 100x30 — 白色占位
    brick = Image.new('RGBA', (100, 30), (255, 255, 255, 255))
    brick.save('brick_placeholder.png')

    print("Placeholder sprites generated (ball/paddle/brick _placeholder.png).")
    print("The real pixel-art assets (ball.png, paddle.png, brick.png) are")
    print("managed via PixelLab MCP — do not overwrite them with this script.")

if __name__ == "__main__":
    generate_placeholders()
