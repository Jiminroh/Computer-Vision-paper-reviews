from typing import Tuple, List

import ast

from roi.wrapper import Wrapper as ROIWrapper


class Config(object):

    IMAGE_MIN_SIDE: float = 800.0
    IMAGE_MAX_SIDE: float = 1333.0

    ANCHOR_RATIOS: List[Tuple[int, int]] = [(1, 2), (1, 1), (2, 1)]
    ANCHOR_SCALES: List[int] = [1]
    POOLING_MODE: ROIWrapper.Mode = ROIWrapper.Mode.ALIGN

    @classmethod
    def describe(cls):
        text = '\nConfig:\n'
        attrs = [attr for attr in dir(cls) if not callable(getattr(cls, attr)) and not attr.startswith('__')]
        text += '\n'.join(['\t{:s} = {:s}'.format(attr, str(getattr(cls, attr))) for attr in attrs]) + '\n'

        return text

    @classmethod
    def setup(cls, image_min_side: float = None, image_max_side: float = None,
              anchor_ratios: List[Tuple[int, int]] = None, anchor_scales: List[int] = None, pooling_mode: str = None):
        if image_min_side is not None:
            cls.IMAGE_MIN_SIDE = image_min_side
        if image_max_side is not None:
            cls.IMAGE_MAX_SIDE = image_max_side

        if anchor_ratios is not None:
            cls.ANCHOR_RATIOS = ast.literal_eval(anchor_ratios)
        if anchor_scales is not None:
            cls.ANCHOR_SCALES = ast.literal_eval(anchor_scales)
        if pooling_mode is not None:
            cls.POOLING_MODE = ROIWrapper.Mode(pooling_mode)
