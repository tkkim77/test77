"""DICOM 파일을 불러와 3D 메쉬로 변환한다.

관련 요구사항: #test1111-301 (SR-01 DICOM 파일을 불러와 3D 메쉬로 변환)
"""


def load_dicom(path):
    """DICOM 시리즈를 읽어 3차원 배열로 돌려준다."""
    raise NotImplementedError


def to_mesh(volume, threshold=300):
    """임계값 이상인 영역을 표면 메쉬로 만든다."""
    return marching_cubes(volume, threshold)
