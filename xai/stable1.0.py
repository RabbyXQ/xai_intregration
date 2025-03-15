import networkx as nx
import re
import json

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

def compute_shapley_scores_and_connections(graph, target_classes):
    """Computes SHAP-like scores and connectivity details."""
    java_net_classes = [node for node in graph.nodes() if node.startswith("java.net.")]

    if not java_net_classes:
        print("No java.net.* classes found in the graph.")

    # Initialize data structures
    reachability_counts = {}
    java_net_connections = {}
    all_connections = {}

    for target_class in target_classes:
        if target_class in graph:
            # java.net.* connections
            reachable_java_net = [
                java_net_class for java_net_class in java_net_classes
                if nx.has_path(graph, java_net_class, target_class)
            ]
            reachability_counts[target_class] = len(reachable_java_net)
            java_net_connections[target_class] = reachable_java_net

            # All direct connections (neighbors in the undirected graph)
            all_connections[target_class] = list(graph.neighbors(target_class))
        else:
            reachability_counts[target_class] = 0
            java_net_connections[target_class] = []
            all_connections[target_class] = []

    # Normalize scores to sum to 1 (if total count > 0) for relative importance
    total_connections = sum(reachability_counts.values())
    shapley_scores = {}
    if total_connections > 0:
        for target_class in target_classes:
            shapley_scores[target_class] = reachability_counts[target_class] / total_connections
    else:
        for target_class in target_classes:
            shapley_scores[target_class] = 0.0

    return shapley_scores, java_net_connections, all_connections

def load_ast_json(file_path):
    """Loads the AST JSON data from the specified file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def find_partial_matches(ast_json, target_classes):
    """Finds and returns classes in AST JSON that partially match the target classes,
    along with their methods."""
    matching_classes = []
    class_methods = {}

    for class_name, class_info in ast_json.items():
        for target_class in target_classes:
            if target_class in class_name:
                matching_classes.append(class_name)

                # Extract methods used by this class
                methods = class_info.get("methods", [])
                class_methods[class_name] = [method["name"] for method in methods]

    return matching_classes, class_methods

def main():
    # Path to the DOT file and AST JSON file
    dot_file_path = './GeoPointer_v1.3_classgraph_1.dot'
    ast_json_file_path = './GeoPointer_v1.3_all_java_asts_1.json'

    # List of classes to prioritize
    target_classes = [
        "com.bosonixbd.placemarker.PlacesActivity",
        "com.bosonixbd.placemarker.MainActivity",
        "com.google.android.gms.common.api.GoogleApiActivity",
        "com.bosonixbd.placemarker.Place"
    ]

    # Parse the DOT file and build the graph
    graph = parse_dot_file(dot_file_path)

    # Compute SHAP-like scores and connection details
    shapley_scores, java_net_connections, all_connections = compute_shapley_scores_and_connections(graph, target_classes)

    # Sort classes by score in descending order (higher score = higher priority)
    prioritized_classes = sorted(shapley_scores.items(), key=lambda x: x[1], reverse=True)

    # Output results with 8 decimal places and connection details
    print("Prioritization of classes based on SHAP-like scores (connectivity to java.net.*):")
    for i, (class_name, score) in enumerate(prioritized_classes, 1):
        java_net_count = len(java_net_connections[class_name])
        java_net_classes = java_net_connections[class_name] if java_net_count > 0 else "None"
        using_classes = all_connections[class_name] if all_connections[class_name] else "None"

        print(f"{i}. Class '{class_name}':")
        print(f"   - SHAP Score: {score:.8f}")
        print(f"   - Connected to {java_net_count} java.net.* classes: {java_net_classes}")
        print(f"   - Used by/connected to these classes: {using_classes}")

    # Load AST JSON and find partial matches
    ast_json = load_ast_json(ast_json_file_path)
    matching_classes, class_methods = find_partial_matches(ast_json, target_classes)

    # Output matching classes and their methods
    print("\nClasses that partially match target classes and their methods:")
    for class_name in matching_classes:
        methods = class_methods.get(class_name, [])
        print(f" - {class_name} -> Methods: {', '.join(methods) if methods else 'No methods found'}.join('[PERMISSION_INTERNET]')")

if __name__ == "__main__":
    main()
