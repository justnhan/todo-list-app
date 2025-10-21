tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách"""
    tasks.append(task_name)
    print(f"Đã thêm công việc:'{task_name}'")
def list_tasks():
    for i in range (len(tasks)):
        print (tasks[i])
#---Điểm bắt đầu của chương trình---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-do-list!")
    add_task("Học bài Git và Github")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()