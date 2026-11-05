# API

## GET /v1/sightings?species=<name>

    [{"id": 1, "species": "Barn Owl", "observer": "ana", "observed_at": "2026-10-04 18:20:00"}]

`observed_at` is the observer's local time, with no offset.

## GET /v1/members/<id>

    {"id": 7, "name": "Ana", "plan": "flock", "plan_renews_on": "2026-12-01"}
