from birdlog_api.db import session
from birdlog_api.models import Member, Sighting


def find_sightings(species=None):
    query = session.query(Sighting)
    if species:
        # An exact match: "barn owl" finds nothing when the row says "Barn Owl".
        query = query.filter(Sighting.species == species)
    return query.order_by(Sighting.observed_at.desc()).all()


def find_member(member_id):
    return session.get(Member, member_id)
