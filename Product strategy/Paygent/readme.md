# Paygent
## Cross-Agent Financial Authority for Agentic Commerce

**Type:** 0→1 Product Discovery / Strategy Case Study  
**Stage:** Discovery  
**Market:** Agentic Commerce / Fintech Infrastructure  
**Initial Market:** India

---

# 1. Executive Summary

AI agents are moving from answering questions toward taking real-world actions: researching products, comparing options, interacting with services, preparing purchases, and increasingly participating in commerce.

The emerging problem is not only whether an AI agent is intelligent enough to make a purchase.

It is:

> Who controls the financial authority given to AI agents when users operate multiple agents across different platforms?

Paygent explores an independent financial-authority layer for AI agents.

Instead of allowing each AI model, agent, merchant, or payment provider to maintain isolated financial permissions, Paygent maintains consumer-defined policies and global spending state across participating agents.

The core architectural principle is:

> The system performing probabilistic reasoning should not also hold unrestricted financial authority.

Paygent does not aim to replace UPI, banks, Razorpay, Cashfree, Visa, Mastercard, or other settlement infrastructure.

It explores the layer above them:

**Agent → Intent → Paygent Authority → Existing Payment Infrastructure**

---

# 2. Why Now?

AI is moving from:

**Chat → Recommendation → Action → Commerce**

Consumers already use AI during shopping, while autonomous purchasing introduces a substantially larger trust problem.

Verified discovery evidence:

- AI-agent market estimated at **$7.84B in 2025**, projected to reach **$52.62B by 2030**.
- **61.5%** of surveyed consumers had used AI for product discovery/recommendations.
- **55.0%** were uncomfortable allowing AI to complete purchases.
- **53.9%** believed AI agents increase online fraud risk.
- **73.9%** expected safeguards such as biometrics or OTP before agent transactions.
- A 2025 study across 18 frontier LLMs reported **94.4% vulnerability to direct prompt injection** and **100% compromise through tested inter-agent trust exploitation**.
- KPMG reported **80% of surveyed leaders identified cybersecurity as the greatest barrier to achieving their AI strategy goals**.

This creates a gap between:

> “I trust AI to help me choose.”

and

> “I trust AI with authority over my money.”

---

# 3. Initial Problem Hypothesis

The first hypothesis was simple:

> Before an AI agent spends money, Paygent asks the human to approve the payment.

Example:

User:
“Buy these Nike shoes under ₹3,000.”

Agent:
Finds shoes for ₹2,899.

Paygent:
“Agent wants to pay ₹2,899 to Nike.”

[Reject] [Approve]

Authentication → Payment.

---

# 4. Why the Initial Hypothesis Was Too Weak

A payment-confirmation screen is not sufficient differentiation.

It could potentially be implemented by:

- AI companies
- operating systems
- payment applications
- payment gateways
- banks

A biometric confirmation is therefore a **feature**, not a defensible standalone company.

This changed the discovery question from:

> How should humans approve AI payments?

to:

> What financial-control problem exists specifically because users may operate multiple independent AI agents and payment systems?

---

# 5. Key Discovery: Fragmented Financial Authority

Consider a user who establishes:

**Total AI-agent spending limit: ₹5,000/month**

Transactions:

ChatGPT Agent → ₹1,200  
Gemini Agent → ₹900  
Claude Agent → ₹1,133

**Total agent spend = ₹3,233**

Claude then attempts to purchase running shoes for ₹3,299.

Individually:

- Claude may consider the purchase valid.
- The merchant may consider it valid.
- The payment provider may consider it valid.
- The user's bank balance may be sufficient.

But:

₹3,233 + ₹3,299 = ₹6,532

The user's global AI spending policy is ₹5,000.

A system with cross-agent state can therefore return:

**DENIED — GLOBAL AGENT BUDGET EXCEEDED**

The problem is not merely transaction authorization.

It is maintaining **financial authority consistently across otherwise isolated agents.**

