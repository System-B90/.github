[**TypeDoc API**](../../index.md)

***

[TypeDoc API](../../index.md) / [settings](../index.md) / WsScope

# Enumeration: WsScope

Defined in: [session-server/session-common.ts:103](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/session-server/session-common.ts#L103)

Privilege label signed into a connect ticket (#656). Bluz serves two kinds
of socket and they may not see the same traffic, so the scope decides what a
socket is allowed to register for — see `session-server.ts`.

## Enumeration Members

### Hanich

> **Hanich**: `"hanich"`

Defined in: [session-server/session-common.ts:107](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/session-server/session-common.ts#L107)

Hanich. Content-free refresh pings and nothing else.

***

### Segel

> **Segel**: `"segel"`

Defined in: [session-server/session-common.ts:105](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/session-server/session-common.ts#L105)

Segel/Admin. The full staff calendar wire.
