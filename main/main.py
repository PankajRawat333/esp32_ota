from ota_update.main.ota_updater import OTAUpdater
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

 def download_and_install_update_if_available():
     o = OTAUpdater('https://github.com/PankajRawat333/esp32_ota')
     o.download_and_install_update_if_available('MI', 'dehradun')


 def start():
    while True:
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)


 def boot():
     download_and_install_update_if_available()
     start()


 boot()
