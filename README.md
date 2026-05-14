# AI Runtime

AI-assisted engineering runtime focused on automated code review, architecture analysis, and multi-agent development workflows.

Built in Python with a provider-based architecture, allowing different LLM providers and specialized agents to execute engineering pipelines from Git diffs and repository context.

---

# Features

- Multi-agent engineering review
- Prompt-driven pipelines
- Git diff analysis
- AI-assisted code review
- Security and architecture validation
- Provider abstraction layer
- Persistent pipeline outputs
- Runtime state tracking
- Modular tooling structure
- Random Groq key rotation

---

# Architecture

```txt
Git Diff
    ↓
Pipeline
    ↓
Agent Loader
    ↓
Provider Factory
    ↓
LLM Provider
    ↓
Engineering Agent
    ↓
Structured Output