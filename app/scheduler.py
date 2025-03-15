from apscheduler.schedulers.background import BackgroundScheduler

from base import SessionLocal

from CRUD import delete_old_schedules


def run_delete():
    db = SessionLocal()
    try:
        delete_old_schedules(db)
    finally:
        db.close()


scheduler = BackgroundScheduler()
scheduler.add_job(run_delete, 'interval', minutes=5)
