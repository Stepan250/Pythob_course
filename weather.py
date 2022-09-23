from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
 
owm = OWM('17a3dd6cb2cf944d512e798ec1b3ad75')
mgr = owm.weather_manager()

place = input(" В каком городе/стране? ") 
observation = mgr.weather_at_place(place)
w = observation.weather
 
temp = w.temperature('celsius')["temp"]

print( "В городе " + place + " сейчас " + str(w) )
print( "Tемпература сейчас в районе " + str(temp))

if temp < 10:
    print( "Сейчас ппц как холодно, одевайся очень тепло!" )
elif temp < 20:
    print( "Сейчас прохладно одевайся теплее." )
else:
    print( "Температура норм, надевай что угодно." )