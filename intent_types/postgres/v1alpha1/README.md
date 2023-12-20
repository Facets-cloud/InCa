# PostgreSQL Intent Type

## Overview

This intent type is designed to represent a Postgresql database configuration within an Infrastructure Catalog. It encapsulates the necessary information for provisioning and managing a Postgresql database instance.

## Fields

- `metadata`: Contains auxiliary information such as the maintainer, documentation link, labels, name, and description.
- `kind`: Specifies the kind of the resource, in this case, `postgresql`.
- `spec`: Contains detailed information about the Postgresql instance including the Postgresql version and architecture.
- `disabled`: Indicates if the resource is disabled (`true`) or enabled (`false`) by default.
- `flavor`: Specifies the default implementation details, including the version and name.

## Specification

In the `spec` object:
- `version`: Specifies the Postgresql version (e.g., `5.7`, `8.0`).
- `architecture`: A field for specifying Postgresql architecture (e.g., `type: "standalone"`).

## Example

See the `sample.json` file for an example instance of this intent type.
