from datetime import datetime, timedelta
import os
import xlwt
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger

from employee_management_app.models import EmployeeTasks

logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(minute=0, hour=20, day_of_week='fri')),
               name="generate_weekly_report",
               ignore_result=True)
def generate_weekly_report():
    '''Function to download task details in xls'''
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("sheet1")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Employee Name', 'Task', 'Time', 'Status']
    ws.col(0).width = len(columns[0]) * 367
    ws.col(1).width = 7 * len(columns[1]) * 367
    ws.col(2).width = 4 * len(columns[2]) * 367
    ws.col(3).width = 3 * len(columns[3]) * 367

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
    # get your data, from database or from a text file...
    week_start = datetime.now() - timedelta(weeks=1)
    data = EmployeeTasks.objects.filter(created_at__gte=week_start).order_by('-created_at')
    for my_row in data:
        row_num = row_num + 1
        ws.write(row_num, 0, my_row.employee.username, font_style)
        ws.write(row_num, 1, my_row.name, font_style)
        ws.write(row_num, 2, my_row.created_at.strftime('%Y-%m-%d %H:%M:%S'), font_style)
        ws.write(row_num, 3, my_row.get_status_display(), font_style)

    wb.save('WeeklyTaskReport' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '.xls')
    logger.info('Weekly report Generated')
