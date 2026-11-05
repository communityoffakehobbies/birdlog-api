from flask import Flask, jsonify, request

from birdlog_api.store import find_member, find_sightings

app = Flask(__name__)


@app.get("/v1/sightings")
def sightings():
    rows = find_sightings(species=request.args.get("species"))
    return jsonify(
        [
            {
                "id": row.id,
                "species": row.species,
                "observer": row.observer,
                "observed_at": row.observed_at.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for row in rows
        ]
    )


@app.get("/v1/members/<int:member_id>")
def member(member_id):
    row = find_member(member_id)
    return jsonify(
        {
            "id": row.id,
            "name": row.name,
            "plan": row.plan,
            "plan_renews_on": row.plan_renews_on.isoformat(),
        }
    )
