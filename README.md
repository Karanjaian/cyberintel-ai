# CyberIntel AI

CyberIntel AI is an open-source cybersecurity intelligence platform that automatically collects, parses, and stores cybersecurity news from trusted sources. The long-term goal is to transform raw cybersecurity news into AI-generated threat intelligence summaries and distribute them through dashboards, APIs, and communication channels.

## Current Features

* RSS feed aggregation from multiple cybersecurity sources
* Article parsing and metadata extraction
* PostgreSQL database integration
* SQLAlchemy ORM models
* Duplicate article detection
* Automated article ingestion pipeline

## Supported Sources

* The Hacker News
* BleepingComputer
* Krebs on Security
* Dark Reading

## Architecture

RSS Feeds
→ RSS Parser
→ Article Processing
→ PostgreSQL Database

## Project Structure

```text
cyberintel-ai/
├── app/
│   ├── config/
│   ├── database/
│   ├── ingestion/
│   ├── models/
│   └── main.py
├── docs/
├── scripts/
├── tests/
├── README.md
└── requirements.txt
```

## Current Progress

### Phase 1 - Foundation ✅

* Repository Setup
* PostgreSQL Configuration
* SQLAlchemy Models
* RSS Feed Ingestion
* Article Parser
* Database Storage

### Phase 2 - AI Layer 🚧

* AI Summarization Engine
* Article Content Extraction
* Threat Classification
* Severity Scoring

## Statistics

Current database capability:

* 125+ cybersecurity articles successfully ingested
* Multi-source RSS aggregation
* Duplicate prevention enabled

## Roadmap

### Completed

* [x] Repository Setup
* [x] Configure PostgreSQL Database
* [x] Create SQLAlchemy Models
* [x] Build RSS Ingestion Service
* [x] Build Article Parser
* [x] Store Articles in Database

### Next Milestone

* [ ] Implement AI Summarization Engine

## Technology Stack

* Python
* PostgreSQL
* SQLAlchemy
* Feedparser
* GitHub Projects

## Author

Ian Karanja

Cybersecurity Student | Security Researcher | Builder of Open Source Security Tools
