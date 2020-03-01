from main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    ota_updater = OTAUpdater('https://github.com/PankajRawat333/esp32_ota')
    ota_updater.download_and_install_update_if_available('MI', 'dehradun')

def start():
    from main.led import Led
    led = Led()
    led.blink()

def boot():
    download_and_install_update_if_available()
    start()


boot()
