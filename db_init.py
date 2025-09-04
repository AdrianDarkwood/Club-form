from models import Base, engine

print("📦 Creating tables if they don’t exist...")
Base.metadata.create_all(bind=engine)
print("✅ Done!")
