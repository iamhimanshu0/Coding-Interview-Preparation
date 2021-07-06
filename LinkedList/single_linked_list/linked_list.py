import math

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        cur_node = self.head 
        
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            return 
        
        cur_node = self.head 
        while cur_node.next:
            cur_node = cur_node.next 
            
        cur_node.next = new_node
        
    
    def prepend(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node
        
        
        
    def add_in_between(self, item, data):
        new_node = Node(data)
        
        cur_node = self.head 
        prev_node = None 
        while cur_node and cur_node.data != item:
            cur_node = cur_node.next
            prev_node = cur_node
        
        
        new_node.next = cur_node.next
        prev_node.next = new_node
        
        
    def length(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next 
            
        print("Length of the LinkedList is:- ", count)
    
    # find_middle element of a LinkedList
    
    def find_middle(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next 
            
        
        if count %2 ==0 :
            # two even node then /2 +1 
            mid = math.ceil(count/2)
            print("Length is even ", mid)
            c = 0
            while self.head and c != mid:
                self.head = self.head.next
                c += 1 
            
            print(self.head.data)
            print("even")
        else:
            # else celing
            mid = count//2
            print("Length is Odd ", mid)
            c = 0
            while self.head and c != mid:
                self.head = self.head.next
                c += 1 
            
            print(self.head.data)
            
    
    # find_middle using 2 pointer method 
    def find_middle_2_pointer(self):
        slow_pointer = self.head 
        fast_pointer = self.head
        
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next 
            slow_pointer = slow_pointer.next
            
        print("middle element:- ", slow_pointer.data)
        
    
    # sum_of_data elements
    def sum_of_data(self):
        cur_node = self.head

        l_sum = 0

        while cur_node:
            l_sum += int(cur_node.data) 
            cur_node = cur_node.next 
        
        print("Sum of the LinkedList elements are :- ", l_sum )
    
    
    def reverse_list(self):
        """
        / Before changing next of current, 
        // store next node 
        next = curr->next
        // Now change next of current 
        // This is where actual reversing happens 
        curr->next = prev 
        // Move prev and curr one step forward 
        prev = curr 
        curr = next
     """
     
        prev_node = None 
        cur_node = self.head 
        next_node = None 
        
        while cur_node:
            next_node = cur_node.next 
            cur_node.next = prev_node
            
            prev_node = cur_node
            cur_node = next_node 
            
        self.head  = prev_node
        
    
    def recursive_reverse(self, head):
        """
        1) Divide the list in two parts - first node and 
        rest of the linked list.
        2) Call reverse for the rest of the linked list.
        3) Link rest to first.
        4) Fix head pointer
        """
        
        if head is None or head.next is None:
            return head 
          
        # reverse the rest link 
        rest = self.recursive_reverse(head.next)
        
        # put first element at the end 
        head.next.next = head 
        head.next = None 
        
        # fix the head pointer
        return rest 
        
    
    def node_swap(self, key_1, key_2):
        
        if key_1 == key_2:
            return 
        
        cur_1= self.head 
        prev_1 = None 
        # check for key_1
        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1
            cur_1 = cur_1.next 
        
        # print("key_1 is",key_1,"and Previous node is ", prev_1.data)
        
        
        cur_2 = self.head
        prev_2 = None
        # check for key_2 
        while cur_2 and cur_2.data != key_2:
            prev_2 = cur_2
            cur_2 = cur_2.next 
        
        # print("key_2 is",key_2, "and Previous node is ", prev_2.data)
        
        if not cur_1 or not cur_2:
            return 
        
        # if prev_1:
        #     prev_1.next = cur_2
        # else:
        #     self.head = cur_2
        
        # if prev_2:
        #     prev_2.next = cur_1
        # else:
        #     self.head = cur_1  
        
        
        # prev_1.next = cur_2  
        # prev_2.next = cur_1
        
        cur_1.data , cur_2.data = cur_2.data, cur_1.data
        
        
    def remove_duplicate(self):
        cur_node = self.head 
        next_node = self.head.next 

        check = {
          
        }

        while cur_node:
            if cur_node.data not in check:
                check[cur_node.data]= cur_node.data
            else:
                print(f"Duplicate occur {cur_node.data}")

            cur_node = cur_node.next 

        print(check)
                
l = LinkedList()
l.append("1")
l.append("2")
l.append("3")
l.append("2")
l.append("5")
l.append("5")
# l.append("6")
# l.add_in_between("2","3")
# print list 

l.print_list()

# print("Node Swap")
# l.node_swap("3","1")
# l.print_list()
    

# only works if data is int 
# l.sum_of_data()
       
# print length of LinkedList
# l.length()
# find find_middle
# l.find_middle()
# l.find_middle_2_pointer()
# l.reverse_list()
# l.recursive_reverse(l.head)
# print("reverse_list")
# l.print_list()

l.remove_duplicate()




