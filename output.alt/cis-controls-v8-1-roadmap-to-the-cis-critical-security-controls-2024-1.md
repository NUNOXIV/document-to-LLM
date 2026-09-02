---
source_file: "CIS_Controls_v8.1_Roadmap_to_the_CIS_Critical_Security_Controls_2024_1.pdf"
source_sha256: 41551b0df0b7a7507af51a03fccbd7e1bd2d0255050c9266c3e93697cad988b5
source_bytes: 728726
pages: 18
tables: 2
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-27T18:24:15+00:00"
text_coverage_percent: 99.592
appended_source_lines: 102
extraction_status: warn
warnings:
  - "102 Quellzeile(n) wurden vom Layout-/Tabellenmodell keinem Element zugeordnet und stehen woertlich im Abschnitt 'Nachtrag: nicht zugeordneter Quelltext' — dort ohne Tabellenstruktur."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- page: 2 -->

## Acknowledgments

The Center for Internet Security® (CIS®) would like to thank the many security experts who volunteer their time and talent to support the CIS Critical Security Controls (CIS Controls) and other CIS work. CIS products represent the effort of a veritable army of volunteers from across the industry, generously giving their time and talent in the name of a more secure online experience for everyone.

As a nonprofit organization driven by its volunteers, we are always in the process of looking for new topics and assistance in creating cybersecurity guidance. If you are interested in volunteering or have questions, comments, or have identified ways to improve this guide, please write us at controlsinfo@cisecurity.org.

All references to tools or other products in this guide are provided for informational purposes only, and do not represent the endorsement by CIS of any particular company, product, or technology.

## Editor

Valecia Stocchetti, CIS

Contributor Robin Regnier, CIS

This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 International Public License (the link can be found at https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode).

