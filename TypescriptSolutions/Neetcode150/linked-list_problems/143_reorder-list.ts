class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

/**
 Do not return anything, modify head in-place instead.
 */
 const reorderList = (head: ListNode | null): void => {
    let dummy = head;

    const reverseList = (head: ListNode | null): ListNode | null => {
        let cur = head;
        let prv: ListNode | null = null;

        while (cur) {
            let nxt = cur.next;
            cur.next = prv;
            prv = cur;
            cur = nxt;
        }

        return prv;
    };

    // 1: Get midpoint
    let slow = head;
    let fast = head;
    while (fast && fast.next) {
        slow = slow!.next;
        fast = fast.next.next;
    }

    // 2: Create two groups
    let second = slow!.next;
    slow!.next = null;
    let first = dummy;

    // 3: Reverse second group
    second = reverseList(second);

    // 4: Connect both lists
    while (first && second) {
        let nxt = first.next;
        first.next = second;
        first = nxt;

        nxt = second.next;
        second.next = first;
        second = nxt;
    }
 };