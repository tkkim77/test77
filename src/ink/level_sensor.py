"""바이오 잉크 잔량을 감시해 부족하면 경고한다.

관련 요구사항: #test1111-303 (SR-03 잉크 잔량 20% 미만 시 경고 표시)
"""

WARN_PERCENT = 20


def need_warning(level_percent):
    return level_percent < WARN_PERCENT
