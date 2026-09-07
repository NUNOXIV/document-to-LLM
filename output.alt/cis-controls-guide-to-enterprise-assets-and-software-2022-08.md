---
source_file: "CIS_Controls__Guide_to_Enterprise_Assets_and_Software__2022_08.pdf"
source_sha256: 682682db1806a23f6040ad6bd62100f7a956dee22e47eb89e8b4ecd58db947fb
source_bytes: 170076
pages: 5
tables: 0
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-27T18:23:05+00:00"
text_coverage_percent: 99.938
appended_source_lines: 5
extraction_status: warn
warnings:
  - "5 Quellzeile(n) wurden vom Layout-/Tabellenmodell keinem Element zugeordnet und stehen woertlich im Abschnitt 'Nachtrag: nicht zugeordneter Quelltext' — dort ohne Tabellenstruktur."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

<!-- image -->

<!-- image -->

## Guide to Enterprise Assets and Software

CIS Critical Security Controls v8

Revised August 2022

Simplifying Security

<!-- image -->

<!-- page: 2 -->

## Introduction

## Enterprise Assets

The CIS Critical Security Controls® (CIS Controls®) are a set of best practices that are designed to protect an enterprise from the most common cyber-attacks. In CIS Controls v8, enhancements were made to keep up with evolving technology, evolving threats, and the evolving workplace. A big part of v8's development involved simplifying the language, ensuring that practical guidance is given, and that each Safeguard is measurable.

At the very foundation of the CIS Controls are a few critical actions that should be taken before any other Safeguards are implemented, which surround knowing your environment. In order to protect what you have, you first must know what you have. When implementing and auditing the CIS Controls, there are several references to terms such as enterprise assets, software, end-user devices, and more. CIS simplified the language in v8 to provide enterprises guidance on how enterprise assets and software are organized in the CIS Controls and to help explain what we mean when we say things like 'Establish and Maintain Detailed Enterprise Asset Inventory.'

Adopters of the CIS Controls should use this guide as a reference during activities such as implementation or auditing to verify that all in-scope assets are being accounted for and are secured.

## What are enterprise assets?

Enterprise assets are assets with the potential to store or process data. Enterprise assets include end-user devices, network devices, non-computing/Internet of Things (IoT) devices, and servers, in virtual, cloud-based, and physical environments.

## Where do remote devices fit into enterprise assets?

Any enterprise asset is capable of connecting to a network remotely, usually from public internet. This can include enterprise assets such as end-user devices, network devices, non-computing/Internet of Things (IoT) devices, and servers.

## What types of environments can enterprise assets exist in?

Enterprise assets can exist in physical, virtual, or cloud environments.

A physical environment consists of hardware parts that make up a network, including cables and routers. The hardware is required for communication and interaction between devices on a network.

A cloud-based environment provides convenient, on-demand network access to a shared pool of configurable resources such as network, computing, storage, applications, and services. There are five essential characteristics to a cloud environment: on-demand selfservice, broad network access, resource pooling, rapid elasticity, and measured service. Some services offered through cloud environments include Software as a Service (SaaS), Platform as a Service (PaaS), and Infrastructure as a Service (IaaS).

A virtualized environment simulates hardware to allow a software environment to run without the need to use a lot of actual hardware. Virtualized environments are used to make a small number of resources act as many-with plenty of processing, memory, storage, and network capacity. Virtualization is a fundamental technology that allows cloud computing to work.

## What are end-user devices?

End-user devices are information technology (IT) assets used among members of an enterprise during work, off-hours, or any other purpose. End-user devices include mobile and portable devices such as laptops, smartphones and tablets, as well as desktops and workstations. End-user devices are a s ubset of enterprise assets.

## Are there subsets of end-user devices?

Yes. There are two subsets of end-user devices: portable end-user devices and mobile enduser devices.

<!-- page: 3 -->

Figure 1. Enterprise Asset Categorization

Portable end-user devices are transportable end-user devices that have the capability to wirelessly connect to a network. Portable end-user devices can include laptops and mobile devices such as smartphones and tablets, all of which are a subset of enterprise assets.

Mobile end-user devices are small, enterprise issued end-user devices with intrinsic wireless capability, such as smartphones and tablets. Mobile end-user devices are a subset of portable end-user devices, including laptops, which may require external hardware for connectivity. Mobile end-user devices are a subset of end-user devices.

## What other types of enterprise assets are there?

Network devices are electronic devices required for communication and interaction between devices on a computer network. Network devices include wireless access points, firewalls, physical/ virtual gateways, routers, and switches. These devices consist of physical hardware, as well as virtual and cloud-based devices. Network devices are a subset of enterprise assets.

