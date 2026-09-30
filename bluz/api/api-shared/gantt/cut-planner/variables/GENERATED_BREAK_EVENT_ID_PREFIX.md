[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / GENERATED\_BREAK\_EVENT\_ID\_PREFIX

# Variable: GENERATED\_BREAK\_EVENT\_ID\_PREFIX

> `const` **GENERATED\_BREAK\_EVENT\_ID\_PREFIX**: `"cut-break:"` = `"cut-break:"`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:164](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L164)

Synthetic `ganttEventId` prefix for breaks the post-pass generated. They are
real schedule events with no gantt event behind them; the prefix marks their
provenance so a pull-back archives them with the rest of the cut and a
re-cut never duplicates them.
