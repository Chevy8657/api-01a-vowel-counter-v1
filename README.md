# Vowel Counter

Single-purpose API. Stateless. Deterministic. Returns JSON only.

## Endpoints
- GET `/health`
- GET `/v1/vowel-count?text=`

## Example

Request:
`/v1/vowel-count?text=Hello%20world`

Response:
```json
{
  "input": "Hello world",
  "vowel_count": 3
}
