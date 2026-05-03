import os

def clean_empty_image_folders(vault_path, target_folder_name="image"):
    print(f"开始扫描库路径: {vault_path}\n" + "-"*40)
    
    deleted_count = 0
    skipped_count = 0
    
    # 使用 topdown=False 进行自底向上遍历，这样在删除深层目录时更安全
    for root, dirs, files in os.walk(vault_path, topdown=False):
        for dir_name in dirs:
            if dir_name == target_folder_name:
                dir_path = os.path.join(root, dir_name)
                
                # 检查文件夹是否为空
                # os.listdir() 如果返回空列表 []，说明里面没有任何文件或子文件夹
                if not os.listdir(dir_path):
                    try:
                        os.rmdir(dir_path) # rmdir 只能删除空文件夹，这是一道天然的安全锁
                        print(f"✅ [已删除] 空文件夹: {dir_path}")
                        deleted_count += 1
                    except Exception as e:
                        print(f"❌ [删除失败] {dir_path}，错误信息: {e}")
                else:
                    print(f"⚠️ [跳过保留] 非空文件夹: {dir_path}")
                    skipped_count += 1

    print("-" * 40)
    print(f"🎉 清理任务完成！")
    print(f"👉 共删除了 {deleted_count} 个空的 '{target_folder_name}' 文件夹。")
    if skipped_count > 0:
        print(f"👉 另外跳过了 {skipped_count} 个非空文件夹（里面可能还有没引用的孤儿图片）。")

if __name__ == "__main__":
    # ==========================================
    # ⚠️ 请在这里填入你的 Obsidian 库的真实绝对路径
    # 注意：Windows 路径前面建议保留字母 r，防止斜杠转义报错
    # ==========================================
    VAULT_PATH = r"E:\Vault Example\git同步×附件分离"
    
    # 如果你的图片文件夹不叫 image，而是 images 或别的，可以修改下面这个参数
    target_folder_name = "image" 
    
    if os.path.exists(VAULT_PATH):
        clean_empty_image_folders(VAULT_PATH, target_folder_name="image")
    else:
        print("❌ 错误：找不到指定的路径，请检查 VAULT_PATH 是否填写正确！")