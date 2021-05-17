from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from typing import Optional
import model.modelo as modelo
import db.database as database
import model.schema as schema
import logging

router = APIRouter(tags=['crud'])
get_db = database.get_db

@router.put('/change', status_code=status.HTTP_202_ACCEPTED)
async def update(item: modelo.Filter_cat, id: int, db:Session = Depends(get_db)):
    if id:
        whole_search = db.query(schema.Cat_schema).filter(schema.Cat_schema.id == id)
    if not whole_search.first():
        logging.info('Requisition not found!')   
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST) 
    whole_search.update({'breed':item.breed, 'location_of_origin': item.location_of_origin, 'coat_length':item.coat_length, 
                        'body_type': item.body_type, 'pattern': item.pattern})
    db.commit()
    logging.info('Updated item!')
    return 'Updated item!'

@router.patch('/change-parameters', status_code=status.HTTP_202_ACCEPTED)
async def alterar_class(item: modelo.Filter_cat, mudar: modelo.Filter_cat, db:Session = Depends(get_db)):
    values_change = item.dict(exclude_none=True)
    new_values = mudar.dict(exclude_none=True)
    for attr,value in values_change.items():
        whole_search = db.query(schema.Cat_schema)
        whole_search = whole_search.filter(getattr(schema.Cat_schema,attr)==value)
        whole_search.update({f'{attr}' : new_values[attr]})
        db.commit()
    logging.info('Updated items!')
    return 'Updated items!'