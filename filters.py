import requests

urls = [
    # AdGuard DNS filter
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt",
    # AdAway Default Blocklist
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_2.txt",
    # NoCoin Filter List
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_8.txt",
    # 1Hosts (Lite)
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_24.txt",
    # CHN: AdRules DNS List
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_29.txt",
    # The NoTracking blocklist
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_32.txt"
]
filters = set()
with open("filters.txt", "w", encoding="utf-8") as f:
    for url in urls:
        r = requests.get(url)
        content = r.text
        content = content.split("\n")
        for filter in content:
            if filter not in filters:
                f.write(filter + "\n")
                filters.add(filter)
