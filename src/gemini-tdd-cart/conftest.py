"""프로젝트 루트를 import 경로에 추가해 `from src...` 가 동작하게 한다."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
