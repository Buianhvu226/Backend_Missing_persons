import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres.clxxtikxcdjbosddoooa",
        password="123456Aa",
        host="aws-0-ap-southeast-1.pooler.supabase.com",  # Corrected host
        port=6543,
    )
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")

    