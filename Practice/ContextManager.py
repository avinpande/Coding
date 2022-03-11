# Python Context Manager program
# Functionality demonstration

class ContextManager:

    def __init__(self, name, mode):
        print('Initialize')
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        print('Enter')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit')
        self.file.close()


with ContextManager(r'C:\Users\avinpandey\Desktop\Refund.txt', 'w') as manager:
    manager.write('Test abhi baki hai mere dost')
