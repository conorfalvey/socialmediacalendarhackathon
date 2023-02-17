import asyncio
import nfl_data_py as nfl
from producers import ScheduleProducer

class Consumer:
    async def consume(self, event):
        pass

class ScheduleConsumer(Consumer):
    def consume(self, event):
        # season_df = await nfl.import_schedules([2022])
        season_df = nfl.import_schedules([2022])
        season_df = season_df.loc[season_df["gameday"] == str(event.date)]
        # season_df = season_df.loc[season_df["gameday"] >= str(event.date)]
        season_df = season_df[["game_id", "gameday", "gametime"]]
        print(season_df)
        return season_df
        # ScheduleProducer().produce(season_df)

class RecordConsumer(Consumer):
    async def consume(self, event):
        #TODO logic
        print("TBD")
        return