---

# 6. Product Thesis

> Paygent is an independent financial-authority layer for AI agents that maintains consumer-defined policy, intent and global spending state across participating AI agents while leaving actual money movement to existing regulated payment infrastructure.

Paygent is NOT:

- a bank
- a wallet
- a payment gateway
- an LLM
- another general AI agent
- a biometric payment screen

Paygent explores:

- cross-agent financial identity
- global spending policies
- intent validation
- transaction state
- authorization
- revocation
- auditability
- agent-specific financial permissions

---

# 7. Core Product Principles

## 7.1 Separation of Reasoning and Authority

The LLM can:

- search
- reason
- compare
- recommend
- prepare an action

The deterministic financial layer decides whether that action is permitted.

---

## 7.2 Global Policies

Users define policies once across participating agents.

Example:

**Global**
₹5,000/month across AI agents

**Food**
₹2,000/month

**Agent A**
Can research + prepare purchases

**Agent B**
Can initiate transactions within defined limits

**Prohibited**
P2P transfers

---

## 7.3 Explicit Human Authority

For transactions requiring confirmation, the user receives:

Merchant  
Product/service  
Amount  
Requesting agent  
Relevant intent/context

The user can approve or reject through the appropriate authenticated payment flow.

---

## 7.4 Universal Financial Freeze

One control revokes/blocks Paygent-governed financial authority.

Important limitation:

Paygent cannot stop an AI model from reasoning or acting outside Paygent.

“Freeze” means:

> Freeze financial authority governed through Paygent.

---

# 8. Intent Integrity

Example original instruction:

> “Buy Nike running shoes under ₹3,000.”

Expected transaction:

Merchant: Nike  
Category: Running shoes  
Amount: ₹2,899  
Quantity: 1

Now imagine malicious content manipulates the agent and it attempts:

Merchant/recipient: Different entity  
Amount: ₹7,000  
Category: Different purpose

Paygent evaluates the proposed financial action against deterministic policy and preserved user intent.

The model saying “this transaction is valid” is not itself sufficient authorization.

Paygent should preserve evidence such as:

- original user instruction
- declared action
- agent identity
- tool calls
- transaction payload
- policy decision
- authorization evidence
- execution result

The system should not depend on accessing private LLM chain-of-thought.

---

# 9. Global Transaction State

Paygent must account for both completed and currently executing transactions.

Example:

Global limit: ₹5,000  
Already spent: ₹1,000

Agent A requests: ₹3,000

Paygent temporarily reserves ₹3,000.

State:

Spent: ₹1,000  
Reserved: ₹3,000  
Available: ₹1,000

Agent B simultaneously requests ₹2,500.

Paygent rejects the request because:

₹1,000 + ₹3,000 + ₹2,500 > ₹5,000

If Agent A succeeds:

RESERVED → SPENT

If Agent A fails:

RESERVED → RELEASED

This prevents multiple agents from independently spending the same remaining budget.

---

# 10. Competitive Landscape

## AI Model Providers
Examples: OpenAI, Anthropic, Google

Strength:
Own the agent/model experience.

Limitation relative to Paygent thesis:
Their controls naturally operate inside their own ecosystems.

Paygent hypothesis:
Users may eventually require financial authority spanning multiple independent agent providers.

---

## Payment Providers / Gateways
Examples: Razorpay, Cashfree, Paytm and existing payment infrastructure.

Strength:
Payment execution, merchant relationships and regulated infrastructure.

Limitation relative to Paygent thesis:
A payment provider may have excellent transaction-level controls without necessarily maintaining the user's semantic financial authority across competing AI agents and external payment providers.

---

## Payment Networks / Banks / UPI

Strength:
Actual financial authority and settlement infrastructure.

Paygent does not attempt to replace this layer.

Paygent's proposed role:

Provide agent identity, intent, policy and global state before execution reaches existing financial rails.

---

