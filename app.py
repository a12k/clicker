import pyautogui, sys, time
from datetime import datetime
import click
import logging

logging.basicConfig(filename="clicker.log", level=logging.DEBUG)
logger = logging.getLogger("clicker")


pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


def image_search(image_to_search):
    try:
        modal = pyautogui.locateOnScreen(image_to_search, confidence=0.8)
    except:
        modal = None
    return modal


def click_modal(modal):
    modal_center = pyautogui.center(modal)
    pyautogui.click(modal_center)


def search_loop(image, interval):
    modal = image_search(image)
    if modal:
        click_modal(modal)
        logging.info("clicked {} {} {}".format(datetime.now(), image, str(interval)))
        print("\n\nmodal clicked at {}!!\n\n".format(datetime.now()))
    else:
        logging.info("not found {} {} {}".format(datetime.now(), image, str(interval)))
        print(
            "not found at {}, trying again in {}".format(datetime.now(), str(interval))
        )


@click.command()
@click.option("--image", default="click.png", prompt="image", help="name of image")
@click.option(
    "--interval", default=30, prompt="loop interval", help="the interval to search on."
)
def main_loop(image, interval):
    logger.info("starting loop {} {} {}".format(datetime.now(), image, str(interval)))
    print("starting...")
    search_loop(image, interval)
    while True:
        time.sleep(interval)
        search_loop(image, interval)


if __name__ == "__main__":
    main_loop()
