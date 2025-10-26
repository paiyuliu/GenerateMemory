#!/usr/bin/env python3

import os
import glob
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

def get_photo_datetime(image_path):
    """
    從圖片的 EXIF 資訊中取得拍照日期時間
    返回格式: yyyyMMddHHmmss
    """
    try:
        # 開啟圖片
        image = Image.open(image_path)
        
        # 取得 EXIF 資訊
        exifdata = image.getexif()
        
        # 查找拍照日期時間
        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            
            # 尋找 DateTime 或 DateTimeOriginal
            if tag in ['DateTime', 'DateTimeOriginal']:
                # EXIF 日期格式通常是 "YYYY:MM:DD HH:MM:SS"
                try:
                    # 解析日期時間
                    dt = datetime.strptime(str(data), "%Y:%m:%d %H:%M:%S")
                    # 轉換為 yyyyMMddHHmmss 格式
                    return dt.strftime("%Y%m%d%H%M%S")
                except ValueError:
                    continue
        
        return "無法取得拍照時間"
        
    except Exception as e:
        return f"讀取失敗: {str(e)}"

def generate_new_filename(old_filename, photo_datetime):
    """
    根據拍照時間生成新檔名
    例如: BOY_0001.JPG -> BOY_20251026083016.JPG
    """
    if photo_datetime == "無法取得拍照時間" or photo_datetime.startswith("讀取失敗"):
        return None  # 無法重命名
    
    # 取得檔案副檔名
    file_ext = os.path.splitext(old_filename)[1]  # .JPG
    
    # 生成新檔名: BOY_yyyyMMddHHmmss.JPG
    new_filename = f"BOY_{photo_datetime}{file_ext}"
    
    return new_filename

def preview_rename_operations():
    """
    預覽所有的重命名操作，讓用戶確認
    """
    # 尋找所有 JPG 檔案
    jpg_files = glob.glob("*.JPG")
    jpg_files.sort()
    
    if not jpg_files:
        print("未找到任何 JPG 檔案")
        return []
    
    rename_operations = []
    
    print(f"找到 {len(jpg_files)} 個 JPG 檔案，準備重命名:")
    print("=" * 80)
    
    for i, old_filename in enumerate(jpg_files, 1):
        # 取得拍照日期時間
        photo_datetime = get_photo_datetime(old_filename)
        
        # 生成新檔名
        new_filename = generate_new_filename(old_filename, photo_datetime)
        
        if new_filename:
            rename_operations.append((old_filename, new_filename))
            print(f"{i:3d}. {old_filename} -> {new_filename}")
        else:
            print(f"{i:3d}. {old_filename} -> [跳過: {photo_datetime}]")
    
    return rename_operations

def execute_rename_operations(rename_operations):
    """
    執行檔案重命名操作
    """
    successful_renames = 0
    failed_renames = 0
    
    print("\n開始執行重命名操作...")
    print("-" * 50)
    
    for old_filename, new_filename in rename_operations:
        try:
            # 檢查目標檔案是否已存在
            if os.path.exists(new_filename):
                print(f"⚠️  跳過 {old_filename}: 目標檔案 {new_filename} 已存在")
                failed_renames += 1
                continue
            
            # 執行重命名
            os.rename(old_filename, new_filename)
            print(f"✅ {old_filename} -> {new_filename}")
            successful_renames += 1
            
        except Exception as e:
            print(f"❌ 重命名失敗 {old_filename}: {str(e)}")
            failed_renames += 1
    
    print("-" * 50)
    print(f"重命名完成! 成功: {successful_renames}, 失敗: {failed_renames}")

def main():
    """
    主程式：預覽並執行 JPG 檔案重命名
    """
    # 取得當前目錄
    current_dir = os.getcwd()
    print(f"掃描目錄: {current_dir}")
    print("=" * 80)
    
    # 預覽重命名操作
    rename_operations = preview_rename_operations()
    
    if not rename_operations:
        print("沒有檔案需要重命名")
        return
    
    # 要求用戶確認
    print(f"\n總共將重命名 {len(rename_operations)} 個檔案")
    confirmation = input("是否繼續執行重命名? (y/N): ").strip().lower()
    
    if confirmation in ['y', 'yes', '是']:
        execute_rename_operations(rename_operations)
    else:
        print("操作已取消")

if __name__ == "__main__":
    main()
