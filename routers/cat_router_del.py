from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from typing import Optional
import db.database as database
import model.schema as schema
import logging

router = APIRouter(tags=['crud'])
get_db = database.get_db

@router.delete('/delete-id', status_code=status.HTTP_200_OK)
async def del_by_id(id: int, db: Session = Depends(get_db)):

    whole_search = db.query(schema.Cat_schema)
    if id:
        whole_search = whole_search.filter(schema.Cat_schema.id == id)

    if not whole_search.first():
        logging.info('Requisition not found!')   
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST) 
    whole_search.delete(synchronize_session=False)
    db.commit()
    logging.info('Deleted item!')
    return "Deleted item!"