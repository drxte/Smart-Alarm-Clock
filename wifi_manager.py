import machine
import network
import config
import time
import socket
import struct

class WiFiManager:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)
        self.oled = config.get_display().get_oled()

    def connect(self):
        self.wlan.active(False)
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)

        self.oled.fill(0)
        self.oled.text("Hello!", 15, 5)
        self.oled.show()
        time.sleep(1)

        a = "."
        while not self.wlan.isconnected():
            self.oled.fill(0)
            if a == "....":
                a = "."
            self.oled.text("Connecting" + a, 15, 5)
            self.oled.show()
            a += "."
            time.sleep(0.5)

        self.oled.fill(0)
        self.oled.text("Connected!", 10, 5)
        self.oled.show()
        time.sleep(1)

    def get_time_from_ntp(self):
        addr = socket.getaddrinfo("pool.ntp.org", 123)[-1][-1]
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(2)

        NTP_QUERY = b'\x1b' + b'\x00' * 47
        s.sendto(NTP_QUERY, addr)

        msg, r_addr = s.recvfrom(48)
        s.close()

        val = struct.unpack("!I", msg[40:44])[0]
        net_seconds = val - 3155673600

        TIMEZONE_OFFSET = 1 * 3600 
        final_seconds = net_seconds + TIMEZONE_OFFSET

        tm = time.localtime(final_seconds)
        machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))