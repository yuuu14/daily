
from typing import List, TypedDict


class Param(TypedDict, total=False):
    name: str
    type: str
    description: str

prompt = """
Implement a function in Python with following properties:

Function name: {function_name}

Description
-----------
{description}

Parameters
----------
{parameters}

Returns
-------
{returns}
"""

def formatted_prompt(
    function_name: str,
    description: str,
    parameters: List[Param] | None = None, 
    returns: List[Param] | None = None):
    str_params = "\n".join(
        [f"{p["name"]} : {p["type"]}\n    {p["description"]}" for p in parameters]
    )
    str_returns = "\n".join(
        [f"{r["name"]} : {r["type"]}\n    {r["description"]}" for r in returns]
    ) if returns else "None"
        
    return prompt.format(
        function_name=function_name,
        description=description,
        parameters=str_params,
        returns=str_returns
    )
