import common.timelapse as timelapse
reload(timelapse)
import maplex.core as core
reload(core)
import maplex.maplexmodel
reload(maplex.maplexmodel)

tl01 = timelapse.TimeLapse()
tl01.initByStrings(None, "1989-01-01 00:00")
print(tl01)
print(tl01.getSqlFilter(["a", "b"]))

print(core.getBlocks(timeLapseBlock=tl01))
