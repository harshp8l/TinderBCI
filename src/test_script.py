#!/usr/local/bin/python2

import numpy as np
from selenium import webdriver
from sklearn.externals import joblib
from selenium.webdriver.common.keys import Keys

def refresh_buttons():
  buttons = []
  buttons.append(driver.find_element_by_xpath("//button[@aria-label='Nope']"))
  buttons.append(driver.find_element_by_xpath("//button[@aria-label='Like']"))
  return buttons

def get_user_response(model):
  pass

def run(model):

  while(True):
    buttons = refresh_buttons()

    action = get_user_response(model)

    if(action == "l"):
      buttons[1].click()
    else:
      buttons[0].click()

def main():
  driver = webdriver.Chrome()
  driver.get("https://tinder.com")

  print "Please manually log in"

  prompt = raw_input("Are you logged in? (y/n): ")

  model = joblib.load('')

  try:
    run(model)
  except(KeyboardInterrupt, EOFError):
    print "Exiting..."
  finally:
    driver.close()

# Boilerplate to run main
if __name__ == '__main__':
  main()

