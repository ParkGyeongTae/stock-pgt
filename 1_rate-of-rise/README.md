# stock-pgt

## 사용방법

### Step 1) 아나콘다 가상환경 만들기

conda create -n stock-py37 python=3.7

### Step 2) 가상환경 접속

conda activate stock-py37


### Step 3) 라이브러리 설치

pip install pandas==1.3.5
pip install openpyxl==3.0.10
pip install exchange_calendars==3.6.2
pip install tabulate==0.8.9
pip install tabulate[widechars]==

### (참고) 아나콘다 명령어 모음 (복사 붙여넣기 용도)

1. 가상환경 리스트 확인 : conda info --envs
2. 가상환경 만들기     : conda create -n stock-py37 python=3.7
3. 가상환경 지우기     : conda env remove -n stock-py37
4. 가상환경 접속      : conda activate stock-py37
5. 가상환경 종료      : conda deactivate