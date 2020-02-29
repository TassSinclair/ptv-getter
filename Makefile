build:
	docker build -t ptv-getter .
run:
	docker run -p 5000:5000 ptv-getter