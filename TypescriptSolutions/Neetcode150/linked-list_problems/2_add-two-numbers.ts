/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

const addTwoNumbers = (l1: ListNode | null, l2: ListNode | null): ListNode | null => {
    let dummy = new ListNode();
    let curr = dummy;

    let carry = 0;
    while (l1 || l2 || carry) {
        let total = carry;

        if (l1) {
            total += l1.val;
            l1 = l1.next;
        }
        if (l2) {
            total += l2.val;
            l2 = l2.next;
        }

        carry = Math.floor(total / 10);
        total = total % 10;

        curr.next = new ListNode(total);
        curr = curr.next;
    }

    return dummy.next;
};