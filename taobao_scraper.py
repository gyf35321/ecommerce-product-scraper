import os
import time
import json
import random
import requests
from hashlib import md5

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


OUTPUT_DIR = "output_taobao"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# 🔥 控制参数（你可以自己改）
MAX_ITEMS = 50              # 每次最多抓多少个商品
SCROLL_ROUNDS = 10         # 滚动次数
SLEEP_MIN = 0.5
SLEEP_MAX = 1.5

os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_driver():
    print("🔗 接管浏览器...")
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def human_sleep():
    time.sleep(random.uniform(SLEEP_MIN, SLEEP_MAX))


def human_scroll(driver):
    print("⬇️ 模拟人工滚动...")
    for i in range(SCROLL_ROUNDS):
        driver.execute_script("window.scrollBy(0, 500)")
        human_sleep()


def find_products(driver):
    print("🔍 查找商品主图...")

    imgs = driver.find_elements(
        By.XPATH,
        "//img[contains(@src,'alicdn')]"
    )

    print(f"👉 原始找到 {len(imgs)} 张图")

    # 🔥 限制数量（关键安全策略）
    imgs = imgs[:MAX_ITEMS]

    print(f"✅ 只取前 {len(imgs)} 张（安全模式）")

    return imgs


def extract_data(img):
    src = img.get_attribute("src") or img.get_attribute("data-src")

    if not src:
        return None

    # ❌ 过滤无效图
    if "tbstatic" in src:
        return None

    if "50x50" in src or "30x30" in src:
        return None

    return {
        "image_url": src
    }


def clean_data(data):
    print("🧹 清洗数据...")

    seen = set()
    cleaned = []

    for d in data:
        if not d:
            continue

        url = d["image_url"]

        if url in seen:
            continue

        seen.add(url)
        cleaned.append(d)

    print(f"✅ 最终保留 {len(cleaned)} 张主图")
    return cleaned


def download_images(data):
    print("📥 下载图片...")

    folder = os.path.join(OUTPUT_DIR, "images")
    os.makedirs(folder, exist_ok=True)

    for i, d in enumerate(data, 1):
        try:
            url = d["image_url"]

            res = requests.get(url, headers=HEADERS, timeout=10)
            if res.status_code != 200:
                continue

            name = md5(url.encode()).hexdigest() + ".jpg"
            path = os.path.join(folder, name)

            with open(path, "wb") as f:
                f.write(res.content)

            print(f"下载 {i}/{len(data)}")

            # 🔥 每次下载也加延迟（防风控）
            human_sleep()

        except:
            pass


def main():
    print("====== 半自动安全抓取系统 ======")

    driver = create_driver()

    input("👉 请确保当前页面是商品列表页，然后按回车继续...")

    # 🔥 模拟人类行为
    human_scroll(driver)

    imgs = find_products(driver)

    print("📦 提取数据...")
    raw = [extract_data(i) for i in imgs]

    with open(os.path.join(OUTPUT_DIR, "raw.json"), "w", encoding="utf-8") as f:
        json.dump(raw, f, ensure_ascii=False, indent=2)

    cleaned = clean_data(raw)

    with open(os.path.join(OUTPUT_DIR, "cleaned.json"), "w", encoding="utf-8") as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=2)

    download_images(cleaned)

    print("🎉 完成！（安全模式）")
    input("👉 回车退出...")


if __name__ == "__main__":
    main()