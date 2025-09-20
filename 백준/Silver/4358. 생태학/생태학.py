import sys

tree_count = {}
total_trees = 0

while True:
    tree = sys.stdin.readline().strip()
    if not tree:
        break

    if tree not in tree_count:
        tree_count[tree] = 1
    else:
        tree_count[tree] += 1

    total_trees += 1

for tree in sorted(tree_count.keys()):
    percentage = (tree_count[tree] / total_trees) * 100
    print(tree, f"{percentage:.4f}")