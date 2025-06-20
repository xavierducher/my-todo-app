# Variables
FILEPATH = "files/todos.txt"

# log element
def log (text_log):
    print("## LOG : ", text_log)

# Get todos from file "a_filepath"
def get_todos (a_filepath=FILEPATH):
    """
    Get todos from the text file
    :param a_filepath: path of the text file
    :return: list of todos
    """
    with open(a_filepath, 'r') as file:
        return (file.readlines())

#write todos to the file "a_filepath"
def write_todos (a_todos, a_filepath=FILEPATH):
    """
    Write todos in the file provided
    :param a_todos: the todos list
    :param a_filepath: the target file
    :return:none
    """
    with open(a_filepath, 'w') as file:
        file.writelines(a_todos)


if __name__ == "__main__":
    print("Hello from functions")
    print (get_todos())