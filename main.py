import pyowm

owm = pyowm.OWM("2cce969ca161ecf172633f34084f3787")

place=input('Enter the city whose weather you want to know:\n')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
temp=w.temperature('celsius')['temp']
print('In the town '+place+' now '+w.detailed_status)
print('temperature now '+str(temp)+' degrees celsius')