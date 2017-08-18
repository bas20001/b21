import pygal
wm = pygal.Worldmap()
wm.title = 'Notrh,Central,and South America'


wm.render_to_file('americas.svg')
