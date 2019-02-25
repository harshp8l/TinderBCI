#!/usr/local/bin/python2

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def refresh_buttons():
  buttons = []
  buttons.append(driver.find_element_by_xpath("//button[@aria-label='Nope']"))
  buttons.append(driver.find_element_by_xpath("//button[@aria-label='Like']"))
  return buttons

if __name__ == "__main__":

  driver = webdriver.Chrome()
  driver.get("https://tinder.com")

  print "Please manually log in"

  prompt = raw_input("Are you logged in? (y/n): ")

  try:
    while(True):
      buttons = refresh_buttons()

      action = raw_input("(l)ike or (d)islike?: ")

      if(action == "like"):
        buttons[1].click()
      else:
        buttons[0].click()

  except(KeyboardInterrupt, EOFError):
    print "Exiting..."
  finally:
    driver.close()
