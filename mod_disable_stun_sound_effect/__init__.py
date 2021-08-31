from gui.Scaleform.daapi.view.battle.shared.timers_panel import TimersPanel
from mod_hooking.strategy import override


@override(TimersPanel, "_TimersPanel__playStunSoundIfNeed")
def noop(*args, **kwargs):
    pass
