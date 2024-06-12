# Week 2 Case Study: Capital One Data Breach: Drawing a Rich Picture

## Critical Lessons Learnt 
The 2019 Capital One data breach was a major cybersecurity incident that exposed personal data of over 100 million individuals. While often portrayed as a simple misconfiguration, a systematic analysis reveals multiple control failures across various levels that enabled the breach:

### Technical Failures
- A misconfigured web application firewall (ModSecurity WAF) allowed the initial server-side request forgery attack
- A weakness in AWS EC2 infrastructure enabled the attacker to harvest credentials and gain control
- An overly permissive IAM role granted excessive privileges to access and decrypt S3 data buckets
- Inadequate encryption methods allowed the attacker to decrypt the stolen data
- Ineffective intrusion detection and monitoring failed to raise alerts on suspicious activities

### Organisational Failures
- Capital One failed to follow security best practices like least privilege, defense-in-depth when operating in the cloud
- Lack of robust application security review and vulnerability management processes
- Mismatch between rapid cloud adoption and risk management maturity
- Insufficient board oversight and prioritization of cybersecurity risks

### Regulatory and Industry Failures
- Lack of regulatory oversight on cloud service providers' security practices
- Layering of uncoordinated security requirements by multiple regulators
- AWS failed to prioritize fixing platform vulnerabilities over new feature releases
- The analysis emphasizes treating cybersecurity as a systemic issue, addressing vulnerabilities from component interactions, organizational structures, and lack of informational feedbacks.

## How People Use Rich Pictures to Help Them Think and Act
- The paper discusses the use of rich pictures as a tool in systems thinking and problem-solving workshops. Rich pictures are hand-drawn sketches that depict a situation from multiple perspectives, including objective elements like layouts and relationships, as well as subjective elements like emotions, biases, and different viewpoints.

### Some key points about rich pictures:
- They allow participants to bypass mental filters and express things that may be difficult to articulate directly.
- They can surface hidden, cryptic, or taboo aspects of a situation through imagery and humor.
- While transient, rich pictures contain valuable insights about the system and group dynamics.
The authors propose a framework for critically analyzing rich pictures, drawing from art criticism principles like examining context, content, themes, and interpretations.

The paper illustrates the analysis approach using two contrasting rich picture examples from workshops in Slovakia on sustainable development indicators:
- One rich picture coherently depicted the perceived dominance of economic indicators over sustainability indicators, expressing deeper themes.
- The other lacked clear insights and failed to address the core question about indicator influence.
- The authors argue that rich picture analysis can reveal what a group really thinks about a complex problem, allowing expression of the group's "inner life" in ways unusual or challenging to articulate directly.
