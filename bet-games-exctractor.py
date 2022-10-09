import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import multiprocessing

queue = multiprocessing.Queue(maxsize=2)
