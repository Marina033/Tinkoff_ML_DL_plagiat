from pathlib import Path

import numpy as np
import argparse
import ast

def levenstein(fst: str, snd: str) -> int:
    if fst == snd:
        return 0
    
    mat = np.zeros((len(fst) + 1, len(snd) + 1))
    mat[0, :] = np.arange(mat.shape[1])
    mat[:, 0] = np.arange(mat.shape[0]).T

    for i in range(1, mat.shape[0]):
        for j in range(1, mat.shape[1]):
            mat[i, j] = min(mat[i, j-1] + 1, mat[i-1, j] + 1, mat[i-1, j-1] + (fst[i-1] != snd[j-1]))

    return int(mat[-1, -1])

def create_ast(s: str) -> str:
    tree = ast.parse(s)
    txt = ast.dump(tree, annotate_fields=False)
    
    for i in [" ", "\n", "(", ")", "[", "]", ","]:
        txt = txt.replace(i, "")

    for i in ['None'] + [s for s in dir(ast) if s[0].isalpha()]:
        txt = txt.replace(i, i[0])
    
    for idx, i in enumerate({node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}):
        txt = txt.replace(i, str(idx))

    return txt

def compare(s1: str, s2: str) -> float:
    s1 = create_ast(Path(s1).read_text())
    s2 = create_ast(Path(s2).read_text())

    return 1 - levenstein(s1, s2) / max(len(s1), len(s2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path")

    args = parser.parse_args()

    files = Path(args.path).read_text().split("\n")

    Path("results.txt").write_text("\n".join([str(compare(*i.split(" "))) for i in files]))
    