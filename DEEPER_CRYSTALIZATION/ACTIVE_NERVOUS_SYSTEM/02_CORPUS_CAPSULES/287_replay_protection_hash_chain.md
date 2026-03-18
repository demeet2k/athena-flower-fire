# Capsule 287 — Replay Protection and Hash Chain

**Source**: 2026-03-18_agency.md
**Family**: agency
**Lens**: S (Square/Structure)

Replay protection is implemented through a seen_hashes registry. When a file hash has already been processed, the event is ignored: if file_hash in seen_hashes: ignore_event(). This prevents infinite loops when multiple gateways interconnect in a ring topology (Machine A -> B -> C -> A).

The hash chain provides integrity: each event's hash incorporates the previous event's hash plus the current payload, creating a tamper-evident sequence anchored at a GENESIS block. The last_hash() function reads the final line of the ledger to retrieve the current chain tip, and append_event() computes the new hash as SHA256(prev_hash + event_payload).

Together, replay protection and hash chaining solve two complementary problems: replay protection prevents circular re-processing in distributed topologies, while hash chaining prevents retroactive tampering. The combination creates a system where the ledger can be audited at any point to verify that no events were inserted, modified, or replayed illegally.

## Key Objects
- seen_hashes set for duplicate detection
- GENESIS anchor for hash chain initialization
- last_hash() and append_event() chain maintenance functions

## Key Laws
- Duplicate file hashes are rejected (replay protection)
- Each event hash depends on all previous events (chain integrity)
- The chain anchors at GENESIS and extends monotonically

## Source
- `29_ACCEPTED_INPUTS/2026-03-18_agency.md`
