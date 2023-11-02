# Infrastructure as Catalog (InCa)

## Introduction
Infrastructure as Catalog (InCa) is an open-source initiative devised to redefine infrastructure management by abstracting complex architectures into a cloud-neutral, declarative catalog. This allows users to articulate their infrastructure needs at a high level through a unified language, abstracting away the intricate details of infrastructure setup and maintenance. Such an abstraction not only streamlines infrastructure management but also promotes flexibility, scalability, and effective knowledge sharing across diverse entities and the broader open-source community.

## Why InCa?
Traditional infrastructure management often involves manual processes, scripts, and configurations tightly bound to specific technologies or platforms. This conventional approach can result in:

1. **Inflexibility**: Any modification to the infrastructure or transition to a new platform becomes a significant undertaking.
2. **Complexity**: As the infrastructure grows, managing it becomes increasingly convoluted, leading to potential errors and inefficiencies.
3. **Limited Scalability**: Tightly intertwined configurations and scripts may not scale efficiently with escalating infrastructure demands.

InCa addresses these challenges through:

1. **Documenting Architecture**: InCa inherently documents the entire infrastructure architecture in a centralized catalog, promoting clarity, transparency, and ease of reference.
2. **Promoting Platform Engineering**: Distinct resource types can be owned and managed by different personas or teams, fostering responsibility and expertise in platform engineering.
3. **Promoting Abstraction**: By focusing on the desired outcome (e.g., a MySQL database or a compute instance) rather than its implementation, users can effortlessly switch between different implementations without altering the overarching definitions.
4. **Boosting Flexibility**: Transitioning from an on-premises MySQL database to a cloud-based one? Simply modify the flavor in your catalog, leaving the core definition intact.
5. **Streamlining Management**: With each resource defined individually, the system becomes modular, facilitating easier management, versioning, and collaboration.

## Why is IaC not enough?
Infrastructure as Code (IaC) has significantly benefited many organizations by enabling automation and management of infrastructure using code. However, writing IaC as per custom requirements poses challenges like:

1. **Custom Language Requirement**: Writing IaC as per custom requirements often requires a deep understanding of both the infrastructure components and the scripting or coding involved, which not every organization possesses. On the other hand, writing against a standard language as proposed by InCa can simplify this process.
2. **Poor Coding Practices**: Like any codebase, IaC can suffer from bad coding practices, resulting in inefficiencies, vulnerabilities, and maintenance issues.
3. **Modularization Issues**: Organizations often struggle to modularize their IaC properly, leading to tightly coupled configurations that are challenging to manage, update, or scale.

InCa mitigates these challenges by abstracting complexities and providing a structured, modular, and intuitive approach to defining infrastructure.

## Envisioning Product Infrastructure as a Catalog
Infrastructure creation for any product typically follows distinct layers:

1. Initially, it often starts with a cloud provider account. While architecting a product, one or multiple accounts might be involved due to varying billing requirements or specific compliance mandates.
2. Following this is the foundational networking layer, where decisions regarding VPCs, subnets, security groups, and other related elements are made in alignment with organizational standards and the chosen cloud provider's specifications.
3. Building on this foundation is the orchestration layer, usually embodied by systems like Kubernetes, set up predominantly by platform teams to provide a conducive environment for application teams to host their applications.
4. At the apex, we have resources - the essential building blocks of any architectural design, encompassing components like services, databases, caches, and more.

Although not exhaustive, this structured overview provides a foundational catalog to aid in visualizing the catalog as per InCa's objective of establishing a cloud-neutral, abstract representation of intricate architectures, fostering effective knowledge sharing and collaborative innovation.


![](assets/catalog-diagram.png)

## Contribute

Being an open-source project, Infrastructure as Catalog (InCa) thrives on community contributions. Whether you're
enhancing the existing FacetsCore implementation, introducing a new flavor, improving documentation, or reporting bugs,
your input is invaluable. Dive into our [GUIDELINES.md](GUIDELINES.md) for guidelines on how to be a part of this
project.

By documenting the architecture and promoting platform engineering, Infrastructure as Catalog (InCa) fosters
responsibility and expertise, ensuring efficient infrastructure management. Join us in redefining the future of
infrastructure!
