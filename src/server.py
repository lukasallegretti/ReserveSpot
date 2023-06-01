from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/avaiable_rooms/{hotel_id}")
def get_avaiable_rooms(hotel_id: int):
    return {"hotel_id": hotel_id}


@app.get("/hotels/{hotel_name}")
def get_hotel_info(hotel_name: str):
    return {"hotel_name": hotel_name}
