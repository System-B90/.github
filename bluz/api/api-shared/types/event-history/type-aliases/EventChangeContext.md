[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event-history](../index.md) / EventChangeContext

# Type Alias: EventChangeContext

> **EventChangeContext** = `object`

Defined in: [ui/src/api-shared/types/event-history.ts:118](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/event-history.ts#L118)

Extra provenance for a change, kept as a narrow, additive record rather than
a free-form blob so it stays queryable.

## Properties

### curriculumId?

> `optional` **curriculumId?**: `string`

Defined in: [ui/src/api-shared/types/event-history.ts:120](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/event-history.ts#L120)

Curriculum whose cut/reload produced this change.

***

### snapshotId?

> `optional` **snapshotId?**: `string`

Defined in: [ui/src/api-shared/types/event-history.ts:122](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/event-history.ts#L122)

Snapshot restored, for SnapshotRestore.
