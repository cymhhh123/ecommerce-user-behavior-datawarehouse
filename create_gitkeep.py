import os
import sys

# 项目根目录
PROJECT_ROOT = r"C:\Users\CYM\Desktop\项目\ecommerce-user-behavior-datawarehouse"

def is_directory_empty(directory):
    """检查目录是否为空（只包含子目录的话也算空）"""
    try:
        # 列出目录中的所有文件和子目录
        items = os.listdir(directory)
        # 检查是否有文件（不是子目录）
        has_files = any(os.path.isfile(os.path.join(directory, item)) for item in items)
        return not has_files
    except Exception as e:
        print(f"检查目录 {directory} 时出错: {e}")
        return False

def create_gitkeep_in_empty_dirs(root_dir):
    """在所有空目录中创建.gitkeep文件"""
    created_count = 0
    
    # 遍历所有目录
    for root, dirs, files in os.walk(root_dir):
        # 检查当前目录是否为空
        if is_directory_empty(root):
            gitkeep_path = os.path.join(root, ".gitkeep")
            # 检查.gitkeep文件是否已存在
            if not os.path.exists(gitkeep_path):
                try:
                    with open(gitkeep_path, "w") as f:
                        f.write("")
                    print(f"在目录 {root} 中创建了 .gitkeep 文件")
                    created_count += 1
                except Exception as e:
                    print(f"在目录 {root} 中创建 .gitkeep 文件时出错: {e}")
    
    return created_count

def main():
    print(f"开始在项目 {PROJECT_ROOT} 中为所有空目录创建 .gitkeep 文件...")
    
    if not os.path.exists(PROJECT_ROOT):
        print(f"错误: 项目目录 {PROJECT_ROOT} 不存在")
        sys.exit(1)
    
    created_count = create_gitkeep_in_empty_dirs(PROJECT_ROOT)
    
    print(f"\n操作完成！")
    print(f"共在 {created_count} 个空目录中创建了 .gitkeep 文件")

if __name__ == "__main__":
    main()