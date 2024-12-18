import os
import sys
import psycopg2


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_booking.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT", 5432)
        )
        cursor = conn.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    type VARCHAR(255),
                    price NUMERIC(10, 2)
                );
                
                CREATE TABLE IF NOT EXISTS rooms (
                    id SERIAL PRIMARY KEY,
                    type VARCHAR(255),
                    price NUMERIC(10, 2)
                );
                
                CREATE TABLE IF NOT EXISTS bookings (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id),
                    room_id INTEGER REFERENCES rooms(id),
                    booking_date DATE,
                    booking_time TIME,
                    total_price NUMERIC(10, 2),
                    payment_type VARCHAR(50)
                );  
            """)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()
