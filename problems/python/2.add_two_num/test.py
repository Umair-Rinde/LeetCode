
from sln import Solution, ListNode

if __name__ == "__main__" :
    # Example usage:
    sol = Solution()
    
    # Creating first linked list: 2 -> 4 -> 3
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    
    # Creating second linked list: 5 -> 6 -> 4
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    
    result = sol.addTwoNumbers(l1, l2)
    
    # Printing the result linked list
    while result:
        print(result.val if result.next else "")
        result = result.next
    # Output should be: 7 -> 0 -> 8