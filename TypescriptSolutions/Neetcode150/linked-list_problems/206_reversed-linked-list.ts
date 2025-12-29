
  // Definition for singly-linked list.
  class ListNode {
      val: number
      next: ListNode | null
      constructor(val?: number, next?: ListNode | null) {
          this.val = (val===undefined ? 0 : val)
          this.next = (next===undefined ? null : next)
      }
  }


const reverseList = (head: ListNode | null): ListNode | null => {
    if (!head) return head;

    let cur = head;
    let prv = null;

    while (cur) {
        let nxt = cur.next;
        cur.next = prv;
        prv = cur;
        cur = nxt;
    }

    return prv;
};