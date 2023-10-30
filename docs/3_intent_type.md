# Giving a Structure to Intent Types

## Introduction
As we progress in our journey with Infrastructure Catalog (InCa), having established the terminologies, our next pivotal step involves solidifying the Intent Type definition. The objective of this document is to provide the standard fields that should be present in the Intent Types for users to accurately and effectively define an intent.

## Why Need Structure
The Intent Type is crucial as it can act as a definition, guiding the realization of Intent. Establishing a standardized set of fields for the IntentType is vital to truly capture the answers to the right questions depending on the Intent Type.

## Key Considerations
- Clarity and Simplicity: The structure should be easy to understand and use, ensuring that users can define intents without ambiguity.
- Flexibility: The Structure should accommodate a range of intent types, providing users with the adaptability to define various Intents.
- Scalability: As projects evolve, the structure should be able to support growth and complexity without becoming cumbersome.
- Compatibility: Ensure that the structure is compatible with various implementation choices and does not restrict the use of different technologies or platforms.

## Standard Fields
| Field     | Type   | Description                                               |
|-----------|--------|-----------------------------------------------------------|
| metadata  | Object | Contains descriptive and auxiliary information.           |
| kind      | String | Describes the intent/kind of the resource.                |
| spec      | Object | Detailed information about the resource.                   |
| disabled  | Boolean| Indicates if the resource is disabled (true) or enabled (false) by default. |
| flavor    | Object | Specifies the default implementation details.             |
| advanced  | Object | Contains flavor-specific specifications.                   |

### Metadata Object:
| Field             | Type   | Description                                |
|-------------------|--------|--------------------------------------------|
| maintainer        | String | The person/team maintaining the resource.  |
| documentation_link| String | Link to the resource documentation.        |
| tags              | Array  | Keywords related to the resource.           |
| name              | String | The name of the resource.                   |
| description       | String | A brief description of the resource.       |

### Flavor Object:
| Field   | Type   | Description                                |
|---------|--------|--------------------------------------------|
| version | String | The version of the default implementation.|
| name    | String | The name of the default implementation.   |

### Advanced Object:
[FlavorName]: Specifications and configurations related to a particular flavor.
Type: Object
Description: Contains attributes and configurations specific to the flavor named [FlavorName].
Sub-fields: Vary depending on the flavor.

### [FlavorName] Object Example:
| Field      | Type   | Description            |
|------------|--------|------------------------|
| attributeA | String | Description of attribute A. |
| attributeB | String | Description of attribute B. |

Note: The fields within each flavor in the advanced section may vary based on the specific requirements and configurations of that flavor.

## Specification Format Choice

In our journey to streamline the process of defining Intent Types, we have chosen **JSON** (JavaScript Object Notation) as the default format for defining intents. The inherent structure and widespread adoption of JSON make it an apt choice for our requirements. Additionally, the availability of JSON Schema provides a robust foundation to introduce validations, auto-completion features, and an intuitive interface for defining new Intent Types. This schema-driven approach will ensure consistency and correctness of the Intent Types defined, thereby reducing errors and improving the user experience.

While JSON stands as our preferred choice, we acknowledge the popularity and the human-readable nature of **YAML** (YAML Ain't Markup Language) as well. YAML can also be used for defining Intent Types. However, it's important to note that the schema validation capabilities over YAML are not as mature or well-supported in current Integrated Development Environments (IDEs) and systems compared to JSON. This limitation may lead to a less rigorous validation process, potentially allowing inconsistencies to creep in.

The decision to primarily use JSON is rooted in our aim to offer a structured, reliable, and efficient mechanism for defining Intent Types, ensuring a smooth and error-free process for our users. The JSON Schema will play a crucial role in achieving this objective by offering a solid framework for validating, documenting, and defining the structure of Intent Types.

