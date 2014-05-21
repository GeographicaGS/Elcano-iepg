import maplex.maplex as maplex
reload(maplex)
import maplex.maplexmodel as maplexmodel
reload(maplexmodel)
import common.helpers as helpers
reload(helpers)

print(maplex.getNames(idNameFamily=1))

blocks = maplex.getBlocks()
for b in blocks:
    print(b["id_geoentity_block"])
    print(maplex.getBlockMembers(b["id_geoentity_block"]))
    print(helpers.getListFromDictionary(maplex.getBlockMembers(b["id_geoentity_block"]), "id_geoentity_child"))