To further clarify the Creative Commons license related to the CIS Controls® content, you are authorized to copy and redistribute the content as a framework for use by you, within your organization and outside of your organization for non-commercial purposes only, provided that (i) appropriate credit is given to CIS, and (ii) a link to the license is provided. Additionally, if you remix, transform, or build upon the CIS Controls, you may not distribute the modified materials. Users of the CIS Controls framework are also required to refer to (http://www.cisecurity.org/controls/) when referring to the CIS Controls in order to ensure that users are employing the most up-to-date guidance. Commercial use of the CIS Controls is subject to the prior approval of the Center for Internet Security, Inc. (CIS®).

<!-- page: 3 -->

## Contents

| Introduction                           |   1 |
|----------------------------------------|-----|
| Getting Started                        |   2 |
| Assess and Measure                     |   5 |
| Implementation Resources/Tools         |   7 |
| Minimization of Threats                |   8 |
| External Frameworks                    |  10 |
| Collaboration                          |  10 |
| Training and Speaking Engagements      |  11 |
| Putting It All Together                |  12 |
| Appendix 1: Acronyms and Abbreviations |  14 |

<!-- page: 4 -->

## Introduction

The CIS Critical Security Controls (CIS Controls) are a set of best practice recommendations that defend against the most common cyber attacks. The CIS Controls themselves are the framework. However, there is a broader ecosystem that surrounds the CIS Controls which offers guidance, tools, resources, mappings, and more to help facilitate the adoption and implementation of the framework.

At times, it can be overwhelming to implement any security framework. Challenges arise such as deciding what to do first, what tools are available for implementation/measurement, and how to get help, if needed. CIS has developed this guide to help adopters of the CIS Controls to understand what is available to them, where to start, and how to put it all together. Shown below are just a few questions the CIS Controls can help to answer. This guide is broken down into six main sections that will help to answer each of these questions: Assess and Measure , Implementation Resources/Tools , Minimization of Threats , External Frameworks , Collaboration , and Training and Speaking Engagements . Note that the resources mentioned throughout this guide support adoption of CIS Controls v8.1, v8, and/or v7.1.

<!-- image -->

<!-- page: 5 -->

## Getting Started

At a high level, the CIS Controls are best practice recommendations that consist of a prioritized set of actions to defend against the most common attacks. In version 8.1 of the Controls, there are 18 top-level Controls, followed by a subset of 153 'actions' called Safeguards. As a part of our core documentation, when the CIS Controls are downloaded (at no cost), users can expect to receive different formats (Adobe® PDF, Microsoft® Excel®) of the Controls, as well as other information such as the Change Log for moving from a previous Controls version to a current version (e.g., v8 → v8.1).

## Figure 1 | The CIS Critical Security Controls

<!-- image -->

## CONTROL 2

Inventory and Control of Software Assets

<!-- image -->

Safeguards:

IG1

<!-- image -->

<!-- image -->

## CONTROL 3

Data Protection

<!-- image -->

Safeguards:

IG1

IG3

IG3

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## CONTROL 4

Secure Confi  guration of Enterprise Assets and Software

<!-- image -->

Safeguards:

IG1

IG2

IG3

7/7

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## CONTROL 8

Audit Log Management

<!-- image -->

Safeguards:

IG1

IG2

<!-- image -->

## CONTROL 9

Email and Web Browser Protections

<!-- image -->

Safeguards:

IG1

IG2

<!-- image -->

## CONTROL 10

Malware Defenses

<!-- image -->

Safeguards:

## CONTROL 11

Data Recovery

<!-- image -->

Safeguards:

IG1

IG1

IG2

IG2

<!-- image -->

<!-- image -->

## CONTROL 12

Network Infrastructure Management

<!-- image -->

Safeguards:

IG1

<!-- image -->

IG2

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

IG3

IG3

IG3

IG3

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## CONTROL 14

Security Awareness and Skills Training

<!-- image -->

Safeguards:

IG1

8/9

## CONTROL 15

Service Provider Management

<!-- image -->

<!-- image -->

Safeguards:

IG1

## CONTROL 16

Application Software Security

<!-- image -->

0/14

Safeguards:

IG1

## CONTROL 17

Incident Response Management

<!-- image -->

3/9

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

9/9

<!-- image -->

<!-- image -->

<!-- image -->

Safeguards:

IG1

IG2

<!-- image -->

IG2

IG2

IG3

IG3

IG3

IG3

<!-- image -->

<!-- page: 6 -->

To help with prioritization, the Safeguards are divided into three Implementation Groups (IGs): IG1, IG2, and IG3. IG1 is essential cyber hygiene and represents the minimum standard of information security for all enterprises. These are the actions that every enterprise should take first, regardless of size. It also lays the foundation for implementing Safeguards in IG2 and IG3 .

Figure 2 | Implementation Groups (IGs) of the CIS Controls

<!-- image -->

The number of Safeguards an enterprise is expected to implement increases based on which group the enterprise falls into.

IG3

IG3 assists enterprises with IT security experts to secure sensitive and confidential data. IG3 aims to prevent and/or lessen the impact of sophisticated attacks.

IG2

IG1

153 TOTAL SAFEGUARDS

23 SAFEGUARDS

74 SAFEGUARDS

56 SAFEGUARDS

IG2 assists enterprises managing IT infrastructure of multiple departments with differing risk profiles. IG2 aims to help enterprises cope with increased operational complexity.

IG1 is the definition of essential cyber hygiene and represents a minimum standard of information security for all enterprises. IG1 assists enterprises with limited cybersecurity expertise thwart general, non-targeted attacks.

Each Safeguard is also assigned an Asset Class, defined as a group of information assets that are evaluated as one set based on their similarity. In v8.1, Asset Classes are categorized into Devices , Software , Data , Users , Network , and Documentation . Within each Asset Class, there are a number of sub-categories that align to language used throughout the CIS Controls. More information on Asset Classes can be found here.

<!-- page: 7 -->

Figure 3| Asset Classes of the CIS Controls

<!-- image -->

Beyond the main documentation associated with the CIS Controls, various tools, guides, and other resources are available to users. These are broken down into six categories - Assess and Measure , Implementation Tools/Resources , Minimization of Threats , External Frameworks , Collaboration , and Training and Speaking Engagements .

<!-- page: 8 -->

## Assess and Measure

Beyond our Implementation Groups (IGs), enterprises often want to know where to start first and how to prioritize Safeguards. Is it by cost? risk? threat? tool? One of the first steps in implementing any security framework is to conduct a baseline assessment.

CIS Controls Self Assessment Tool (CSAT) | One of the first steps in implementing any security framework is to conduct a baseline assessment. CIS offers a selection of tools that can help with this. To start, our CIS Controls Self Assessment Tool (CSAT) enables enterprises to assess and track their implementation of the CIS Controls. This powerful tool can improve an enterprise's cyber defense program regardless of size or resources. CIS CSAT can help enterprises identify where CIS Safeguards are already well-implemented and where there are opportunities for improvement. This can be useful information as enterprises decide where to devote their limited cybersecurity resources. CSAT can also allow an enterprise to anonymously compare their results to the average of their industry or other peer groups to help drive the direction of their security program. There are two different versions of CSAT: CIS-Hosted CSAT (no-cost) and CSAT Pro (paid).

CIS Business Impact Analysis Tool | Enterprises may want or need to conduct a risk-based assessment and analysis. As a compliment to CIS-Hosted CSAT, the CIS Business Impact Analysis tool provides a cyber risk analysis by identifying specific Safeguards and cross-referencing them to an enterprise's CIS CSAT assessment. This helps to identify unique enterprise assets and estimate the potential costs incurred with a successful ransomware attack against those assets. The tool provides enterprises with the insight they need, now and over time, to communicate cyber risk to a variety of audiences, identify potential weak points in an enterprise's cybersecurity policy, and prioritize cyber threat abatement activities.

CIS Risk Assessment Method (RAM) | CIS has also published the CIS Risk Assessment Method (RAM), which is an information security risk assessment method that helps enterprises implement and assess their security posture against the CIS Controls. While CIS RAM is not a replacement for other risk assessment standards, it conforms to and supplements established information security risk assessment standards and methods, such as ISO 27005, NIST SP 800-30, and Risk Information Technology. CIS RAM also helps enterprises justify investments for reasonable implementation of the CIS Controls. Guides for CIS RAM are available for IG1, IG2, and IG3.

A Guide to Defining Reasonable Cybersecurity | To assess whether reasonable cybersecurity measures were implemented, CIS released A Guide to Defining Reasonable Cybersecurity to help with this. Several prominent data breaches, court cases, and state data privacy laws have placed the concept of 'reasonable' cybersecurity in the public discourse, but there has been no real definition of what 'reasonable' cybersecurity is. This guide provides practical and specific guidance to enterprises seeking to develop a cybersecurity program that satisfies the general standard of 'reasonable cybersecurity.'

<!-- page: 9 -->

The Cost of Cyber Defense: Implementation Group 1 (IG1) | As with any business decision, budget may play a role in the prioritization and assessment of where to allocate resources first when it comes to the CIS Controls. CIS has published The Cost of Cyber Defense: Implementation Group 1 (IG1), to help answer the questions as to which protections to start with, which tools will be needed to implement those protections, and how much an implementation will cost. The purpose of this guide is to provide enterprises with a picture into how realistic and cost effective it can be to achieve essential cyber hygiene (IG1). In turn, this information will help enterprises make informed and prioritized decisions when it comes to cyber defense.

CIS Controls Assessment Specification | During implementation, enterprises may also be wondering how to measure the implementation of a Safeguard. The purpose of the CIS Controls Assessment Specification is to provide a common understanding of what should be measured in order to verify that CIS Safeguards are properly implemented. The Controls Assessment Specification provides the inputs, operations, measures, and metrics that are needed during implementation of the Controls.

Below is a summary of the various products available when assessing and measuring the CIS Controls.

<!-- image -->

<!-- page: 10 -->

## Implementation Resources/Tools

Once an enterprise begins to assess which Safeguards to select, implementation begins. CIS offers several resources that can be used during implementation of the CIS Controls.

Environment-Specific Guidance | Learn how to implement the CIS Controls in different environments such as cloud, mobile, Industrial Control System (ICS) environments, and Internet of Things (IoT). CIS also offers guides on privacy, small- to medium-sized enterprises (SMEs), managed service providers (MSPs), Windows 10, and teleworking.

Establishing Essential Cyber Hygiene | When tasked to implement a cybersecurity program, many enterprises ask, 'How do we get started?' In response, CIS sorted the Safeguards into three IGs based on an enterprise's risk profile and the resources available to them. Establishing Essential Cyber Hygiene is a resource to assist with IG1 ( 'essential cyber hygiene' ), providing specific tools and resources that can be used during implementation.

CIS Policy Templates | CIS has created several policy templates to function as a 'jumping off point' for when enterprises are drafting their own policies. Using these policy templates, you can work to meet your cybersecurity goals around establishing essential cyber hygiene at a faster pace than if you were working alone.

OSCAL | The Open Security Controls Assessment Language (OSCAL) framework contains OSCAL serializations of the CIS Controls. OSCAL assists with the automation of mappings and improves an end-user's transition from one framework version to the next.

Implementation Guide for Small and Medium-Sized Enterprises (SME) | A guide to help SMEs protect their enterprises with a limited number of high-priority actions based on the CIS Controls. It works as a ladder to help SMEs rapidly adopt IG1 - essential cyber hygiene . The SME Guide contains several helpful resources such as spreadsheets for tracking various different items and a guide that provides a step-by-step walk-through of what actions to take.

Hardware and Software Asset Tracking Spreadsheet | A simple, easy-to-use spreadsheet for tracking an enterprise's assets and software.

CIS Benchmarks™ | Many of the Safeguards in the CIS Controls require the configuration of certain technologies. CIS Benchmarks are prescriptive secure configuration recommendations for hardening specific technologies in an enterprise environment, available for over 25 vendor product families.

- CIS Hardened Images | Virtual machine (VM) images are pre-hardened to the CIS Benchmarks. Available on major cloud service platforms like AWS, Azure, Google Cloud Platform, and Oracle Cloud.

<!-- page: 11 -->

- CIS Build Kits | CIS offers Build Kits for certain technologies to assist in the automation of hardening systems. The Build Kit is designed to cover the majority of the Benchmark settings.
- CIS-Configuration Assessment Tool (CIS-CAT) | A powerful tool for automating CIS Benchmark assessment and reporting. CIS-CAT has two types: CIS-CAT Pro (paid with a SecureSuite Membership) and CIS-CAT Lite (no-cost).
- CIS SecureSuite | A Membership that provides scalable, customizable tools and resources to suit an enterprise's needs. CIS SecureSuite includes access to CIS-CAT Pro, CIS CSAT Pro, CIS Build Kits, CIS WorkBench, and more.

<!-- image -->

## Minimization of Threats

Every enterprise is faced with at least one threat and often more than one. Whether it be ransomware, malware, web application attacks, or a wide variety of other threats, CIS has developed some key resources that will assist in minimizing the threats that impact the majority of enterprises.

CIS Community Defense Model (CDM) | CIS Community Defense Model (CDM) v2.0 can be used to design, prioritize, implement, and improve an enterprise's cybersecurity program. Enterprises naturally want to know 'How effective are the CIS Controls against the most prevalent types of attacks?' The CDM was created to help answer that and other questions about the value of the Controls based on currently available threat data from industry reports.

CDM v2.0 leverages industry threat data to determine the top five attack types ( Ransomware , Malware , Web Application Hacking , Insider and Privilege Misuse , and Targeted Intrusions ) and create comprehensive attack patterns (the set of attacker techniques that are required to execute an attack). Version 2.0 of the CDM builds on the original version, by mapping the Safeguards to the MITRE

<!-- page: 12 -->

Enterprise ATT&amp;CK® v8.2 framework. This methodology allows CIS to measure which Safeguards are most effective overall for defense across attack types. As an example, CDM v2.0 asserts that, independent of any specific attack type, implementing IG1 Safeguards defends against 74% of ATT&amp;CK (sub-)techniques in the MITRE ATT&amp;CK framework.

Blueprint for Ransomware Defense | In response to Action 3.1.1 of the Ransomware Task Force (RTF) report, which calls for the cybersecurity community to 'develop a clear, actionable framework for ransomware mitigation, response, and recovery, ' the Blueprint for Ransomware Defense Working Group developed a blueprint. In partnership with the Ransomware Task Force (RTF), which consists of more than 60 members (including CIS) spanning several sectors, the Blueprint for Ransomware Defense provides a set of 40 Foundational and Actionable Safeguards from IG1 of the CIS Controls that assist with ransomware defense while considering those SMEs that have limited cybersecurity expertise.

Living off the Land (LotL) Attacks | Attacks using exploited protocols and other LotL attack techniques have been, and continue to be, on the rise. CIS has published several guides that address the most commonly exploited LotL techniques including:

- [Scheduled Tasks](https://www.cisecurity.org/insights/blog/abusing-scheduled-tasks-with-living-off-the-land-attacks)
- [PowerShell](https://www.cisecurity.org/insights/white-papers/living-off-the-land-powershell)
- [Windows Management Instrumentation (WMI)](https://www.cisecurity.org/insights/white-papers/cis-controls-commonly-exploited-protocols-windows-management-instrumentation)
- [Server Message Block (SMB)](https://www.cisecurity.org/insights/white-papers/cis-controls-v8-exploited-protocols-server-message-block-smb)
- [Remote Desktop Protocol (RDP)](https://www.cisecurity.org/insights/white-papers/exploited-protocols-remote-desktop-protocol-rdp)

<!-- image -->

<!-- page: 13 -->

## External Frameworks

Many enterprises are required to comply with multiple other industry regulations or frameworks. By implementing the CIS Controls, enterprises create an on-ramp to comply with PCI DSS, HIPAA, GDPR, and more. The CIS Controls are mapped to over 25 industry frameworks for ease of implementation. These mappings are offered in two forms: Microsoft® Excel® spreadsheet and through our CIS Controls Navigator (available for v8.1, v8, and v7.1 of the CIS Controls).

<!-- image -->

## Collaboration

CIS is proud to offer a platform where users can collaborate with other professionals in the industry around the world. CIS WorkBench brings together adopters of the CIS Controls and CIS Benchmarks by providing communities of common interests. Discussions range from the most detailed technical configuration settings to broader cybersecurity policies. Integrating these groups on the same platform provides enterprises with greater insight into key initiatives.

<!-- image -->

<!-- page: 14 -->

## Training and Speaking Engagements

CIS participates in a variety of webinars, podcasts, conferences (virtual and in-person), and more.

Additionally, training on various CIS Controls topics are available through a few different platforms including:

- [SANS SEC366: CIS Controls IG1](https://www.sans.org/cyber-security-courses/cis-implementation-group-1/)
- [SANS SEC566: Implementing and Auditing CIS Controls](https://www.sans.org/cyber-security-courses/implementing-auditing-cis-controls/)
- Salesforce Trailhead:
- [Trailhead Controls Introductory Course](https://trailhead.salesforce.com/en/content/learn/modules/the-center-for-internet-security-controls-version-8)
- [Trailhead CIS RAM Course](https://trailhead.salesforce.com/content/learn/trails/use-cis-risk-assessment-method)
- [Trailhead The Value of Security Controls](https://trailhead.salesforce.com/content/learn/modules/the-value-of-security-controls)

CIS also offers a CIS Controls Accreditation for CIS SecureSuite Members. This initiative gives the ability to provide CIS Controls implementation, auditing, and/or assessment with the assurance that they have met the consistent and rigorous standards of CREST certification. It also offers service providers a 'stamp of approval' at the organization level, assuring that their customers can feel confident that they are doing business with a reputable and reliable CIS Controls assessment organization.

<!-- image -->

<!-- page: 15 -->

## Putting It All Together

Whether you use the CIS Controls, and/or another way to guide your security improvement program, you should recognize that 'it's not about the list.' You can get a credible list of security recommendations from many sources-it is best to think of the list as a starting point. It is important to look for the ecosystem that grows up around the list. Questions that are at the forefront of many enterprises' minds include:

- Where can I get training, complementary information, explanations?
- How have others implemented and used these recommendations?
- Is there a marketplace of vendor tools and services to choose from?
- How will I measure progress or maturity?
- How does this align with the myriad regulatory and compliance frameworks that apply to me?

The true power of the CIS Controls is not about creating the best list, it is about harnessing the experience of a community of individuals and enterprises to actually make security improvements through the sharing of ideas, tools, lessons, and collective action.

<!-- page: 16 -->

<!-- image -->

<!-- page: 17 -->

## Appendix A

## Acronyms and Abbreviations

| AWS          | Amazon Web Services                                                                      |
|--------------|------------------------------------------------------------------------------------------|
| CIS BIA Tool | CIS Business Impact Analysis Tool                                                        |
| CIS CAT      | CIS Configuration Assessment Tool                                                        |
| CIS CDM      | CIS Community Defense Model                                                              |
| CIS CSAT     | CIS Controls Self Assessment Tool                                                        |
| CIS HIs      | CIS Hardened Images                                                                      |
| CIS RAM      | CIS Risk Assessment Method                                                               |
| CISA         | Cybersecurity and Infrastructure Security Agency                                         |
| CMMC         | Cybersecurity Maturity Model Certification                                               |
| CSA          | Cloud Security Alliance                                                                  |
| GDPR         | General Data Protection Regulation                                                       |
| HIPAA        | Health Insurance Portability and Accountability Act                                      |
| HPH CPGs     | Healthcare and Public Health (HPH) Cybersecurity Performance Goals                       |
| ICS          | Industrial Control Systems                                                               |
| IG           | Implementation Group                                                                     |
| IoT          | Internet of Things                                                                       |
| ISO/IEC      | International Organization for Standardization/International Electrotechnical Commission |
| IT           | Information Technology                                                                   |
| LotL         | Living off the Land                                                                      |
| MITRE ATT&CK | MITRE Adversarial Tactics, Techniques, and Common Knowledge                              |
| MSP          | Managed Service Provider                                                                 |
| NIST CSF     | National Institute of Standards and Technology Cybersecurity Framework                   |
| NIST SP      | National Institute of Standards and Technology Special Publication                       |
| NY DFS       | New York State Department of Financial Services                                          |
| OSCAL        | Open Security Controls Assessment Language                                               |
| PCI DSS      | Payment Card Industry Data Security Standard                                             |
| RDP          | Remote Desktop Protocol                                                                  |
| RTF          | Ransomware Task Force                                                                    |
| SMB          | Server Message Block                                                                     |
| SME          | Small and medium-sized enterprises                                                       |
| VM           | Virtual Machine                                                                          |
| WMI          | Windows Management Instrumentation                                                       |

<!-- page: 18 -->

The Center for Internet Security, Inc. (CIS®) makes the connected world a safer place for people, businesses, and governments through our core competencies of collaboration and innovation.

We are a community-driven nonprofit, responsible for the CIS Controls® and CIS Benchmarks™, globally recognized best practices for securing IT systems and data. We lead a global community of IT professionals to continuously evolve these standards and provide products and services to proactively provide secure, on-demand, scalable computing environments

CIS is home to the Multi-State Information Sharing and Analysis Center® (MS-ISAC®), the trusted resource for cyber State, Local, Tribal, and Territorial government entities, and Center® (EI-ISAC®), which supports the rapidly changing cybersecurity needs of U.S. elections offices.

safeguard against emerging threats. Our CIS Hardened Images® in the cloud. threat prevention, protection, response, and recovery for U.S. the Elections Infrastructure Information Sharing and Analysis

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

www.cisecurity.org

info@cisecurity.org

518-266-3460

Center for Internet Security CenterforIntSec

<!-- image -->

@CISecurity

<!-- image -->

<!-- image -->

<!-- image -->

TheCISecurity

cisecurity

## Nachtrag: nicht zugeordneter Quelltext

<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite angeben und den Zusammenhang in der Quelle pruefen. -->

<!-- page: 1 -->

> A Roadmap to

> November 2024

<!-- page: 2 -->

> This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 International Public

> License (the link can be found at https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode).

> non-commercial purposes only, provided that (i) appropriate credit is given to CIS, and (ii) a link to the license is provided.

<!-- page: 3 -->

> 2

> 5

> 7

> 8

> 11

> 12

> 14

<!-- page: 4 -->

> At times, it can be overwhelming to implement any security framework. Challenges arise such as

> deciding what to do first, what tools are available for implementation/measurement, and how to get

> what is available to them, where to start, and how to put it all together. Shown below are just a few

> questions the CIS Controls can help to answer. This guide is broken down into six main sections that

> How do

> minimize specific

<!-- page: 5 -->

> of actions to defend against the most common attacks. In version 8.1 of the Controls, there are 18

> the Change Log for moving from a previous Controls version to a current version (e.g., v8 → v8.1).

> 5

> 2/5

> 4/5

> 5/5

> IG1

> IG3

> 7

> 3/7

> 6/7

> IG1

> 14

> 6/14

> 12/14

> CONTROL 4

> 12

> 7/12

> 11/12

> 12/12

> CONTROL 5

> 6

> 4/6

> 6/6

> 8

> 5/8

> Continuous Vulnerability

> Audit Log

> 11/12

> CONTROL 11

> 5

> 4/5

> 5/5

> 5/5

> CONTROL 13

> Network Monitoring

> 11

> Penetration

> Testing

<!-- page: 7 -->

> Nework

> Nework

> Architecture

> Architecture

> Servers

> Things (IoT)

> Things (IoT)

> Removable

> Media

> Removable

> Media

> Portable

> Operating

> Operating

> Libraries

> APIs

> Libraries

> APIs

> Firmware

> Physical

> Physical

> Workforce

> Accounts

> Accounts

> Administrator

> Accounts

> Administrator

> Accounts

> Accounts

> Accounts

> Plans

> Processes

> Procedures

<!-- page: 10 -->

> environments such as cloud, mobile, Industrial Control System (ICS) environments, and Internet of

<!-- page: 11 -->

> ICS, Privacy, etc.

> ICS, Privacy, etc.

> Version 2.0 of the CDM builds on the original version, by mapping the Safeguards to the MITRE

<!-- page: 12 -->

> Windows Management Instrumentation (WMI)

<!-- page: 13 -->

> • CSA Cloud Controls Matrix

> • ISO/IEC 27001:2002

> • NIST SP 800-171 Rev 2

> • NIST SP 800-53 Rev 5

> • NYDFS Part 500

> • PCI DSS v4.0

<!-- page: 16 -->

> minimize specific
