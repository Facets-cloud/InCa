# PostgreSQL Intent Type

## Overview

This intent type is designed to represent a PostgreSQL database configuration within an Infrastructure Catalog. It encapsulates the necessary information for provisioning and managing a PostgreSQL database instance.

## Fields

- `metadata`: Contains auxiliary information such as the maintainer, documentation link, labels, name, and description.
- `kind`: Specifies the kind of the resource, in this case, `PostgreSQL`.
- `spec`: Contains detailed information about the PostgreSQL instance including the PostgreSQL version and architecture.
- `disabled`: Indicates if the resource is disabled (`true`) or enabled (`false`) by default.
- `flavor`: Specifies the default implementation details, including the version and name.

## Specification

In the `spec` object:
- `version`: Specifies the PostgreSQL version (e.g., `5.7`, `8.0`).
- `configuration_parameters`: A field for specifying PostgreSQL parameters (e.g., `max_connections: "1000"`).
- `encryption`: A field to encrypt the db connection between client and server.
- `replication`: A field to define the type of replication.
- `backup`: A field to define if backup is to be taken and how frequently it is to be done.

## Example

See the `sample.json` file for an example instance of this intent type.
