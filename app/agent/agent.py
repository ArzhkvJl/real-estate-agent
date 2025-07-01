from ..llm.gemini import get_llm
from .tools import list_tables, tables_schema, execute_sql, check_sql
from langgraph.prebuilt import create_react_agent
from shared import constants


def create_agent(api_key):
    llm = get_llm(api_key=api_key)
    llm_with_tools = llm.bind_tools([list_tables, tables_schema, execute_sql, check_sql])
    agent = create_react_agent(

            prompt=constants.AGENT_PROMPT,
            model=llm_with_tools,
            tools=[list_tables, tables_schema, execute_sql, check_sql],
    )
    return agent
