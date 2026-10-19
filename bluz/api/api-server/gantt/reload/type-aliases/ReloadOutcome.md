[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/reload](../index.md) / ReloadOutcome

# Type Alias: ReloadOutcome

> **ReloadOutcome** = \{ `error`: [`ApiCurriculumReloadError`](../../../../api-shared/types/gantt/reload/type-aliases/ApiCurriculumReloadError.md); `ok`: `false`; \} \| \{ `ok`: `true`; `result`: [`ApiCurriculumReloadResponse`](../../../../api-shared/types/gantt/reload/type-aliases/ApiCurriculumReloadResponse.md); \}

Defined in: [ui/src/api-server/gantt/reload.ts:52](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/reload.ts#L52)

Schedule reload ("עדכון הלו״ז לפי הגאנט"): re-plans a curriculum that was
already cut and reconciles the difference into the linked iteration's
schedule — adding new occurrences, retiming changed ones and archiving ones
the gantt dropped.

Precedence: an event a human edited after the cut wins. Such events are
reported as conflicts and skipped unless the caller passes their ids in
`overrideEventIds`. "Edited by a human" comes from the event change log
(`db-event-history`), never from guessing at field values.
