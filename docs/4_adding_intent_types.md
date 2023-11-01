# Contributing a New Intent Type

The Infrastructure as Catalog (InCa) community encourages contributions that extend and enrich the ecosystem by introducing new intent types. This document outlines the process and guidelines for submitting a new intent type to the centralized repository.

## Repository Structure:

The repository contains a directory named `intent_types`, which holds all available intent types. Within this directory, an `index.yaml` file serves as the registry.

### Intent Type Directory Structure:

- **Folder Naming**: Each Intent Type is represented as a folder within the `intent_types` directory.
- **API Versioning**: The API version is denoted as a subfolder within the Intent Type folder.

### Intent Type Declaration Files:

Each Intent Type folder should contain the following files:

1. `README.md`: A markdown file with documentation about the intent type.
2. `intent.json`: A JSON file containing meta-information about the intent type.
3. `schema.json`: A JSON schema file defining the structure and data types for the intent type.
4. `sample.json`: A JSON file with a sample intent created using this type.

```json 
{
  "name": "ExampleIntent",
  "api_version":"v1alpha1",
  "description": "A brief description of what Example Intent Type represents.",
  "schema": "https://xyz.com/path_to_intent/schema.json",
  "example": "https://xyz.com/path_to_intent/sample.json"
}
```


## Intent Type Submission Process:

1. **Intent Type Proposal**:
   - Propose a new intent type by creating a Pull Request (PR) on the repository.
   - Ensure the PR contains all details as outlined in the PR template.

2. **Community Discussion**:
   - Engage with the community to discuss the proposed intent type, its validity, utility, and any potential modifications or improvements.

3. **Merge & List**:
   - Once the PR is approved, it will be merged into the repository.
   - The new intent type will be added to the registry (`index.yaml`).

## Qualification Criteria for an Intent Type:

1. **Defined Purpose**:
   - Clear and specific purpose.
   
2. **Implementation Neutrality**:
   - Spec should be neutral of specific implementations.
   
3. **Community Applicability**:
   - Should address common or impactful use cases within the community.
   
4. **Non-Redundancy**:
   - Should not duplicate the functionality of an existing intent type.

Contributions are vital for the growth and evolution of the InCa community. We look forward to your proposals and active participation in expanding the repository of intent types.