# 11. Why Paygent Cannot Be Just an SDK

A simple SDK that performs:

IF spending > limit:
    DENY

is reproducible.

A developer could implement:

- counters
- spending limits
- local rules
- simple audit logs

Therefore Paygent's long-term value cannot come from the policy check itself.

Potential defensibility must come from shared infrastructure such as:

- cross-agent state
- normalized agent financial identity
- transaction history
- authorization state
- multiple agent integrations
- payment-provider integrations
- risk signals
- reliability
- regulatory/financial partnerships

The network is potentially more valuable than the individual rule engine.

---

# 12. Cold-Start Strategy Hypothesis

Initial adoption does not necessarily require payment-provider integration.

An agent developer could voluntarily call Paygent before executing an agent-driven transaction.

Example:

Agent wants to spend ₹2,999.

↓

POST /authorize-intent

↓

Paygent evaluates:

Agent identity  
User policy  
Global spend  
Current reservations  
Intent

↓

APPROVED / DENIED

↓

Only an approved request proceeds toward payment.

This provides standalone developer value through reusable authorization, budgeting, audit and transaction-state infrastructure.

However, this only governs **Paygent-connected agents**.

---

# 13. Major Unresolved Problem: Bypass

Suppose:

Agent A → Paygent → Payment

Agent B → Payment directly

Agent B can spend without Paygent knowing beforehand.

Therefore Paygent cannot currently promise:

> “No AI agent can exceed your global limit.”

It can only promise:

> “Paygent-governed agents share and enforce the same global authority state.”

Universal enforcement would eventually require deeper integration with agents, financial institutions, payment providers or another authoritative execution point.

This remains a major open question.

---

# 14. Major Unresolved Problem: Payment-Provider Incentive

A second strategic question remains:

> Why would Razorpay, Cashfree, Paytm, banks or other financial infrastructure integrate Paygent instead of ignoring it or building equivalent functionality?

Potential Paygent value:

Payment infrastructure normally receives transaction information.

Paygent could potentially provide richer agent context:

- which agent initiated the transaction
- original declared user intent
- authorization scope
- global policy status
- transaction history
- agent identity
- authorization evidence
- risk/policy outcome

Whether this creates sufficient economic value for payment providers remains unvalidated.

---

# 15. Technical Feasibility Hypothesis

Proposed architecture:

AI Agent
↓
Paygent Control Plane
↓
Policy + Global State + Intent
↓
Existing Payment Infrastructure
↓
Bank / UPI / Card Rail
↓
Merchant

Paygent would aim to remain outside actual settlement.

It would manage policy and authorization state while regulated financial institutions continue moving money.

Current assessment:

**Technically plausible.**

Regulatory status:

**Not established.**

Being non-custodial does not automatically prove that Paygent requires no financial authorization or regulatory obligations.

Actual classification requires validation with payment partners and qualified Indian fintech/legal specialists.

---

# 16. Relevant Indian Infrastructure

Existing Indian infrastructure makes agentic payments increasingly plausible.

Relevant systems include:

### UPI Circle
Supports delegated payment authority with defined transaction/monthly limits.

### UPI Reserve Pay
Supports blocking funds and subsequently debiting against the reserved amount under defined conditions.

### Agentic Payment Initiatives
Indian payment companies and NPCI are already experimenting with agent-driven commerce and integrations involving AI platforms.

Paygent's thesis is therefore not that payment rails for agents don't exist.

The thesis is:

> As those rails proliferate, financial authority may become fragmented across agents and payment systems.

---

# 17. Prototype Scenario

## Normal Purchase

User:

“Find Nike running shoes under ₹3,000.”

↓

Agent finds:

Nike Running Shoes  
₹2,899

↓

Paygent:

Agent: Shopping Agent  
Merchant: Nike  
Amount: ₹2,899  
Global remaining budget: ₹3,400

Policy: PASS

[Reject] [Continue to Payment]

↓

