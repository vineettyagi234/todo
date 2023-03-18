FILEPATH = ('todo.txt')

def getTodos(filepath = FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def writeTodos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("hello")
    print(getTodos(FILEPATH))