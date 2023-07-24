from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import insert_messag as im
import uvicorn
import os

app = FastAPI()
app.include_router(im.novelroute, prefix="/api/v1")


# Generate OpenAPI schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="My API",
        version="1.0",
        description="API for performing various operations",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi



if __name__ == '__main__':
    uvicorn.run(app,host="0.0.0.0", port=os.environ.get('PORT_API'))
