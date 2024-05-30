import logging as log
from typing import List, Tuple, Any

import psycopg2



def create_table(
        quey: str,
        conn: psycopg2.extensions.connection,
        cur: psycopg2.extensions.cursor
) -> None:
    try:
        cur.execute(quey)
        log.info(f"Executed SQL query {quey}")
    except Exception as e:
        log.error(f"{type(e).__name__}: {e}")
        log.error(f"Query: {cur.query}")
        conn.rollback()
        cur.close()
    else:
        conn.commit()


def insert_table(
        query: str,
        params: tuple,
        conn: psycopg2.extensions.connection,
        cur: psycopg2.extensions.cursor
) -> None:
    try:
        cur.execute(query, params)
        log.info(f"Executed SQL query {query} for insertion with params {params}")
    except Exception as e:
        log.error(f"{type(e).__name__}: {e}")
        log.error(f"Query: {cur.query}")
        conn.rollback()
        cur.close()
    else:
        conn.commit()


def select_datas(query: str,
                 params: tuple,
                 cur: psycopg2.extensions.cursor) -> List[Tuple[Any, ...]]:
    try:
        cur.execute(query, params)
        log.info(f"Executed SQL query {query} for insertion with params {params}")
        return cur.fetchall()
    except Exception as e:
        log.error(f"{type(e).__name__}: {e}")
        log.error(f"Query: {cur.query}")
    else:
        return []

def update_data(query: str,
                params: tuple,
                conn: psycopg2.extensions.connection,
                cur: psycopg2.extensions.cursor) -> None:
    try:
        cur.execute(query, params)
        log.info(f"Executed SQL query {query} for updated with params {params}")
    except Exception as e:
        log.error(f"{type(e).__name__}: {e}")
        log.error(f"Query: {cur.query}")
        conn.rollback()
        cur.close()
    else:
        conn.commit()