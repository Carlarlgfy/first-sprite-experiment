import pygame


def get_tight_hitbox(surface):
    """Return a pygame.Rect tightly wrapping the visible (non-transparent) pixels of a surface."""
    mask = pygame.mask.from_surface(surface)
    rects = mask.get_bounding_rects()
    if not rects:
        return pygame.Rect(0, 0, surface.get_width(), surface.get_height())
    return rects[0].unionall(rects[1:])
