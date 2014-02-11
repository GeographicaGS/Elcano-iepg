# -*- coding: utf-8 -*-
# coding=UTF8

import iepgdataimport.core as core
reload(core)

l = core.FileLoader('backend/Energy_2.csv', '\r', 'mac_roman')

c = core.ImportIepgData(l.readFile())
c.processData()

