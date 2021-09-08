from main import progress_bar
import time

progress_bar.percentage_number = True
progress_bar.percentage = True

for i in range(1001):
    progress_bar.create(i, 1000)
    time.sleep(0.01)