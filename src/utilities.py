__all__ = ["singular"]

def singular(plural): # FIXME: deprecated, use translation metadata
    # converse of plural (kinda)
    # this is used to map plural team names back to singular,
    # so we don't need to worry about stuff like possessives
    # Note that this is currently only ever called on team names,
    # and will require adjustment if one wishes to use it on roles.
    # fool is present since we store fool wins as 'fool' rather than
    # 'fools' as only a single fool wins, however we don't want to
    # chop off the l and have it report 'foo wins'
    # same thing with 'everyone'
    conv = {"wolves": "wolf",
            "succubi": "succubus",
            "fool": "fool",
            "everyone": "everyone"}
    if plural in conv:
        return conv[plural]
    # otherwise we just added an s on the end
    return plural[:-1]
