import os
import random
import time
from datetime import datetime, timedelta

# 生成模拟用户数据
def generate_user_data():
    users = []
    for i in range(1, 101):  # 生成100个用户
        user_id = f"user_{i:03d}"
        user_name = f"user{i}"
        age = random.randint(18, 60)
        gender = random.choice(["男", "女"])
        register_time = datetime.now() - timedelta(days=random.randint(1, 365))
        last_login_time = datetime.now() - timedelta(hours=random.randint(1, 24))
        users.append([user_id, user_name, age, gender, register_time.strftime("%Y-%m-%d %H:%M:%S"), last_login_time.strftime("%Y-%m-%d %H:%M:%S")])
    return users

# 生成模拟产品数据
def generate_product_data():
    products = []
    categories = ["电子产品", "服装", "食品", "图书", "家居"]
    brands = ["品牌A", "品牌B", "品牌C", "品牌D", "品牌E"]
    
    for i in range(1, 201):  # 生成200个产品
        product_id = f"prod_{i:03d}"
        product_name = f"产品{i}"
        category_id = f"cat_{random.randint(1, 5)}"
        category_name = random.choice(categories)
        price = round(random.uniform(10, 1000), 2)
        stock = random.randint(100, 1000)
        brand = random.choice(brands)
        products.append([product_id, product_name, category_id, category_name, price, stock, brand])
    return products

# 生成模拟用户行为数据
def generate_user_behavior_data(users, products):
    behaviors = []
    behavior_types = ["pv", "cart", "buy", "fav"]
    
    for i in range(1, 10001):  # 生成10000条行为记录
        log_id = f"log_{i:05d}"
        user = random.choice(users)
        user_id = user[0]
        product = random.choice(products)
        product_id = product[0]
        behavior_type = random.choices(behavior_types, weights=[60, 20, 10, 10])[0]
        behavior_time = datetime.now() - timedelta(hours=random.randint(1, 720))  # 过去30天
        ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        user_agent = random.choice(["Mozilla/5.0", "Chrome/90.0", "Safari/14.0"])
        referer = random.choice(["https://www.baidu.com", "https://www.google.com", "直接访问"])
        behaviors.append([log_id, user_id, product_id, behavior_type, behavior_time.strftime("%Y-%m-%d %H:%M:%S"), ip, user_agent, referer])
    return behaviors

# 保存数据到文件
def save_data(data, file_path, delimiter="\t"):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        for row in data:
            f.write(delimiter.join(map(str, row)) + "\n")

if __name__ == "__main__":
    print("开始生成模拟数据...")
    
    # 生成数据
    users = generate_user_data()
    products = generate_product_data()
    behaviors = generate_user_behavior_data(users, products)
    
    # 保存数据
    save_data(users, "data/raw/users.txt")
    save_data(products, "data/raw/products.txt")
    save_data(behaviors, "data/raw/user_logs.txt")
    
    print("模拟数据生成完成！")
    print(f"生成了 {len(users)} 个用户")
    print(f"生成了 {len(products)} 个产品")
    print(f"生成了 {len(behaviors)} 条用户行为记录")