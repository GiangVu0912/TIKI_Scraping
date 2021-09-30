# install selenium and other resources for crawling data
!pip install selenium
!apt-get update
!apt install chromium-chromedriver

# Import library
import re
import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Header for chromedriver
HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}
# Urls
TIKI                = 'https://tiki.vn'
MAIN_CATEGORIES = [
    {'Name': 'Điện Thoại - Máy Tính Bảng',
     'URL': 'https://tiki.vn/dien-thoai-may-tinh-bang/c1789?src=c.1789.hamburger_menu_fly_out_banner'},

    {'Name': 'Điện Tử - Điện Lạnh',
     'URL': 'https://tiki.vn/tivi-thiet-bi-nghe-nhin/c4221?src=c.4221.hamburger_menu_fly_out_banner'},

    {'Name': 'Phụ Kiện - Thiết Bị Số', 
     'URL': 'https://tiki.vn/thiet-bi-kts-phu-kien-so/c1815?src=c.1815.hamburger_menu_fly_out_banner'},

    {'Name': 'Laptop - Thiết bị IT', 
     'URL': 'https://tiki.vn/laptop-may-vi-tinh/c1846?src=c.1846.hamburger_menu_fly_out_banner'},

    {'Name': 'Máy Ảnh - Quay Phim', 
     'URL': 'https://tiki.vn/may-anh/c1801?src=c.1801.hamburger_menu_fly_out_banner'},

    {'Name': 'Điện Gia Dụng', 
     'URL': 'https://tiki.vn/dien-gia-dung/c1882?src=c.1882.hamburger_menu_fly_out_banner'},

    {'Name': 'Nhà Cửa Đời Sống', 
     'URL': 'https://tiki.vn/nha-cua-doi-song/c1883?src=c.1883.hamburger_menu_fly_out_banner'},

    {'Name': 'Hàng Tiêu Dùng - Thực Phẩm', 
     'URL': 'https://tiki.vn/bach-hoa-online/c4384?src=c.4384.hamburger_menu_fly_out_banner'},

    {'Name': 'Đồ chơi, Mẹ & Bé', 
     'URL': 'https://tiki.vn/me-va-be/c2549?src=c.2549.hamburger_menu_fly_out_banner'},

    {'Name': 'Làm Đẹp - Sức Khỏe', 
     'URL': 'https://tiki.vn/lam-dep-suc-khoe/c1520?src=c.1520.hamburger_menu_fly_out_banner'},

    {'Name': 'Thể Thao - Dã Ngoại', 
     'URL': 'https://tiki.vn/the-thao/c1975?src=c.1975.hamburger_menu_fly_out_banner'},

    {'Name': 'Xe Máy, Ô tô, Xe Đạp', 
     'URL': 'https://tiki.vn/o-to-xe-may-xe-dap/c8594?src=c.8594.hamburger_menu_fly_out_banner'},

    {'Name': 'Hàng quốc tế', 
     'URL': 'https://tiki.vn/hang-quoc-te/c17166?src=c.17166.hamburger_menu_fly_out_banner'},

    {'Name': 'Sách, VPP & Quà Tặng', 
     'URL': 'https://tiki.vn/nha-sach-tiki/c8322?src=c.8322.hamburger_menu_fly_out_banner'},

    {'Name': 'Voucher - Dịch Vụ - Thẻ Cào', 
     'URL': 'https://tiki.vn/voucher-dich-vu/c11312?src=c.11312.hamburger_menu_fly_out_banner'}
]

start_driver(force_restart=True)

i = 0
while i< len(MAIN_CATEGORIES):
    main_cat_url = MAIN_CATEGORIES[i]['URL']
    main_cat_name = MAIN_CATEGORIES[i]['Name']
    for e in range(1,3):
        page_url = re.sub(r'([\w\/\-\.\:]+\?)(src[\w\/\-\.\:\=]+)', r'\1page={}&\2'.format(e), main_cat_url)
        data = get_product_info_from_page(page_url)
        df = pd.DataFrame(data, columns=data[0].keys())
        df.to_csv(f'tiki_products_{main_cat_name}_page{e}.csv')
    i += 1
    
close_driver()
