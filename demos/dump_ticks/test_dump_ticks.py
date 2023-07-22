from wtpy.wrapper import WtDataHelper
import os

dtHelper = WtDataHelper()
# the python running in wtpy/demos/dump_ticks/ folder
dtHelper.dump_ticks(binFolder="../storage/bin/ticks/", csvFolder='./ticks_csv/')
