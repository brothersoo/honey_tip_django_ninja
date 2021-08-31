import uvicorn


if __name__ == '__main__':
    uvicorn.run("honey_tip.asgi:application", reload=True)

