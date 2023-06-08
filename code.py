import undetected_chromedriver as uc
from a_selenium_screenshots_all_elements import get_screenshots_from_all_elements

if __name__ == "__main__":
    driver = uc.Chrome()
    driver.get(r"https://www.google.com")
    get_screenshots_from_all_elements(driver, saveinfolder='c:\\googlescreenshots',
                                      cutinfos=120)  # cutinfos = max letters in one line



