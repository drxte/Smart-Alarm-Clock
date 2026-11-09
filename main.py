import wifi_manager
import nightlight
import config
import time

network = wifi_manager.WiFiManager("iPhone KY", "ovtu4144")

#network = wifi_manager.WiFiManager("WIFI ZSSK", "")

network.connect()
network.get_time_from_ntp()

display = config.get_display()
display.show_time()
#time.sleep(2)
#display.volume_level_screen()
#time.sleep(10)

nightlight.nightlight()