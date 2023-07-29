from fastapi import FastAPI
from api.v1.api import api_router


app = FastAPI(title='Order System', version='0.1.0')

app.include_router(api_router, prefix='/api/v1')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='localhost', port=8000, log_level='info', reload=True)