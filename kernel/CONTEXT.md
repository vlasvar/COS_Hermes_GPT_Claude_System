# Domain context

This file defines the canonical vocabulary. It contains no platform-specific implementation detail.

## Terms

**Instance** — A private deployment owned by one person or organization. It contains live data and is never committed to this template repository.

**Kernel** — The model-agnostic rules, terminology, permissions, and workflows shared by every agent adapter.

**Agent adapter** — A thin set of instructions that loads the kernel into a specific agent environment without redefining it.

**Operational store** — Structured records describing current work. The default implementation is Google Sheets.

**Evidence store** — Source documents, files, and links supporting operational records. The default implementation is Google Drive.

**Inbox item** — Unprocessed information that has entered the system.

**Project** — A desired outcome requiring more than one action.

**Action** — A concrete, observable next step that can be completed by one owner.

**Commitment** — A promise made by or to the user, with an expected outcome or date.

**Decision** — A selected course of action plus rationale and a trigger for reconsideration.

**Contact** — A person or organization relevant to an active record.

**Review** — A scheduled examination of system state that produces findings and next actions.

**Agent log entry** — An auditable record of a material operation proposed or completed by an agent.

**Approval gate** — A policy check that prevents an agent from performing a high-impact action without explicit authorization.

**Dashboard** — A replaceable view of the operational store. It is not a source of truth.
