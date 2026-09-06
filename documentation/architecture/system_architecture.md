# Zecpath AI – System Architecture

## 1. Overview

Zecpath AI is organized as a modular AI recruitment platform.

The architecture separates recruitment processing, scoring, interviews, security, integration, performance, and monitoring components.

---

## 2. High-Level Architecture

```text
                    Candidate
                       |
                       v
                 Resume Upload
                       |
                       v
                Resume Parser
                       |
                       v
                  ATS Engine
                       |
                       v
                HR Screening
                       |
                       v
                 HR Interview
                       |
                       v
              Technical Interview
                       |
                       v
             Behavioral Analysis
                       |
                       v
              Integrity Detection
                       |
                       v
                Unified Scoring
                       |
                       v
             Final Recommendation
                       |
                       v
          Hiring Intelligence Report