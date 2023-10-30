from aStar_heuristic1_visualizer import AStar_heuristic_1
from aStar_heuristic2_visualizer import AStar_heuristic_2
from bfs_visualizer import BFS
from dfs_visualizer import DFS
from GBFS_heuristic1_visualizer import  GBFS_heuristic_1
from GBFS_heuristic2_visualizer import GBFS_heuristic_2
from gift_aStar import AStarGreedy
from teleport_visualizer import TeleBFS
from GBFS_station import GBFS_station
from ucs_visualizer import USC
import os

INPUT_ROOT="../input/"

def solve(prob_path):
    for f in os.listdir(prob_path):
        file_path = os.path.join(prob_path, f)
        if os.path.isfile(file_path):
            if "level_1" in prob_path:
                BFS(file_path)
                DFS(file_path)
                GBFS_heuristic_1(file_path)
                GBFS_heuristic_2(file_path)
                USC(file_path)
            elif "level_2" in prob_path:
                AStarGreedy(file_path)
            elif "level_3" in prob_path:
                GBFS_station(file_path)
            elif "advance" in prob_path:
                TeleBFS(file_path)
def main():
    solve(INPUT_ROOT + "level_1/")
    solve(INPUT_ROOT + "level_2/")
    #solve(INPUT_ROOT + "level_3/")
    solve(INPUT_ROOT + "advance/")

if __name__ == "__main__":
    main()