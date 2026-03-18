# Capsule 285 — Event Witness Bundle Schema

**Source**: 2026-03-18_agency.md
**Family**: agency
**Lens**: S (Square/Structure)

Each action in the Micro-Gateway v2 produces a structured witness record called an Event Witness Bundle. The schema is: EVENT = {id: SHA256(file_bytes), ts: unix_timestamp, src_path, dst_path, size, actor: gateway_id, prev_hash: last_event_hash, hash: SHA256(prev_hash + event_payload)}. This creates a tamper-evident chain where every event references its predecessor.

The witness bundle serves as both audit trail and integrity proof. Because each event's hash incorporates the previous event's hash, the chain cannot be modified retroactively without invalidating all subsequent entries. This is the same principle as blockchain ledgers but applied to file-movement events within the Athena nervous system.

The bundle schema directly parallels the broader corpus concept of witness crystals: durable, externalized proof that a transformation occurred lawfully. In the scaling path, v3 adds event bus (NATS/Kafka/Redis), v4 adds ed25519 signed witness bundles, and v5 adds autonomous nodes with gossip synchronization.

## Key Objects
- EVENT record with chained SHA-256 hashes
- Tamper-evident append-only ledger (ledger.log)
- Gateway identity as actor field

## Key Laws
- Every event must reference the previous event hash (chain integrity)
- No event may be inserted or modified without breaking the chain
- Witness bundles must be externalized durably, never held only in memory

## Source
- `29_ACCEPTED_INPUTS/2026-03-18_agency.md`
