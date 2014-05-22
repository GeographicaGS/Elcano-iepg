import maplex.maplex as maplex
reload(maplex)
import maplex.maplexmodel as maplexmodel
reload(maplexmodel)
import common.helpers as helpers
reload(helpers)

print maplex.getGeoentityBlocks(40, year=2010)
