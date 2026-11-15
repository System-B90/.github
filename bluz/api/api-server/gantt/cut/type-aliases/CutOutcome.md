[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / CutOutcome

# Type Alias: CutOutcome

> **CutOutcome** = \{ `error`: [`ApiCurriculumCutError`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutError.md); `ok`: `false`; \} \| \{ `ok`: `true`; `result`: [`ApiCurriculumCutResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutResponse.md); \}

Defined in: [ui/src/api-server/gantt/cut.ts:103](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/gantt/cut.ts#L103)

Server orchestration for the curriculum → schedule cut ("גזירה ללו"ז", #118).
Consumes the pure planner (#117) and writes the resulting occurrences into the
linked iteration's MongoDB. This is `api-server`: it reads gantt data from
Postgres (Drizzle) and writes schedule events to Mongo. The pure adaptation /
mapping helpers are exported so they can be unit-tested without any DB.
