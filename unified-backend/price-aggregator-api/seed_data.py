"""
Seed data for Price Aggregator API
Creates sample products with Tier 1-2 fields
"""

from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, Product, Retailer, Price
from datetime import datetime

def generate_search_url(retailer_name: str, search_query: str) -> str:
    """Generate actual search URLs for retailers"""
    search_urls = {
        "Apple": f"https://www.apple.com/search/{search_query}",
        "Best Buy": f"https://www.bestbuy.com/site/searchpage.jsp?st={search_query}",
        "Walmart": f"https://www.walmart.com/search?q={search_query}",
        "Target": f"https://www.target.com/s?searchTerm={search_query}",
        "Amazon": f"https://www.amazon.com/s?k={search_query}",
        "B&H Photo": f"https://www.bhphotovideo.com/c/search?q={search_query}",
        "Adorama": f"https://www.adorama.com/search?searchinfo={search_query}",
        "eBay": f"https://www.ebay.com/sch/i.html?_nkw={search_query}",
        "CDW": f"https://www.cdw.com/search/?key={search_query}"
    }
    return search_urls.get(retailer_name, f"https://www.google.com/search?q={search_query}")

def seed_retailers(db: Session):
    """Create sample retailers"""
    retailers = [
        {
            "name": "Apple",
            "base_url": "https://www.apple.com",
            "scraper_type": "custom",
            "config": {"rate_limit": 1.0}
        },
        {
            "name": "Best Buy",
            "base_url": "https://www.bestbuy.com",
            "scraper_type": "custom",
            "config": {"rate_limit": 2.0}
        },
        {
            "name": "Walmart",
            "base_url": "https://www.walmart.com",
            "scraper_type": "custom",
            "config": {"rate_limit": 2.0}
        },
        {
            "name": "Target",
            "base_url": "https://www.target.com",
            "scraper_type": "custom",
            "config": {"rate_limit": 2.0}
        },
        {
            "name": "Amazon",
            "base_url": "https://www.amazon.com",
            "scraper_type": "custom",
            "config": {"rate_limit": 1.0}
        },
        {
            "name": "B&H Photo",
            "base_url": "https://www.bhphotovideo.com",
            "scraper_type": "custom",
            "config": {"rate_limit": 2.0}
        },
        {
            "name": "Adorama",
            "base_url": "https://www.adorama.com",
            "scraper_type": "custom",
            "config": {"rate_limit": 2.0}
        },
        {
            "name": "eBay",
            "base_url": "https://www.ebay.com",
            "scraper_type": "ebay",
            "config": {"rate_limit": 2.0}
        },
        {
            "name": "CDW",
            "base_url": "https://www.cdw.com",
            "scraper_type": "custom",
            "config": {"rate_limit": 2.0}
        }
    ]

    for r in retailers:
        existing = db.query(Retailer).filter(Retailer.name == r["name"]).first()
        if not existing:
            db.add(Retailer(**r))

    db.commit()
    print(f"✅ Seeded {len(retailers)} retailers")

def seed_mac_products(db: Session):
    """Create sample Mac products with Tier 2 fields"""
    products = [
        {
            "name": "MacBook Pro 14-inch M3 Pro",
            "category": "mac",
            "description": "2023 MacBook Pro with M3 Pro chip, Space Black",
            "model_identifier": "Mac15,3",
            "release_year": 2023,
            "specs": {
                "cpu": "Apple M3 Pro (11-core CPU, 14-core GPU)",
                "ram": "18GB Unified Memory",
                "storage": "512GB SSD",
                "display": "14.2-inch Liquid Retina XDR",
                "ports": ["3x Thunderbolt 4", "HDMI", "SD Card", "MagSafe 3"],
                "color": "Space Black"
            },
            "image_url": "https://example.com/macbook-pro-14.jpg"
        },
        {
            "name": "MacBook Air 15-inch M2",
            "category": "mac",
            "description": "2023 MacBook Air with M2 chip, Midnight",
            "model_identifier": "Mac14,2",
            "release_year": 2023,
            "specs": {
                "cpu": "Apple M2 (8-core CPU, 10-core GPU)",
                "ram": "8GB Unified Memory",
                "storage": "256GB SSD",
                "display": "15.3-inch Liquid Retina",
                "ports": ["2x Thunderbolt 3", "MagSafe 3", "Headphone Jack"],
                "color": "Midnight"
            },
            "image_url": "https://example.com/macbook-air-15.jpg"
        },
        {
            "name": "Mac mini M2 Pro",
            "category": "mac",
            "description": "Desktop Mac with M2 Pro chip",
            "model_identifier": "Mac14,12",
            "release_year": 2023,
            "specs": {
                "cpu": "Apple M2 Pro (10-core CPU, 16-core GPU)",
                "ram": "16GB Unified Memory",
                "storage": "512GB SSD",
                "ports": ["4x Thunderbolt 4", "2x USB-A", "HDMI", "Ethernet"]
            },
            "image_url": "https://example.com/mac-mini.jpg"
        }
    ]

    for p in products:
        existing = db.query(Product).filter(Product.name == p["name"]).first()
        if not existing:
            db.add(Product(**p))

    db.commit()
    print(f"✅ Seeded {len(products)} Mac products")

