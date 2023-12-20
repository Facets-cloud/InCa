# Redis Intent Type

## Overview

This intent type is designed to represent a Redis database configuration within an Infrastructure Catalog. It encapsulates the necessary information for provisioning and managing a Redis database instance.

## Fields

- `metadata`: Contains auxiliary information such as the maintainer, documentation link, labels, name, and description.
- `kind`: Specifies the kind of the resource, in this case, `redis`.
- `spec`: Contains detailed information about the Redis instance including the Redis version.
- `disabled`: Indicates if the resource is disabled (`true`) or enabled (`false`) by default.
- `flavor`: Specifies the default implementation details, including the version and name.

## Specification

In the `spec` object:
- `version`: Specifies the Redis version (e.g., `7.2.2`, `6.2.14`).
- `server_mode`: A field to specify if want to Redis in standalone or cluster mode
- `persistence`: Optional configuration for enabling redis persistence, here you can specify persistence options like RBD, AOF
- `replication`: Optional configuration for enabling redis master slave replication, you can specify replicas required
- `redis_conf`: Any redis configuration that can be specified in redis.conf can be specified here
- `auth`: Optional If password auth should be enabled or not can be specified here (if not specified then no-auth required to connect to redis) 

## Example

See the `sample.json` file for an example instance of this intent type.