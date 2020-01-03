"""Usefull links

Tuto: https://code-maven.com/create-images-with-python-pil-pillow

"""
import json
import os

from tqdm import tqdm
import networkx as nx
from networkx.drawing.nx_pydot import write_dot, to_pydot

HERE = os.path.dirname(os.path.abspath(__file__))


class DataGenerator1:
    def __init__(self, path, test_mode=False):
        self.path = path
        self.path_img = os.path.join(self.path, "img")
        self.path_dot = os.path.join(self.path, "dot")
        self.setup()
        self.test_mode = test_mode  # test or prod
        self.node_shapes = ["rectangle", "square", "ellipse", "egg", "circle"]
        self.graph_depth = (1, 11)
        self.layouts = ["neato", "dot", "twopi", "circo", "fdp"]
        self.arrowheads = ["normal", "vee", "onormal"]
        self.data_size = (
            len(self.node_shapes)
            * (self.graph_depth[1] - self.graph_depth[0])
            * len(self.layouts)
            * len(self.arrowheads)
        )
        print("data size = ", self.data_size)

    def setup(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            print(f"Created {self.path}")

        if not os.path.exists(self.path_img):
            os.makedirs(self.path_img)
            print(f"Created {self.path_img}")

        if not os.path.exists(self.path_dot):
            os.makedirs(self.path_dot)
            print(f"Created {self.path_dot}")

    def create(self):
        r = 1
        # l = "dot"  # layout
        for h in tqdm(range(*self.graph_depth)):
            G = nx.balanced_tree(r=r, h=h, create_using=nx.DiGraph)
            dot_is_written = False
            g_dot_name = f"r-{r}_h-{h}"

            for l in self.layouts:
                for n_shape in self.node_shapes:
                    for arrowhead in self.arrowheads:
                        g_fname = f"{g_dot_name}_nsh-{n_shape}_l-{l}_ah-{arrowhead}"

                        gphz_G = nx.nx_agraph.to_agraph(G)

                        if not dot_is_written:
                            with open(
                                os.path.join(self.path_dot, f"{g_dot_name}.dot"), "w"
                            ) as fdot:
                                fdot.write(gphz_G.to_string())
                            dot_is_written = True

                        gphz_G.node_attr["shape"] = n_shape
                        gphz_G.edge_attr["arrowhead"] = arrowhead

                        gphz_G.draw(
                            os.path.join(self.path_img, f"{g_fname}.png"),
                            format="png",
                            prog=l,
                        )
