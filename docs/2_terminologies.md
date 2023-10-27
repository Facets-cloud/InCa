# Infrastructure as Catalog (InCa) Terminologies

Refer to the [discussion on GitHub](https://github.com/Facets-cloud/InCa/discussions/1) for the origin and context of this document.

---

## Infrastructure Catalog

### Definition

An Infrastructure Catalog describes the high level architecture of a software. It accomplishes this by describing the building blocks and their inter-dependencies with each other. The language to describe the catalog is what InCa aims to provide. The information in the catalog must be sufficient to manifest a functional deployment of the software.

### Rationale

Such a catalog serves several purposes:

- Ability  to describe, share and modify software architectures
- Leverage the information to provision and maintain deployments of the software 

### Example

For a simple three-tier order processing web service, the catalog would describe the orders-frontend application, the orders-backend application, the orders-database MySQL database and the load balancer used. The catalog would also describe the relations between these.

---

## Intent

### Definition

Intents are the building blocks that form an Infrastructure Catalog. An Intent identifies itself with a name, states its purpose, provides its specifications, dependencies on other Intents and how other Intents can interact with it.

### Rationale

The building blocks of an Infrastructure Catalog must clearly capture and describe the software architect's "Intent". Hence, the term "Intent" in InCa to refer to these building blocks.

### Example

In the catalog discussed earlier, the orders-frontend application would be one of the Intents. It would state that it is named "orders-frontend". It would specify the runtime it uses, health check endpoint etc. It would provide the port it exposes for other Intents to consume. It would also state it depends on the Intent called "orders-backend".

---

## Intent Type

### Definition

Just like variables in programming languages, Intents are typed. An Intent type defines how an Intent of that type can be specified aka it's schema.

### Rationale

InCa must be a "Typed" specification to ensure that consumers of a Catalog can interact with it programmatically. Say an IaC project should be able to consume a catalog and manifest it as IaC.

### Example

In the catalog discussed earlier, "orders-backend" and "orders-frontend" are both Intents of type "application". Their specifications must use the schema as defined in the "application" type.

---

## Flavors

### Definition

Intents of the same type may still differ in details of its implementation. But the intent specification and the mode of interaction with it remains unchanged. These intents are then said to be of different "flavors".

### Rationale

It must be possible to manifest of a functional deployment of the software described in an Infrastructure Catalog. Implementation is an important piece of information to capture in this regard.

### Example

For the "orders-database" Intent under the "MySQL" Intent Kind, the flavor may be "RDS" in AWS, "CloudSQL" in GCP etc.

---

## Environments and Overrides

### Definition

An environment is an isolated deployment of the software described in a Catalog. It would include manifestations of all the Intents in the Catalog. Overrides are environment specific customization of the Catalog.

### Rationale

Real-world scenarios often demand adjustments. Environments provide the platform for users to bring their configurations to life, and Overrides offer the nimbleness to customize them based on unique needs.

### Example

The orders-database Intent might have to be fulfilled with a larger resource allocation in production environment than in the lower environments