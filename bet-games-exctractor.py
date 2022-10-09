import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import multiprocessing

queue = multiprocessing.Queue(maxsize=2)


def find_data(url):
    driver = get_driver(url)
    time.sleep(10)
    all_iframes = driver.find_elements_by_tag_name('iframe')
    driver.switch_to.frame(all_iframes[1])
    all_titles = driver.find_elements_by_css_selector('div.game-title')[6].click()
    time.sleep(1)
    all_samples = driver.find_elements_by_css_selector('div.game-result')
    all_times = driver.find_elements_by_css_selector('div.last-results-item-time')

    collect_data(all_titles, all_samples, all_times)


def get_driver(url):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(url)
    return driver


def collect_data(all_titles, all_samples, all_times):
    for index, sample in enumerate(all_samples):
        balls = sample.find_elements_by_css_selector('span.ball-item').text
        queue.put(balls)
        queue.append(all_times[index])
    return


def save_data(loca_file):
    with open(loca_file, 'w+') as f:
        f.write(queue.get())


if __name__ == '__main__':
    find_data("https://www.bet.co.za/bet-games/")
    save_data('data_scraping.txt')
