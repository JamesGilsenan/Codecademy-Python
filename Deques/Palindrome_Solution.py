from Deque import Deque

def main(data):
    deque = Deque()
    for character in data:
        deque.add_rear(character)
    
    while deque.size() >= 2:
        front_item = deque.peek_front()
        rear_item = deque.peek_rear()
        deque.remove_front()
        deque.remove_rear()

        if rear_item != front_item:
            return False
    return True

print(main("nitin"))
print(main("car"))
