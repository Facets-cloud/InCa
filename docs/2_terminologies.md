# Infrastructure as Catalog (InCa) Terminologies

Refer to the [discussion on GitHub](https://github.com/Facets-cloud/InCa/discussions/1) for the origin and context of this document.

---

## Infrastructure as Catalog (InCa)

The **Infrastructure as Catalog** (InCa) system is a repository or collection of user intentions, referred to as "Intents". This collection acts as a structured inventory of various resources or setups that users might wish to establish.

---

## Intent Kind

### Definition

**Intent Kind** provides a foundational classification within the InCa system, offering clarity about the general category or type of resource a user is aiming to set up.

### Rationale

The Intent Kind ensures that the catalog captures the user's basic intention. It should be general enough to avoid reflecting intricate implementation details but specific enough to convey the user's exact needs.

### Example

Imagine a company that wants to set up a new database system. Instead of a nebulous category like "database", they'd specify the Intent Kind as "MySQL", pinpointing their preference.

---

## Intents

### Definition

An **Intent** delves deeper into the specific resource under the broad category defined by its associated Intent Kind. While Intent Kind gives a general classification, an Intent specifies the exact resource or configuration a user wishes to establish.

### Rationale

Intents add granularity to the catalog, ensuring that users can detail their requirements beyond the general category provided by the Intent Kind.

### Example

Following the previous scenario, under the "MySQL" Intent Kind, the company could have multiple Intents like "Orders Database", "Customer Database", and "Inventory Database".

---

## Flavors

### Definition

For every Intent and its corresponding Kind, there are diverse ways to achieve or implement it. These methods are termed "Flavors", offering users a range of options on how they'd like their intent to be manifested.

### Rationale

A single Intent can have multiple approaches to realization. Flavors empower users with choices, allowing them to pick an implementation that aligns best with their needs.

### Example

For the "Orders Database" Intent under the "MySQL" Intent Kind, the company might be offered Flavors like "Helm chart in Kubernetes", "RDS in AWS", or "Docker Container".

---

## Environments and Overrides

### Definition

An **Environment** symbolizes the actual instantiation of the entire InCa catalog. Moreover, **Environment Overrides** allow users to tweak specific configurations for this environment.

### Rationale

Real-world scenarios often demand adjustments. Environments provide the platform for users to bring their configurations to life, and Overrides offer the nimbleness to customize them based on unique needs.

### Example

The company, after choosing the "Orders Database" Intent, the "MySQL" Intent Kind, and the "RDS in AWS" Flavor, initiates the database in a production environment. However, they might prefer a smaller instance size for their development environment. This alteration in instance size is an instance of an **Environment Override**.

---

In summation, the **Infrastructure as Catalog** system is structured with **Intent Kinds** at its foundation. Each Intent Kind can house multiple specific **Intents**, adding depth to the user's requirements. Varied **Flavors** outline the ways to bring each Intent to fruition. The entire catalog can then be actualized in an **Environment**, with provisions for custom adjustments through **Environment Overrides**.
