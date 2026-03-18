# Capsule 289 — Multi-Gateway Orchestration

**Source**: 2026-03-18_agency.md
**Family**: agency
**Lens**: C (Cloud/Admissibility)

When multiple gateways run in a ring topology (Machine A -> gateway -> Machine B -> gateway -> Machine C -> gateway -> Machine A), the ledger chain enables tracing origin, verifying integrity, detecting corruption, and reconstructing history. This creates a distributed file nervous system where every movement is auditable across the entire network.

The scaling path from single gateway to full nervous system follows explicit versions: v3 adds an event bus (NATS, Kafka, or Redis streams) for real-time coordination, v4 adds signed witness bundles using ed25519 signatures for cryptographic authentication, and v5 adds autonomous nodes with gossip synchronization for decentralized coordination without a central controller.

This multi-gateway topology directly models the corpus concept of distributed brain architecture: each gateway is an autonomous node with its own ledger, its own corridor constraints, and its own witness chain, but all nodes participate in a shared integrity fabric that allows the system to self-verify across boundaries.

## Key Objects
- Ring topology: Machine A -> B -> C -> A
- Version roadmap: v3 (event bus), v4 (signatures), v5 (gossip)
- Distributed ledger fabric across gateway network

## Key Laws
- Every cross-gateway movement must be traceable to its origin
- Replay protection must work across the full ring, not just locally
- Integrity verification must be possible at any node for any event chain

## Source
- `29_ACCEPTED_INPUTS/2026-03-18_agency.md`
