[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/snapshot-diff](../index.md) / SnapshotChange

# Enumeration: SnapshotChange

Defined in: [ui/src/components/schedule/calendar/calendar/snapshot-diff.ts:22](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/schedule/calendar/calendar/snapshot-diff.ts#L22)

How one event differs between a snapshot and the live schedule.

## Enumeration Members

### Added

> **Added**: `"added"`

Defined in: [ui/src/components/schedule/calendar/calendar/snapshot-diff.ts:29](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/schedule/calendar/calendar/snapshot-diff.ts#L29)

Live only (added since): restoring removes it.

***

### Changed

> **Changed**: `"changed"`

Defined in: [ui/src/components/schedule/calendar/calendar/snapshot-diff.ts:25](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/schedule/calendar/calendar/snapshot-diff.ts#L25)

In both, with different content: restoring writes the snapshot's back.

***

### Deleted

> **Deleted**: `"deleted"`

Defined in: [ui/src/components/schedule/calendar/calendar/snapshot-diff.ts:27](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/schedule/calendar/calendar/snapshot-diff.ts#L27)

In the snapshot only (deleted since): restoring re-creates it.
