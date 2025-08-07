import math
import cmath
import base64
import os
import requests
import json
#首次开发by Github@Wandermuluo

# ==================== 数学计算功能 ====================
def quadratic_equation():
    print("\n--- 解二次方程 ax² + bx + c = 0 ---")
    try:
        a = float(input("输入 a: "))
        b = float(input("输入 b: "))
        c = float(input("输入 c: "))

        delta = b**2 - 4*a*c  

        if delta < 0:
            root1 = (-b + cmath.sqrt(delta)) / (2*a)
            root2 = (-b - cmath.sqrt(delta)) / (2*a)
            print(f"复数解：\nX1 = {format_complex(root1)}\nX2 = {format_complex(root2)}")
        else:
            sqrt_delta = math.sqrt(delta)  
            root1 = (-b + sqrt_delta) / (2*a)  
            root2 = (-b - sqrt_delta) / (2*a)  
            print(f"实数解：\nX1 = {format_number(root1)}\nX2 = {format_number(root2)}")
    except ValueError:
        print("输入错误，请确保输入的是数字")

def linear_equation():
    print("\n--- 解线性方程 kx + b = 0 ---")
    try:
        k = float(input("输入 k: "))
        b = float(input("输入 b: "))
        
        if k == 0:
            print("无解" if b != 0 else "无限多解")
        else:
            x = -b / k
            print(f"解: x = {format_number(x)}")
    except ValueError:
        print("输入错误，请确保输入的是数字")

def square_root():
    print("\n--- 计算平方根 √x ---")
    try:
        x = float(input("输入 x: "))
        
        if x >= 0:
            sqrt_x = math.sqrt(x)
            print(f"√{x} = {format_number(sqrt_x)}")
        else:
            sqrt_x = cmath.sqrt(x)
            print(f"√{x} = {format_complex(sqrt_x)}")
    except ValueError:
        print("输入错误，请确保输入的是数字")

def absolute_value():
    print("\n--- 计算绝对值 |x| ---")
    try:
        x = float(input("输入 x: "))
        print(f"|{x}| = {format_number(abs(x))}")
    except ValueError:
        print("输入错误，请确保输入的是数字")

def factorial():
    print("\n--- 计算阶乘 n! ---")
    try:
        n = int(input("输入 n (非负整数): "))
        if n < 0:
            print("错误：阶乘仅适用于非负整数")
        else:
            print(f"{n}! = {math.factorial(n)}")
    except ValueError:
        print("输入错误，请确保输入的是整数")

def power():
    print("\n--- 计算指数 a^b ---")
    try:
        a = float(input("输入 a: "))
        b = float(input("输入 b: "))
        print(f"{a}^{b} = {format_number(a ** b)}")
    except ValueError:
        print("输入错误，请确保输入的是数字")

def logarithm():
    print("\n--- 计算对数 logₐb ---")
    try:
        a = float(input("输入 底数 a (a > 0, a ≠ 1): "))
        b = float(input("输入 真数 b (b > 0): "))
        if a <= 0 or a == 1 or b <= 0:
            print("错误：a 必须 > 0 且 ≠ 1，b 必须 > 0")
        else:
            print(f"log_{a}({b}) = {math.log(b, a)}")
    except ValueError:
        print("输入错误，请确保输入的是数字")

# ==================== Base64功能 ====================
def base64_encode():
    print("\n--- Base64 编码 ---")
    print("1. 编码文本\n2. 编码文件")
    choice = input("请选择 (1/2): ")
    
    if choice == "1":
        text = input("输入要编码的文本: ")
        encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
        print(f"Base64 编码结果:\n{encoded}")
    elif choice == "2":
        file_path = input("输入文件路径: ")
        if not os.path.exists(file_path):
            print("文件不存在！")
            return
        try:
            with open(file_path, "rb") as f:
                file_data = f.read()
            encoded = base64.b64encode(file_data).decode("utf-8")
            print(f"Base64 编码结果（前100字符）:\n{encoded[:100]}...")
        except Exception as e:
            print(f"文件读取错误: {e}")
    else:
        print("无效输入！")

def base64_decode():
    print("\n--- Base64 解码 ---")
    print("1. 解码为文本\n2. 解码为文件")
    choice = input("请选择 (1/2): ")
    
    encoded = input("输入 Base64 字符串: ")
    if not encoded.strip():
        print("输入不能为空！")
        return
    
    try:
        decoded_data = base64.b64decode(encoded)
    except Exception as e:
        print(f"Base64解码失败: {e}")
        return
    
    if choice == "1":
        try:
            decoded = decoded_data.decode("utf-8")
            print(f"解码结果:\n{decoded}")
        except UnicodeDecodeError:
            print("解码失败：内容不是有效文本")
    elif choice == "2":
        output_path = input("输入保存路径（如 output.jpg）: ")
        try:
            with open(output_path, "wb") as f:
                f.write(decoded_data)
            print(f"文件已保存到 {output_path}")
        except Exception as e:
            print(f"文件写入错误: {e}")
    else:
        print("无效输入！")

# ==================== B站API功能 ====================
def bilibili_user_info():
    print("\n--- B站UID查询 ---")
    uid = input("请输入B站UID: ")
    
    if not uid.isdigit():
        print("UID必须是数字喵~zako")
        return
    
    try:
        api_url = f"https://api.bilibili.com/x/space/acc/info?mid={uid}"
        response = requests.get(api_url, timeout=5)
        data = response.json()
        
        if data["code"] == 0:
            user = data["data"]
            print("\n=== 用户信息 ===")
            print(f"UID: {user['mid']}")
            print(f"昵称: {user['name']}")
            print(f"签名: {user['sign']}")
            print(f"等级: Lv{user['level']}")
            print(f"粉丝数: {user['follower']}")
        else:
            print(f"查询失败: {data.get('message', '未知错误')}")
    except requests.exceptions.RequestException as e:
        print(f"网络错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

# ==================== 辅助函数 ====================
def format_number(num):
    return int(num) if isinstance(num, float) and num.is_integer() else round(num, 4)

def format_complex(z):
    real = int(z.real) if z.real.is_integer() else round(z.real, 4)
    imag = int(z.imag) if z.imag.is_integer() else round(z.imag, 4)
    if imag == 0:
        return real
    elif real == 0:
        return f"{imag}j"
    else:
        return f"{real} + {imag}j"

# ==================== 主菜单 ====================
def main_menu():
    menu_options = {
        "1": ("解二次方程", quadratic_equation),
        "2": ("解线性方程", linear_equation),
        "3": ("计算平方根", square_root),
        "4": ("计算绝对值", absolute_value),
        "5": ("计算阶乘", factorial),
        "6": ("计算指数", power),
        "7": ("计算对数", logarithm),
        "8": ("Base64编码", base64_encode),
        "9": ("Base64解码", base64_decode),
        "10": ("B站UID查询", bilibili_user_info),
        "0": ("退出", None)
    }

    while True:
        print("\n===== 多功能工具箱 =====")
        for key, (desc, _) in menu_options.items():
            print(f"{key}. {desc}")
        
        choice = input("请选择功能 (0-10): ")
        
        if choice == "0":
            print("Bye-Bye ~ (∠・ω < )⌒★")
            break
        elif choice in menu_options:
            menu_options[choice][1]()
        else:
            print("无效输入，请重新选择！Invalid Input")

if __name__ == "__main__":
    # 检查requests库是否安装
    try:
        import requests
    except ImportError:
        print("错误：需要requests库，请先运行: pip install requests")
        exit(1)
    
    main_menu()