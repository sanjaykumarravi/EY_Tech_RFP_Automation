Agentic AI – B2B RFP Automation System
EY Techathon 6.0 | Challenge IV – FMCG (Asian Paints)

Team: T-Flames
Institute: Bharathidasan Institute of Management (BIM), Trichy

Project Overview

Large industrial manufacturers in the FMCG and FMEG space rely heavily on B2B tenders issued by government departments, PSUs, and LSTK project executors. While this channel drives significant revenue, the RFP response process is largely manual, fragmented, and time-consuming across Sales, Technical, and Pricing teams.

This project introduces an Agentic AI–driven RFP Automation System that automates the end-to-end RFP lifecycle — from detection and qualification to technical SKU matching, pricing estimation, and final PDF quotation generation.

The system leverages a Master Orchestrator Agent coordinating multiple specialized AI worker agents, enabling faster response times, improved accuracy, and higher win probability.

Key Features

Automated RFP detection from public tender portals

Intelligent RFP summarization

Technical specification extraction and SKU matching

Transparent Spec Match (%) scoring

Automated pricing and testing cost estimation

System-generated, ready-to-submit PDF quotation

Web-based dashboard for review, download, and archival

Modular, scalable agent-based architecture

System Architecture
Agent Roles

Sales Agent

Scans predefined tender URLs

Detects new RFPs and deadlines

Summarizes RFP requirements

Technical Agent

Extracts technical specifications

Matches RFP specs to OEM product SKUs

Calculates Spec Match percentage

Pricing Agent

Estimates material pricing

Adds testing and acceptance costs

Generates commercial breakdown

Master Orchestrator Agent

Coordinates agent workflows

Consolidates outputs

Triggers PDF quotation generation

Technology Stack

Frontend: Streamlit (Web UI)

Backend: Python

Agent Orchestration: Custom Agent Logic (Extensible to n8n / LangGraph)

Data Processing: Pandas

Web Scraping: Requests, BeautifulSoup

Document Generation: ReportLab / FPDF (PDF generation)

Storage: Local file system (CSV, PDF)

LLM Ready: OpenAI / HuggingFace (Optional extension)

Project Structure
rfp_automation/
│
├── app.py                 # Streamlit application
├── agents.py              # Master & worker agent logic
├── scraper.py             # RFP detection and scraping
├── matcher.py             # SKU matching and spec scoring
├── pricing.py             # Pricing and cost estimation
├── pdf_generator.py       # PDF quotation generation
│
├── data/
│   ├── rfp_sample.txt
│   ├── product_catalog.csv
│   └── pricing_table.csv
│
├── saved_rfps/             # Generated outputs
│   ├── quotations/
│   ├── sku_matching.csv
│   └── pricing.csv
│
├── requirements.txt
└── README.md

Installation & Setup
1. Clone the Repository
git clone <repository-url>
cd rfp_automation

2. Install Dependencies
pip install -r requirements.txt

3. Run the Application
streamlit run app.py

User Journey

System detects new RFPs from tender portals

Sales Agent summarizes and qualifies RFP

Technical Agent matches specs to OEM SKUs

Pricing Agent estimates costs

Master Agent consolidates results

System generates a PDF quotation

User reviews, downloads, and archives the RFP

Key Metrics & Business Impact

70–80% reduction in RFP response turnaround time

3–5× increase in number of RFPs responded to

Higher accuracy & compliance through standardized logic

Improved win probability via faster submissions

Reduced dependency on expert availability

Scalable solution for enterprise deployment

Future Enhancements

Integration with ERP, CRM, and PLM systems

Real-time tender monitoring using schedulers

Advanced NLP-based spec similarity scoring

Multi-language RFP support

Approval workflows and audit logs

Cloud deployment with role-based access

Team T-Flames

Sanjaykumar S R
Analytics & Technology Specialist

Python, automation, agent orchestration

Streamlit, n8n, API integration

AI-powered business automation

Charulatha R
Finance & Business Strategy Specialist

Pricing logic and commercial modeling

Business requirement mapping

RFP financial evaluation

Disclaimer

This project is developed as part of EY Techathon 6.0 using synthetic and publicly available data for demonstration purposes only.
