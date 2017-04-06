#!/usr/bin/env python
#-*- coding: utf-8 -*-
# componentes para un vector

import math

dist = 200
grados = 30

def magnitud(dist, grados):
    g = math.radians(grados)
    i = dist * math.cos(g)
    j = dist * math.sin(g)
    mag = math.sqrt(i ** 2+ j ** 2)
    print "las componentes del vector ({} i),({} j) ".format(i,j)
    print "la magnitud del vector es :\n{}".format(mag)

magnitud(dist,grados)
