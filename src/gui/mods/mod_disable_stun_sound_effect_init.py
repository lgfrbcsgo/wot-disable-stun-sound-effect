from debug_utils import LOG_CURRENT_EXCEPTION


def init():
    try:
        import mod_disable_stun_sound_effect
    except Exception:
        LOG_CURRENT_EXCEPTION()
