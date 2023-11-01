# Infrastructure as Catalog (InCa) Terminologies

Refer to the [discussion on GitHub](https://github.com/Facets-cloud/InCa/discussions/1) for the origin and context of this document.

---

## Infrastructure Catalog

### Definition

An Infrastructure Catalog describes the architecture of a software. It accomplishes this by describing the building blocks and their inter-dependencies with each other. The language to describe the catalog is what InCa aims to provide. The information in the catalog must be sufficient to manifest a functional deployment of the software.

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

In the catalog discussed earlier, the "orders-database" would be one of the Intents. It would state that it is named "orders-database". It would specify the type of database (e.g., MySQL), version, configuration settings, and any initialization scripts required. It would also provide the connection details that other Intents, such as "orders-backend", need to interact with it.

---

## Intent Type

### Definition

An Intent Type provides a clear and detailed structure for describing a specific intent in an Infrastructure Catalog. It must be precise and comprehensive, ensuring that a user has all the necessary information to replicate the architecture independently.

### Rationale

Intent Types are vital for maintaining interoperability across various tools and systems, ensuring that each component in the Infrastructure Catalog is described in a standardized and predictable manner. This clarity and precision are crucial for creating a reliable and effective specification that can be universally understood and utilized.

### Example

In the case of a "MySQL" Intent Type, the structure would guide the user to specify essential details such as the MySQL version, storage sizing etc. as well as provide the necessary connection details for other components to interact with the database.

---

## Flavors

### Definition

Flavors represent specific implementations of the Intents described by a generic Intent Type, detailing the unique aspects of its implementation while maintaining consistent specifications and interaction modes.

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

The orders-database Intent might have to be fulfilled with a larger resource allocation in production environment than in the lower environments. This information is captured as overrides, which are environment specific.