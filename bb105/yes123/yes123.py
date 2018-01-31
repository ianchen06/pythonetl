import tasks

[tasks.get_list.delay(page) for page in range(1,11)]

