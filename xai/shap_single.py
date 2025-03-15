import networkx as nx
import re

def parse_dot_file(dot_file_path):
    """Parses the DOT file and returns an undirected graph."""
    graph = nx.Graph()  # Undirected graph

    with open(dot_file_path, 'r') as file:
        dot_data = file.read()

    # Extract edges from the DOT file
    edges = re.findall(r'"(.*?)"\s*->\s*"(.*?)";', dot_data)

    for src, dest in edges:
        graph.add_edge(src, dest)

    return graph

def compute_shapley_scores(graph, target_classes):
    """Computes simplified SHAP-like scores based on connectivity to java.net.* classes."""
    java_net_classes = [node for node in graph.nodes() if node.startswith("java.net.")]

    if not java_net_classes:
        print("No java.net.* classes found in the graph.")
        return {target: 0.0 for target in target_classes}, {}

    # Count how many java.net.* classes are reachable from/to each target class
    reachability_counts = {}
    reachability_details = {}

    for target_class in target_classes:
        if target_class in graph:
            reachable_java_net = [
                java_net_class for java_net_class in java_net_classes
                if nx.has_path(graph, java_net_class, target_class)
            ]
            reachability_counts[target_class] = len(reachable_java_net)
            reachability_details[target_class] = reachable_java_net
        else:
            reachability_counts[target_class] = 0
            reachability_details[target_class] = []

    # Normalize scores to sum to 1 (if total count > 0) for relative importance
    total_connections = sum(reachability_counts.values())
    shapley_scores = {}
    if total_connections > 0:
        for target_class in target_classes:
            shapley_scores[target_class] = reachability_counts[target_class] / total_connections
    else:
        for target_class in target_classes:
            shapley_scores[target_class] = 0.0

    return shapley_scores, reachability_details

def main():
    # Path to the DOT file
    dot_file_path = './GeoPointer_v1.3_classgraph_1.dot'

    # List of classes to prioritize
    target_classes = [
        "com.bosonixbd.placemarker.PlacesActivity",
        "com.bosonixbd.placemarker.MainActivity",
        "com.google.android.gms.common.api.GoogleApiActivity"
    ]

    # Parse the DOT file and build the graph
    graph = parse_dot_file(dot_file_path)

    # Compute SHAP-like scores and get reachability details
    shapley_scores, reachability_details = compute_shapley_scores(graph, target_classes)

    # Sort classes by score in descending order (higher score = higher priority)
    prioritized_classes = sorted(shapley_scores.items(), key=lambda x: x[1], reverse=True)

    # Output results
    print("Prioritization of classes based on SHAP-like scores (connectivity to java.net.*):")
    for i, (class_name, score) in enumerate(prioritized_classes, 1):
        connected_count = len(reachability_details[class_name])
        connected_classes = reachability_details[class_name] if connected_count > 0 else "None"
        print(f"{i}. Class '{class_name}':")
        print(f"   - SHAP Score: {score:.3f}")
        print(f"   - Connected to {connected_count} java.net.* classes: {connected_classes}")

if __name__ == "__main__":
    main()