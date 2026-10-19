[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event-history](../index.md) / EventChangeContext

# Type Alias: EventChangeContext

> **EventChangeContext** = `object`

Defined in: [ui/src/api-shared/types/event-history.ts:118](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event-history.ts#L118)

Extra provenance for a change, kept as a narrow, additive record rather than
a free-form blob so it stays queryable.

## Properties

### curriculumId?

> `optional` **curriculumId?**: `string`

Defined in: [ui/src/api-shared/types/event-history.ts:120](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event-history.ts#L120)

Curriculum whose cut/reload produced this change.

***

### snapshotId?

> `optional` **snapshotId?**: `string`

Defined in: [ui/src/api-shared/types/event-history.ts:122](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event-history.ts#L122)

Snapshot restored, for SnapshotRestore.
