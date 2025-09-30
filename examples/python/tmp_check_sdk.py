import os
import sys
import json
import urllib3

try:
    import qoery
except Exception as import_error:
    print(f"Import failed: {import_error}")
    sys.exit(1)


def main() -> int:
    api_key = os.getenv("QOERY_API_KEY") or os.getenv("API_KEY") or os.getenv("X_API_KEY")
    if not api_key:
        print("Missing API key. Set QOERY_API_KEY or API_KEY.")
        return 2

    config = qoery.Configuration()
    config.host = "https://api.qoery.com/v0"
    config.api_key["ApiKeyAuth"] = api_key

    try:
        with qoery.ApiClient(config) as client:
            # Usage
            usage_api = qoery.UsageApi(client)
            u_resp = usage_api.usage_get_without_preload_content()
            u_data = json.loads(u_resp.data)
            queries_used = int(u_data.get("queries_used", 0)) if u_data.get("queries_used") is not None else 0
            queries_limit = int(u_data.get("queries_limit", 0)) if u_data.get("queries_limit") is not None else 0
            tokens_in = u_data.get("tokens_in")
            tokens_out = u_data.get("tokens_out")
            period_start = u_data.get("period_start")
            period_end = u_data.get("period_end")
            print("OK: Usage endpoint")
            print(f"Queries: {queries_used}/{queries_limit}")
            if tokens_in is not None and tokens_out is not None:
                print(f"Tokens in/out: {tokens_in}/{tokens_out}")
            if period_start is not None and period_end is not None:
                print(f"Period: {period_start} -> {period_end}")

            # NL Query
            queries_api = qoery.QueriesApi(client)
            nl_resp = queries_api.query_nl_post_without_preload_content()
            print(f"NL status: {nl_resp.status}")
            try:
                nl_json = json.loads(nl_resp.data)
                print("NL response keys:", list(nl_json.keys())[:5])
            except Exception:
                pass

            # SQL Query
            sql_resp = queries_api.query_sql_post_without_preload_content()
            print(f"SQL status: {sql_resp.status}")
            try:
                sql_json = json.loads(sql_resp.data)
                print("SQL response keys:", list(sql_json.keys())[:5])
            except Exception:
                pass

            # Scrape
            ws_api = qoery.WebScrapingApi(client)
            sc_resp = ws_api.scrape_post_without_preload_content(markdown=True)
            print(f"Scrape status: {sc_resp.status}")
            try:
                sc_json = json.loads(sc_resp.data)
                print("Scrape response keys:", list(sc_json.keys())[:5])
            except Exception:
                pass
            # Direct HTTP calls with bodies (workaround until SDK models accept bodies)
            http = urllib3.PoolManager()
            headers = {
                "Content-Type": "application/json",
                "X-API-Key": api_key,
            }
            base = "https://api.qoery.com/v0"

            # NL body
            nl_body = {"query": "latest CPI for United States"}
            nl_r = http.request(
                "POST", f"{base}/query/nl", body=json.dumps(nl_body), headers=headers
            )
            print(f"Direct NL status: {nl_r.status}")
            try:
                nl_direct = json.loads(nl_r.data)
                print("Direct NL keys:", list(nl_direct.keys())[:5])
            except Exception:
                pass

            # SQL body
            sql_body = {"query": "SELECT ts, value FROM series_latest WHERE entity_id='united_states' AND metric_id='cpi' ORDER BY ts DESC LIMIT 5"}
            sql_r = http.request(
                "POST", f"{base}/query/sql", body=json.dumps(sql_body), headers=headers
            )
            print(f"Direct SQL status: {sql_r.status}")
            try:
                sql_direct = json.loads(sql_r.data)
                print("Direct SQL keys:", list(sql_direct.keys())[:5])
            except Exception:
                pass

            # Scrape body
            scrape_body = {"url": "https://example.com"}
            sc_r = http.request(
                "POST", f"{base}/scrape?markdown=true", body=json.dumps(scrape_body), headers=headers
            )
            print(f"Direct Scrape status: {sc_r.status}")
            try:
                sc_direct = json.loads(sc_r.data)
                print("Direct Scrape keys:", list(sc_direct.keys())[:5])
            except Exception:
                pass
            return 0
    except Exception as e:
        print(f"SDK call failed: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())


