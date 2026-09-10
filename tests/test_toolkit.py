"""Native Agno registration and transport-boundary tests."""

from copy import deepcopy
from unittest.mock import patch

import pytest
from agno.agent import Agent
from agno.tools.function import Function, FunctionCall
from fxmacrodata_public import Result, list_operations

from agno_fxmacrodata import FXMacroDataTools

PAYLOAD = {"data": [{"fixture": "synthetic", "announcement_datetime": "2026-01-01T12:00:00Z", "value": None}]}


@pytest.mark.parametrize("operation", list_operations(), ids=lambda item: item.name)
def test_native_function_inventory_and_lossless_execution(operation):
    toolkit = FXMacroDataTools(api_key="")
    tool = toolkit.functions["fxmd_" + operation.name]
    assert isinstance(tool, Function)
    tool.process_entrypoint()
    assert tool.parameters == operation.input_schema
    arguments = {"fixture_argument": {"nested": [1, None]}}
    with patch.object(toolkit._client, "execute", return_value=Result(operation.name, deepcopy(PAYLOAD))) as execute:
        result = tool.entrypoint(**arguments)
    execute.assert_called_once_with(operation.name, arguments)
    assert result["data"] == PAYLOAD
    assert result["records"][0]["announcement_datetime"] == "2026-01-01T12:00:00Z"
    assert result["records"][0]["value"] is None
    assert "utm_source=agno" in result["provider_url"]


def test_agent_and_function_call_are_real_host_objects():
    toolkit = FXMacroDataTools(api_key="", include_tools=["fxmd_data_catalogue"])
    agent = Agent(tools=[toolkit])
    assert agent.tools[0] is toolkit
    tool = toolkit.functions["fxmd_data_catalogue"]
    call = FunctionCall(function=tool, arguments={"currency": "USD"})
    with patch.object(toolkit._client, "execute", return_value=Result("data_catalogue", [])):
        result = call.execute()
    assert result is not None
    assert call.result["records"] == []


def test_exception_details_do_not_escape():
    toolkit = FXMacroDataTools(api_key="DO_NOT_DISCLOSE_SENTINEL")
    with patch.object(
        toolkit._client, "execute", side_effect=RuntimeError("https://example.org/?api_key=DO_NOT_DISCLOSE_SENTINEL")
    ):
        result = toolkit.functions["fxmd_data_catalogue"].entrypoint(currency="USD")
    assert "error" in result
    assert "SENTINEL" not in str(result)
    assert "example.org" not in str(result)


def test_inventory_exact_and_filters_work():
    names = {"fxmd_" + operation.name for operation in list_operations()}
    assert set(FXMacroDataTools(api_key="").functions) == names
    assert set(FXMacroDataTools(api_key="", exclude_tools=["fxmd_health"]).functions) == names - {"fxmd_health"}
