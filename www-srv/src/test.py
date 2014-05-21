import common.timelapse as timelapse
reload(timelapse)
import maplex.core as core
reload(core)

tl01 = timelapse.TimeLapse()
tl01.initByStrings("1990-01-01 00:00", None)
print(tl01)
print(tl01.getSqlFilter(["a", "b"]))

print(core.getBlocks(timeLapseBlock=tl01))
