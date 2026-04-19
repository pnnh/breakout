from PIL import Image

# 创建球 (20x20)
ball = Image.new('RGBA', (20, 20), (255, 255, 255, 255))
ball.save('ball.png')

# 创建挡板 (120x20)
paddle = Image.new('RGBA', (120, 20), (255, 255, 255, 255))
paddle.save('paddle.png')

# 创建砖块 (100x30)
brick = Image.new('RGBA', (100, 30), (255, 255, 255, 255))
brick.save('brick.png')

print("Individual sprite images generated.")
