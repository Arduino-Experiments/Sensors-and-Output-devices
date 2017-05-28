import SchemDraw as schem
import SchemDraw.elements as e

d = schem.Drawing()

rinputs = {
    'cnt':1,
    'labels':['port_13']
}
binputs = {'cnt':1,
    'labels':['GND']
}

linputs = {
    'cnt':2,
    'labels':['port_11','port_3_3v']
}

d = schem.Drawing()
ARDUINO = e.blackbox(d.unit*1.3, d.unit*2.25,
rinputs=rinputs,
binputs=binputs,
linputs=linputs,
mainlabel='ARDUINO')

T = d.add(ARDUINO)
d.push()
d.add(e.RBOX,label='1000$\Omega$',xy=T.port_13)
d.add(e.LED,d='down')
d.add(e.GND)
d.pop()
d.push()
Line1 = d.add(e.LINE,xy=T.port_11,d='left',tox=T.port_11+[-0.5,0])
r1 = d.add(e.RBOX,label='1000$\Omega$',xy=Line1.end,d="down")
Line2=d.add(e.LINE,xy=r1.end,tox=T.GND,d='right')
d.add(e.LINE,xy=T.GND,toy=Line2.end,d='down')
d.pop()
Line3 = d.add(e.LINE,xy=T.port_3_3v,d='left',tox=T.port_3_3v+[-0.5,0])

d.add(e.SWITCH_SPST,xy=Line3.end,toy=Line1.end,d='down')

d.draw()
d.save('source/switch.eps')
