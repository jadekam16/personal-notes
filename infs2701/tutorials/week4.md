# TUTORIAL 4: Equifax data breach & Data Lifecycle Management

## Learning Focus

This case study examines the Equifax data breach through the lens of Data Lifecycle
Management (DLM), focusing on how understanding and securing each stage of the data
lifecycle can prevent such incidents.

Objectives
• Understand the concepts and stages of Data Lifecycle Management (DLM).
• Analyse the cybersecurity failures that led to the Equifax data breach.
• Identify best practices for securing data at each stage of its lifecycle.
• Understand the importance of timely incident response and patch management.
• Learn about the impact of regulatory compliance on data security practices.

## Summary 
In September 2017, Equifax, one of the largest consumer credit reporting agencies, announced a data breach that exposed the personal information of approximately **147 million individuals**. The breach resulted from a **vulnerability in a web application**, which the
company failed to patch despite being aware of it. Attackers exploited this vulnerability to gain access to Equifax’s servers and steal sensitive information, including Social Security numbers, driver’s license numbers, credit card numbers, and full names. This incident
highlighted the critical importance of robust cybersecurity measures and timely patch management.

## Individual Tasks (before the tutorial):
Review the details of the Equifax data breach. Your preparation should focus on:

### Understanding the stages of Data Lifecycle Management: Creation, Storage, Use, Sharing, Archiving, and Destruction.
Data Lifecycle Management refers to the process of managing data throughout its entire lifecycle, from creation to destruction. The main stages are:

- **Creation**: Data is generated or collected from various sources.
- **Storage**: Data is stored securely, often in databases or data warehouses.
- **Use**: Data is accessed, processed, and analysed for various purposes.
- **Sharing**: Data may be shared internally or externally, following proper access controls.
- **Archiving**: Older data is archived for long-term retention and compliance purposes.
- **Destruction**: Data is securely deleted or destroyed when no longer needed.

Securing data at each stage is crucial to prevent unauthorized access, data breaches, and compliance violations.

### Understanding the importance of securing data at each stage of its lifecycle.
Securing data throughout its entire lifecycle is crucial to prevent data breaches, maintain regulatory compliance, and protect sensitive information. Here are the key reasons why securing data at each stage is important:

**Creation Stage**
- Implement data minimization principles to only collect necessary data, reducing risk exposure.
- Properly classify data based on sensitivity to apply appropriate security controls from the outset.
- Validate data inputs to prevent injection of malicious code or unauthorized data.

**Storage Stage**
- Encrypt data at rest to protect against unauthorized access or theft of storage media.
- Implement access controls and authentication measures for stored data.
- Maintain secure backups to enable recovery in case of data loss or corruption.

**Use Stage**
- Encrypt data in transit when accessed or transmitted over networks.
- Implement robust access controls and monitoring for authorized data usage.
- Prevent data leakage by restricting copy/paste, printing, or downloading of sensitive data.

**Sharing Stage**
- Use secure file transfer protocols and encryption when sharing data internally or externally.
- Implement data loss prevention (DLP) tools to monitor and control data sharing.
- Maintain audit trails to track who accessed or shared what data and when.

**Archiving Stage**
- Ensure archived data remains encrypted and access is restricted to authorized personnel only.
- Implement data integrity checks to detect any tampering or corruption of archived data.
- Migrate archived data to new formats as technology evolves to maintain accessibility.

**Destruction Stage**
- Permanently and securely delete data from all storage locations, including backups.
- Use proven data destruction techniques like secure wiping or physical destruction of media.
- Maintain records of data destruction activities for compliance and auditing purposes.
- Failing to secure data at any stage can expose it to threats like unauthorized access, data tampering, or data loss, leading to regulatory violations, reputational damage, and financial losses. A comprehensive data security strategy across the entire lifecycle is essential.

### Understanding the concepts of Incident Response and Patch Management.
- **Incident Response**: The process of identifying, responding to, and recovering from cybersecurity incidents like data breaches. Timely response can minimise damage.

- **Patch Management**: The process of identifying, testing, and applying software updates and security patches to address known vulnerabilities. Failing to patch promptly leaves systems exposed.

### Read about the Apache Struts vulnerability (CVE-2017-5638) and Equifax’s failure to patch it && Learn how the failure to patch the Apache Struts vulnerability led to the breach.
- The breach occurred due to a vulnerability in the **Apache Struts web application framework (CVE-2017-5638)**. Specifically, the vulnerability exploited was CVE-2017-5638, a critical remote code execution flaw in Apache Struts.
- Equifax failed to patch the vulnerability despite being aware of it and having a patch available. Attackers exploited the unpatched vulnerability to gain access to Equifax's systems and steal sensitive personal data.

**FURTHER DETAILS**
- Apache Struts is an open-source framework used for developing Java web applications. The CVE-2017-5638 vulnerability allowed remote attackers to execute arbitrary code on the server by sending a crafted request to the Struts application. This gave the attackers a foothold into Equifax's systems, allowing them to potentially access and exfiltrate sensitive consumer data.

- Key points about the vulnerability:
  - It was disclosed and a patch was made available in March 2017, but Equifax failed to promptly apply the patch to their systems.
  - Equifax discovered the breach on July 29, 2017, indicating the vulnerability had been left unpatched for several months.
  - Exploiting the vulnerability was relatively straightforward once Equifax's vulnerable systems were identified by the attackers.
  - The flaw allowed the attackers to gain access to Equifax's servers and network, potentially exposing vast amounts of consumer data.

### How it impacted individuals
Equifax's delayed notification of the data breach had significant negative impacts on the affected individuals:

- It left them unaware and vulnerable for over a month after the breach occurred on July 29, 2017. During this time, their personal information could have been exploited by attackers for identity theft, fraud, etc.
- By not promptly notifying consumers, Equifax deprived them of the ability to take timely protective measures like freezing their credit reports to prevent misuse of their stolen data.
- The delay eroded public trust in Equifax and raised concerns about whether the company prioritized protecting consumers over its own interests. This was compounded by executives selling stock before the breach was disclosed.
- Equifax initially required consumers to waive their legal rights to join class-action lawsuits in order to receive free credit monitoring, further angering those impacted by the breach and delay.
- The six-week delay violated data breach notification laws in several states that require companies to inform consumers within a specified timeframe, usually 30-60 days.
- It created confusion and frustration when Equifax's website for checking breach impact and enrolling in credit monitoring services did not work properly after the belated notification.
- The delayed notification left millions of people exposed to potential fraud and identity theft for over a month without their knowledge or ability to take protective action. Equifax's poor handling compounded the breach's impact and highlighted the need for stricter data protection laws and timely breach disclosure requirements.

### Research best practices for patch management and how timely updates can prevent data breaches.
- Implement robust patch management processes to apply security updates promptly.
- Maintain an inventory of all software components and their versions to identify vulnerabilities.
- Regularly monitor for new vulnerabilities and patches from software vendors.
- Conduct risk assessments and prioritize patching based on criticality and exposure.
- Implement defense-in-depth security measures, as patching alone is not sufficient.
- Develop and test incident response plans to minimize the impact of potential breaches.

Regulatory compliance frameworks like GDPR and industry standards also emphasize the importance of data security and timely incident response.

### Understand the importance of managing and maintaining third-party software components effectively to prevent vulnerabilities.