class amazon_locators(object):
    main_link = 'https://www.amazon.in/'
    search_bar = 'twotabsearchtextbox'  # id
    search_button = '#nav-search > form > div.nav-right > div'  # css_selector
    data_table = '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]'  # xpath
    data_table_backup = '#search > div.s-desktop-width-max.s-opposite-dir > div > div.sg-col-20-of-24.s-matching-dir.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row'


class flipkart_locators(object):
    main_link = 'https://www.flipkart.com/'
    short_cut_link = 'https://www.flipkart.com/search?q=Apple%20iPhone%20XR%20%2864GB%29&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

    close_button = '/html/body/div[2]/div/div/button'  # xpath
    search_bar = '#container > div > div._3ybBIU > div._1tz-RS > div._3pNZKl > div.Y5-ZPI > form > div > div > input'  # css
    search_button = '#container > div > div._3ybBIU > div._1tz-RS > div._3pNZKl > div.Y5-ZPI > form > div > button'  # css_selector
    data_table = '#container > div > div.t-0M7P._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div:nth-child(2)'  # xpath