def seed_mactrackr_products(db: Session):
    """Create MacTrackr Apple products - Feb 19, 2026"""
    products = [
        # Mac Products
        {
            "name": "MacBook Pro 14-inch M5",
            "category": "mac",
            "description": "MacBook Pro 14-inch with M5 chip",
            "model_identifier": "A3113",
            "release_year": 2025,
            "specs": {
                "cpu": "Apple M5 (10-core CPU)",
                "ram": "24GB Unified Memory",
                "storage": "512GB SSD",
                "display": "14.2-inch Liquid Retina XDR",
                "color": "Space Black"
            },
            "image_url": "https://example.com/macbook-pro-14-m5.jpg"
        },
        {
            "name": "MacBook Air 13-inch M4",
            "category": "mac",
            "description": "MacBook Air 13-inch with M4 chip",
            "model_identifier": "A3115",
            "release_year": 2025,
            "specs": {
                "cpu": "Apple M4 (8-core CPU)",
                "ram": "16GB Unified Memory",
                "storage": "256GB SSD",
                "display": "13.6-inch Liquid Retina",
                "color": "Space Gray"
            },
            "image_url": "https://example.com/macbook-air-13-m4.jpg"
        },
        {
            "name": "MacBook Air 15-inch M4",
            "category": "mac",
            "description": "MacBook Air 15-inch with M4 chip",
            "model_identifier": "A3116",
            "release_year": 2025,
            "specs": {
                "cpu": "Apple M4 (8-core CPU)",
                "ram": "16GB Unified Memory",
                "storage": "512GB SSD",
                "display": "15.3-inch Liquid Retina",
                "color": "Space Gray"
            },
            "image_url": "https://example.com/macbook-air-15-m4.jpg"
        },
        {
            "name": "Mac mini M4",
            "category": "mac",
            "description": "Mac mini with M4 chip",
            "model_identifier": "A3232",
            "release_year": 2024,
            "specs": {
                "cpu": "Apple M4 (8-core CPU)",
                "ram": "16GB Unified Memory",
                "storage": "256GB SSD",
                "ports": "3x Thunderbolt 4"
            },
            "image_url": "https://example.com/mac-mini-m4.jpg"
        },
        {
            "name": "Mac Studio M3 Max",
            "category": "mac",
            "description": "Mac Studio with M3 Max chip",
            "model_identifier": "A2901",
            "release_year": 2024,
            "specs": {
                "cpu": "Apple M3 Max (12-core CPU)",
                "ram": "36GB Unified Memory",
                "storage": "512GB SSD",
                "ports": "6x Thunderbolt 4"
            },
            "image_url": "https://example.com/mac-studio.jpg"
        },
        {
            "name": "iMac 24-inch M4",
            "category": "mac",
            "description": "iMac 24-inch with M4 chip",
            "model_identifier": "A3138",
            "release_year": 2024,
            "specs": {
                "cpu": "Apple M4 (8-core CPU)",
                "ram": "16GB Unified Memory",
                "storage": "256GB SSD",
                "display": "24-inch 4.5K Retina",
                "color": "Blue"
            },
            "image_url": "https://example.com/imac-24-m4.jpg"
        },
        # iPad Products
        {
            "name": "iPad Air 13-inch M3",
            "category": "ipad",
            "description": "iPad Air 13-inch with M3 chip",
            "model_identifier": "A3240",
            "release_year": 2025,
            "specs": {
                "cpu": "Apple M3 (8-core CPU)",
                "storage": "256GB",
                "display": "13-inch Liquid Retina"
            },
            "image_url": "https://example.com/ipad-air-13-m3.jpg"
        },
        {
            "name": "iPad Air 11-inch M3",
            "category": "ipad",
            "description": "iPad Air 11-inch with M3 chip",
            "model_identifier": "A3241",
            "release_year": 2025,
            "specs": {
                "cpu": "Apple M3 (8-core CPU)",
                "storage": "256GB",
                "display": "11-inch Liquid Retina"
            },
            "image_url": "https://example.com/ipad-air-11-m3.jpg"
        },
        {
            "name": "iPad 11-inch A16",
            "category": "ipad",
            "description": "iPad 11-inch with A16 chip",
            "model_identifier": "A3354",
            "release_year": 2025,
            "specs": {
                "cpu": "Apple A16 (6-core CPU)",
                "storage": "128GB",
                "display": "11-inch Liquid Retina"
            },
            "image_url": "https://example.com/ipad-11-a16.jpg"
        },
        {
            "name": "iPad mini A17 Pro",
            "category": "ipad",
            "description": "iPad mini with A17 Pro chip",
            "model_identifier": "A2993",
            "release_year": 2024,
            "specs": {
                "cpu": "Apple A17 Pro (6-core CPU)",
                "storage": "256GB",
                "display": "8.3-inch Liquid Retina"
            },
            "image_url": "https://example.com/ipad-mini.jpg"
        },
        # Apple Watch
        {
            "name": "Apple Watch SE 40mm",
            "category": "watch",
            "description": "Apple Watch SE 40mm GPS",
            "model_identifier": "A2723",
            "release_year": 2024,
            "specs": {
                "display": "40mm",
                "case": "Silver Aluminum",
                "storage": "32GB"
            },
            "image_url": "https://example.com/apple-watch-se-40mm.jpg"
        },
        # AirPods
        {
            "name": "AirPods 4",
            "category": "airpods",
            "description": "AirPods 4 with Spatial Audio",
            "model_identifier": "A3213",
            "release_year": 2024,
            "specs": {
                "features": "Spatial Audio, H2 chip"
            },
            "image_url": "https://example.com/airpods-4.jpg"
        },
        # Accessories
        {
            "name": "Apple Pencil Pro",
            "category": "accessories",
            "description": "Apple Pencil Pro",
            "model_identifier": "A2837",
            "release_year": 2024,
            "specs": {
                "features": "Haptic Feedback, Find My"
            },
            "image_url": "https://example.com/apple-pencil-pro.jpg"
        },
        {
            "name": "AirTag 4-Pack",
            "category": "accessories",
            "description": "AirTag 4-Pack",
            "model_identifier": "A2198",
            "release_year": 2021,
            "specs": {
                "features": "Precision Finding, Find My Network"
            },
            "image_url": "https://example.com/airtag-4pack.jpg"
        },
        # iPhone Products (17 more products to reach 31 total)
        {
            "name": "iPhone 16 Pro Max",
            "category": "iphone",
            "description": "iPhone 16 Pro Max 256GB",
            "model_identifier": "A3105",
            "release_year": 2024,
            "specs": {
                "storage": "256GB",
                "display": "6.9-inch Super Retina XDR",
                "color": "Natural Titanium"
            },
            "image_url": "https://example.com/iphone-16-pro-max.jpg"
        },
        {
            "name": "iPhone 16 Pro",
            "category": "iphone",
            "description": "iPhone 16 Pro 256GB",
            "model_identifier": "A3104",
            "release_year": 2024,
            "specs": {
                "storage": "256GB",
                "display": "6.3-inch Super Retina XDR",
                "color": "Natural Titanium"
            },
            "image_url": "https://example.com/iphone-16-pro.jpg"
        },
        {
            "name": "iPhone 16 Plus",
            "category": "iphone",
            "description": "iPhone 16 Plus 256GB",
            "model_identifier": "A3103",
            "release_year": 2024,
            "specs": {
                "storage": "256GB",
                "display": "6.7-inch Super Retina XDR",
                "color": "Black"
            },
            "image_url": "https://example.com/iphone-16-plus.jpg"
        },
        {
            "name": "iPhone 16",
            "category": "iphone",
            "description": "iPhone 16 128GB",
            "model_identifier": "A3102",
            "release_year": 2024,
            "specs": {
                "storage": "128GB",
                "display": "6.1-inch Super Retina XDR",
                "color": "Black"
            },
            "image_url": "https://example.com/iphone-16.jpg"
        },
        {
            "name": "MacBook Pro 16-inch M5",
            "category": "mac",
            "description": "MacBook Pro 16-inch with M5 chip",
            "model_identifier": "A3114",
            "release_year": 2025,
            "specs": {
                "cpu": "Apple M5 Pro (12-core CPU)",
                "ram": "32GB Unified Memory",
                "storage": "1TB SSD",
                "display": "16.2-inch Liquid Retina XDR",
                "color": "Space Black"
            },
            "image_url": "https://example.com/macbook-pro-16-m5.jpg"
        },
        {
            "name": "iPad Pro 13-inch M5",
            "category": "ipad",
            "description": "iPad Pro 13-inch with M5 chip",
            "model_identifier": "A3350",
            "release_year": 2025,
            "specs": {
                "cpu": "Apple M5 (8-core CPU)",
                "storage": "512GB",
                "display": "13-inch Liquid Retina XDR"
            },
            "image_url": "https://example.com/ipad-pro-13-m5.jpg"
        },
        {
            "name": "iPad Pro 11-inch M5",
            "category": "ipad",
            "description": "iPad Pro 11-inch with M5 chip",
            "model_identifier": "A3351",
            "release_year": 2025,
            "specs": {
                "cpu": "Apple M5 (8-core CPU)",
                "storage": "256GB",
                "display": "11-inch Liquid Retina XDR"
            },
            "image_url": "https://example.com/ipad-pro-11-m5.jpg"
        },
        {
            "name": "Apple Watch Series 10",
            "category": "watch",
            "description": "Apple Watch Series 10 42mm GPS",
            "model_identifier": "A3000",
            "release_year": 2024,
            "specs": {
                "display": "42mm",
                "case": "Aluminum",
                "storage": "32GB"
            },
            "image_url": "https://example.com/apple-watch-10.jpg"
        },
        {
            "name": "Apple Watch Ultra 2",
            "category": "watch",
            "description": "Apple Watch Ultra 2 49mm GPS + Cellular",
            "model_identifier": "A3001",
            "release_year": 2024,
            "specs": {
                "display": "49mm",
                "case": "Titanium",
                "storage": "64GB"
            },
            "image_url": "https://example.com/apple-watch-ultra-2.jpg"
        },
        {
            "name": "AirPods Pro 3rd Gen",
            "category": "airpods",
            "description": "AirPods Pro 3rd Generation",
            "model_identifier": "A3214",
            "release_year": 2024,
            "specs": {
                "features": "Adaptive Audio, USB-C"
            },
            "image_url": "https://example.com/airpods-pro-3.jpg"
        },
        {
            "name": "AirPods Max",
            "category": "airpods",
            "description": "AirPods Max USB-C",
            "model_identifier": "A3215",
            "release_year": 2024,
            "specs": {
                "features": "Active Noise Cancellation, USB-C"
            },
            "image_url": "https://example.com/airpods-max.jpg"
        },
        {
            "name": "HomePod",
            "category": "accessories",
            "description": "HomePod 2nd Generation",
            "model_identifier": "A2764",
            "release_year": 2023,
            "specs": {
                "features": "Spatial Audio, Thread"
            },
            "image_url": "https://example.com/homepod.jpg"
        },
        {
            "name": "HomePod mini",
            "category": "accessories",
            "description": "HomePod mini",
            "model_identifier": "A2374",
            "release_year": 2020,
            "specs": {
                "features": "Siri, Thread"
            },
            "image_url": "https://example.com/homepod-mini.jpg"
        },
        {
            "name": "Magic Keyboard for iPad Pro",
            "category": "accessories",
            "description": "Magic Keyboard for iPad Pro 13-inch",
            "model_identifier": "A2836",
            "release_year": 2024,
            "specs": {
                "features": "Trackpad, USB-C"
            },
            "image_url": "https://example.com/magic-keyboard-ipad.jpg"
        },
        {
            "name": "MagSafe Battery Pack",
            "category": "accessories",
            "description": "MagSafe Battery Pack for iPhone",
            "model_identifier": "A2384",
            "release_year": 2021,
            "specs": {
                "features": "Wireless Charging, MagSafe"
            },
            "image_url": "https://example.com/magsafe-battery.jpg"
        },
        {
            "name": "Apple TV 4K",
            "category": "accessories",
            "description": "Apple TV 4K 128GB",
            "model_identifier": "A2843",
            "release_year": 2022,
            "specs": {
                "storage": "128GB",
                "features": "4K HDR, Dolby Atmos"
            },
            "image_url": "https://example.com/apple-tv-4k.jpg"
        },
        {
            "name": "Studio Display",
            "category": "accessories",
            "description": "Studio Display 27-inch 5K",
            "model_identifier": "A2525",
            "release_year": 2022,
            "specs": {
                "display": "27-inch 5K Retina",
                "features": "12MP Ultra Wide camera"
            },
            "image_url": "https://example.com/studio-display.jpg"
        }
    ]

    count = 0
    for p in products:
        existing = db.query(Product).filter(Product.name == p["name"]).first()
        if not existing:
            db.add(Product(**p))
            count += 1

    db.commit()
    print(f"✅ Seeded {count} MacTrackr products")

