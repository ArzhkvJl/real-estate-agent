from typing import Any
from langchain_community.tools import (
    QuerySQLDatabaseTool,
    InfoSQLDatabaseTool,
    ListSQLDatabaseTool,
    QuerySQLCheckerTool,
)
from langchain_core.tools import tool
from ..db.database import db


@tool("list_tables")
def list_tables() -> dict:
    """Returns a list of all available table names in the connected SQL database.

    Use this function to discover which tables exist before writing or validating queries.
    Ideal as the first step before schema inspection or data analysis."""
    result = ListSQLDatabaseTool(db=db).invoke("")
    return {"result": result}


@tool("tables_schema")
def tables_schema(tables: str) -> dict:
    """
    Retrieves the schema (column names, types) and a sample of rows for the specified tables.

    Input: A comma-separated list of table names.
    Example: "tenants, transactions, year"

    This tool is essential for understanding the structure and contents of each table before
    formulating SQL queries. Make sure the table names are valid by calling `list_tables` first.
    """
    t = InfoSQLDatabaseTool(db=db)
    result = t.invoke(tables)
    return {"result": result}


@tool("execute_sql")
def execute_sql(sql_query: str) -> dict:
    """Executes a SQL query against the connected database and returns the raw result.

    Recommended for final, verified queries.  
    To avoid errors or side effects, always validate the SQL with `check_sql` before using this tool."""
    result = QuerySQLDatabaseTool(db=db).invoke(sql_query)
    return {"result": result}


@tool("check_sql")
def check_sql(sql_query: str) -> dict:
    """
    Use this tool to double-check if the query is correct before executing it. Always use this
    tool before executing a query with `execute_sql`.
    """
    result = QuerySQLCheckerTool(db=db, llm=None).invoke({"query": sql_query})
    return {"result": result}
