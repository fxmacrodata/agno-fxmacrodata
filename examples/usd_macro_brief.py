"""Run public USD tools through Agno without an LLM or credentials."""

from datetime import date, timedelta

from agno_fxmacrodata import FXMacroDataTools


def main() -> None:
    toolkit = FXMacroDataTools(api_key="")
    today = date.today()
    calls = [
        ("data_catalogue", {"currency": "USD"}),
        ("indicator_history", {
            "currency": "USD", "indicator": "inflation",
            "start_date": (today - timedelta(days=90)).isoformat(), "end_date": today.isoformat(),
        }),
        ("release_calendar", {
            "currency": "USD", "start_date": today.isoformat(),
            "end_date": (today + timedelta(days=30)).isoformat(),
        }),
    ]
    for operation, arguments in calls:
        result = toolkit.functions["fxmd_" + operation].entrypoint(**arguments)
        if result.get("error"):
            raise RuntimeError(result["error"])
        print(f"{operation}: {len(result['records'])} records")
        print(result["source_url"])
        print(result["provider_url"])
        if not result["records"]:
            print("No records available in this window.")


if __name__ == "__main__":
    main()
