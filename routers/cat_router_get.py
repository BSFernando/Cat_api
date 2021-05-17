from fastapi import APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from fastapi import Depends, status, HTTPException
from fastapi.responses import RedirectResponse
from typing import Optional, List
import model.modelo as modelo
import db.database as database
import model.schema as schema
import logging

router = APIRouter(tags=['crud'])
get_db = database.get_db

@router.get("/", include_in_schema=False)
async def main():
    return RedirectResponse(url="/docs")

@router.get('/cats', response_model=List[modelo.Show_cat], status_code=status.HTTP_202_ACCEPTED)
async def search(db:Session = Depends(get_db), sort: Optional[str] = None, limit: Optional[int] = None):
    whole_search = db.query(schema.Cat_schema)
    if sort:
        if sort[0] == '-':
            sort = sort[1:]
            whole_search = whole_search.order_by(desc(getattr(schema.Cat_schema,sort)))
        else: 
            whole_search = whole_search.order_by(asc(getattr(schema.Cat_schema,sort)))
        logging.info(f'Sort by {sort}!')
    whole_search = whole_search.limit(limit).all()
    if not whole_search:
        logging.info('Requisition not found!')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    logging.info('Search all itens: ok')
    return whole_search

@router.get('/filter-cats', response_model=List[modelo.Show_cat], status_code=status.HTTP_202_ACCEPTED)
async def search_par(db:Session = Depends(get_db), breed : Optional[str] = None, 
        location_of_origin : Optional[str] = None, coat_length : Optional[float] = None,
        body_type : Optional[str] = None, pattern : Optional[str] = None, sort: Optional[str] = None, limit: Optional[int] = None):
    
    values = {'breed':breed,'location_of_origin':location_of_origin,'coat_length':coat_length,
        'body_type':body_type, 'pattern':pattern}

    whole_search = db.query(schema.Cat_schema)
    for attr,value in values.items():
        if value == None:
            pass
        else:
            whole_search = whole_search.filter(getattr(schema.Cat_schema,attr)==value)
    if not whole_search:
        logging.info('Requisition not found!')   
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)   

    if sort:
        if sort[0] == '-':
            sort = sort[1:]
            whole_search = whole_search.order_by(desc(getattr(schema.Cat_schema,sort)))
        else: 
            whole_search = whole_search.order_by(asc(getattr(schema.Cat_schema,sort)))
        logging.info(f'Sort by {sort}!') 

    whole_search = whole_search.limit(limit).all()
    logging.info('Search itens: ok')
    return whole_search