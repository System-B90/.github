[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / GENERATED\_BREAK\_EVENT\_ID\_PREFIX

# Variable: GENERATED\_BREAK\_EVENT\_ID\_PREFIX

> `const` **GENERATED\_BREAK\_EVENT\_ID\_PREFIX**: `"cut-break:"` = `"cut-break:"`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:159](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/gantt/cut-planner.ts#L159)

Synthetic `ganttEventId` prefix for breaks the post-pass generated. They are
real schedule events with no gantt event behind them; the prefix marks their
provenance so a pull-back archives them with the rest of the cut and a
re-cut never duplicates them.
