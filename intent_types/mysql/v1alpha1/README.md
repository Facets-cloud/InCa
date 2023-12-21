# MySQL Intent Type

## Overview

This intent type is designed to represent a MySQL database configuration within an Infrastructure Catalog. It encapsulates the necessary information for provisioning and managing a MySQL database instance.

## Fields

- `metadata`: Contains auxiliary information such as the maintainer, documentation link, labels, name, and description.
- `kind`: Specifies the kind of the resource, in this case, `mysql`.
- `spec`: Contains detailed information about the MySQL instance including the MySQL version and optional server variables.
- `disabled`: Indicates if the resource is disabled (`true`) or enabled (`false`) by default.
- `flavor`: Specifies the default implementation details, including the version and name.

## Specification

In the `spec` object:
- `version`: Specifies the MySQL version (e.g., `5.7`, `8.0`).
- `server_variables`: An optional field for specifying MySQL server variables as a map of key-value pairs (e.g., `max_connections: "1000"`).
- `replication`: Specifies the master-reader/master-master relation and their replication(s).
- `backup`: Specifies the backup frequency and retention details in days.
## Example

See the `sample.json` file for an example instance of this intent type.