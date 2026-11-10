"""프린팅 진행률을 1초 간격으로 갱신한다.

관련 요구사항: #test1111-302 (SR-02 프린팅 진행률을 1초 간격으로 표시)
"""

REFRESH_SECONDS = 1


def progress(done_layers, total_layers):
    return round(done_layers / total_layers * 100, 1)
