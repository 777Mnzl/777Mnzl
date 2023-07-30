from segno import helpers

qrcode = helpers.make_wifi(
    ssid='enter your wifi name here',
    password='enter your password here',
    security='WPA'
)

qrcode.designator
'3-M'
qrcode.save('wifi.png', scale=10)
