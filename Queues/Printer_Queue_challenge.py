#Code Challenge - Create 3 classes that model how a printer takes jobs out of a print queue
#PrintQueue Class must follow Queue data structure implementation
#Job class - has pages attribute. Random number between 1-10 for pages.
#Job class - print_page() function that decrements pages. check_complete() checks all pages are printed.
#Printer class - get_job() function that uses dequeue to take 1st job in print queue off of the queue. 
#                Account for get_job() having no jobs

class PrintQueue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == [] 


class Job:
    def __init__(self, pages):
        self.pages = pages

    def __repr__(self):
        return str(self.pages)

    def print_pages(self):
        while self.pages:
            self.pages -= 1 
            print("Printing page... {total_pg} remaining".format(total_pg = self.pages))
        self.check_complete()

    def check_complete(self):
        if self.pages > 0:
            print("There's still pages to print")
            self.print_pages()
        else:
            print("{pages} remaining. Job complete".format(pages=self.pages))

class Printer:
    def get_job(self, q):
        print(q.items)
        while q.items:
            next_job = q.peek()
            print(next_job)
            Job.print_pages(next_job)
            q.dequeue()
        print("All jobs are complete")

print_q = PrintQueue()
printer = Printer()
job_1 = Job(5)
job_2 = Job(3)
job_3 = Job(1) 
print_q.enqueue(job_1)
print_q.enqueue(job_2)
print_q.enqueue(job_3)

printer.get_job(print_q)


