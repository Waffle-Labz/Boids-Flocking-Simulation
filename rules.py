
from config import *

def get_offset(boid, other):
    """Return the shortest wrapped displacement from boid to other."""
    dx = other.x - boid.x
    dy = other.y - boid.y

    dx = (dx + WIDTH / 2) % WIDTH - WIDTH / 2
    dy = (dy + HEIGHT / 2) % HEIGHT - HEIGHT / 2

    return dx, dy

def get_distance(boid, other):
    """Calculate distance using the wrapped screen geometry."""
    dx, dy = get_offset(boid, other)
    return (dx ** 2 + dy ** 2) ** 0.5

def cohesion(boid, boids):
    offset_x = 0
    offset_y = 0
    total = 0

    for other in boids:
        if other is boid:
            continue

        dx, dy = get_offset(boid, other)
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < PERCEPTION_RADIUS_COHESION:
            offset_x += dx
            offset_y += dy
            total += 1

    if total > 0:
        offset_x /= total
        offset_y /= total

        boid.a_x += offset_x * COHESION_STRENGTH
        boid.a_y += offset_y * COHESION_STRENGTH

def separation(boid, boids):
    move_x = 0
    move_y = 0
    total = 0

    for other in boids:
        if other is boid:
            continue

        dx, dy = get_offset(boid, other)
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < PERCEPTION_RADIUS_SEPARATION:
            move_x -= dx
            move_y -= dy
            total += 1

    if total > 0:
        move_x /= total
        move_y /= total

        boid.a_x += move_x * SEPARATION_STRENGTH
        boid.a_y += move_y * SEPARATION_STRENGTH

def alignment(boid, boids):
    avg_v_x = 0
    avg_v_y = 0
    total = 0

    for other in boids:
        if other is boid:
            continue

        distance = get_distance(boid, other)

        if distance < PERCEPTION_RADIUS_ALIGNMENT:
            avg_v_x += other.v_x
            avg_v_y += other.v_y
            total += 1

    if total > 0:
        avg_v_x /= total
        avg_v_y /= total

        boid.a_x += (avg_v_x - boid.v_x) * ALIGNMENT_STRENGTH
        boid.a_y += (avg_v_y - boid.v_y) * ALIGNMENT_STRENGTH
