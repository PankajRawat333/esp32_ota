from main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    OTAUpdater.using_network('MI','dehradun')
    ota_updater = OTAUpdater('https://github.com/PankajRawat333/esp32_ota')
    ota_updater.check_for_update_to_install_during_next_reboot()
    ota_updater.download_and_install_update_if_available('MI','dehradun')

def start():
    from main.led import Led
    led = Led()
    led.blink()

def boot():
    download_and_install_update_if_available()
    start()

boot()