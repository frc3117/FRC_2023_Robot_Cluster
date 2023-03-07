import uvicorn

from fastapi import FastAPI

from routers import apriltags, physic

app = FastAPI()
app.include_router(apriltags.router)
app.include_router(physic.router)

def main(port: int):
    uvicorn.run('main:app', port=port, host='0.0.0.0')

if __name__ == '__main__':
    main(3117)