def seed_pokemon_products(db: Session):
    """Create sample Pokemon cards with Tier 2 fields"""
    products = [
        {
            "name": "Charizard EX",
            "category": "pokemon",
            "description": "Ultra Rare Charizard card from Scarlet & Violet set",
            "set_name": "Scarlet & Violet",
            "card_number": "125/198",
            "rarity": "Ultra Rare",
            "condition": "NM",
            "image_url": "https://example.com/charizard-ex.jpg"
        },
        {
            "name": "Pikachu VMAX",
            "category": "pokemon",
            "description": "Rainbow Rare Pikachu from Vivid Voltage",
            "set_name": "Vivid Voltage",
            "card_number": "188/185",
            "rarity": "Secret Rare",
            "condition": "NM",
            "image_url": "https://example.com/pikachu-vmax.jpg"
        },
        {
            "name": "Mewtwo V",
            "category": "pokemon",
            "description": "Holo Rare Mewtwo from Pokemon GO set",
            "set_name": "Pokemon GO",
            "card_number": "072/078",
            "rarity": "Holo Rare",
            "condition": "LP",
            "image_url": "https://example.com/mewtwo-v.jpg"
        }
    ]

    for p in products:
        existing = db.query(Product).filter(Product.name == p["name"]).first()
        if not existing:
            db.add(Product(**p))

    db.commit()
    print(f"✅ Seeded {len(products)} Pokemon cards")