Authenticated payment flow

↓

Transaction recorded.

---

## Simulated Compromised-Agent Scenario

User originally requested:

“Nike running shoes under ₹3,000.”

A simulated malicious instruction causes the agent to request:

₹7,000  
Different recipient/merchant

Paygent evaluates:

Amount exceeds policy  
Intent mismatch  
Recipient mismatch

↓

**TRANSACTION BLOCKED**

[View Details]

[Freeze Financial Authority]

This prototype demonstrates the separation between:

**what the AI attempts**

and

**what the financial-control system permits.**

---

# 18. Initial Target User Hypothesis

Paygent is NOT initially targeting every consumer.

Early potential users are:

> AI-aware consumers who use multiple AI agents/services and begin delegating commerce or financially consequential actions to them.

Potential initial developer customer:

> Companies/developers building AI agents that execute commerce and do not want to independently build authorization, budgeting, global state, audit and revocation infrastructure.

Both hypotheses require validation.

---

# 19. Core Risks

### Adoption Risk
Agent developers may simply build policy systems themselves.

### Bypass Risk
Non-integrated agents can operate outside Paygent.

### Platform Risk
OpenAI, Google, Anthropic or other platforms could build strong native financial controls.

### Payment Infrastructure Risk
Gateways may build their own agent-governance layers.

### Regulatory Risk
Paygent's exact regulatory obligations are not yet established.

### Network Cold Start
Cross-agent value becomes stronger as more agents participate, creating an early adoption challenge.

### Reliability Risk
If Paygent becomes an authorization dependency, Paygent downtime could prevent legitimate transactions.

---

# 20. What Has Been Invalidated During Discovery

The discovery process rejected several initial assumptions.

### Rejected:
“Biometric approval is the product.”

Reason:
Easy for existing platforms to reproduce.

### Rejected:
“Paygent should become another payment gateway.”

Reason:
Existing regulated payment infrastructure already handles settlement better.

### Rejected:
“A simple spending-limit SDK creates a strong moat.”

Reason:
Developers can reproduce local policy checks.

### Rejected:
“Paygent can guarantee control over every AI agent from Day 1.”

Reason:
Non-integrated agents can bypass the system.

### Rejected:
“Non-custodial automatically means regulatory clearance.”

Reason:
Actual regulatory classification depends on architecture and role.

---

# 21. Current Position

The strongest current Paygent hypothesis is:

> Paygent is an independent financial-authority layer for AI agents, maintaining consumer-defined policy, intent and global spending state across participating models while leaving settlement to existing regulated financial institutions.

The potential moat is not the approval UI.

It is not a fingerprint prompt.

It is not a spending-limit IF statement.

The potential moat is the shared authority infrastructure created if multiple independent agents and eventually multiple financial systems rely on Paygent's representation of:

**Who authorized which agent to spend what, where, why, and under which limits?**

---

# 22. Current Discovery Status

**Problem existence:** Strong evidence

**Consumer trust gap:** Strong evidence

**Agent security problem:** Strong evidence

**Technical concept:** Plausible

**Cross-agent differentiation:** Promising hypothesis

**Developer willingness to integrate:** Unvalidated

**Payment-provider incentive:** Unvalidated

**Universal enforcement:** Unsolved

**Indian regulatory classification:** Unvalidated

**Business model:** Not yet validated

**Product-market fit:** Not established

---

# 23. Next Discovery Question

The next question is not:

“How big could Paygent become?”

It is:

> What is the first real transaction category where Paygent can create standalone value for one agent developer and one user without requiring a major merchant, PSP or bank to adopt Paygent first?

That wedge must provide a credible path from:

First governed transaction
↓
Multiple agents sharing authority
↓
Developer adoption
↓
Transaction volume
↓
Financial/merchant partnerships
↓
Cross-provider authority infrastructure

Until that wedge is identified and validated, Paygent remains a product hypothesis rather than a proven startup.
