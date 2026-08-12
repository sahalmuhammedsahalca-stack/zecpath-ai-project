# AI Data Entity Design Document

## Objective

The objective of this document is to define the standard data entities used in the AI Recruitment System. These entities help convert unstructured resume and job description data into structured information that can be processed by AI modules such as Resume Parser, ATS Scoring Engine, Candidate Ranking, and Interview AI.

## Candidate Profile Entity

The Candidate Profile represents all important information extracted from a candidate's resume.

### Attributes

- Name
- Email
- Phone Number
- Location
- Skills
- Education
- Work Experience
- Certifications
- Projects
- Languages

## Job Profile Entity

The Job Profile represents all important information extracted from a job description.

### Attributes

- Job Title
- Company
- Location
- Required Skills
- Preferred Skills
- Experience Required
- Education Required
- Responsibilities
- Salary
- Employment Type

## Skill Object

The Skill Object represents an individual skill that belongs to a candidate or is required for a job.

### Attributes

- Skill Name
- Skill Category
- Skill Level

### Example

- Skill Name: Python
- Skill Category: Programming
- Skill Level: Intermediate

## Experience Object

The Experience Object represents a candidate's work history in a structured format.

### Attributes

- Company Name
- Job Title
- Duration
- Responsibilities

### Example

- Company Name: XYZ Technologies
- Job Title: Python Developer
- Duration: 2 Years
- Responsibilities:
  - Developed backend APIs
  - Fixed software bugs
  - Collaborated with the development team