# Week 2 Case Study: Capital One Data Breach 

## Paper 1
### Summary
The Capital One data breach in 2019 was a major cybersecurity incident where a hacker gained unauthorized access to the company's cloud-based servers hosted on Amazon Web Services (AWS). The attack exploited a **misconfigured web application firewall (WAF)** and a server-side request forgery (SSRF) vulnerability, allowing the hacker to obtain temporary credentials and access data stored in AWS S3 buckets.

### Key Points
- The hacker used anonymizing services like TOR to hide their IP address and executed an SSRF attack to trick the server into running commands as a remote user.
- The misconfigured WAF allowed the hacker to relay commands to AWS's metadata service, obtaining temporary credentials for the environment.
- With the stolen credentials, the hacker listed all S3 buckets and copied nearly 30GB of sensitive data, including credit application records of over 100 million customers.
- The incident exposed failures in implementing security controls recommended by the NIST Cybersecurity Framework, such as access controls, vulnerability management, monitoring, and auditing.
- It highlighted the importance of properly configuring cloud services, implementing the principle of least privilege, and continuously monitoring for unauthorized access and activities.
- Despite existing regulations and compliance standards, the Capital One breach demonstrated gaps in effectively implementing and maintaining robust cybersecurity controls, leading to one of the largest data breaches in the financial sector.

## Paper 2 
### Summary 
The Capital One data breach in 2019 was a major cybersecurity incident that exposed the personal information of over 100 million individuals. This systematic analysis using the Cybersafety methodology reveals that the breach was not just caused by a single misconfigured firewall, but rather a series of control failures spanning multiple levels of the organization and its external environment.

### Key Findings
- The breach exploited vulnerabilities like Server-Side Request Forgery (SSRF), weaknesses in AWS infrastructure, an overly permissive IAM role, inadequate encryption, and ineffective intrusion detection systems.
- Control failures occurred at various levels, from technical (misconfigured firewall, excessive privileges) to organizational (lack of risk management processes, inadequate security practices) to regulatory (lack of oversight, uncoordinated security requirements).
- The analysis identifies nine key control failures, including the cloud service provider's failure to protect against reverse proxy attacks, Capital One's lack of intrusion monitoring, violation of least privilege principle, and use of inadequate encryption techniques.
- Contributing factors included Capital One's rapid cloud adoption without maturing risk management practices, lack of board involvement in cybersecurity, and the cloud service provider's prioritization of new features over fixing vulnerabilities.

### Recommendations
- Match the pace of technology adoption with risk management maturity.
- Implement rigorous risk management processes and revisit the shared responsibility model.
- Involve the board and CISO in cybersecurity risk management.
- Cloud providers should reduce complexity, prioritize security over new features, and address vulnerabilities promptly.
- Improve regulatory oversight of cloud providers and coordinate security requirements.
- Reinforce security practices like least privilege, defense-in-depth, and robust application review processes.
- The analysis emphasizes treating cybersecurity as a systemic issue, considering interactions between components and addressing organizational and environmental factors beyond just technical controls.

## Paper 3: Cease and Desist Order
### Summary
This is a Consent Order issued by the Office of the Comptroller of the Currency (OCC) against Capital One, N.A. and Capital One Bank (USA), N.A. (collectively referred to as "the Bank"). The key points are:

### OCC's Findings
The Bank failed to establish effective risk assessment processes before migrating to the cloud environment, and lacked appropriate risk management controls for the cloud.
The Bank's internal audit failed to identify numerous control weaknesses in the cloud environment and did not effectively report identified issues to the Audit Committee.
The Board failed to hold management accountable for addressing certain internal control gaps and weaknesses raised by internal audit.
The Bank was in noncompliance with information security standards and engaged in unsafe or unsound practices.

### Corrective Actions Required
Appoint a Compliance Committee to monitor the Bank's compliance with the Order.
Develop a comprehensive Action Plan detailing remedial actions for compliance.
Improve Board and management oversight of the cloud information security program.
Enhance risk assessment processes for cloud and legacy environments.
Strengthen risk management for cloud operations.
Enhance internal controls testing in the cloud environment.
Improve the internal audit program, including risk assessment methodology and reporting to the Audit Committee.
The Order outlines specific requirements, deadlines, and oversight mechanisms for the Bank to address the identified deficiencies.
