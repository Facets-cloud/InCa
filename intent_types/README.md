# Intent Types Directory

This directory contains the definitions for various Intent Types that can be used within the Infrastructure Catalog (InCa) system. Each Intent Type is organized in a dedicated subfolder, and different versions of the same Intent Type are further organized within subfolders under the respective Intent Type's folder.

## Structure

Here's a brief overview of the directory structure and the contents you would find in each folder:

- `/intent_types/`
    - `/intent_name/` (e.g., `/mysql/`, `/mongo/`, `/redis/`)
        - `/version/` (e.g., `/0.1.0/`, `/0.1.1/`)
            - `schema.json`: The JSON Schema file defining the structure and rules for this version of the intent.
            - `README.md`: The documentation file providing detailed information about this version of the intent.
            - `sample.json`: A sample JSON file showing a valid instance of this version of the intent.
            - `intent.json`: Contains details such as the intent's name, API version, and a brief description. Used to construct the `index.yaml` file.

### `intent.json` File

The `intent.json` file in each version folder contains metadata about the intent, including:

- `name`: The name of the intent.
- `api_version`: The version of the API.
- `description`: A brief description of the intent.

Here is an example of what the `intent.json` file might look like:

```json
{
  "name": "mysql",
  "api_version": "0.1.0",
  "description": "An Intent Type for deploying and managing MySQL databases."
}
```

## Index Structure

The `index.yaml` file in this directory provides a consolidated view of all the Intent Types and their versions available. Here is a sample structure of the `index.yaml` file:

```
version: v1
intent_types:
- name: mysql
  description: An Intent Type for MySQL databases.
  versions:
    - version: 0.1.1
      schema: https://github.com/Facets-cloud/InCa/blob/main/intent_types/mysql/0.1.1/schema.json
      documentation: https://github.com/Facets-cloud/InCa/blob/main/intent_types/mysql/0.1.1/documentation.md
      sample: https://github.com/Facets-cloud/InCa/blob/main/intent_types/mysql/0.1.1/sample.json
    - version: 0.1.0
      schema: https://github.com/Facets-cloud/InCa/blob/main/intent_types/mysql/0.1.0/schema.json
      documentation: https://github.com/Facets-cloud/InCa/blob/main/intent_types/mysql/0.1.0/documentation.md
      sample: https://github.com/Facets-cloud/InCa/blob/main/intent_types/mysql/0.1.0/sample.json
      ... (additional intent types)
```

It's crucial that the `index.yaml` file is automatically updated whenever a new intent or version is added to the `intent_types` directory. This ensures that the index accurately reflects the current state of available intent types and their versions in the repository.

## Contributing

When contributing a new Intent Type or a new version of an existing Intent Type, please follow the [Pull Request Template](./PULL_REQUEST_TEMPLATE.md) provided in this directory.

Ensure that your contributions adhere to the following guidelines:
- The Intent Type has a clear and specific purpose.
- Adequate documentation is provided.
- The schema is clearly defined.
- A valid sample instance is provided.
- The Intent Type is neutral regarding specific technologies or implementations.
- The Intent Type addresses common or impactful use cases within the community.
- The Intent Type avoids duplicating the functionality of existing intents.

## Questions or Issues?

If you have questions or encounter issues, please open an issue on the [InCa GitHub repository](https://github.com/Facets-cloud/InCa/issues).
