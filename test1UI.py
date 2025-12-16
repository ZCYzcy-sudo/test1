import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

# 1. 创建应用程序对象
app = QApplication(sys.argv)

# 2. 创建窗口
window = QWidget()
window.setWindowTitle("PyQt5测试窗口")
window.resize(300, 200)  # 窗口大小

# 3. 添加控件
label = QLabel("Hello PyQt5!", window)
label.move(100, 50)  # 控件位置

btn = QPushButton("点击我", window)
btn.move(100, 100)

# 4. 显示窗口
window.show()

# 5. 运行应用
sys.exit(app.exec_())