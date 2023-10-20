import matplotlib.pyplot as plt
import networkx as nx

# Создаем направленный граф
G = nx.DiGraph()

# Добавляем узлы для функциональных требований с определенным атрибутом
functional_requirements = [
    "Virtual Tours", "Interactive Maps", "Online Consultations",
    "Reviews and Ratings", "Social Media Integration"
]
G.add_nodes_from(functional_requirements, type="Functional Requirement")

# Добавляем узлы для нефункциональных требований с определенным атрибутом
non_functional_requirements = [
    "Usability", "Reliability and Stability", "Mobile Adaptation",
    "High Performance and Speed", "Data Security"
]
G.add_nodes_from(non_functional_requirements, type="Non-functional Requirement")

# Определяем рёбра на основе выявленных отношений
edges_with_labels = {
    ("Virtual Tours", "Usability"): "impacts",
    ("Virtual Tours", "Mobile Adaptation"): "impacts",
    ("Virtual Tours", "High Performance and Speed"): "impacts",
    ("Interactive Maps", "Usability"): "impacts",
    ("Interactive Maps", "Mobile Adaptation"): "impacts",
    ("Interactive Maps", "High Performance and Speed"): "impacts",
    ("Online Consultations", "Reliability and Stability"): "impacts",
    ("Online Consultations", "Data Security"): "impacts",
    ("Online Consultations", "Mobile Adaptation"): "impacts",
    ("Reviews and Ratings", "Data Security"): "includes",
    ("Social Media Integration", "Usability"): "impacts",
    ("Social Media Integration", "Data Security"): "includes",
    ("Social Media Integration", "Mobile Adaptation"): "impacts",
}

# Добавляем рёбра в граф
G.add_edges_from(edges_with_labels.keys())

# Определяем позиции для узлов вручную, чтобы избежать наложения
pos = {
    "Virtual Tours": (0, 1),
    "Interactive Maps": (1, 1),
    "Online Consultations": (2, 1),
    "Reviews and Ratings": (1.5, 0),
    "Social Media Integration": (0.5, 10),
    "Usability": (0, -1),
    "Reliability and Stability": (1, -1),
    "Mobile Adaptation": (2, -1),
    "High Performance and Speed": (1.5, -2),
    "Data Security": (0.5, -2),
}

# Рисуем граф
plt.figure(figsize=(12, 8))

# Рисуем узлы
nx.draw_networkx_nodes(G, pos, nodelist=functional_requirements, node_color='skyblue', label='Functional Requirements')
nx.draw_networkx_nodes(G, pos, nodelist=non_functional_requirements, node_color='lightcoral', label='Non-functional Requirements')

# Рисуем рёбра
nx.draw_networkx_edges(G, pos)

# Рисуем подписи к рёбрам
nx.draw_networkx_edge_labels(G, pos, edge_labels=edges_with_labels)

# Рисуем подписи к узлам
nx.draw_networkx_labels(G, pos)

# Показываем легенду и заголовок
plt.legend()
plt.title("Concept Map of Requirements with Explicit Relationships")
plt.show()
