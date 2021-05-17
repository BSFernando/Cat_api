from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from typing import List
import model.modelo as modelo
import db.database as database
import model.schema as schema
import logging

router = APIRouter(tags=['crud'])
get_db = database.get_db

@router.post('/include', status_code=status.HTTP_201_CREATED)
async def inseri(item: modelo.Cat_model, db:Session = Depends(get_db)):
    new_cat = schema.Cat_schema(breed=item.breed, location_of_origin=item.location_of_origin, coat_length=item.coat_length, 
                        body_type= item.body_type, pattern=item.pattern)
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    logging.info(f'Insert {item.breed} with sucess!')
    return new_cat

@router.post('/include-three', status_code=status.HTTP_201_CREATED)
async def inseri_three(itens: List[modelo.Cat_model], db:Session = Depends(get_db)):
    if len(itens) > 3 or len(itens) < 3:
        logging.error('Insert three items!')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    for item in itens:
        new_cat = schema.Cat_schema(breed=item.breed, location_of_origin=item.location_of_origin, coat_length=item.coat_length, 
                        body_type= item.body_type, pattern=item.pattern)
        db.add(new_cat)
        db.commit()
        db.refresh(new_cat)
        logging.info(f'Insert {item.breed} with sucess!')
    return new_cat