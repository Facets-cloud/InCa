import os
import json
import yaml

def generate_index_yaml():
    intent_types_dir = "."
    index_yaml_path = "index.yaml"
    base_url = "https://raw.githubusercontent.com/Facets-cloud/InCa/main/intent_types"

    intent_types = []
    for intent_name in os.listdir(intent_types_dir):
        intent_path = os.path.join(intent_types_dir, intent_name)
        if os.path.isdir(intent_path) and intent_name != "utils":
            versions = []
            for version in os.listdir(intent_path):
                version_path = os.path.join(intent_path, version)
                if os.path.isdir(version_path):
                    intent_type_json_path = os.path.join(version_path, "intent_type.json")
                    if os.path.exists(intent_type_json_path):
                        with open(intent_type_json_path, 'r') as f:
                            intent_type_data = json.load(f)
                        version_data = {
                            "version": version,
                            "schema": f"{base_url}/{intent_name}/{version}/schema.json",
                            "documentation": f"{base_url}/{intent_name}/{version}/README.md",
                            "sample": f"{base_url}/{intent_name}/{version}/sample.json"
                        }
                        versions.append(version_data)
            if versions:
                intent_type = {
                    "name": intent_name,
                    "description": intent_type_data.get("description", ""),
                    "versions": versions
                }
                intent_types.append(intent_type)

    index_data = {
        "version": "v1",
        "intent_types": intent_types
    }

    with open(index_yaml_path, 'w') as f:
        yaml.dump(index_data, f, default_flow_style=False)

    print("index.yaml updated successfully.")

if __name__ == "__main__":
    generate_index_yaml()

