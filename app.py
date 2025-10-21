tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách"""
    dictionary_tasks = {'name': 'Tên công việc', 'completed': False}
    dictionary_tasks ['name'] = task_name
    tasks.append(dictionary_tasks)
    print(f"Đã thêm công việc:'{task_name}'")
def list_tasks():
    for i in range (len(tasks)):
        if tasks[i]['completed']==True:
            print("[X]", tasks[i]['name'])
        else:
            print("[ ]",tasks[i]['name'])
def complete_task(task_index):
    tasks [task_index] ['completed']=True
def delete_task(task_index):
    try:
        del tasks[task_index]
    except IndexError:
        print("---chỉ số không hợp lệ. Không thể xóa.")
#---Điểm bắt đầu của chương trình---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-do-list!")
    add_task("Học bài Git và Github")
    add_task("Làm bài tập thực hành ở nhà")
    complete_task(0)
    delete_task(2)
    list_tasks()
