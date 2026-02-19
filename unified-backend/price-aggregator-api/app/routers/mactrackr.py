"""
MacTrackr Compatibility Router
Returns 31 Apple products with search URLs (static data, no database)
"""

from fastapi import APIRouter

router = APIRouter(tags=["mactrackr"])

def generate_search_url(retailer: str, product_name: str) -> str:
    """Generate search URLs for retailers"""
    query = product_name.replace(" ", "+")
    urls = {
        "apple": f"https://www.apple.com/search/{query}",
        "bestbuy": f"https://www.bestbuy.com/site/searchpage.jsp?st={query}",
        "walmart": f"https://www.walmart.com/search?q={query}",
        "target": f"https://www.target.com/s?searchTerm={query}",
        "amazon": f"https://www.amazon.com/s?k={query}",
        "bhphoto": f"https://www.bhphotovideo.com/c/search?q={query}",
        "adorama": f"https://www.adorama.com/search?searchinfo={query}",
        "ebay": f"https://www.ebay.com/sch/i.html?_nkw={query}",
        "cdw": f"https://www.cdw.com/search/?key={query}"
    }
    return urls.get(retailer, f"https://www.google.com/search?q={query}")

# Static product data (31 products)
MACTRACKR_PRODUCTS = [
    {
        "id": "macbook-pro-14-m5",
        "name": "MacBook Pro 14\" M5",
        "category": "mac",
        "specs": {"chip": "M5", "ram": "24GB", "storage": "512GB SSD"},
        "releaseDate": "2025-01-15",
        "prices": [
            {"retailer": "apple", "price": 1999, "inStock": True, "url": generate_search_url("apple", "MacBook Pro 14 M5")},
            {"retailer": "bestbuy", "price": 1949, "inStock": True, "url": generate_search_url("bestbuy", "MacBook Pro 14 M5")},
            {"retailer": "amazon", "price": 1949, "inStock": True, "url": generate_search_url("amazon", "MacBook Pro 14 M5")},
        ]
    },
    {
        "id": "macbook-air-13-m4",
        "name": "MacBook Air 13\" M4",
        "category": "mac",
        "specs": {"chip": "M4", "ram": "16GB", "storage": "256GB SSD"},
        "releaseDate": "2025-03-01",
        "prices": [
            {"retailer": "apple", "price": 999, "inStock": True, "url": generate_search_url("apple", "MacBook Air 13 M4")},
            {"retailer": "bestbuy", "price": 949, "inStock": True, "url": generate_search_url("bestbuy", "MacBook Air 13 M4")},
            {"retailer": "amazon", "price": 949, "inStock": True, "url": generate_search_url("amazon", "MacBook Air 13 M4")},
        ]
    },
    {
        "id": "macbook-air-15-m4",
        "name": "MacBook Air 15\" M4",
        "category": "mac",
        "specs": {"chip": "M4", "ram": "16GB", "storage": "512GB SSD"},
        "releaseDate": "2025-03-01",
        "prices": [
            {"retailer": "apple", "price": 1299, "inStock": True, "url": generate_search_url("apple", "MacBook Air 15 M4")},
            {"retailer": "bestbuy", "price": 1249, "inStock": True, "url": generate_search_url("bestbuy", "MacBook Air 15 M4")},
            {"retailer": "amazon", "price": 1249, "inStock": True, "url": generate_search_url("amazon", "MacBook Air 15 M4")},
        ]
    },
    {
        "id": "macbook-pro-16-m5",
        "name": "MacBook Pro 16\" M5",
        "category": "mac",
        "specs": {"chip": "M5 Pro", "ram": "32GB", "storage": "1TB SSD"},
        "releaseDate": "2025-01-15",
        "prices": [
            {"retailer": "apple", "price": 2499, "inStock": True, "url": generate_search_url("apple", "MacBook Pro 16 M5")},
            {"retailer": "bestbuy", "price": 2399, "inStock": True, "url": generate_search_url("bestbuy", "MacBook Pro 16 M5")},
            {"retailer": "amazon", "price": 2399, "inStock": True, "url": generate_search_url("amazon", "MacBook Pro 16 M5")},
        ]
    },
    {
        "id": "mac-mini-m4",
        "name": "Mac mini M4",
        "category": "mac",
        "specs": {"chip": "M4", "ram": "16GB", "storage": "256GB SSD"},
        "releaseDate": "2024-11-01",
        "prices": [
            {"retailer": "apple", "price": 599, "inStock": True, "url": generate_search_url("apple", "Mac mini M4")},
            {"retailer": "bestbuy", "price": 579, "inStock": True, "url": generate_search_url("bestbuy", "Mac mini M4")},
            {"retailer": "amazon", "price": 579, "inStock": True, "url": generate_search_url("amazon", "Mac mini M4")},
        ]
    },
    {
        "id": "mac-studio-m3-max",
        "name": "Mac Studio M3 Max",
        "category": "mac",
        "specs": {"chip": "M3 Max", "ram": "36GB", "storage": "512GB SSD"},
        "releaseDate": "2024-06-01",
        "prices": [
            {"retailer": "apple", "price": 2999, "inStock": True, "url": generate_search_url("apple", "Mac Studio M3 Max")},
            {"retailer": "bestbuy", "price": 2799, "inStock": True, "url": generate_search_url("bestbuy", "Mac Studio M3 Max")},
        ]
    },
    {
        "id": "imac-24-m4",
        "name": "iMac 24\" M4",
        "category": "mac",
        "specs": {"chip": "M4", "ram": "16GB", "storage": "256GB SSD"},
        "releaseDate": "2024-11-01",
        "prices": [
            {"retailer": "apple", "price": 1299, "inStock": True, "url": generate_search_url("apple", "iMac 24 M4")},
            {"retailer": "bestbuy", "price": 1199, "inStock": True, "url": generate_search_url("bestbuy", "iMac 24 M4")},
            {"retailer": "amazon", "price": 1199, "inStock": True, "url": generate_search_url("amazon", "iMac 24 M4")},
        ]
    },
    {
        "id": "iphone-16-pro-max",
        "name": "iPhone 16 Pro Max",
        "category": "iphone",
        "specs": {"storage": "256GB", "display": "6.9\""},
        "releaseDate": "2024-09-20",
        "prices": [
            {"retailer": "apple", "price": 1199, "inStock": True, "url": generate_search_url("apple", "iPhone 16 Pro Max")},
            {"retailer": "bestbuy", "price": 1149, "inStock": True, "url": generate_search_url("bestbuy", "iPhone 16 Pro Max")},
            {"retailer": "amazon", "price": 1149, "inStock": True, "url": generate_search_url("amazon", "iPhone 16 Pro Max")},
        ]
    },
    {
        "id": "iphone-16-pro",
        "name": "iPhone 16 Pro",
        "category": "iphone",
        "specs": {"storage": "256GB", "display": "6.3\""},
        "releaseDate": "2024-09-20",
        "prices": [
            {"retailer": "apple", "price": 999, "inStock": True, "url": generate_search_url("apple", "iPhone 16 Pro")},
            {"retailer": "bestbuy", "price": 949, "inStock": True, "url": generate_search_url("bestbuy", "iPhone 16 Pro")},
            {"retailer": "amazon", "price": 949, "inStock": True, "url": generate_search_url("amazon", "iPhone 16 Pro")},
        ]
    },
    {
        "id": "iphone-16-plus",
        "name": "iPhone 16 Plus",
        "category": "iphone",
        "specs": {"storage": "256GB", "display": "6.7\""},
        "releaseDate": "2024-09-20",
        "prices": [
            {"retailer": "apple", "price": 899, "inStock": True, "url": generate_search_url("apple", "iPhone 16 Plus")},
            {"retailer": "bestbuy", "price": 849, "inStock": True, "url": generate_search_url("bestbuy", "iPhone 16 Plus")},
            {"retailer": "amazon", "price": 849, "inStock": True, "url": generate_search_url("amazon", "iPhone 16 Plus")},
        ]
    },
    {
        "id": "iphone-16",
        "name": "iPhone 16",
        "category": "iphone",
        "specs": {"storage": "128GB", "display": "6.1\""},
        "releaseDate": "2024-09-20",
        "prices": [
            {"retailer": "apple", "price": 799, "inStock": True, "url": generate_search_url("apple", "iPhone 16")},
            {"retailer": "bestbuy", "price": 749, "inStock": True, "url": generate_search_url("bestbuy", "iPhone 16")},
            {"retailer": "amazon", "price": 749, "inStock": True, "url": generate_search_url("amazon", "iPhone 16")},
        ]
    },
    {
        "id": "ipad-pro-13-m5",
        "name": "iPad Pro 13\" M5",
        "category": "ipad",
        "specs": {"chip": "M5", "storage": "512GB"},
        "releaseDate": "2025-05-01",
        "prices": [
            {"retailer": "apple", "price": 1299, "inStock": True, "url": generate_search_url("apple", "iPad Pro 13 M5")},
            {"retailer": "bestbuy", "price": 1249, "inStock": True, "url": generate_search_url("bestbuy", "iPad Pro 13 M5")},
            {"retailer": "amazon", "price": 1249, "inStock": True, "url": generate_search_url("amazon", "iPad Pro 13 M5")},
        ]
    },
    {
        "id": "ipad-pro-11-m5",
        "name": "iPad Pro 11\" M5",
        "category": "ipad",
        "specs": {"chip": "M5", "storage": "256GB"},
        "releaseDate": "2025-05-01",
        "prices": [
            {"retailer": "apple", "price": 999, "inStock": True, "url": generate_search_url("apple", "iPad Pro 11 M5")},
            {"retailer": "bestbuy", "price": 949, "inStock": True, "url": generate_search_url("bestbuy", "iPad Pro 11 M5")},
            {"retailer": "amazon", "price": 949, "inStock": True, "url": generate_search_url("amazon", "iPad Pro 11 M5")},
        ]
    },
    {
        "id": "ipad-air-13-m3",
        "name": "iPad Air 13\" M3",
        "category": "ipad",
        "specs": {"chip": "M3", "storage": "256GB"},
        "releaseDate": "2025-03-01",
        "prices": [
            {"retailer": "apple", "price": 799, "inStock": True, "url": generate_search_url("apple", "iPad Air 13 M3")},
            {"retailer": "bestbuy", "price": 749, "inStock": True, "url": generate_search_url("bestbuy", "iPad Air 13 M3")},
            {"retailer": "amazon", "price": 749, "inStock": True, "url": generate_search_url("amazon", "iPad Air 13 M3")},
        ]
    },
    {
        "id": "ipad-air-11-m3",
        "name": "iPad Air 11\" M3",
        "category": "ipad",
        "specs": {"chip": "M3", "storage": "256GB"},
        "releaseDate": "2025-03-01",
        "prices": [
            {"retailer": "apple", "price": 599, "inStock": True, "url": generate_search_url("apple", "iPad Air 11 M3")},
            {"retailer": "bestbuy", "price": 549, "inStock": True, "url": generate_search_url("bestbuy", "iPad Air 11 M3")},
            {"retailer": "amazon", "price": 549, "inStock": True, "url": generate_search_url("amazon", "iPad Air 11 M3")},
        ]
    },
    {
        "id": "ipad-11-a16",
        "name": "iPad 11\" A16",
        "category": "ipad",
        "specs": {"chip": "A16", "storage": "128GB"},
        "releaseDate": "2025-03-01",
        "prices": [
            {"retailer": "apple", "price": 499, "inStock": True, "url": generate_search_url("apple", "iPad 11 A16")},
            {"retailer": "bestbuy", "price": 449, "inStock": True, "url": generate_search_url("bestbuy", "iPad 11 A16")},
            {"retailer": "amazon", "price": 449, "inStock": True, "url": generate_search_url("amazon", "iPad 11 A16")},
        ]
    },
    {
        "id": "ipad-mini-a17-pro",
        "name": "iPad mini A17 Pro",
        "category": "ipad",
        "specs": {"chip": "A17 Pro", "storage": "256GB"},
        "releaseDate": "2024-10-01",
        "prices": [
            {"retailer": "apple", "price": 599, "inStock": True, "url": generate_search_url("apple", "iPad mini A17 Pro")},
            {"retailer": "bestbuy", "price": 549, "inStock": True, "url": generate_search_url("bestbuy", "iPad mini A17 Pro")},
            {"retailer": "amazon", "price": 549, "inStock": True, "url": generate_search_url("amazon", "iPad mini A17 Pro")},
        ]
    },
    {
        "id": "apple-watch-series-10",
        "name": "Apple Watch Series 10",
        "category": "watch",
        "specs": {"size": "42mm"},
        "releaseDate": "2024-09-20",
        "prices": [
            {"retailer": "apple", "price": 399, "inStock": True, "url": generate_search_url("apple", "Apple Watch Series 10")},
            {"retailer": "bestbuy", "price": 379, "inStock": True, "url": generate_search_url("bestbuy", "Apple Watch Series 10")},
            {"retailer": "amazon", "price": 379, "inStock": True, "url": generate_search_url("amazon", "Apple Watch Series 10")},
        ]
    },
    {
        "id": "apple-watch-ultra-2",
        "name": "Apple Watch Ultra 2",
        "category": "watch",
        "specs": {"size": "49mm"},
        "releaseDate": "2024-09-20",
        "prices": [
            {"retailer": "apple", "price": 799, "inStock": True, "url": generate_search_url("apple", "Apple Watch Ultra 2")},
            {"retailer": "bestbuy", "price": 749, "inStock": True, "url": generate_search_url("bestbuy", "Apple Watch Ultra 2")},
            {"retailer": "amazon", "price": 749, "inStock": True, "url": generate_search_url("amazon", "Apple Watch Ultra 2")},
        ]
    },
    {
        "id": "apple-watch-se-40mm",
        "name": "Apple Watch SE 40mm",
        "category": "watch",
        "specs": {"size": "40mm"},
        "releaseDate": "2024-09-20",
        "prices": [
            {"retailer": "apple", "price": 249, "inStock": True, "url": generate_search_url("apple", "Apple Watch SE")},
            {"retailer": "bestbuy", "price": 219, "inStock": True, "url": generate_search_url("bestbuy", "Apple Watch SE")},
            {"retailer": "amazon", "price": 219, "inStock": True, "url": generate_search_url("amazon", "Apple Watch SE")},
        ]
    },
    {
        "id": "airpods-pro-3",
        "name": "AirPods Pro 3rd Gen",
        "category": "airpods",
        "specs": {},
        "releaseDate": "2024-09-20",
        "prices": [
            {"retailer": "apple", "price": 249, "inStock": True, "url": generate_search_url("apple", "AirPods Pro 3")},
            {"retailer": "bestbuy", "price": 229, "inStock": True, "url": generate_search_url("bestbuy", "AirPods Pro 3")},
            {"retailer": "amazon", "price": 229, "inStock": True, "url": generate_search_url("amazon", "AirPods Pro 3")},
        ]
    },
    {
        "id": "airpods-4",
        "name": "AirPods 4",
        "category": "airpods",
        "specs": {},
        "releaseDate": "2024-09-20",
        "prices": [
            {"retailer": "apple", "price": 129, "inStock": True, "url": generate_search_url("apple", "AirPods 4")},
            {"retailer": "bestbuy", "price": 109, "inStock": True, "url": generate_search_url("bestbuy", "AirPods 4")},
            {"retailer": "amazon", "price": 109, "inStock": True, "url": generate_search_url("amazon", "AirPods 4")},
        ]
    },
    {
        "id": "airpods-max",
        "name": "AirPods Max",
        "category": "airpods",
        "specs": {},
        "releaseDate": "2024-09-20",
        "prices": [
            {"retailer": "apple", "price": 549, "inStock": True, "url": generate_search_url("apple", "AirPods Max")},
            {"retailer": "bestbuy", "price": 499, "inStock": True, "url": generate_search_url("bestbuy", "AirPods Max")},
            {"retailer": "amazon", "price": 499, "inStock": True, "url": generate_search_url("amazon", "AirPods Max")},
        ]
    },
    {
        "id": "homepod",
        "name": "HomePod",
        "category": "accessories",
        "specs": {},
        "releaseDate": "2023-02-01",
        "prices": [
            {"retailer": "apple", "price": 299, "inStock": True, "url": generate_search_url("apple", "HomePod")},
            {"retailer": "bestbuy", "price": 279, "inStock": True, "url": generate_search_url("bestbuy", "HomePod")},
            {"retailer": "amazon", "price": 279, "inStock": True, "url": generate_search_url("amazon", "HomePod")},
        ]
    },
    {
        "id": "homepod-mini",
        "name": "HomePod mini",
        "category": "accessories",
        "specs": {},
        "releaseDate": "2020-11-01",
        "prices": [
            {"retailer": "apple", "price": 99, "inStock": True, "url": generate_search_url("apple", "HomePod mini")},
            {"retailer": "bestbuy", "price": 89, "inStock": True, "url": generate_search_url("bestbuy", "HomePod mini")},
            {"retailer": "amazon", "price": 89, "inStock": True, "url": generate_search_url("amazon", "HomePod mini")},
        ]
    },
    {
        "id": "apple-pencil-pro",
        "name": "Apple Pencil Pro",
        "category": "accessories",
        "specs": {},
        "releaseDate": "2024-05-01",
        "prices": [
            {"retailer": "apple", "price": 129, "inStock": True, "url": generate_search_url("apple", "Apple Pencil Pro")},
            {"retailer": "bestbuy", "price": 109, "inStock": True, "url": generate_search_url("bestbuy", "Apple Pencil Pro")},
            {"retailer": "amazon", "price": 109, "inStock": True, "url": generate_search_url("amazon", "Apple Pencil Pro")},
        ]
    },
    {
        "id": "airtag-4pack",
        "name": "AirTag 4-Pack",
        "category": "accessories",
        "specs": {},
        "releaseDate": "2021-04-01",
        "prices": [
            {"retailer": "apple", "price": 79, "inStock": True, "url": generate_search_url("apple", "AirTag 4-Pack")},
            {"retailer": "bestbuy", "price": 69, "inStock": True, "url": generate_search_url("bestbuy", "AirTag 4-Pack")},
            {"retailer": "amazon", "price": 69, "inStock": True, "url": generate_search_url("amazon", "AirTag 4-Pack")},
        ]
    },
    {
        "id": "magic-keyboard-ipad",
        "name": "Magic Keyboard for iPad Pro",
        "category": "accessories",
        "specs": {},
        "releaseDate": "2024-05-01",
        "prices": [
            {"retailer": "apple", "price": 349, "inStock": True, "url": generate_search_url("apple", "Magic Keyboard iPad Pro")},
            {"retailer": "bestbuy", "price": 329, "inStock": True, "url": generate_search_url("bestbuy", "Magic Keyboard iPad Pro")},
            {"retailer": "amazon", "price": 329, "inStock": True, "url": generate_search_url("amazon", "Magic Keyboard iPad Pro")},
        ]
    },
    {
        "id": "magsafe-battery",
        "name": "MagSafe Battery Pack",
        "category": "accessories",
        "specs": {},
        "releaseDate": "2021-07-01",
        "prices": [
            {"retailer": "apple", "price": 99, "inStock": True, "url": generate_search_url("apple", "MagSafe Battery Pack")},
            {"retailer": "bestbuy", "price": 89, "inStock": True, "url": generate_search_url("bestbuy", "MagSafe Battery Pack")},
            {"retailer": "amazon", "price": 89, "inStock": True, "url": generate_search_url("amazon", "MagSafe Battery Pack")},
        ]
    },
    {
        "id": "apple-tv-4k",
        "name": "Apple TV 4K",
        "category": "accessories",
        "specs": {"storage": "128GB"},
        "releaseDate": "2022-11-01",
        "prices": [
            {"retailer": "apple", "price": 129, "inStock": True, "url": generate_search_url("apple", "Apple TV 4K")},
            {"retailer": "bestbuy", "price": 119, "inStock": True, "url": generate_search_url("bestbuy", "Apple TV 4K")},
            {"retailer": "amazon", "price": 119, "inStock": True, "url": generate_search_url("amazon", "Apple TV 4K")},
        ]
    },
    {
        "id": "studio-display",
        "name": "Studio Display",
        "category": "accessories",
        "specs": {"size": "27\""},
        "releaseDate": "2022-03-01",
        "prices": [
            {"retailer": "apple", "price": 1599, "inStock": True, "url": generate_search_url("apple", "Studio Display")},
            {"retailer": "bestbuy", "price": 1499, "inStock": True, "url": generate_search_url("bestbuy", "Studio Display")},
            {"retailer": "amazon", "price": 1499, "inStock": True, "url": generate_search_url("amazon", "Studio Display")},
        ]
    },
]

@router.get("/api/products")
async def get_mactrackr_products():
    """MacTrackr compatibility endpoint - returns 31 products with search URLs"""
    return MACTRACKR_PRODUCTS
