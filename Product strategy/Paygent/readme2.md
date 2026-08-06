# Paygent

A cross-agent financial authority layer for AI agents.

Paygent V0 proves one core mechanism: multiple independent AI agents can request financial authority against one shared user-defined spending limit.

Example:

```text
Global authority: INR 5,000
Agent A requests INR 3,000 -> APPROVED
Remaining authority: INR 2,000
Agent B requests INR 2,500 -> DENIED
