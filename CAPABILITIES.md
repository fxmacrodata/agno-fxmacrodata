# Supported operations

Every operation is registered as `fxmd_<operation>` in the native tool surface. The original response is preserved alongside its record view.

| Operation | Contract | Native surface |
| --- | --- | --- |
| `health` | `GET /v1/health` | Agno Function |
| `ping` | `GET /v1/ping` | Agno Function |
| `forex` | `GET /v1/forex/{base}/{quote}` | Agno Function |
| `intraday_reference_rates` | `GET /v1/fx/intraday-reference-rates/{base}/{quote}` | Agno Function |
| `fx_sources` | `GET /v1/fx/sources` | Agno Function |
| `fx_source_universe` | `GET /v1/fx/source-universe` | Agno Function |
| `data_catalogue` | `GET /v1/data_catalogue/{currency}` | Agno Function |
| `release_calendar` | `GET /v1/calendar/{currency}` | Agno Function |
| `market_sessions` | `GET /v1/market_sessions` | Agno Function |
| `rate_differentials` | `GET /v1/rate_differentials/{base}/{quote}` | Agno Function |
| `curves` | `GET /v1/curves/{currency}` | Agno Function |
| `financial_prices` | `GET /v1/financial_prices/{currency}` | Agno Function |
| `press_releases` | `GET /v1/press-releases/{currency}` | Agno Function |
| `risk_sentiment` | `GET /v1/risk_sentiment` | Agno Function |
| `factors` | `GET /v1/factors/{currency}/{factor}` | Agno Function |
| `event_predictions` | `GET /v1/predictions/{currency}/{indicator}` | Agno Function |
| `latest_announcements` | `GET /v1/announcements/{currency}/latest` | Agno Function |
| `indicator_history` | `GET /v1/announcements/{currency}/{indicator}` | Agno Function |
| `cot` | `GET /v1/cot/{currency}` | Agno Function |
| `latest_commodities` | `GET /v1/commodities/latest` | Agno Function |
| `commodities` | `GET /v1/commodities/{indicator}` | Agno Function |
| `announcement_changes` | `GET /v1/announcements/changes` | Agno Function |
| `stream_events` | `GET /v1/stream/events` | Agno Function |
| `mcp_ping` | `MCP /mcp` | Agno Function |
| `mcp_mcp_capabilities` | `MCP /mcp` | Agno Function |
| `mcp_mcp_auth_guide` | `MCP /mcp` | Agno Function |
| `mcp_subscribe_for_mcp_access` | `MCP /mcp` | Agno Function |
| `mcp_data_catalogue` | `MCP /mcp` | Agno Function |
| `mcp_risk_sentiment` | `MCP /mcp` | Agno Function |
| `mcp_macro_news` | `MCP /mcp` | Agno Function |
| `mcp_release_calendar` | `MCP /mcp` | Agno Function |
| `mcp_release_calendar_visual_artifact` | `MCP /mcp` | Agno Function |
| `mcp_event_predictions` | `MCP /mcp` | Agno Function |
| `mcp_latest_announcements` | `MCP /mcp` | Agno Function |
| `mcp_announcement_changes` | `MCP /mcp` | Agno Function |
| `mcp_press_releases` | `MCP /mcp` | Agno Function |
| `mcp_macro_factor` | `MCP /mcp` | Agno Function |
| `mcp_fx_reference_sources` | `MCP /mcp` | Agno Function |
| `mcp_fx_reference_universe` | `MCP /mcp` | Agno Function |
| `mcp_fx_intraday_reference_rates` | `MCP /mcp` | Agno Function |
| `mcp_rate_curve` | `MCP /mcp` | Agno Function |
| `mcp_rate_differentials` | `MCP /mcp` | Agno Function |
| `mcp_latest_commodities` | `MCP /mcp` | Agno Function |
| `mcp_forex` | `MCP /mcp` | Agno Function |
| `mcp_seasonality` | `MCP /mcp` | Agno Function |
| `mcp_indicator_query` | `MCP /mcp` | Agno Function |
| `mcp_plot_visual_artifact` | `MCP /mcp` | Agno Function |
| `mcp_indicator_visual_artifact` | `MCP /mcp` | Agno Function |
| `mcp_forex_visual_artifact` | `MCP /mcp` | Agno Function |
| `mcp_commodities_visual_artifact` | `MCP /mcp` | Agno Function |
| `mcp_cot_visual_artifact` | `MCP /mcp` | Agno Function |
| `mcp_policy_rate_differential_visual_artifact` | `MCP /mcp` | Agno Function |
| `mcp_macro_briefing_task` | `MCP /mcp` | Agno Function |
| `mcp_indicator_intel_task` | `MCP /mcp` | Agno Function |
| `mcp_pair_intel_task` | `MCP /mcp` | Agno Function |
| `mcp_macro_heatmap_task` | `MCP /mcp` | Agno Function |
| `mcp_policy_scenario_modeler_task` | `MCP /mcp` | Agno Function |
| `mcp_macro_war_room_task` | `MCP /mcp` | Agno Function |
| `mcp_event_impact_replay_task` | `MCP /mcp` | Agno Function |
| `mcp_quant_scenario_lab_task` | `MCP /mcp` | Agno Function |
| `mcp_known_at_time_task` | `MCP /mcp` | Agno Function |
| `mcp_macro_regime_classifier_task` | `MCP /mcp` | Agno Function |
| `mcp_release_risk_score_task` | `MCP /mcp` | Agno Function |
| `mcp_portfolio_risk_engine_task` | `MCP /mcp` | Agno Function |
| `mcp_fx_trade_setup_task` | `MCP /mcp` | Agno Function |
| `mcp_fx_backtest_task` | `MCP /mcp` | Agno Function |
| `mcp_macro_research_pack_task` | `MCP /mcp` | Agno Function |
| `mcp_market_sessions` | `MCP /mcp` | Agno Function |
| `mcp_cot_data` | `MCP /mcp` | Agno Function |
| `mcp_commodities` | `MCP /mcp` | Agno Function |
| `mcp_financial_prices` | `MCP /mcp` | Agno Function |
| `mcp_official_dataset_family` | `MCP /mcp` | Agno Function |

REST supplies 23 operations and hosted MCP supplies 49 tools. The `mcp_` prefix distinguishes MCP capabilities from REST operations. Parameters retain their complete documented JSON schemas, including required fields, arrays, nested objects and enums.

USD catalogue, macro history and release-calendar examples are no-key. Access to other datasets follows the service's published access rules; a tool being discoverable is not a guarantee of account entitlement.

SSE event collection is finite: `max_events` and `max_seconds` bound the stream. MCP analytical operations retain their hosted semantics. MCP Apps resources and visual artifacts remain in the original response; these integrations expose data, documents and tools but do not embed an MCP Apps iframe renderer.

Forecasts retain their product labels. FXMacroData-generated predictions must not be relabelled as market consensus. No timestamps, missing observations or future release dates are inferred.
