# tests/conftest.py — 승인 테스트가 실패할 때 diff 도구(GUI)를 열지 않고 터미널에 차이를 보여 준다
import approvaltests
from approvaltests.reporters import PythonNativeReporter

approvaltests.set_default_reporter(PythonNativeReporter())
