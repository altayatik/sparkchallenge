check-in:
	python3 checkin.py
check-out:
	python3 checkout.py
clean:
	> checkin_logs.txt
	> checkout_logs.txt
	> checkin_time.txt
	> checkout_time.txt
	> checkin_puid.txt
	> checkout_puid.txt
	> checkout_difference.txt
