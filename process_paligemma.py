from typing import Dict, List, Optional, Union, Tuple, Iterable
import numpy as np
from PIL import Image
import torch

IMAGENET_STANDARD_MEAN = [0.5, 0.5, 0.5]
IMAGENET_STANDARD_STD = [0.5, 0.5, 0.5]

class PaligemmaProcessor:

    def __init__(self, tokenizer, num_image_tokens: int, image_size: int):
        super().__init__()
        