Non-computing and Internet of Things (IoT) devices are devices embedded with sensors, software, and other technologies for the purpose of connecting, storing, and exchanging data with other devices and systems over the internet. While these devices are not used for computational processes, they support an enterprise's ability to conduct business processes. Examples of these devices include printers, smart screens, physical security sensors, industrial control systems, and information technology sensors. Non-computing/IoT devices are a subset of enterprise assets.

Servers are devices or systems that provides resources, data, services, or programs to other devices on either a local area network or wide area network. Servers can provide resources and use them from another system at the same time. Examples include web servers, application servers, mail servers, and file servers.

## What is removable media and is it considered an enterprise asset?

Removable media is any type of storage device that can be removed from a computer while the system is running and allows data to be moved from one system to another. Examples of removable media include compact discs (CDs), digital versatile discs (DVDs) and Blu-ray discs, tape backups, as well as diskettes and universal serial bus (USB) drives. Removable media is not considered a subset of an enterprise asset. However, several Safeguards within the CIS Controls are specifically applicable to the security and management of removable media devices.

Shown below is a high-level chart of how enterprise assets are categorized in CIS Controls v8. Cells in white are examples of the enterprise asset subsets and are not meant to represent an exhaustive list.

<!-- image -->

<!-- page: 4 -->

## Software Assets

Figure 2. Software Categorization

## Resources

## What are software assets?

Also referred to as software in CIS Controls v8, these are the programs and other operating information used within an enterprise asset. Software assets include operating systems and applications. Enterprise assets contain software assets.

## Are there subsets of software assets?

Yes. There are two subsets of software assets: applications and operating systems.

An application is a program, or group of programs, hosted on enterprise assets and designed for end users. Applications are considered a software asset in this document. Examples include web, database, cloud-based, and mobile applications. Applications are a subset of software.

An operating system is system software on enterprise assets that manages computer hardware and software resources, and provides common services for programs. Operating systems are considered a software asset and can be single- and multi-tasking, single- and multi-user, distributed, templated, embedded, real-time, and library. Operating systems are a subset of software.

## Are there components of applications and operating systems?

Yes. While there are multiple components that make up applications and operating systems, CIS Controls v8 focuses on two key areas that are most vulnerable to exploitation: services and libraries.

A service refers to a software functionality or a set of software functionalities, such as the retrieval of specified information or the execution of a set of operations. Services provide a mechanism to enable access to one or more capabilities, where the access is provided using a prescribed interface and based on the identity of the requestor per the enterprise's usage policies.

A library is pre-written code, classes, procedures, scripts, configuration data, and more, used to develop software programs and applications. It is designed to assist both the programmer and the programming language compiler in building and executing software.

Shown below is a high-level chart of how software assets are categorized in v8 of the CIS Controls.

<!-- image -->

For more information on CIS Controls v8, visit our website at www.cisecurity.org/controls. Additionally, find out more here on how to join one of our Communities on CIS WorkBench.

[CIS Hardware and Software Asset Tracking Spreadsheet](https://www.cisecurity.org/insights/white-papers/cis-hardware-and-software-asset-tracking-spreadsheet)

CIS Critical Security Controls v8 CIS Critical Security Controls Community The Center for Internet Security, Inc. (CIS®) makes the connected world a safer place for people, businesses, and governments through our core competencies of collaboration and innovation. We are a community-driven nonprofit, responsible for the CIS Critical Security Controls® and CIS Benchmarks™, globally recognized best practices for securing IT systems and data. We lead a global community of IT professionals to continuously evolve these standards and provide products and services to proactively safeguard against emerging threats. Our CIS Hardened Images® provide secure, on-demand, scalable computing environments in the cloud.

<!-- page: 5 -->

<!-- image -->

CIS is home to the Multi-State Information Sharing and Analysis Center® (MS-ISAC®), the trusted resource for cyber threat prevention, protection, response, and recovery for U.S. State, Local, Tribal, and Territorial government entities, and the Elections Infrastructure Information Sharing and Analysis Center® (EI-ISAC®), which supports the rapidly changing cybersecurity needs of U.S. election offices. To learn more, visit CISecurity.org or follow us on Twitter: @CISecurity.

<!-- image -->

<!-- image -->

cisecurity.org

info@cisecurity.org

<!-- image -->

518-266-3460

Center for Internet Security

<!-- image -->

<!-- image -->

<!-- image -->

@CISecurity

TheCISecurity

<!-- image -->

cisecurity

Simplifying Security

4

## Nachtrag: nicht zugeordneter Quelltext

<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite angeben und den Zusammenhang in der Quelle pruefen. -->

<!-- page: 3 -->

> Email Servers

> Laptops (P)

> Tablets (P)(M)

<!-- page: 4 -->

> CONTAINED WITHIN

> CONTAINED WITHIN
