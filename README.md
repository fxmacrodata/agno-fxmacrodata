# FXMacroData for Agno

Give Agno agents official macroeconomic history, release calendars and sourced market context. The USD catalogue, macro history and release calendar work without an API key, account or credit card.

[Explore FXMacroData](https://fxmacrodata.com/?utm_source=github&utm_medium=referral&utm_campaign=open_source_integrations&utm_content=agno_readme) · [API documentation](https://fxmacrodata.com/documentation/reference?utm_source=github&utm_medium=referral&utm_campaign=open_source_integrations&utm_content=agno_docs)

The public example requests the most recent 90 days of USD history. Broader history and protected datasets follow the documented access limits.

## Install from source

With this project and the companion public client in sibling directories:

```bash
python -m pip install ./fxmacrodata-public-client ./agno-fxmacrodata
```

No package-registry publication is assumed by this installation command. Python 3.10+ and Agno 3.0.9+ are supported.

## Use with an agent

```python
from agno.agent import Agent
from agno_fxmacrodata import FXMacroDataTools

tools = FXMacroDataTools()
agent = Agent(tools=[tools], markdown=True)
# Configure your preferred Agno model before running the agent.
```

Run `python examples/usd_macro_brief.py` for a working no-key workflow that calls Agno's registered tools directly, without an LLM. It discovers the USD catalogue, reads recent inflation history and retrieves upcoming releases.

Every supported REST operation and hosted MCP capability has a separate `fxmd_...` Agno Function with its complete input schema. Use the normal `include_tools` or `exclude_tools` constructor arguments to give a particular agent a smaller subset. All operations remain available by default; see [CAPABILITIES.md](CAPABILITIES.md).

Results include the original response in `data`, a tabular view in `records`, and public source/provider links. Preserve timestamps, units, provenance and forecast labels when writing briefs. Empty records mean no available observations for the query. MCP visual resources remain in the original response; this toolkit does not render MCP Apps.

## Optional authenticated coverage

Use your own key through `FXMACRODATA_API_KEY` or pass `api_key` from your application's secret manager. Credentials are not tool arguments and must never be put into prompts or checked-in examples. Pass `api_key=""` to force no-key access. Entitlements remain enforced by FXMacroData.

README links use static campaign parameters to identify referrals. The toolkit emits no analytics events or click beacons.

## Test

```bash
python -m pytest tests -n 8 --dist load
```

The code is Apache-2.0 licensed. API access and data usage follow the applicable FXMacroData terms; the software licence does not grant brand rights.
