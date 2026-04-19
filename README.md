# Breakout Game - Defold

一个使用Defold引擎开发的经典打砖块游戏。

## ⚠️ 重要提示

由于Defold的collection文件需要通过Defold编辑器创建（二进制格式），本项目使用了简化的结构。**首次运行时需要在Defold编辑器中手动设置启动场景。**

## 首次设置

1. 使用Defold编辑器打开项目
2. 在编辑器中创建新的collection文件：
   - 右键点击`/main`文件夹
   - 选择 `New` > `Collection`
   - 命名为 `main.collection`
3. 在collection中添加以下游戏对象：
   - 添加 `/main/main.go` 作为根对象
4. 更新 `game.project` 中的启动路径为 `/main/main.collection`

## 游戏说明

### 控制方式
- **鼠标/触摸**: 移动挡板
- **点击/触摸**: 开始游戏

### 游戏规则
1. 使用挡板反弹球，击碎所有砖块
2. 球掉落到底部会失去一条生命
3. 失去所有3条生命后游戏结束
4. 击碎所有砖块即可获胜

### 评分
- 每击碎一个砖块得10分

## 项目结构

```
Breakout/
├── main/
│   ├── game.script          # 游戏主脚本
│   ├── paddle.script        # 挡板脚本
│   ├── ball.script          # 球脚本
│   ├── brick.script         # 砖块脚本
│   ├── main.go              # 主游戏对象
│   ├── paddle.go            # 挡板游戏对象
│   ├── ball.go              # 球游戏对象
│   ├── brick.go             # 砖块游戏对象
│   ├── brick.factory        # 砖块工厂
│   ├── sprites.atlas        # 精灵图集
│   └── sprites.png          # 精灵图片
├── input/
│   └── game.input_binding   # 输入绑定
├── game.project             # 项目配置
└── README.md
```

## 运行游戏

### 方法1：使用Defold编辑器
1. 使用Defold编辑器打开项目
2. 按上述"首次设置"步骤创建collection
3. 按`Ctrl+B`构建项目
4. 按`F5`或点击播放按钮运行游戏

### 方法2：手动启动
如果项目配置正确：
1. 使用Defold编辑器打开项目
2. 按`F5`直接运行

## 自定义

### 修改难度
- 在`ball.script`中调整`speed`和`max_speed`值
- 在`game.script`中调整砖块行数和列数
- 修改`lives`值来改变生命数量

### 修改颜色
- 在`brick.script`中修改`brick_colors`表

## 技术特点

- 使用Defold 2D游戏引擎
- 自定义游戏脚本
- 物理碰撞检测
- 工厂模式创建游戏对象
- 支持鼠标和触摸控制
- 响应式设计

## 故障排除

### "collection not found" 错误
需要在Defold编辑器中手动创建collection文件。

### 脚本错误
检查所有`.script`文件的语法是否正确。

### 碰撞不工作
确保collisionobject组件正确配置了collision_group。

## 许可

MIT License
