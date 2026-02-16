import asyncio
import nest_asyncio
import re
import pandas as pd
from playwright.async_api import async_playwright
from geopy.geocoders import Nominatim

nest_asyncio.apply()
geolocator = Nominatim(user_agent="bpo_fresh_recon_2026")

async def scan_leads(urls):
    results = []
    keywords = ["my home", "our home", "owner", "we own", "my villa", "my business", "local", "own and operate"]
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context(user_agent="Mozilla/5.0")
        page = await context.new_page()
        for url in urls:
            if not url.strip(): continue
            print(f"👤 Checking: {url}")
            try:
                await page.goto(url.strip(), wait_until="domcontentloaded", timeout=60000)
                await asyncio.sleep(5)
                content = await page.content()
                if not any(w in content.lower() for w in keywords):
                    print(f"  ⏩ Skipping: No owner bio found.")
                    continue
                room_ids = list(set(re.findall(r'/rooms/(\d+)', content)))
                for rid in room_ids[:3]:
                    room_url = f"https://www.airbnb.com/rooms/{rid}"
                    await page.goto(room_url, wait_until="domcontentloaded")
                    await asyncio.sleep(3)
                    r_content = await page.content()
                    lat = re.search(r'"lat":([-+]?\d*\.\d+|\d+)', r_content)
                    lng = re.search(r'"lng":([-+]?\d*\.\d+|\d+)', r_content)
                    address, maps_url = "Vicinity Only", "N/A"
                    if lat and lng:
                        lt, lg = lat.group(1), lng.group(1)
                        maps_url = f"https://www.google.com/maps?q={lt},{lg}"
                        loc = geolocator.reverse(f"{lt}, {lg}", exactly_one=True, addressdetails=True)
                        if loc:
                            raw = loc.raw.get('address', {})
                            h_num, road = raw.get('house_number', ''), raw.get('road', '')
                            address = f"{h_num} {road}".strip() if h_num and road else loc.address
                    results.append({"Host": url.split('/')[-1], "Address": address, "Maps": maps_url, "Link": room_url})
            except Exception as e: print(f"  ⚠️ Error: {e}")
        await browser.close()
    return pd.DataFrame(results)
