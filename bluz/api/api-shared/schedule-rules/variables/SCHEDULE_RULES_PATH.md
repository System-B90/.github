[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/schedule-rules](../index.md) / SCHEDULE\_RULES\_PATH

# Variable: SCHEDULE\_RULES\_PATH

> `const` **SCHEDULE\_RULES\_PATH**: `"/rules"` = `"/rules"`

Defined in: [ui/src/api-shared/schedule-rules.ts:11](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/schedule-rules.ts#L11)

The week-building rules ("R-<n>") as data: one id, title and meaning per
rule. Mirrors `plugin/bluz/skills/bluz/RULES.md` (the agent's copy); keep
the two in sync. The staff page `/rules` renders it, and any UI that cites
a rule id links to its anchor there (`scheduleRuleHref`).

Pure data — imported by the server check (`shuffle-alignment.ts`) for its
rule ids and by the client for titles and links.
