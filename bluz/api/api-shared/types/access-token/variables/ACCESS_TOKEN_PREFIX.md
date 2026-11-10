[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/access-token](../index.md) / ACCESS\_TOKEN\_PREFIX

# Variable: ACCESS\_TOKEN\_PREFIX

> `const` **ACCESS\_TOKEN\_PREFIX**: `"bluz_pat_"` = `"bluz_pat_"`

Defined in: [ui/src/api-shared/types/access-token.ts:14](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/access-token.ts#L14)

Every token starts with this, so secret scanners (and people) can spot a
leaked one. The CLI keys its header choice off it too.
