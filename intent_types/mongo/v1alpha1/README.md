# Mongo Intent Type

## Overview

This intent type is designed to represent a Mongo database configuration within an Infrastructure Catalog. It encapsulates the necessary information for provisioning and managing a Mongo database instance.

## Fields

- `metadata`: Contains auxiliary information such as the maintainer, documentation link, labels, name, and description.
- `kind`: Specifies the kind of the resource, in this case, `Mongo`.
- `spec`: Contains detailed information about the Mongo instance including the Mongo version and optional server variables.
- `disabled`: Indicates if the resource is disabled (`true`) or enabled (`false`) by default.
- `flavor`: Specifies the default implementation details, including the version and name.

## Specification (TBD)


## Example

See the `sample.json` file for an example instance of this intent type.