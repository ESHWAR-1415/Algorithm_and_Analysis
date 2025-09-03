#stack Implementation
n = 3
top = -1
stack = [None]*n
def push(item):
     global top
     if top >= n-1:
         print("Stack is full")
     else:
         top += 1
         stack[top] = item
         print(f"pushed item onto the stack:{item}")

def pop():
    global top
    if top == -1:
        return"stack is empty"
    else:
        item = stack[top]
        print(f"Removed from top: {item}")
        top -= 1
        return item

def display_stack():
    if top == -1:
        print("Stack is empty")
    else:
        print("Stack elements (top to bottom) are:")
        for i in range(top, -1, -1):
            print(stack[i])

display_stack()
push(10)
push(20)
push(30)
push(40)
display_stack()
popped_item = pop()
print(f"popped item:{popped_item}")
display_stack()
pop()
display_stack()
pop()
display_stack()