def seed_audio_products(db: Session):
    """Create sample audio gear with Tier 2 fields"""
    products = [
        {
            "name": "Fender American Professional II Stratocaster",
            "category": "audio",
            "description": "Professional electric guitar with V-Mod II pickups",
            "brand": "Fender",
            "model": "American Professional II Stratocaster",
            "image_url": "https://example.com/fender-strat.jpg"
        },
        {
            "name": "Shure SM7B",
            "category": "audio",
            "description": "Professional dynamic microphone for broadcast and podcasting",
            "brand": "Shure",
            "model": "SM7B",
            "image_url": "https://example.com/shure-sm7b.jpg"
        },
        {
            "name": "Focusrite Scarlett 2i2 3rd Gen",
            "category": "audio",
            "description": "USB audio interface with 2 inputs/outputs",
            "brand": "Focusrite",
            "model": "Scarlett 2i2 Gen 3",
            "image_url": "https://example.com/focusrite-2i2.jpg"
        }
    ]

    for p in products:
        existing = db.query(Product).filter(Product.name == p["name"]).first()
        if not existing:
            db.add(Product(**p))

    db.commit()
    print(f"✅ Seeded {len(products)} audio products")

def seed_sample_prices(db: Session):
    """Create sample prices for products"""
    retailers = db.query(Retailer).all()
    products = db.query(Product).all()

    if not retailers or not products:
        print("⚠️  Need retailers and products first")
        return

    # Map retailers to indices
    retailer_map = {r.name: r for r in retailers}

    # MacTrackr products with prices - Feb 19, 2026
    product_prices = [
        # Mac Products
        {"product_name": "MacBook Pro 14-inch M5", "prices": [
            {"retailer": "Apple", "price": 1999, "condition": "new"},
            {"retailer": "Best Buy", "price": 1949, "condition": "new"},
            {"retailer": "Amazon", "price": 1949, "condition": "new"},
            {"retailer": "Walmart", "price": 1999, "condition": "new"},
            {"retailer": "B&H Photo", "price": 1949, "condition": "new"},
            {"retailer": "Adorama", "price": 1949, "condition": "new"},
        ]},
        {"product_name": "MacBook Air 13-inch M4", "prices": [
            {"retailer": "Apple", "price": 999, "condition": "new"},
            {"retailer": "Best Buy", "price": 949, "condition": "new"},
            {"retailer": "Amazon", "price": 949, "condition": "new"},
            {"retailer": "Walmart", "price": 999, "condition": "new"},
            {"retailer": "B&H Photo", "price": 899, "condition": "new"},
            {"retailer": "Adorama", "price": 999, "condition": "new"},
        ]},
        {"product_name": "MacBook Air 15-inch M4", "prices": [
            {"retailer": "Apple", "price": 1299, "condition": "new"},
            {"retailer": "Best Buy", "price": 1249, "condition": "new"},
            {"retailer": "Amazon", "price": 1249, "condition": "new"},
            {"retailer": "Walmart", "price": 1299, "condition": "new"},
            {"retailer": "B&H Photo", "price": 1199, "condition": "new"},
            {"retailer": "Adorama", "price": 1299, "condition": "new"},
        ]},
        {"product_name": "Mac mini M4", "prices": [
            {"retailer": "Apple", "price": 599, "condition": "new"},
            {"retailer": "Best Buy", "price": 579, "condition": "new"},
            {"retailer": "Amazon", "price": 579, "condition": "new"},
            {"retailer": "Walmart", "price": 599, "condition": "new"},
            {"retailer": "B&H Photo", "price": 579, "condition": "new"},
            {"retailer": "Adorama", "price": 579, "condition": "new"},
        ]},
        {"product_name": "Mac Studio M3 Max", "prices": [
            {"retailer": "Apple", "price": 2999, "condition": "new"},
            {"retailer": "Best Buy", "price": 2799, "condition": "new"},
            {"retailer": "Amazon", "price": 2799, "condition": "new"},
            {"retailer": "Walmart", "price": 2999, "condition": "new"},
            {"retailer": "B&H Photo", "price": 2799, "condition": "new"},
            {"retailer": "Adorama", "price": 2799, "condition": "new"},
        ]},
        {"product_name": "iMac 24-inch M4", "prices": [
            {"retailer": "Apple", "price": 1299, "condition": "new"},
            {"retailer": "Best Buy", "price": 1199, "condition": "new"},
            {"retailer": "Amazon", "price": 1199, "condition": "new"},
            {"retailer": "Walmart", "price": 1299, "condition": "new"},
            {"retailer": "B&H Photo", "price": 1199, "condition": "new"},
            {"retailer": "Adorama", "price": 1199, "condition": "new"},
        ]},
        # iPad Products
        {"product_name": "iPad Air 13-inch M3", "prices": [
            {"retailer": "Apple", "price": 799, "condition": "new"},
            {"retailer": "Best Buy", "price": 749, "condition": "new"},
            {"retailer": "Amazon", "price": 749, "condition": "new"},
            {"retailer": "Walmart", "price": 799, "condition": "new"},
            {"retailer": "Target", "price": 799, "condition": "new"},
        ]},
        {"product_name": "iPad Air 11-inch M3", "prices": [
            {"retailer": "Apple", "price": 599, "condition": "new"},
            {"retailer": "Best Buy", "price": 549, "condition": "new"},
            {"retailer": "Amazon", "price": 549, "condition": "new"},
            {"retailer": "Walmart", "price": 599, "condition": "new"},
            {"retailer": "Target", "price": 599, "condition": "new"},
        ]},
        {"product_name": "iPad 11-inch A16", "prices": [
            {"retailer": "Apple", "price": 499, "condition": "new"},
            {"retailer": "Best Buy", "price": 449, "condition": "new"},
            {"retailer": "Amazon", "price": 449, "condition": "new"},
            {"retailer": "Walmart", "price": 499, "condition": "new"},
            {"retailer": "Target", "price": 499, "condition": "new"},
        ]},
        {"product_name": "iPad mini A17 Pro", "prices": [
            {"retailer": "Apple", "price": 599, "condition": "new"},
            {"retailer": "Best Buy", "price": 549, "condition": "new"},
            {"retailer": "Amazon", "price": 549, "condition": "new"},
            {"retailer": "Walmart", "price": 599, "condition": "new"},
            {"retailer": "Target", "price": 599, "condition": "new"},
        ]},
        # Apple Watch
        {"product_name": "Apple Watch SE 40mm", "prices": [
            {"retailer": "Apple", "price": 249, "condition": "new"},
            {"retailer": "Best Buy", "price": 219, "condition": "new"},
            {"retailer": "Amazon", "price": 219, "condition": "new"},
            {"retailer": "Walmart", "price": 249, "condition": "new"},
            {"retailer": "Target", "price": 249, "condition": "new"},
        ]},
        # AirPods
        {"product_name": "AirPods 4", "prices": [
            {"retailer": "Apple", "price": 129, "condition": "new"},
            {"retailer": "Best Buy", "price": 109, "condition": "new"},
            {"retailer": "Amazon", "price": 109, "condition": "new"},
            {"retailer": "Walmart", "price": 129, "condition": "new"},
            {"retailer": "Target", "price": 129, "condition": "new"},
        ]},
        # Accessories
        {"product_name": "Apple Pencil Pro", "prices": [
            {"retailer": "Apple", "price": 129, "condition": "new"},
            {"retailer": "Best Buy", "price": 109, "condition": "new"},
            {"retailer": "Amazon", "price": 109, "condition": "new"},
            {"retailer": "Walmart", "price": 129, "condition": "new"},
            {"retailer": "Target", "price": 129, "condition": "new"},
        ]},
        {"product_name": "AirTag 4-Pack", "prices": [
            {"retailer": "Apple", "price": 79, "condition": "new"},
            {"retailer": "Best Buy", "price": 69, "condition": "new"},
            {"retailer": "Amazon", "price": 69, "condition": "new"},
            {"retailer": "Walmart", "price": 79, "condition": "new"},
            {"retailer": "Target", "price": 79, "condition": "new"},
        ]},
        # New products (17 more to reach 31 total)
        {"product_name": "iPhone 16 Pro Max", "prices": [
            {"retailer": "Apple", "price": 1199, "condition": "new"},
            {"retailer": "Best Buy", "price": 1149, "condition": "new"},
            {"retailer": "Amazon", "price": 1149, "condition": "new"},
            {"retailer": "Walmart", "price": 1199, "condition": "new"},
            {"retailer": "Target", "price": 1199, "condition": "new"},
        ]},
        {"product_name": "iPhone 16 Pro", "prices": [
            {"retailer": "Apple", "price": 999, "condition": "new"},
            {"retailer": "Best Buy", "price": 949, "condition": "new"},
            {"retailer": "Amazon", "price": 949, "condition": "new"},
            {"retailer": "Walmart", "price": 999, "condition": "new"},
            {"retailer": "Target", "price": 999, "condition": "new"},
        ]},
        {"product_name": "iPhone 16 Plus", "prices": [
            {"retailer": "Apple", "price": 899, "condition": "new"},
            {"retailer": "Best Buy", "price": 849, "condition": "new"},
            {"retailer": "Amazon", "price": 849, "condition": "new"},
            {"retailer": "Walmart", "price": 899, "condition": "new"},
            {"retailer": "Target", "price": 899, "condition": "new"},
        ]},
        {"product_name": "iPhone 16", "prices": [
            {"retailer": "Apple", "price": 799, "condition": "new"},
            {"retailer": "Best Buy", "price": 749, "condition": "new"},
            {"retailer": "Amazon", "price": 749, "condition": "new"},
            {"retailer": "Walmart", "price": 799, "condition": "new"},
            {"retailer": "Target", "price": 799, "condition": "new"},
        ]},
        {"product_name": "MacBook Pro 16-inch M5", "prices": [
            {"retailer": "Apple", "price": 2499, "condition": "new"},
            {"retailer": "Best Buy", "price": 2399, "condition": "new"},
            {"retailer": "Amazon", "price": 2399, "condition": "new"},
            {"retailer": "B&H Photo", "price": 2399, "condition": "new"},
            {"retailer": "Adorama", "price": 2399, "condition": "new"},
        ]},
        {"product_name": "iPad Pro 13-inch M5", "prices": [
            {"retailer": "Apple", "price": 1299, "condition": "new"},
            {"retailer": "Best Buy", "price": 1249, "condition": "new"},
            {"retailer": "Amazon", "price": 1249, "condition": "new"},
            {"retailer": "Target", "price": 1299, "condition": "new"},
        ]},
        {"product_name": "iPad Pro 11-inch M5", "prices": [
            {"retailer": "Apple", "price": 999, "condition": "new"},
            {"retailer": "Best Buy", "price": 949, "condition": "new"},
            {"retailer": "Amazon", "price": 949, "condition": "new"},
            {"retailer": "Target", "price": 999, "condition": "new"},
        ]},
        {"product_name": "Apple Watch Series 10", "prices": [
            {"retailer": "Apple", "price": 399, "condition": "new"},
            {"retailer": "Best Buy", "price": 379, "condition": "new"},
            {"retailer": "Amazon", "price": 379, "condition": "new"},
            {"retailer": "Target", "price": 399, "condition": "new"},
        ]},
        {"product_name": "Apple Watch Ultra 2", "prices": [
            {"retailer": "Apple", "price": 799, "condition": "new"},
            {"retailer": "Best Buy", "price": 749, "condition": "new"},
            {"retailer": "Amazon", "price": 749, "condition": "new"},
        ]},
        {"product_name": "AirPods Pro 3rd Gen", "prices": [
            {"retailer": "Apple", "price": 249, "condition": "new"},
            {"retailer": "Best Buy", "price": 229, "condition": "new"},
            {"retailer": "Amazon", "price": 229, "condition": "new"},
            {"retailer": "Target", "price": 249, "condition": "new"},
        ]},
        {"product_name": "AirPods Max", "prices": [
            {"retailer": "Apple", "price": 549, "condition": "new"},
            {"retailer": "Best Buy", "price": 499, "condition": "new"},
            {"retailer": "Amazon", "price": 499, "condition": "new"},
        ]},
        {"product_name": "HomePod", "prices": [
            {"retailer": "Apple", "price": 299, "condition": "new"},
            {"retailer": "Best Buy", "price": 279, "condition": "new"},
            {"retailer": "Amazon", "price": 279, "condition": "new"},
        ]},
        {"product_name": "HomePod mini", "prices": [
            {"retailer": "Apple", "price": 99, "condition": "new"},
            {"retailer": "Best Buy", "price": 89, "condition": "new"},
            {"retailer": "Amazon", "price": 89, "condition": "new"},
            {"retailer": "Target", "price": 99, "condition": "new"},
        ]},
        {"product_name": "Magic Keyboard for iPad Pro", "prices": [
            {"retailer": "Apple", "price": 349, "condition": "new"},
            {"retailer": "Best Buy", "price": 329, "condition": "new"},
            {"retailer": "Amazon", "price": 329, "condition": "new"},
        ]},
        {"product_name": "MagSafe Battery Pack", "prices": [
            {"retailer": "Apple", "price": 99, "condition": "new"},
            {"retailer": "Best Buy", "price": 89, "condition": "new"},
            {"retailer": "Amazon", "price": 89, "condition": "new"},
        ]},
        {"product_name": "Apple TV 4K", "prices": [
            {"retailer": "Apple", "price": 129, "condition": "new"},
            {"retailer": "Best Buy", "price": 119, "condition": "new"},
            {"retailer": "Amazon", "price": 119, "condition": "new"},
            {"retailer": "Target", "price": 129, "condition": "new"},
        ]},
        {"product_name": "Studio Display", "prices": [
            {"retailer": "Apple", "price": 1599, "condition": "new"},
            {"retailer": "Best Buy", "price": 1499, "condition": "new"},
            {"retailer": "Amazon", "price": 1499, "condition": "new"},
            {"retailer": "B&H Photo", "price": 1499, "condition": "new"},
        ]},
    ]

    count = 0
    for pp in product_prices:
        product = db.query(Product).filter(Product.name == pp["product_name"]).first()
        if product:
            for price_info in pp["prices"]:
                retailer = retailer_map.get(price_info["retailer"])
                if retailer:
                    existing = db.query(Price).filter(
                        Price.product_id == product.id,
                        Price.retailer_id == retailer.id
                    ).first()

                    if not existing:
                        # Generate search URL instead of fake direct URL
                        search_query = product.name.replace(" ", "+")
                        listing_url = generate_search_url(retailer.name, search_query)
                        db.add(Price(
                            product_id=product.id,
                            retailer_id=retailer.id,
                            price=price_info["price"],
                            condition=price_info["condition"],
                            listing_url=listing_url,
                            listing_title=product.name
                        ))
                        count += 1

    db.commit()
    print(f"✅ Seeded {count} prices")

def main():
    """Run all seed functions"""
    print("🌱 Seeding database...")

    # Create tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        seed_retailers(db)
        seed_mac_products(db)
        seed_mactrackr_products(db)
        seed_sample_prices(db)

        print("\n✅ Database seeded successfully!")
        print("\nSample data created:")
        print("  - 9 Retailers (Apple, Best Buy, Walmart, Target, Amazon, B&H, Adorama, eBay, CDW)")
        print("  - 3 Original Mac products")
        print("  - 15 MacTrackr products (Feb 19, 2026)")
        print("  - Sample prices for all products")

    except Exception as e:
        print(f"❌ Error seeding: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()
