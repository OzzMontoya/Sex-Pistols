from enum import Enum


class SignalAction(str, Enum):
    SWITCH_PHASE = "switch_phase"
    EXTEND_GREEN = "extend_green"
    PRIORITIZE_DIRECTION = "prioritize_direction"


def apply_signal_action(current_phase: str, action: SignalAction) -> str:
    if action == SignalAction.SWITCH_PHASE:
        return "NEXT_PHASE"
    if action == SignalAction.EXTEND_GREEN:
        return current_phase
    if action == SignalAction.PRIORITIZE_DIRECTION:
        return "PRIORITY_CORRIDOR"
    return current_phase
