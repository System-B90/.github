[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/schedule-validation/rule-ids](../index.md) / VALIDATED\_RULE\_IDS

# Variable: VALIDATED\_RULE\_IDS

> `const` **VALIDATED\_RULE\_IDS**: readonly \[`"R-10"`, `"R-11"`, `"R-12"`, `"R-20"`, `"R-21"`, `"R-23"`, `"R-24"`, `"R-25"`, `"R-26"`, `"R-27"`, `"R-32"`, `"R-40"`, `"R-41"`, `"R-42"`, `"R-47"`, `"R-49b"`, `"R-49d"`, `"R-48a"`, `"R-50"`, `"R-51"`, `"R-55"`, `"R-57"`, `"R-58"`, `"R-60"`, `"R-64"`, `"R-65"`, `"R-71"`, `"R-68"`, `"R-69"`, `"R-6A"`\]

Defined in: [ui/src/api-shared/schedule-validation/rule-ids.ts:17](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/schedule-validation/rule-ids.ts#L17)

The rules the schedule validator checks, in the order it runs them (the
rules page order). Kept apart from the checks so the client can list them
without bundling the checks; `registry.ts` must hold exactly these
(pinned by `tests/backend/schedule-validation.test.ts`).

Not here — procedural or not checkable from a schedule's events:
R-01–R-03, R-13 (its violations are R-12's), R-14 (needs the previous
week's `weekendDuty`), R-22 (an action; the content is R-20's), R-30,
R-31 (covered by R-24 and R-32), R-43, R-44 (needs Gantt recurrence),
R-45, R-46 (needs the event's history), R-48, R-48b, R-48c, R-49a, R-49c,
R-49e, R-52/R-53 (exemptions inside R-50/R-51), R-54 (inside R-50), R-56,
R-59, R-5A, R-61 (no headcounts), R-62, R-63, R-66, R-67, R-70, R-80–R-85.
