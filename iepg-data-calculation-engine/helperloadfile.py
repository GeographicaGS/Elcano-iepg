# -*- coding: utf-8 -*-
# coding=UTF8

import iepgdataimport.core as core
import iepgdataimport.postgresqlutils as postgresqlutils
reload(core)

# l = core.FileLoader('backend/Energy_2.csv', '\r', 'mac_roman')

# c = core.ImportIepgData(l.readFile())
# c.processData()

m = postgresqlutils.PostgreSqlUtils()
m.createTable('iepg_data', 'test_table', ['field1', 'field2'], ['integer', 'varchar(10)'])

