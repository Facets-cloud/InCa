# Structuring Intent Types

## Introduction
As we advance in our journey with Infrastructure Catalog (InCa), having established the terminologies, our next crucial step involves solidifying the Intent Type definition. The objective of this document is to provide the standard fields that should be present in the Intent Types for users to accurately and effectively define an intent.

## Why We Need Structure
The Intent Type is crucial as it serves as a guide for the realization of Intent. Establishing a standardized set of fields for the Intent Type is vital to truly capture the answers to the right questions depending on the Intent Type.

## Key Considerations
- Clarity and Simplicity: The structure should be easy to understand and use, ensuring that users can define intents without ambiguity.
- Flexibility: The structure should accommodate a range of intent types, providing users with the adaptability to define various Intents.
- Scalability: As projects evolve, the structure should be able to support growth and complexity without becoming cumbersome.
- Compatibility: Ensure that the structure is compatible with various implementation choices and does not restrict the use of different technologies or platforms.

## Standard Fields
| Field       | Type   | Description                                           | Required |
|-------------|--------|-------------------------------------------------------|----------|
| api_version | String | Specifies the version of the schema.                  | Yes      |
| metadata    | Object | Contains descriptive and auxiliary information.       | Yes      |
| kind        | String | Describes the intent/kind of the resource.            | Yes      |
| spec        | Object | Detailed information about the resource.              | Yes      |
| disabled    | Boolean| Indicates if the resource is disabled. Default: false | No       |
| flavor      | Object | Specifies the default implementation details.         | Yes      |
| advanced    | Object | Contains flavor-specific specifications.              | No       |

### Metadata Object:
| Field             | Type   | Description                                | Required |
|-------------------|--------|--------------------------------------------|----------|
| maintainer        | String | The person/team maintaining the resource.  | No       |
| documentation_link| String | Link to the resource documentation.        | No       |
| labels            | Map    | Map of string to string to capture contextual information.| No |
| name              | String | The name of the resource.                   | Yes      |
| description       | String | A brief description of the resource.       | No       |

### Flavor Object:
| Field   | Type   | Description                                | Required |
|---------|--------|--------------------------------------------|----------|
| version | String | The version of the default implementation.| Yes      |
| name    | String | The name of the default implementation.   | Yes      |

### Advanced Object:
[FlavorName]: Specifications and configurations related to a particular flavor.
Type: Object
Description: Contains attributes and configurations specific to the flavor named [FlavorName].
Sub-fields: Vary depending on the flavor.

### [FlavorName] Object Example:
| Field      | Type   | Description            | Required |
|------------|--------|------------------------|----------|
| attributeA | String | Description of attribute A. | No |
| attributeB | String | Description of attribute B. | No |

Note: The fields within each flavor in the advanced section may vary based on the specific requirements and configurations of that flavor.

## Specification Format Choice

In our journey to streamline the process of defining Intent Types, we have chosen **JSON** (JavaScript Object Notation) as the default format for defining intents. The inherent structure and widespread adoption of JSON make it an apt choice for our requirements. Additionally, the availability of JSON Schema provides a robust foundation for introducing validations, auto-completion features, and an intuitive interface for defining new Intent Types. This schema-driven approach will ensure consistency and correctness of the Intent Types defined, thereby reducing errors and improving the user experience.

While JSON stands as our preferred choice, we acknowledge the popularity and the human-readable nature of **YAML** (YAML Ain't Markup Language) as well. YAML can also be used for defining Intent Types. However, it's important to note that the schema validation capabilities over YAML are not as mature or well-supported in current Integrated Development Environments (IDEs) and systems compared to JSON. This limitation may lead to a less rigorous validation process, potentially allowing inconsistencies to creep in.

The decision to primarily use JSON is rooted in our aim to offer a structured, reliable, and efficient mechanism for defining Intent Types, ensuring a smooth and error-free process for our users. The JSON Schema will play a crucial role in achieving this objective by offering a solid framework for validating, documenting, and defining the structure of Intent Types.