# Function to extract product info from the product
def get_product_info_single(product):
    d = {'name':'',
         'price':'',
         'product_url':'',
         'image':''}

    # name get name through find_element_by_class_name
    try:
        d['name'] = product.find_element_by_class_name('name').find_element_by_tag_name('span').text.strip(' - Hàng Chính Hãng')
    except NoSuchElementException:
        d['name'] = None
        pass

    # get price find_element_by_class_name
    try:
        price_tag = product.find_element_by_class_name('price-discount__price')
        d['price'] = price_tag.text
    except NoSuchElementException:
        d['price'] = None
        pass
    
    # get link from .get_attribute()
    try:
        product_link     = product.get_attribute('href')
        d['product_url'] = product_link
    except NoSuchElementException:
        d['product_url'] = None
        pass
    
    # get thumbnail by class_name and Tag name and get_attribute()
    try:
        thumbart_class = product.find_element_by_class_name('thumbnail')
        thumbnail = thumbart_class.find_element_by_tag_name('img').get_attribute('src')
        d['image'] = thumbnail
    except NoSuchElementException:
        d['image'] = None
        pass
    
    return d

# Function to extract product info from the product 
def get_product_info_from_page(page_url):
    """ Extract info from all products of a specfic page_url on Tiki website
        Args:
            page_url: (string) url of the page to scrape
        Returns:
            data: list of dictionary of products info. If no products shown, return empty list.
    """
    global DRIVER
    
    data = []
    DRIVER.get(page_url) # Use the driver to get info from the product page
    time.sleep(5) ## Must have the sleep function

    products_all = DRIVER.find_elements_by_class_name('product-item')
    print(f'Found {len(products_all)} products')
    data = []
    for product in products_all:
        d = get_product_info_single(product)
        data.append(d)
      
    return data
