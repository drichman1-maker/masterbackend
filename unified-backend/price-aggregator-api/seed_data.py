"""
Seed data for Price Aggregator API
Creates sample products with Tier 1-2 fields
"""

from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, Product, Retailer, Price
from datetime import datetime

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
        # HomePod
        {
            "name": "HomePod mini",
            "category": "homepod",
            "description": "HomePod mini",
            "model_identifier": "A2375",
            "release_year": 2020,
            "specs": {
                "chip": "Apple S5",
                "features": "Spatial Audio, Thread"
            },
            "image_url": "https://example.com/homepod-mini.jpg"
        },
        {
            "name": "HomePod",
            "category": "homepod",
            "description": "HomePod",
            "model_identifier": "A2919",
            "release_year": 2023,
            "specs": {
                "chip": "Apple S7",
                "features": "Spatial Audio, Room Sensing"
            },
            "image_url": "https://example.com/homepod.jpg"
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
        # HomePod
        {"product_name": "HomePod mini", "prices": [
            {"retailer": "Apple", "price": 99, "condition": "new"},
            {"retailer": "Best Buy", "price": 79, "condition": "new"},
            {"retailer": "Amazon", "price": 79, "condition": "new"},
            {"retailer": "Walmart", "price": 99, "condition": "new"},
            {"retailer": "Target", "price": 99, "condition": "new"},
        ]},
        {"product_name": "HomePod", "prices": [
            {"retailer": "Apple", "price": 299, "condition": "new"},
            {"retailer": "Best Buy", "price": 249, "condition": "new"},
            {"retailer": "Amazon", "price": 249, "condition": "new"},
            {"retailer": "Walmart", "price": 299, "condition": "new"},
            {"retailer": "Target", "price": 299, "condition": "new"},
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
                        db.add(Price(
                            product_id=product.id,
                            retailer_id=retailer.id,
                            price=price_info["price"],
                            condition=price_info["condition"],
                            listing_url=f"https://{retailer.base_url}/product/{product.id}",
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
