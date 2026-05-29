import networkx as nx
import matplotlib.pyplot as plt

# create knowledgegraph
KG = nx.DiGraph()

KG.add_node("Student", type="Student")
KG.add_node("Harry Potter", type="Book")
KG.add_node("The Hunger Games", type="Book")
KG.add_node("The Maze Runner", type="Book")
KG.add_node("The Chronicles of Narnia", type="Book")

# authors
KG.add_node("J.K. Rowling", type="Author")
KG.add_node("Suzanne Collins", type="Author")
KG.add_node("James Dashner", type="Author")
KG.add_node("C.S. Lewis", type="Author")

# genres
KG.add_node("Fantasy", type="Genre")
KG.add_node("Dystopian Fiction", type="Genre")
KG.add_node("Science Fiction", type="Genre")

# relationships
# Harry Potter
KG.add_edge(
    "Harry Potter",
    "J.K. Rowling",
    relation="written_by"
)

KG.add_edge(
    "Harry Potter",
    "Fantasy",
    relation="belongs_to"
)

# The Hunger Games
KG.add_edge(
    "The Hunger Games",
    "Suzanne Collins",
    relation="written_by"
)

KG.add_edge(
    "The Hunger Games",
    "Dystopian Fiction",
    relation="belongs_to"
)

# The Maze Runner
KG.add_edge(
    "The Maze Runner",
    "James Dashner",
    relation="written_by"
)

KG.add_edge(
    "The Maze Runner",
    "Science Fiction",
    relation="belongs_to"
)

# The Chronicles of Narnia
KG.add_edge(
    "The Chronicles of Narnia",
    "C.S. Lewis",
    relation="written_by"
)

KG.add_edge(
    "The Chronicles of Narnia",
    "Fantasy",
    relation="belongs_to"
)

# borrowed
KG.add_edge(
    "Student",
    "Harry Potter",
    relation="borrowed"
)

print("\nKNOWLEDGE GRAPH\n")

for source, target, data in KG.edges(data=True):
    print(
        f"{source} --[{data['relation']}]--> {target}"
    )

print("\nBooks borrowed by Student")
for source, target, data in KG.edges(data=True):
    if source == "Student" and data["relation"] == "borrowed":
        print("-", target)

print("\nBooks written by C.S. Lewis")
for book, author, data in KG.edges(data=True):
    if author == "C.S. Lewis" and data["relation"] == "written_by":
        print("-", book)

print("\nBooks in Fantasy")
for book, genre, data in KG.edges(data=True):
    if genre == "Fantasy" and data["relation"] == "belongs_to":
        print("-", book)

print("\nGraph Statistics")
print("Nodes :", KG.number_of_nodes())
print("Edges :", KG.number_of_edges())

# graph visulaization
plt.figure(figsize=(14, 10))

pos = nx.spring_layout(
    KG,
    k=2.5,
    iterations=100,
    seed=42
)

nx.draw(
    KG,
    pos,
    with_labels=True,
    node_size=3500,
    font_size=10,
    arrows=True
)

edge_labels = {
    (u, v): d["relation"]
    for u, v, d in KG.edges(data=True)
}

nx.draw_networkx_edge_labels(
    KG,
    pos,
    edge_labels=edge_labels,
    font_size=9
)

plt.title("Library Knowledge Graph")
plt.axis("off")
plt.show()
