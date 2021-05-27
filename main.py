from fastapi import FastAPI
from controller.testController import router
from starlette.middleware.cors import CORSMiddleware
import uvicorn

# mysql and orm init
from tortoise import Tortoise


async def initDB():
    # Here we connect to a SQLite DB file.
    # also specify the app name of "models"
    # which contain models from "app.models"
    await Tortoise.init(
        db_url='mysql://root:1qaz!QAZ@192.168.30.195:3306/pythonorm',
        modules={'models': ['entity.modeltest']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


def create_app():
    app = FastAPI()
    
    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    @app.on_event("startup")
    async def startup():
        await initDB()
        print('start up')

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )    

    app.include_router(router)
    return app

app_ = create_app()


    
if __name__ == '__main__':
    uvicorn.run("main:app_", debug=True, reload=True)
    