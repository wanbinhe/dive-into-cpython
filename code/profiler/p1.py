import threading

data = []


def add_data(n):
	for i in range(n):
		data.append(i)


if __name__ == '__main__':
	ts = [threading.Thread(target=add_data, args=(100000,)) for _ in range(100)]
	for t in ts:
		t.start()
	for t in ts:
		t.join()

	print(data)
	print(len(data))
	print(sum(data))
