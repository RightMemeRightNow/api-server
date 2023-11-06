# Right Meme Right Now API Server
## API Document
API server URI:   
`https://api.right-meme-right-now.site/`

Document:    
[Swagger](https://api.right-meme-right-now.site/docs)

## 구동
### Docker
1. 이미지 풀
```bash
docker pull psymonkey/rmrn-api-server:latest
```
2. 컨테이너 실행
```bash
docker run -d -p 8000:8000 psymonkey/rmrn-api-server:latest
```
### 직접 실행
0. python 3.11 설치(venv 등 가상 환경 사용 권장)
1. 의존성 패키지 설치
```bash
pip install -r requirements.txt
```
2. uvicorn 실행
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
