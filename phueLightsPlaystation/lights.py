from phue import Bridge


bridge = Bridge("YOUR IP ADDRESS")


#Error will go away once you put your own bridge ip
bridge.connect()


lights = bridge.get_light_objects('name')




def connect():
    lights["Top light"].hue = 50000
    lights["Top light east"].hue = 45000
    lights["Nightstand lamp"].hue = 250

    lights["Top light"].saturation = 250
    lights["Top light east"].saturation = 250
    lights["Nightstand lamp"].saturation = 250

    lights["Top light"].brightness = 125
    lights["Top light east"].brightness = 125
    lights["Nightstand lamp"].brightness = 125

def notConnected():
    lights["Top light"].saturation = 100
    lights["Top light east"].saturation = 100
    lights["Nightstand lamp"].saturation = 100

    lights["Top light"].brightness = 250
    lights["Top light east"].brightness = 250
    lights["Nightstand lamp"].brightness = 250


