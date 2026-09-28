"""
@Time  : 2021/6/9 11:49
@Author: Luoyang
@File  : sdp.py
@Desc  : ""
"""
import pickle

import networkx as nx
from tqdm import tqdm


def get_sdp(edges, subject_index, object_index):
    graph = nx.Graph(edges)
    try:
        paths = nx.shortest_path(graph, source=subject_index, target=object_index)
    except:
        paths = [subject_index, object_index]

    return paths


def write_to_pickle(data, filename):
    with open(filename, 'wb')as fp:
        pickle.dump(data, fp)


if __name__ == '__main__':
    with open("riedel_processed_sdp.pkl", "rb")as fp:
        data = pickle.load(fp)
    index = 0
    num = 0
    for item in tqdm(data["test"]):
        if item["SubPos"][0] >= len(item["X"][0]) or item["ObjPos"][0] >= len(item["X"][0]):
            path = []
        else:
            edges = [(b[0], b[1]) for b in item["DepEdges"][0]]
            path = get_sdp(edges, item["SubPos"][0], item["ObjPos"][0])
        data["test"][index]["sdp"] = [path]
        data["test"][index]["sdp_words"] = [[item["X"][0][i] for i in path]]
        index += 1
        if not path:
            num += 1
    print(num / index)
    write_to_pickle(data, "riedel_processed_sdp2.pkl")
