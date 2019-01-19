import osrparse
from config import PATH_REPLAYS_USER, PATH_REPLAYS_CHECK, WHITELIST
from replay import Replay
from comparer import Comparer

parsed_replay = osrparse.parse_replay_file(PATH_REPLAYS_USER[0], pure_lzma=True)
replay_data = parsed_replay.play_data

replay1 = [Replay(replay_data, "reshi")]

parsed_replay = osrparse.parse_replay_file(PATH_REPLAYS_CHECK[0], pure_lzma=True)
replay_data = parsed_replay.play_data

replay2 = [Replay(replay_data, "nanako")]

comparer = Comparer(10000, replay1, replays2=replay2)
comparer.compare(mode="double")