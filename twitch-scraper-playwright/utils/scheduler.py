import schedule
import time
from main import main


def run_scheduler():
    
    # Jadwalkan scraping setiap 15 menit
    schedule.every(15).minutes.do(main)
    
    print("Scheduler aktif. Menjalankan scraping setiap 15 menit")
    
    while True:
        schedule.run_pending()
        time.sleep(1)