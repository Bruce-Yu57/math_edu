# 國中數學教學資源平台

## 專案簡介
這是一個專為國中數學教師和學生設計的綜合性教學資源平台。平台提供教學資源管理、影片教學、互動練習、討論交流等功能。

## 主要功能
- 教學資源庫：教案、課件、試卷的上傳和下載
- 教學影片：數學概念講解和解題技巧影片
- 學生專區：互動式練習題和學習進度追蹤
- 論壇交流：教師和學生交流平台
- 用戶管理：支持教師和學生角色區分

## 技術需求
- Python 3.9+
- Django 5.0.1
- 其他依賴項請參見 requirements.txt

## 安裝說明
1. 創建虛擬環境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. 安裝依賴：
```bash
pip install -r requirements.txt
```

3. 執行數據庫遷移：
```bash
python manage.py migrate
```

4. 啟動開發服務器：
```bash
python manage.py runserver
```

## 開發團隊
- [您的姓名] - 項目負責人

## 版本信息
- 版本：1.0
- 更新日期：2025年2月14日
