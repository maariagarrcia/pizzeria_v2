
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

from schemas import InfoBaseModel, InfoDisplayModel

from db import db_info_extra

router = APIRouter(
    prefix='/info_personal',
    tags=['Info_personal']
)

@router.post('/', response_model=InfoDisplayModel)
async def create_info(request: InfoBaseModel, db: Session = Depends(get_db)):
    new_info= db_info_extra.CrudInfo.create_info(db, request)
    return new_info

@router.put('/{id}', response_model=InfoDisplayModel)
async def update_info(id: int, request: InfoBaseModel, db: Session = Depends(get_db)):
    return db_info_extra.CrudInfo.update_info(id,db,request)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_info(id: int, db: Session = Depends(get_db)):
    return db_info_extra.CrudInfo.delete_info(id,db)